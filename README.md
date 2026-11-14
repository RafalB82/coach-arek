# Coach Arek

Skill w formacie Agent Skills do praktycznego nadzoru procesu treningowego, ze szczególnym naciskiem na hipertrofię. Pomaga analizować ciągłość planu, objętość i progresję treningową, regenerację oraz trendy masy ciała i kaloryczności.

## Jak powstał

Skill powstał na prośbę użytkownika jako źródło wiedzy dla agenta nadzorującego trening. Punktem wyjścia było dziesięć polskojęzycznych materiałów z Arkadiuszem Czerwem: dziewięć rozmów (z Pawłem Albrechtem, Dawidem Olszewskim lub Robusiem Pasjonatem) oraz jeden materiał treningowy. Transkrypcje przygotowano wcześniej z nagrań za pomocą lokalnego workflow MLX Whisper, poprawiono redakcyjnie i uzupełniono o przypisanie mówców. Pełne transkrypcje nie są dołączone do tego publicznego repozytorium; repo zawiera syntezę tematyczną, identyfikatory źródeł, linki i timestampy.

Na podstawie tych materiałów przygotowano:

- `references/knowledge_base_hipertrofia.md` — tematyczną syntezę, zasady operacyjne, zastrzeżenia i odnośniki do fragmentów źródłowych;
- `references/knowledge_base_hipertrofia.json` — ustrukturyzowaną wersję bazy do wyszukiwania i dopasowywania reguł, z blokiem `evidence_review`;
- `references/weryfikacja_naukowa.md` — przegląd zgodności twierdzeń z aktualnymi syntezami i metaanalizami (stan: listopad 2026), z werdyktami i bibliografią;
- `SKILL.md` — instrukcje określające, kiedy i jak agent ma korzystać z syntezy i źródeł;
- `INSTALL.md` — instalacja w Codexie i Claude Code: wariant prosty oraz jedno źródło z symlinkami.

Synteza kładzie nacisk na monitorowanie trendów i zachowanie ciągłości procesu, zamiast pochopnego zmieniania całego planu po pojedynczym słabszym treningu. Zalecenia są ostrożnymi, indywidualizowanymi hipotezami do monitorowania. Skill uwzględnia też granice bezpieczeństwa: nie diagnozuje, nie zaleca dopingu ani leków i kieruje sygnały alarmowe do odpowiedniego specjalisty.

## Weryfikacja naukowa

Baza nie jest zbiorem niepodważalnych twierdzeń. Obok syntezy źródeł zawiera warstwę weryfikacji, która rozdziela trzy poziomy:

- **praktykę źródłową** — „Arkadiusz tak robi”;
- **praktykę popartą** — kierunek zgodny z aktualnymi syntezami i metaanalizami;
- **twierdzenie weryfikowalne** — wymaga danych, których podcast nie dostarcza (np. mechanizm „whoosh”, tempo przyrostu 10–12 kg, częstość prawdziwego OTS).

Warstwa składa się z:

- `references/weryfikacja_naukowa.md` — 25 twierdzeń z werdyktami, uzasadnieniami i bibliografią (stan: listopad 2026);
- bloku `evidence_review` w `references/knowledge_base_hipertrofia.json` — te same werdykty w formie do wyszukiwania, przypisane do źródeł i timestampów;
- sekcji „Weryfikacja naukowa” w `references/knowledge_base_hipertrofia.md` — skrót najważniejszych korekt.

Najważniejsze korekty dotyczą snu i przetrenowania, dawki podtrzymującej 1/3 objętości, diet breaków, mechanizmu „whoosh”, progu dla stretchingu oraz skali przyrostu 10–12 kg w pierwszym roku. Weryfikacja jest celowa, nie systematyczna: nie jest przeglądem całej literatury i nie zamienia poradnika trenerskiego w wytyczną medyczną.

## Instalacja

Skill działa w Codexie i Claude Code, bo oba czytają format Agent Skills: katalog z `SKILL.md` i materiałami w `references/`. Nie wymaga Pythona, Node ani MCP.

Claude Code — skill osobisty:

```bash
git clone https://github.com/RafalB82/coach-arek.git ~/.claude/skills/coach-arek
```

Codex — skill użytkownika:

```bash
git clone https://github.com/RafalB82/coach-arek.git ~/.agents/skills/coach-arek
```

Starsze buildy Codexa czytają `~/.codex/skills`; wtedy zainstaluj lub podlinkuj skill także tam. Pełna instrukcja, wariant z jednym checkoutem i symlinkami, weryfikacja i typowe problemy: **[INSTALL.md](INSTALL.md)**.

