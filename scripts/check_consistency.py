#!/usr/bin/env python3
"""Kontrola spójności bazy wiedzy skilla coach-arek.

Skrypt nie wymaga transkrypcji ani dodatkowych zależności: sprawdza wyłącznie
pliki w repozytorium (SKILL.md, README.md, INSTALL.md, references/*.md|json).
Dzięki temu działa w CI publicznego repozytorium, gdzie pełne transkrypcje
nie są publikowane.

Kontrola cytowań wobec samych transkrypcji (trafienie w blok, atrybucja
mówcy) nie jest częścią CI, bo transkrypcje nie są publikowane; wykonuj ją
lokalnie, porównując `references/transcripts/<id>.md` z kotwicą w bazie.

Użycie:
    python scripts/check_consistency.py [--repo .] [--quiet]

Kod wyjścia 0 = brak niespójności, 1 = znaleziono niespójności.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# --- taksonomia (musi zgadzać się z references/knowledge_base_hipertrofia.json) ---

KIND_LEGEND = {
    "speaker_statement": "wypowiedź rozmówcy (parafraza nagrania)",
    "editorial_caution": "uwaga redakcyjna autora: ostrożność interpretacyjna, nie twierdzenie rozmówcy",
    "author_addition": "procedura dodana przez autora skilla",
}

CONFIDENCE_LEGEND = {
    "verbatim": "wiernie oddaje wypowiedź rozmówcy, bez zastrzeżeń",
    "contextual": "wypowiedź wierna, ale wymaga kontekstu (metoda, ramka, wyjątek)",
    "not_universal": "wypowiedź wierna, ale opisuje praktykę rozmówcy, nie regułę ogólną",
    "requires_verification": "podcast tego nie dowodzi — sprawdź w źródle naukowym",
}

VERDICTS = {
    "supported",
    "partially_supported",
    "overstated",
    "unsupported_mechanism",
    "contradicted_partially",
}

REQUIRED_FILES = (
    "SKILL.md",
    "README.md",
    "INSTALL.md",
    "agents/openai.yaml",
    "repo-about.json",
    "references/knowledge_base_hipertrofia.md",
    "references/knowledge_base_hipertrofia.json",
    "references/weryfikacja_naukowa.md",
)

FORBIDDEN_PHRASES = (
    "etykiety zostały odwrócone",
    "etykiety odwrócono",
    "kopia skilla ma je odwrócone",
    "podcast_paraphrase",
    "check_citations.py",
)

# Symbole w tabeli zbiorczej `weryfikacja_naukowa.md` §1 <-> werdykty JSON.
SYMBOL_TO_VERDICT = {
    "✅": "supported",
    "🟡": "partially_supported",
    "🟠": "overstated",
    "🔴": "unsupported_mechanism",
    "⛔": "contradicted_partially",
}

# Jednostki, dla których liczba w treści musi znaleźć się w tabeli liczb.
# Świadomie pominięte: MB (rozmiar repo), liczby plików i nagrań, liczby twierdzeń.
UNIT_WORDS = (
    "kcal", "kg", "g", "%", "min", "sek", "s", "godz", "tydz", "tyg", "tygodni",
    "dni", "powtórzeń", "powtórzenia", "serii", "seria", "sesji", "sesja",
    "treningów", "treningi", "kroków", "lat", "dól", "góra", "tys",
)

CITE_RE = re.compile(r"\[(\d{1,2}:\d{2}(?::\d{2})?)\]\((https://youtu\.be/([^?)]+))\?t=(\d+)\)")
PAREN_CITE_RE = re.compile(r"\((S\d{1,2})@(\d{1,2}:\d{2}(?::\d{2})?)\)")
PRINCIPLE_RE = re.compile(r"^P\d{2,3}$")
TIMESTAMP_RE = re.compile(r"^\d{1,2}:\d{2}(?::\d{2})?$")


def secs(ts: str) -> int:
    parts = [int(x) for x in ts.split(":")]
    if len(parts) == 2:
        return parts[0] * 60 + parts[1]
    return parts[0] * 3600 + parts[1] * 60 + parts[2]


def md_sections(md: str) -> dict[str, str]:
    """Rozcina markdown na sekcje po nagłówkach '## ' (bez '# ' poziomu 1)."""
    out: dict[str, str] = {}
    current = "_preamble"
    buf: list[str] = []
    for line in md.splitlines():
        if line.startswith("## "):
            out[current] = "\n".join(buf)
            current = line[3:].strip()
            buf = []
        else:
            buf.append(line)
    out[current] = "\n".join(buf)
    return out


def numbers_table(md: str) -> str:
    marker = "## Wszystkie liczby w bazie"
    if marker not in md:
        return ""
    tail = md.split(marker, 1)[1]
    return tail.split("\n## ", 1)[0]


def table_values(table: str) -> list[str]:
    values = []
    for line in table.splitlines():
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or cells[0] in ("Wartość", "") or set(cells[0]) <= {"-", ":"}:
            continue
        values.append(cells[0])
    return values


def numeric_cores(text: str) -> set[str]:
    """Rdzenie liczbowe z tekstu (np. '2,5–3', '100–180'), bez jednostek i kontekstu."""
    cores: set[str] = set()
    pattern = re.compile(
        r"(?<![\w.,])(\d{1,3}(?:[.,]\d+)?(?:\s*[–-]\s*\d{1,3}(?:[.,]\d+)?)?)"
        r"(?:\s*/\s*\d{1,3})?"
        r"(?:\s*([A-Za-z%×/]{1,12}))?"
    )
    for m in pattern.finditer(text):
        core = re.sub(r"\s+", "", m.group(1))
        unit = (m.group(2) or "").lower().strip(".,;:")
        if not unit:
            continue
        if not any(unit.startswith(u) or u.startswith(unit) for u in UNIT_WORDS):
            continue
        if re.fullmatch(r"(19|20)\d{2}", core):  # rok publikacji
            continue
        if re.fullmatch(r"\d+", core) and len(core) < 2:
            continue
        cores.add(core)
    return cores


def citations(text: str, url_to_sid: dict[str, str] | None = None) -> set[tuple[str, str]]:
    """Zestaw (źródło, timestamp) z cytowań w tekście markdown."""
    out: set[tuple[str, str]] = set()
    for m in CITE_RE.finditer(text):
        video_id = m.group(3)
        sid = (url_to_sid or {}).get(video_id, video_id)
        out.add((sid, m.group(1)))
    for m in PAREN_CITE_RE.finditer(text):
        out.add((m.group(1), m.group(2)))
    return out


def check(md: str, kb: dict, files: dict[str, str]) -> tuple[list[str], list[str]]:
    problems: list[str] = []
    warnings: list[str] = []

    def problem(msg: str) -> None:
        problems.append(msg)

    def warn(msg: str) -> None:
        warnings.append(msg)

    # --- 1. wymagane pliki -----------------------------------------------------
    for rel in REQUIRED_FILES:
        if rel not in files:
            problem(f"brak wymaganego pliku: {rel}")

    # --- 2. wersja bazy --------------------------------------------------------
    md_version = re.search(r"^Wersja:\s*(\S+)", md, re.MULTILINE)
    if not md_version:
        problem("brak linii 'Wersja: X' w references/knowledge_base_hipertrofia.md")
    elif md_version.group(1) != kb.get("version"):
        problem(
            f"wersja bazy niespójna: md {md_version.group(1)} vs json {kb.get('version')!r}"
        )

    # --- 3. taksonomia kind/confidence ----------------------------------------
    kinds = set(kb.get("kind_legend") or {})
    confidences = set(kb.get("confidence_legend") or {})
    if kinds != set(KIND_LEGEND):
        problem(
            "kind_legend w JSON nie zgadza się ze słownikiem skryptu: "
            f"{sorted(kinds)} vs {sorted(KIND_LEGEND)}"
        )
    if confidences != set(CONFIDENCE_LEGEND):
        problem(
            "confidence_legend w JSON nie zgadza się ze słownikiem skryptu: "
            f"{sorted(confidences)} vs {sorted(CONFIDENCE_LEGEND)}"
        )
    for name, legend in (("kind", KIND_LEGEND), ("confidence", CONFIDENCE_LEGEND)):
        for value in legend:
            if f"`{value}`" not in md:
                problem(f"brak wartości `{value}` w legendzie taksonomii ({name}) w pliku md")

    for p in kb.get("principles", []):
        pid = p.get("id", "?")
        if not PRINCIPLE_RE.match(str(pid)):
            problem(f"{pid}: id nie ma formatu P##")
        if p.get("kind") not in KIND_LEGEND:
            problem(f"{pid}: nieznany kind {p.get('kind')!r}")
        if p.get("confidence") not in CONFIDENCE_LEGEND:
            problem(f"{pid}: nieznany confidence {p.get('confidence')!r}")
        if not p.get("rule"):
            problem(f"{pid}: brak treści reguły")
        if not p.get("source") or not p.get("timestamp"):
            problem(f"{pid}: brak źródła lub timestampu")
        elif not TIMESTAMP_RE.match(str(p.get("timestamp"))):
            problem(f"{pid}: timestamp {p.get('timestamp')!r} ma zły format")
        if p.get("kind") == "author_addition" and p.get("source"):
            problem(f"{pid}: kind=author_addition, ale podano źródło")
        if p.get("kind") == "editorial_caution" and not p.get("speaker"):
            warn(f"{pid}: kind=editorial_caution bez pola 'speaker' (kogo dotyczy uwaga)")

    ids = [p.get("id") for p in kb.get("principles", [])]
    if len(set(ids)) != len(ids):
        problem("duplikaty id w tablicy principles")
    expected = [f"P{i:02d}" for i in range(1, len(ids) + 1)]
    if ids != expected:
        problem(f"id principles nie są kolejne: oczekiwano {expected[0]}..{expected[-1]}")

    # --- 4. tablica liczb: json <-> md ----------------------------------------
    table = numbers_table(md)
    if not table:
        problem("brak sekcji 'Wszystkie liczby w bazie' w pliku md")
        table = ""
    md_values = table_values(table)
    md_value_set = set(md_values)
    json_values = [q.get("value", "") for q in kb.get("quantitative_claims", [])]
    json_value_set = set(json_values)

    for value in md_values:
        if md_values.count(value) > 1:
            problem(f"liczba {value!r} występuje w tabeli więcej niż raz")

    for q in kb.get("quantitative_claims", []):
        value = q.get("value", "")
        if not value:
            problem("liczba bez wartości w quantitative_claims")
            continue
        if value not in md_value_set:
            problem(
                f"liczba {value!r} jest w JSON, ale nie ma wiersza w kolumnie "
                f"'Wartość' tabeli 'Wszystkie liczby w bazie'"
            )
        kind = q.get("kind")
        if kind is not None and kind not in KIND_LEGEND:
            problem(f"liczba {value!r}: nieznany kind {kind!r}")
        if q.get("source") is None and kind != "author_addition":
            problem(f"liczba {value!r} bez źródła musi mieć kind=author_addition")
        src = q.get("source")
        if src:
            _, _, ts = src.partition("@")
            if ts and ts not in table:
                problem(f"liczba {value!r}: kotwica {src} nie występuje w tabeli liczb")
    for value in md_values:
        if value not in json_value_set:
            problem(f"wiersz {value!r} jest w tabeli md, ale brak go w quantitative_claims (JSON)")

    duplicates = sorted({v for v in json_values if v and json_values.count(v) > 1})
    for value in duplicates:
        problem(f"zduplikowana liczba w quantitative_claims: {value!r}")

    # --- 5. każda liczba z treści ma być w tabeli liczb ------------------------
    sections = md_sections(md)
    body = "\n".join(
        text for name, text in sections.items()
        if name not in ("Wszystkie liczby w bazie", "Zawartość")
    )
    body = re.sub(r"\[\d{1,2}:\d{2}(?::\d{2})?\]\([^)]*\)", " ", body)   # znaczniki czasu
    body = re.sub(r"§\s?\d+(\.\d+)?", " ", body)                        # numery sekcji
    value_cores = numeric_cores(" ".join(md_values))
    value_text = " ".join(md_values)

    def covered(core: str) -> bool:
        if core in value_cores:
            return True
        # liczba może być podzakresem wiersza, np. 250 w "250–300 kcal"
        return re.search(rf"(?<![\d.,]){re.escape(core)}(?![\d.,])", value_text) is not None

    missing_cores = sorted(c for c in numeric_cores(body) if not covered(c))
    for core in missing_cores:
        problem(
            f"liczba {core!r} pojawia się w treści, ale nie ma wiersza w kolumnie "
            f"'Wartość' tabeli 'Wszystkie liczby w bazie'"
        )

    # --- 6. cytowania md <-> json ---------------------------------------------
    url_to_sid = {s["url"].rstrip("/").split("/")[-1]: s["id"] for s in kb.get("sources", [])}
    md_cites = citations(md, url_to_sid)
    json_cites: set[tuple[str, str]] = set()
    for p in kb.get("principles", []):
        json_cites.add((p["source"], p["timestamp"]))
        for key in ("additional_sources", "conflicts_with"):
            for item in p.get(key, []):
                sid, _, ts = item.partition("@")
                json_cites.add((sid, ts))
    for st in kb.get("source_tensions", []):
        for item in st.get("sources", []):
            sid, _, ts = item.partition("@")
            json_cites.add((sid, ts))
    for q in kb.get("quantitative_claims", []):
        for item in [q.get("source")] + q.get("additional_sources", []):
            if item:
                sid, _, ts = item.partition("@")
                json_cites.add((sid, ts))

    for p in kb.get("principles", []):
        if (p["source"], p["timestamp"]) not in md_cites:
            problem(
                f"{p['id']}: zasada {p['source']}@{p['timestamp']} nie ma cytowania w pliku md"
            )
    for m in CITE_RE.finditer(md):
        ts, url, off = m.group(1), m.group(2), int(m.group(4))
        if secs(ts) != off:
            problem(f"{url}: etykieta czasu {ts} nie zgadza się z offsetem ?t={off}")
    md_only = sorted(md_cites - json_cites)
    if md_only:
        warn(
            f"{len(md_only)} cytowań jest tylko w pliku md (nie ma ich w zasadach JSON) — "
            f"plik md jest bogatszy: "
            + ", ".join(f"{s}@{t}" for s, t in md_only[:6])
        )

    # --- 7. źródła ------------------------------------------------------------
    source_ids = {s["id"] for s in kb.get("sources", [])}
    if source_ids != {f"S{i}" for i in range(1, len(source_ids) + 1)}:
        problem(f"identyfikatory źródeł nie są ciągłe: {sorted(source_ids)}")
    for s in kb.get("sources", []):
        if not s.get("url"):
            problem(f"źródło {s['id']} bez url")
        if s["url"] not in md:
            problem(f"url źródła {s['id']} nie występuje w pliku md")
        if not s.get("topic"):
            warn(f"źródło {s['id']} bez opisu tematu")
    for p in kb.get("principles", []):
        if p.get("source") not in source_ids:
            problem(f"{p['id']}: nieznane źródło {p.get('source')!r}")

    # --- 8. osoby -------------------------------------------------------------
    people = kb.get("people", [])
    if not people:
        problem("brak tablicy people")
    for person in people:
        if person.get("name") not in md:
            problem(f"osoba {person.get('name')!r} nie występuje w sekcji 'Kto jest kim'")
        for sid in person.get("sources", []):
            if sid not in source_ids:
                problem(f"osoba {person.get('name')!r}: nieznane źródło {sid}")
    md_people_section = sections.get("Kto jest kim", "")
    for person in people:
        if person.get("name") and person["name"] not in md_people_section:
            warn(f"osoba {person['name']!r} nie występuje w sekcji 'Kto jest kim'")
    attributed = {sid for person in people for sid in person.get("sources", [])}
    for sid in sorted(source_ids):
        if sid not in attributed:
            problem(f"źródło {sid} nie jest przypisane do żadnej osoby w tablicy people")

    # --- 9. granice wiedzy ----------------------------------------------------
    limits = kb.get("knowledge_limits", [])
    if len(limits) < 5:
        problem(f"w JSON jest za mało wpisów knowledge_limits ({len(limits)})")
    if "### Granice wiedzy" not in md:
        problem("brak sekcji 'Granice wiedzy' w pliku md")
    md_limits = sections.get("Ograniczenia i bezpieczeństwo", "")
    md_limit_bullets = 0
    in_limits = False
    for line in md_limits.splitlines():
        if line.startswith("### "):
            in_limits = line.startswith("### Granice wiedzy")
            continue
        if in_limits and line.startswith("- "):
            md_limit_bullets += 1
    if md_limit_bullets != len(limits):
        problem(
            f"liczba granic wiedzy: json {len(limits)} vs sekcja 'Granice wiedzy' w md "
            f"{md_limit_bullets} (muszą się zgadzać)"
        )

    # --- 10. warstwa weryfikacji ----------------------------------------------
    review = kb.get("evidence_review", {})
    verdicts = review.get("verdicts", [])
    review_doc = files.get("references/weryfikacja_naukowa.md", "")
    md_rows = []
    if "## 1. Tabela zbiorcza" in review_doc:
        chunk = review_doc.split("## 1. Tabela zbiorcza", 1)[1].split("\n---", 1)[0]
        for line in chunk.splitlines():
            if not re.match(r"^\|\s*\d+\s*\|", line):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 4:
                problem(f"wiersz tabeli zbiorczej bez 4 kolumn: {line[:60]!r}")
                continue
            md_rows.append((int(cells[0]), cells[1], cells[2]))
    else:
        problem("brak sekcji '## 1. Tabela zbiorcza' w references/weryfikacja_naukowa.md")
    if len(md_rows) != len(verdicts):
        problem(
            f"tabela zbiorcza ma {len(md_rows)} wierszy, a evidence_review.verdicts "
            f"{len(verdicts)} werdyktów — muszą być 1:1"
        )
    for (num, claim, symbol), verdict in zip(md_rows, verdicts):
        expected = SYMBOL_TO_VERDICT.get(symbol)
        if expected is None:
            problem(
                f"tabela zbiorcza #{num}: symbol {symbol!r} spoza skali "
                f"{sorted(SYMBOL_TO_VERDICT)}"
            )
        elif expected != verdict.get("verdict"):
            problem(
                f"tabela zbiorcza #{num} ({claim[:40]!r}): symbol {symbol} oznacza "
                f"{expected!r}, a werdykt JSON to {verdict.get('verdict')!r}"
            )
    for key, meaning in review.get("legend", {}).items():
        if key not in VERDICTS:
            problem(f"evidence_review.legend ma nieznany werdykt {key!r}")
        if not meaning:
            problem(f"evidence_review.legend: brak opisu werdyktu {key!r}")
    known_sources = set(json_cites)
    for v in verdicts:
        if v.get("verdict") not in VERDICTS:
            problem(f"werdykt {v.get('claim')!r}: nieznana wartość {v.get('verdict')!r}")
        src = v.get("source", "")
        sid, _, ts = src.partition("@")
        if sid not in source_ids:
            problem(f"werdykt {v.get('claim')!r}: nieznane źródło {src!r}")
        elif (sid, ts) not in known_sources:
            warn(f"werdykt {v.get('claim')!r}: kotwica {src} nie występuje w zasadach/ liczbach JSON")
        for pid in v.get("principles", []):
            if pid not in ids:
                problem(f"werdykt {v.get('claim')!r}: nieznane id zasady {pid!r}")

    # --- 11. format odpowiedzi ------------------------------------------------
    template = kb.get("response_template", [])
    skill = files.get("SKILL.md", "")
    for field in template:
        if field not in skill:
            problem(f"format odpowiedzi: brak etykiety {field!r} w SKILL.md")

    # --- 12. dokumentacja plików ---------------------------------------------
    for key in ("version", "sources", "principles", "author_additions",
                "source_tensions", "evidence_review", "safety", "response_template"):
        if key not in kb:
            problem(f"brak klucza {key!r} w JSON")
    install = files.get("INSTALL.md", "")
    for rel in REQUIRED_FILES:
        if rel.startswith("references/") and rel not in install:
            warn(f"INSTALL.md nie wymienia pliku {rel} w tabeli 'Co zawiera instalacja'")
    readme = files.get("README.md", "")
    for rel in ("SKILL.md", "references/knowledge_base_hipertrofia.md",
                "references/knowledge_base_hipertrofia.json"):
        if rel not in readme:
            warn(f"README.md nie wymienia pliku {rel}")

    # --- 13. taksonomia wspomniana w treści -----------------------------------
    for name, text in files.items():
        if not name.endswith(".md"):
            continue
        for match in re.finditer(r"`kind`\s*[:=]\s*`([a-z_]+)`|kind:\s*`([a-z_]+)`", text):
            value = match.group(1) or match.group(2)
            if value not in KIND_LEGEND:
                problem(f"{name}: nieaktualna wartość kind {value!r} w treści")
        for match in re.finditer(r"`confidence`\s*[:=]\s*`([a-z_]+)`|confidence:\s*`([a-z_]+)`", text):
            value = match.group(1) or match.group(2)
            if value not in CONFIDENCE_LEGEND:
                problem(f"{name}: nieaktualna wartość confidence {value!r} w treści")

    # --- 14. zakazane sformułowania ------------------------------------------
    for name, text in files.items():
        if not name.endswith((".md", ".json", ".yaml")):
            continue
        for phrase in FORBIDDEN_PHRASES:
            if phrase in text:
                problem(f"{name}: zawiera nieaktualne sformułowanie {phrase!r}")

    return problems, warnings


def run_checks(repo: Path) -> tuple[list[str], list[str]]:
    """Wykonuje wszystkie kontrole i zwraca (problemy, ostrzeżenia)."""
    files = {}
    for path in sorted(repo.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(repo).as_posix()
        if rel.startswith(".git/") or "/.git/" in rel:
            continue
        if path.suffix in (".md", ".json", ".yaml"):
            try:
                files[rel] = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
    md = files.get("references/knowledge_base_hipertrofia.md", "")
    json_path = repo / "references" / "knowledge_base_hipertrofia.json"
    try:
        kb = json.loads(json_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return ([f"{json_path.name}: nie jest poprawnym JSON-em: {exc}"], [])
    return check(md, kb, files)


def main() -> int:
    parser = argparse.ArgumentParser(description="Kontrola spójności bazy wiedzy coach-arek")
    parser.add_argument("--repo", default=str(Path(__file__).resolve().parent.parent),
                        help="katalog repozytorium (domyślnie katalog nadrzędny skryptu)")
    parser.add_argument("--quiet", action="store_true", help="tylko kod wyjścia, bez raportu")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    problems, warnings = run_checks(repo)

    if not args.quiet:
        for w in warnings:
            print(f"UWAGA: {w}")
        if problems:
            print(f"\nZNALEZIONE NIESPOJNOŚCI ({len(problems)}):")
            for p in problems:
                print(f"  - {p}")
        else:
            print("OK: wszystkie kontrole przeszły.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
