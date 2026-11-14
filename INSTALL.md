# Instalacja

Skill `coach-arek` działa w Codexie i Claude Code, bo oba czytają format [Agent Skills](https://agentskills.io): katalog z plikiem `SKILL.md` i opcjonalnymi materiałami w `references/`.

Skill jest **tylko instrukcjami** — nie uruchamia skryptów, nie instaluje zależności i nie wymaga kluczy API. Cztery pliki w `references/` to baza wiedzy i weryfikacja naukowa; pełne transkrypcje nie są częścią publicznego repo, więc timestampy prowadzą do YouTube.

## Wymagania

- Codex CLI / IDE extension albo Claude Code,
- `git` (zalecane) lub możliwość skopiowania katalogu,
- nic więcej — Python, Node i MCP nie są potrzebne.

## Wariant A: prosta instalacja (osobno dla każdego narzędzia)

### Claude Code

Skill osobisty, dostępny we wszystkich projektach na tej maszynie:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/RafalB82/coach-arek.git ~/.claude/skills/coach-arek
```

Skill projektowy, commitowany razem z repozytorium:

```bash
mkdir -p .claude/skills
git clone https://github.com/RafalB82/coach-arek.git .claude/skills/coach-arek
rm -rf .claude/skills/coach-arek/.git
```

Po instalacji uruchom Claude Code i wpisz `/skills` — `coach-arek` powinien być na liście. Możesz też wywołać go wprost:

```text
/coach-arek
```

albo pozwolić Claude’owi wybrać skill po opisie, np.:

```text
Mam zastój w redukcji od trzech tygodni. Co sprawdzić najpierw?
```

### Codex

Aktualna dokumentacja OpenAI wskazuje katalog użytkownika `~/.agents/skills`:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/RafalB82/coach-arek.git ~/.agents/skills/coach-arek
```

W repozytorium projektowym odpowiednikiem jest `.agents/skills`:

```bash
mkdir -p .agents/skills
git clone https://github.com/RafalB82/coach-arek.git .agents/skills/coach-arek
rm -rf .agents/skills/coach-arek/.git
```

**Starsze buildy Codexa** czytają `~/.codex/skills` — tak ten skill był pierwotnie zainstalowany. Jeśli Twoja wersja nie widzi skilla w `~/.agents/skills`, dodaj go także tam:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/RafalB82/coach-arek.git ~/.codex/skills/coach-arek
```

W Codex CLI sprawdź listę przez `/skills` i wywołaj skill wprost:

```text
$coach-arek
```

albo z opcjonalnym pytaniem:

```text
$coach-arek Oceń mój plan pod kątem objętości tygodniowej.
```

## Wariant B: jedno źródło i symlinki (Codex + Claude Code)

Jeżeli używasz obu narzędzi, trzymaj jeden checkout i podlinkuj go w oba miejsca. Aktualizacja to wtedy jedno `git pull`.

```bash
mkdir -p ~/.local/share ~/.claude/skills ~/.agents/skills
git clone https://github.com/RafalB82/coach-arek.git ~/.local/share/coach-arek

ln -s ~/.local/share/coach-arek ~/.claude/skills/coach-arek
ln -s ~/.local/share/coach-arek ~/.agents/skills/coach-arek
```

Dla starszych buildów Codexa dodaj jeszcze:

```bash
mkdir -p ~/.codex/skills
ln -s ~/.local/share/coach-arek ~/.codex/skills/coach-arek
```

Claude Code obsługuje symlinki katalogów skilli; Codex również podąża za symlinkiem. Nie kopiuj tego samego skilla pod dwiema różnymi nazwami — to tworzy duplikaty na liście.

## Weryfikacja

Sprawdź, czy plik istnieje i ma poprawny frontmatter:

```bash
head -5 ~/.claude/skills/coach-arek/SKILL.md     # Claude Code
head -5 ~/.agents/skills/coach-arek/SKILL.md     # Codex
```

Oczekiwany początek:

```yaml
---
name: coach-arek
description: "Monitor and reason about resistance-training hypertrophy..."
---
```

Test działania:

1. **Claude Code** — `/skills`, potem `/coach-arek` albo pytanie o zastój, objętość lub trend masy.
2. **Codex** — `/skills`, potem `$coach-arek` albo pytanie o ten sam temat.

Poprawna odpowiedź powinna:
- odwołać się do źródeł `S1`–`S10` i timestampów,
- sprawdzić kontekst liczby, zanim ją poda,
- rozróżnić praktykę źródłową, praktykę popartą i twierdzenie niepotwierdzone,
- nie diagnozować i nie przepisywać całego planu po jednej sesji.

## Aktualizacja

```bash
git -C ~/.claude/skills/coach-arek pull --ff-only
git -C ~/.agents/skills/coach-arek pull --ff-only
# lub, w wariancie B:
git -C ~/.local/share/coach-arek pull --ff-only
```

Claude Code wykrywa zmiany w `~/.claude/skills/` w trakcie sesji. Codex również wykrywa zmiany automatycznie; jeśli nowa wersja się nie pojawia, zrestartuj narzędzie.

## Odinstalowanie

```bash
rm -rf ~/.claude/skills/coach-arek
rm -rf ~/.agents/skills/coach-arek
rm -rf ~/.codex/skills/coach-arek
```

W wariancie B usuń najpierw symlinki, potem checkout:

```bash
rm ~/.claude/skills/coach-arek ~/.agents/skills/coach-arek
rm -rf ~/.local/share/coach-arek
```

## Typowe problemy

| Objaw | Przyczyna | Rozwiązanie |
|---|---|---|
| Skill nie pojawia się na liście | zły katalog lub brak `SKILL.md` w katalogu głównym | sprawdź ścieżkę i `head -5 SKILL.md` |
| Frontmatter nie działa | `---` nie jest w pierwszej linii pliku | usuń puste linie przed frontmatterem |
| Claude Code nie widzi nowego katalogu | katalog skilli powstał po starcie sesji | `/reload-skills` lub restart |
| Codex nie widzi skilla | starsza wersja czyta `~/.codex/skills` | dodaj symlink także tam |
| Dwa razy ten sam skill | klon i symlink pod różnymi nazwami | zostaw jedno źródło i jeden wpis |
| Skill nie działa w sesji chmurowej Claude | sesje chmurowe nie czytają `~/.claude/skills` | użyj skilla projektowego albo pluginu |
| Opis skilla jest skrócony | Codex limituje rozmiar listy przy wielu skillach | usuń nieużywane skille lub zwiększ `skills.max_context_tokens` |

## Co zawiera instalacja

| Plik | Rola |
|---|---|
| `SKILL.md` | instrukcje i reguły operacyjne agenta |
| `references/knowledge_base_hipertrofia.md` | synteza źródeł, zasady, zastrzeżenia, timestampy |
| `references/knowledge_base_hipertrofia.json` | wersja strukturalna z blokiem `evidence_review` |
| `references/weryfikacja_naukowa.md` | weryfikacja twierdzeń względem aktualnych badań |
| `README.md` | opis projektu i podstawy źródłowej |
| `agents/openai.yaml` | opcjonalne metadane UI dla Codexa |

## Bezpieczeństwo

Skill nie zawiera porad medycznych, nie diagnozuje i nie zaleca dopingu ani leków. Przy bólu, urazie, zaburzeniach odżywiania lub chorobie kieruje do specjalisty. Weryfikacja naukowa jest celowa, nie systematyczna — nie zastępuje indywidualnej konsultacji.
