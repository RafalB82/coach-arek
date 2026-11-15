# Instalacja

Skill `coach-arek` działa w Codexie i Claude Code, bo oba czytają format [Agent Skills](https://agentskills.io): katalog z plikiem `SKILL.md` i opcjonalnymi materiałami w `references/`.

Skill jest **tylko instrukcjami** — nie uruchamia skryptów, nie instaluje zależności i nie wymaga kluczy API. Trzy pliki w `references/` to baza wiedzy (w MD i JSON) oraz weryfikacja naukowa; pełne transkrypcje nie są częścią publicznego repo, więc timestampy prowadzą do YouTube.

## Wymagania

- Codex CLI / IDE extension albo Claude Code,
- `git` (zalecane) lub możliwość skopiowania katalogu,
- nic więcej — Python, Node i MCP nie są potrzebne.

---

## Wariant GUI (bez terminala) — Windows i Mac

Dla osoby, która nie chce otwierać terminala. Wystarczy przeglądarka i Eksplorator/Finder. Skill to folder z plikami — nie instaluje programów ani nie wymaga kluczy API.

### Najpierw pobierz skill (Windows i Mac)

1. Wejdź na `https://github.com/RafalB82/coach-arek`.
2. Kliknij zielony przycisk **Code** → **Download ZIP**.
3. Plik `coach-arek-main.zip` trafi do **Pobranych**.
4. Rozpakuj archiwum — powstanie folder `coach-arek-main`.
5. Zmień nazwę folderu na dokładnie **`coach-arek`**: kliknij nazwę, wpisz nową, naciśnij Enter.

Nazwa folderu musi odpowiadać nazwie skilla z frontmattera. Dlatego nie zostawiaj `coach-arek-main`.

---

### Windows

#### Claude: instalacja przez stronę

To najprostsza droga, bo nie trzeba dotykać folderów systemowych.

1. Zaloguj się na `claude.ai`.
2. Otwórz **Settings → Capabilities**.
3. Włącz **Code execution and file creation** (w nowszym układzie: **Create and edit files**). Bez tego skill się nie uruchomi.
4. W Eksploratorze kliknij prawym przyciskiem na folder **`coach-arek`** → **Wyślij do → Folder skompresowany (ZIP)**. Powstanie `coach-arek.zip`.
5. Na `claude.ai` kliknij **Customize** w lewym panelu, potem **Skills**.
6. Kliknij **+** → **Create skill** → **Upload a skill**.
7. Wskaż **`coach-arek.zip`** i poczekaj na przeskanowanie.
8. Włącz przełącznik przy **coach-arek**.

Skill będzie dostępny w czacie Claude’a, a po zalogowaniu tym samym kontem — także w Claude Code (wymagane Claude Code 2.1.273+).

#### Claude Code: sprawdzenie

1. Otwórz Claude Desktop i zakładkę **Code**.
2. Zaloguj się tym samym kontem co na `claude.ai`.
3. W polu wpisz `/skills`.
4. Skill powinien być na liście pod **claude.ai sync**.
5. Wywołaj go: `/coach-arek`.

Jeśli go nie ma: zaktualizuj aplikację i zrestartuj. Jeśli nadal nie ma, sprawdź, czy skill jest włączony w **Customize → Skills** na `claude.ai`.

#### Codex: poproś agenta

Jeśli masz aplikację ChatGPT z zakładką **Codex**, nie musisz szukać folderów.

1. Otwórz nowy wątek w **Codex**.
2. Wklej:

   ```text
   Zainstaluj skill coach-arek z https://github.com/RafalB82/coach-arek
   do folderu ~/.agents/skills/coach-arek.
   Upewnij się, że SKILL.md jest bezpośrednio w tym folderze.
   Nie zmieniaj innych plików. Potwierdź ścieżkę.
   ```

3. Zatwierdź operacje na plikach, o które poprosi.
4. Zamknij i otwórz Codex ponownie.
5. Wpisz `/skills` albo `$coach-arek`.

#### Codex: ręcznie w Eksploratorze

1. Rozpakuj ZIP i zmień nazwę folderu na **`coach-arek`**.
2. Otwórz folder domowy użytkownika (`C:\Users\<TwojaNazwa>`).
3. Włącz pokazywanie ukrytych elementów: **Widok → Pokaż → Ukryte elementy** (Windows 11) lub **Widok → Opcje → Zmień ustawienia folderów i wyszukiwania → Widok → Pokaż ukryte pliki, foldery i dyski** (Windows 10).
4. Jeśli nie istnieje folder `.agents`, utwórz go, a w nim folder `skills`. Docelowa ścieżka: `C:\Users\<TwojaNazwa>\.agents\skills`.
5. Przeciągnij folder **`coach-arek`** do `skills`. Docelowa ścieżka to `~\.agents\skills\coach-arek\SKILL.md`.
6. Zamknij i otwórz Codex.
7. Wpisz `$coach-arek`.

Starsze buildy Codexa czytają `~\.codex\skills`. Jeśli skill się nie pojawia, powtórz kroki, tworząc w punkcie 4 folder `.codex` zamiast `.agents`, albo poproś Codex o skopiowanie folderu także tam.

---

### Mac

#### Claude: instalacja przez stronę

To najprostsza droga, bo nie trzeba dotykać folderów systemowych.

1. Zaloguj się na `claude.ai`.
2. Otwórz **Settings → Capabilities**.
3. Włącz **Code execution and file creation** (w nowszym układzie: **Create and edit files**). Bez tego skill się nie uruchomi.
4. W Finderze kliknij prawym przyciskiem na folder **`coach-arek`** → **Compress**. Powstanie `coach-arek.zip`.
5. Na `claude.ai` kliknij **Customize** w lewym panelu, potem **Skills**.
6. Kliknij **+** → **Create skill** → **Upload a skill**.
7. Wskaż **`coach-arek.zip`** i poczekaj na przeskanowanie.
8. Włącz przełącznik przy **coach-arek**.

Skill będzie dostępny w czacie Claude’a, a po zalogowaniu tym samym kontem — także w Claude Code (wymagane Claude Code 2.1.273+).

#### Claude Code: sprawdzenie

1. Otwórz Claude Desktop i zakładkę **Code**.
2. Zaloguj się tym samym kontem co na `claude.ai`.
3. W polu wpisz `/skills`.
4. Skill powinien być na liście pod **claude.ai sync**.
5. Wywołaj go: `/coach-arek`.

Jeśli go nie ma: zaktualizuj aplikację i zrestartuj. Jeśli nadal nie ma, sprawdź, czy skill jest włączony w **Customize → Skills** na `claude.ai`.

#### Codex: poproś agenta

Jeśli masz aplikację ChatGPT z zakładką **Codex**, nie musisz szukać folderów.

1. Otwórz nowy wątek w **Codex**.
2. Wklej:

   ```text
   Zainstaluj skill coach-arek z https://github.com/RafalB82/coach-arek
   do folderu ~/.agents/skills/coach-arek.
   Upewnij się, że SKILL.md jest bezpośrednio w tym folderze.
   Nie zmieniaj innych plików. Potwierdź ścieżkę.
   ```

3. Zatwierdź operacje na plikach, o które poprosi.
4. Zamknij i otwórz Codex ponownie.
5. Wpisz `/skills` albo `$coach-arek`.

#### Codex: ręcznie w Finderze

1. Rozpakuj ZIP i zmień nazwę folderu na **`coach-arek`**.
2. W Finderze naciśnij **Shift + Command + G**.
3. Wpisz `~/.agents/skills` i naciśnij Enter. Jeśli folder nie istnieje, wykonaj kroki 4–8; jeśli istnieje, przejdź do kroku 8.
4. Naciśnij **Shift + Command + H** (katalog domowy).
5. Naciśnij **Command + Shift + .** (kropka), żeby pokazać ukryte foldery.
6. Kliknij prawym → **New Folder**, wpisz `.agents`, potwierdź **Use .**.
7. Wejdź do `.agents`, utwórz folder `skills`.
8. Przeciągnij folder **`coach-arek`** do `skills`. Docelowa ścieżka to `~/.agents/skills/coach-arek/SKILL.md`.
9. Zamknij i otwórz Codex.
10. Wpisz `$coach-arek`.

Starsze buildy Codexa czytają `~/.codex/skills`. Jeśli skill się nie pojawia, powtórz kroki, wpisując w punkcie 3 `~/.codex/skills`, albo poproś Codex o skopiowanie folderu także tam.

---

### Jak sprawdzić, że działa (GUI)

Zadaj pytanie kontrolne:

> Jakie masz źródła i jak rozróżniasz praktykę Arka od tego, co potwierdzają badania?

Dobra odpowiedź powinna wspomnieć o źródłach `S1`–`S10`, Arkadiuszu Czerwem i warstwie weryfikacji naukowej oraz rozróżnić praktykę źródłową od twierdzeń popartych. Jeśli odpowiedź jest ogólna, napisz wprost: **„Użyj skilla coach-arek”**.

### Jak z nim rozmawiać

Podaj dane, o które skill i tak zapyta: cel, staż, plan i ostatnie treningi, trend masy ciała, kalorie i białko, sen, ból oraz to, co się nie zgadza.

```text
Użyj coach-arek. Redukcja stoi od 3 tygodni. Waga 82 kg, kalorie 2300,
białko 160 g, kroki 8 tys., 4 treningi siłowe. Co sprawdzić najpierw?
```

```text
Użyj coach-arek. Czy 10 serii na grupę tygodniowo wystarczy przy 2 latach stażu?
```

### Aktualizacja i usunięcie (GUI)

- **Claude:** pobierz nowy ZIP, popraw nazwę folderu, spakuj, usuń starą wersję w **Customize → Skills** (menu „...” → **Delete**) i wgraj nową.
- **Codex:** poproś agenta o aktualizację z GitHuba albo zamień folder ręcznie.
- **Usunięcie w Claude:** **Customize → Skills → coach-arek** → wyłącz przełącznik → „...” → **Delete**.
- **Usunięcie w Codex:** usuń skill w aplikacji albo przeciągnij `~/.agents/skills/coach-arek` (Windows: `%USERPROFILE%\.agents\skills\coach-arek`) do kosza.

---

## Wariant terminalowy (Claude Code / Codex) — na końcu

### Wariant A: prosta instalacja (osobno dla każdego narzędzia)

#### Claude Code

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

#### Codex

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

### Wariant B: jedno źródło i symlinki (Codex + Claude Code)

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

---

## Weryfikacja instalacji

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
| `references/knowledge_base_hipertrofia.json` | wersja strukturalna z blokiem `evidence_review` i taksonomią `kind`/`confidence` |
| `references/weryfikacja_naukowa.md` | weryfikacja twierdzeń względem aktualnych badań |
| `README.md` | opis projektu i podstawy źródłowej |
| `agents/openai.yaml` | opcjonalne metadane UI dla Codexa |
| `scripts/check_consistency.py` | kontrola spójności bazy; uruchamia się w CI, nie jest częścią działania skilla |
| `LICENSE` / `LICENSE-CONTENT` | licencje: MIT dla kodu, CC BY 4.0 dla treści |

## Bezpieczeństwo

To nie jest porada medyczna. Skill nie diagnozuje, nie zaleca dopingu ani leków i nie zastępuje indywidualnej konsultacji: przy bólu, urazie, chorobie lub zaburzeniach odżywiania skieruj sprawę do specjalisty. Weryfikacja naukowa w `references/weryfikacja_naukowa.md` jest celowa, nie systematyczna. Nie wklejaj danych, których nie chcesz przekazywać dostawcy modelu. Skill nie uruchamia skryptów; plik `scripts/set_repo_about.py` służy wyłącznie do metadanych repozytorium i nie jest częścią działania skilla.