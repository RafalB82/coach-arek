# Coach Arek

Skill w formacie Agent Skills do praktycznego nadzoru procesu treningowego, ze szczególnym naciskiem na hipertrofię. Pomaga analizować ciągłość planu, objętość i progresję treningową, regenerację oraz trendy masy ciała i kaloryczności.

## Jak powstał

Skill powstał na prośbę użytkownika jako źródło wiedzy dla agenta nadzorującego trening. Punktem wyjścia było dziesięć polskojęzycznych materiałów z Arkadiuszem Czerwem: dziewięć rozmów (z Pawłem Albrechtem, Dawidem Olszewskim lub Robusiem Pasjonatem) oraz jeden materiał treningowy. Transkrypcje przygotowano wcześniej z nagrań za pomocą lokalnego workflow MLX Whisper, poprawiono redakcyjnie i uzupełniono o przypisanie mówców. Pełne transkrypcje nie są dołączone do tego publicznego repozytorium; repo zawiera syntezę tematyczną, identyfikatory źródeł, linki i timestampy.

Na podstawie tych materiałów przygotowano:

- `references/knowledge_base_hipertrofia.md` — tematyczną syntezę, zasady operacyjne, zastrzeżenia i odnośniki do fragmentów źródłowych;
- `references/knowledge_base_hipertrofia.json` — ustrukturyzowaną wersję bazy do wyszukiwania i dopasowywania reguł, z blokiem `evidence_review` i jawną taksonomią `kind` (pochodzenie wpisu) oraz `confidence` (status epistemiczny);
- `references/weryfikacja_naukowa.md` — przegląd zgodności twierdzeń z aktualnymi syntezami i metaanalizami (stan: listopad 2026), z werdyktami i bibliografią;
- `SKILL.md` — instrukcje określające, kiedy i jak agent ma korzystać z syntezy i źródeł;
- `INSTALL.md` — instalacja w Codexie i Claude Code: wariant prosty, jedno źródło z symlinkami oraz wersja tylko GUI (bez terminala).

Synteza kładzie nacisk na monitorowanie trendów i zachowanie ciągłości procesu, zamiast pochopnego zmieniania całego planu po pojedynczym słabszym treningu. Zalecenia są ostrożnymi, indywidualizowanymi hipotezami do monitorowania. Skill uwzględnia też granice bezpieczeństwa: nie diagnozuje, nie zaleca dopingu ani leków i kieruje sygnały alarmowe do odpowiedniego specjalisty.

## Weryfikacja naukowa

Baza nie jest zbiorem niepodważalnych twierdzeń. Obok syntezy źródeł zawiera warstwę weryfikacji, która rozdziela trzy poziomy:

- **praktykę źródłową** — „Arkadiusz tak robi”;
- **praktykę popartą** — kierunek zgodny z aktualnymi syntezami i metaanalizami;
- **twierdzenie weryfikowalne** — wymaga danych, których podcast nie dostarcza (np. mechanizm „whoosh”, tempo przyrostu 10–12 kg, częstość prawdziwego OTS).

Warstwa składa się z:

- `references/weryfikacja_naukowa.md` — 26 twierdzeń z werdyktami, uzasadnieniami i bibliografią (stan: listopad 2026);
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

Starsze buildy Codexa czytają `~/.codex/skills`; wtedy zainstaluj lub podlinkuj skill także tam. Pełna instrukcja, wariant z jednym checkoutem i symlinkami, wersja tylko GUI, weryfikacja i typowe problemy: **[INSTALL.md](INSTALL.md)**.

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
├── INSTALL.md
├── LICENSE
├── LICENSE-CONTENT
├── .gitignore
├── .github/
│   └── workflows/
│       └── check.yml
├── agents/
│   └── openai.yaml
├── references/
│   ├── knowledge_base_hipertrofia.json
│   ├── knowledge_base_hipertrofia.md
│   └── weryfikacja_naukowa.md
├── repo-about.json
└── scripts/
    ├── check_consistency.py
    └── set_repo_about.py