## Podstawa źródłowa

Linki prowadzą do materiałów pierwotnych. S1–S4, S9 i S10 to rozmowy Pawła Albrechta z Arkadiuszem Czerwem, S5 to rozmowa Dawida Olszewskiego z Arkadiuszem, S6 to materiał treningowy Arkadiusza, a S7–S8 to rozmowy Arkadiusza z Robusiem Pasjonatem. Pełne transkrypcje nie są publikowane w tym repozytorium.

| ID | Temat | Nagranie |
|---|---|---|
| S1 | Redukcja tkanki tłuszczowej | [YouTube](https://youtu.be/bpSubkCA168) |
| S2 | Budowanie masy mięśniowej i hipertrofia | [YouTube](https://youtu.be/XLTbnKL_fwk) |
| S3 | Układanie planu treningowego | [YouTube](https://youtu.be/IIi8e4i6pZE) |
| S4 | Dieta i kaloryczność | [YouTube](https://youtu.be/ySgq9XysjD0) |
| S5 | Programowanie planu treningowego — Dawid Olszewski i Arkadiusz Czerw | [YouTube](https://youtu.be/h2Vj5ai9Ang) |
| S6 | Praktyczny trening, progresja i objętość — Arkadiusz Czerw | [YouTube](https://youtu.be/blaB3aBrf1o) |
| S7 | Programowanie treningu, wysiłek, przerwy, regeneracja i żywienie — Arkadiusz Czerw i Robuś Pasjonat | [YouTube](https://youtu.be/Xb2y18_B0QY) |
| S8 | Trening siłowy, redukcja tkanki tłuszczowej, cardio i autoregulacja — Arkadiusz Czerw i Robuś Pasjonat | [YouTube](https://youtu.be/54BCbUZaHo0) |
| S9 | Stara i nowa szkoła kulturystyki, hipertrofia, pompa, przerwy i superserie — Paweł Albrecht i Arkadiusz Czerw | [YouTube](https://youtu.be/U_shUYXSiHM) |
| S10 | Przełamywanie stagnacji w redukcji, budowaniu masy i sile — Paweł Albrecht i Arkadiusz Czerw | [YouTube](https://youtu.be/Xs-YqL1bBII) |

Synteza wskazuje identyfikatory źródeł i znaczniki czasu, aby można było sprawdzić kontekst konkretnej wypowiedzi w nagraniu. Gdy potrzebny jest dokładny cytat, szerszy kontekst albo porównanie wypowiedzi, należy sprawdzić oryginalne nagranie.

Uwaga redakcyjna do S7: nagranie z kanału KFD.pl, gospodarz to Robuś Pasjonat. W kopii transkrypcji dołączonej do skilla etykiety mówców są poprawne (oryginał z globalnie zamienionymi etykietami nie jest w pakiecie). Z nagrania usunięto klauzulę kanałową, reklamę w intro i promocyjną przyśpiewkę na outro.

Uwaga redakcyjna do S8: nagranie z kanału KFD.pl, gospodarz to Robuś Pasjonat. W kopii transkrypcji dołączonej do skilla etykiety mówców są poprawne; montaż i reklama w pierwszej minucie pozostają w pliku.

Uwaga redakcyjna do S9: prowadzącym jest Paweł Albrecht, gościem Arkadiusz Czerw. Diarization skleił krótką odpowiedź Arkadiusza przy 00:53 z wypowiedzią Pawła; w lokalnej transkrypcji rozdzielono ją ręcznie. Twierdzenia o literaturze nie są tu niezależnie zweryfikowane.

Uwaga redakcyjna do S10: prowadzącym jest Paweł Albrecht, gościem Arkadiusz Czerw. Transkrypcja powstała lokalnie z MLX Whisper large-v3 i diaryzacji pyannote; etykiety mówców sprawdzono po treści. ASR może zniekształcać pojedyncze słowa, a liczby i twierdzenia o literaturze weryfikuj w nagraniu.

## Ważne ograniczenie

Repozytorium dokumentuje wiedzę przekazaną w wymienionych rozmowach. Warstwa weryfikacji oznacza, gdzie kierunek twierdzenia zgadza się z aktualnymi syntezami, a gdzie jest uproszczeniem lub opinią bez podstaw — ale nie jest systematycznym przeglądem całej literatury. Konkretne liczby, prognozy tempa zmian oraz szerokie twierdzenia fizjologiczne należy traktować jako wypowiedzi rozmówców lub praktyczne hipotezy, a nie gwarantowane prawa ani spersonalizowaną poradę medyczną.

## Zawartość

```text
coach-arek/
├── SKILL.md
├── README.md
├── .gitignore
├── agents/
│   └── openai.yaml
└── references/
    ├── knowledge_base_hipertrofia.json
    └── knowledge_base_hipertrofia.md
```

Publiczna paczka to wyłącznie pliki powyżej. Nagrania źródłowe, wygenerowane transkrypcje i skrypty pipeline trzymane są lokalnie w katalogu `mlx_whisper/`, który jest świadomie pomijany przez git (`.gitignore`) — nie są potrzebne do użycia skilla.

## Poza repozytorium: lokalne źródła i pipeline

Poniżej opisany katalog `mlx_whisper/` nie jest częścią repozytorium (patrz `.gitignore`) — to lokalne źródła, pipeline i transkrypcje. Opisuję go, bo transkrypcje są źródłem cytowań w `references/`: każdy plik `.md` ma w nagłówku linię `Pipeline:` z użytymi ustawieniami (źródło etykiet, cięcia redakcyjne, podział bloków), więc plik opisuje sam siebie.

- **Przebudowa bez modelu** (deterministyczna, ~2 s dla ośmiu nagrań): `cd mlx_whisper && ./transkrypcja.sh --rebuild` — bierze czasy słów z gotowego JSON-a, a etykiety mówców z istniejącego Markdowna, i odtwarza pliki `.md` (dla S5–S8 bajt w bajt; S1–S4 różnią się drobną redakcją ASR i kolejnością mówców w nagłówku, bo ich pliki `.md` powstały z wcześniejszej wersji JSON-a).
- **Pełny przebieg** wymaga `yt-dlp`, `mlx_whisper` i środowiska z `pyannote.audio` (`DIAR_PY`, domyślnie `~/diar311/bin/python`): `cd mlx_whisper && ./transkrypcja.sh`.
- Ustawienia per nagranie (mapa nazw mówców, liczba mówców, cięcia, podział bloków) są w skrypcie i można je nadpisać zmiennymi `NAMES_<id>`, `SPEAKERS_<id>`, `DROP_WORDS_<id>`, `MAX_BLOCK_<id>`, `SOURCE_URL_<id>`, `RENAME_<id>`.

### Kontrola jakości bazy wiedzy

Lokalny skrypt `mlx_whisper/check_citations.py` (poza repozytorium, razem z transkrypcjami) sprawdza, czy baza nadal jest spójna z transkrypcjami: każde cytowanie musi trafiać w blok transkrypcji i w odległości, którą da się odnaleźć w pliku, atrybucja mówcy w zasadach JSON musi zgadzać się z etykietą w transkrypcji, linki `?t=` muszą odpowiadać etykiecie czasu, pliki md i json muszą się zgadzać w zakresie cytowań, a tabela liczb, tabela osób i granice wiedzy muszą istnieć w obu formatach. Skrypt zwraca kod 1, gdy znajdzie niezgodność — warto uruchamiać go po każdej zmianie `references/`.

Uwagi do konkretnych plików:

- **S5** (`h2Vj5ai9Ang`) to nagranie z kanału HSS (`@dawidolszewski`); gospodarz to **Dawid Olszewski** — ta sama osoba, której Arkadiusz w rozmowie nazywa „Dawid". To nie jest gospodarz z S7/S8.
- **S6** (`blaB3aBrf1o`) to monolog Arkadiusza; plik `.md` dzieli go na bloki ~25 s na granicach segmentów Whispera, bo model diarization nie dzieli nagrania jednogłosowego.
- **S7** (`Xb2y18_B0QY`) pozbawiono klauzuli kanałowej (0:00–0:25), reklamy w intro (1:05–1:19) i promocyjnej przyśpiewki na outro (1:08:39–1:08:59) — te fragmenty nie są ani wypowiedzią gospodarza, ani gościa. Zakresy cięć zapisuje linia `Pipeline:` w nagłówku pliku.

## Korzystanie ze skilla

Folder `coach-arek/` jest kompletnym publicznym skillem Codex opartym na syntezie źródeł. Instrukcje działania znajdują się w `SKILL.md`, synteza MD/JSON w katalogu `references/`, a metadane interfejsu w `agents/openai.yaml`. Pełne transkrypcje nie są częścią publicznej paczki.