```

Publiczna paczka to wyłącznie pliki powyżej. Nagrania źródłowe, wygenerowane transkrypcje i skrypty pipeline trzymane są lokalnie, poza repozytorium — nie są potrzebne do użycia skilla.

## Poza repozytorium: lokalne źródła i pipeline

Pipeline nie jest częścią repozytorium i nie ma go w tym katalogu. Żyje w `~/transkrypcja/`:

- `bin/transkrypcja.sh` — kolejka nagrań: `yt-dlp` → `mlx_whisper` (large-v3, word timestamps) → `bin/merge.py`;
- `bin/merge.py` — diaryzacja `pyannote` + scalanie słów w Markdown z blokami mówców;
- `out/` — wynikowe `.json` i `.md`; `audio/` — nagrania źródłowe.

Bez argumentów skrypt przetwarza cztery odcinki z zakodowanej listy, a z podanymi plikami audio działa w trybie ogólnym. Dostępne opcje to `--speakers N`, `--names "SPEAKER_00=Imię,SPEAKER_01=Imię"` i `--source-url URL`. Nie ma flagi przebudowy ani zmiennych per nagranie: jedyne nadpisanie dla pojedynczego odcinka to `NAMES_<id>` (mapa etykiet mówców), resztę ustawia się globalnie (`MODEL`, `LANGUAGE`, `SPEAKERS`, `MIN_SPEAKERS`, `MAX_SPEAKERS`, `OUT`, `AUDIO_DIR`, `DIAR_MODEL`, `DIAR_PY`, `PROMPT`, `YTDLP`).

Pełny przebieg wymaga `yt-dlp`, `mlx_whisper` w `PATH` i środowiska z `pyannote.audio` (`DIAR_PY`, domyślnie `~/diar311/bin/python`):

```bash
cd ~/transkrypcja && ./bin/transkrypcja.sh
```

Transkrypcje są artefaktem lokalnym: publiczne repo ich nie zawiera, a `references/transcripts/` w instalacji lokalnej to kopia z `~/transkrypcja/out/`. Wszystkie dziesięć nagrań jest dostępnych lokalnie — także S9 i S10.

### Kontrola jakości bazy wiedzy

Publiczny skrypt `scripts/check_consistency.py` sprawdza spójność repozytorium bez transkrypcji: zgodność wersji bazy, taksonomię `kind`/`confidence` (wraz z legendą w JSON i w MD), spójność MD ↔ JSON (cytowania, zasady, liczby, osoby, granice wiedzy), to, czy każda liczba z treści ma wiersz w kolumnie „Wartość" tabeli „Wszystkie liczby w bazie" (i odwrotnie), zgodność tabeli werdyktów z `evidence_review.verdicts`, przypisanie każdego źródła do co najmniej jednej osoby oraz zgodność offsetów `?t=` z etykietami czasu. Skrypt zwraca kod 1, gdy znajdzie niespójność, i jest uruchamiany w CI (`.github/workflows/check.yml`) przy każdym pushu i pull requeście:

```bash
python3 scripts/check_consistency.py
```

Cytowania wobec samych transkrypcji (trafienie w blok, atrybucja mówcy) nie są częścią CI, bo transkrypcje nie są publikowane. Sprawdzaj je lokalnie, porównując `references/transcripts/<id>.md` z kotwicą w bazie; przy rozbieżności popraw kotwicę, nie tekst.

Uwagi do konkretnych plików:

- **S5** (`h2Vj5ai9Ang`) to nagranie z kanału HSS (`@dawidolszewski`); gospodarz to **Dawid Olszewski** — ta sama osoba, której Arkadiusz w rozmowie nazywa „Dawid". To nie jest gospodarz z S7/S8.
- **S6** (`blaB3aBrf1o`) to monolog Arkadiusza. Diaryzacja nie dzieli nagrania jednogłosowego, więc plik `.md` w instalacji lokalnej jest ręcznie podzielony na bloki w miejscach cytowanych w bazie: 00:28, 01:11, 02:30, 04:05, 06:08, 08:10, 08:52, 09:40. Podział nie zmienia tekstu — przy regeneracji z `out/` trzeba go odtworzyć.
- **S7** (`Xb2y18_B0QY`) zachowuje klauzulę kanałową (0:00–0:05), a wycięto z niego reklamę w intro (0:05–1:19) i promocyjną przyśpiewkę na outro (po 1:08:09). Pozostałe cięcia redakcyjne nie są zapisywane w pliku.

## Korzystanie ze skilla

Folder `coach-arek/` jest kompletnym publicznym skillem Codex opartym na syntezie źródeł. Instrukcje działania znajdują się w `SKILL.md`, synteza MD/JSON w katalogu `references/`, a metadane interfejsu w `agents/openai.yaml`. Pełne transkrypcje nie są częścią publicznej paczki.

## Licencja

- **Kod** (`scripts/*.py`, `.github/workflows/check.yml`, `.gitignore`) — licencja **MIT**, pełny tekst w pliku [LICENSE](LICENSE).
- **Treść i dokumentacja** (`SKILL.md`, `README.md`, `INSTALL.md`, `agents/openai.yaml`, `references/*`, `repo-about.json`) — licencja **CC BY 4.0**, szczegóły i sugerowane oznaczenie autorstwa w pliku [LICENSE-CONTENT](LICENSE-CONTENT).

Repozytorium nie zawiera nagrań źródłowych ani pełnych transkrypcji podcastów; licencja dotyczy opracowania, nie cudzych wypowiedzi.
