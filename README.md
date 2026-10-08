# Coach Arek

Skill Codex do praktycznego nadzoru procesu treningowego, ze szczególnym naciskiem na hipertrofię. Pomaga analizować ciągłość planu, objętość i progresję treningową, regenerację oraz trendy masy ciała i kaloryczności.

## Jak powstał

Skill powstał na prośbę użytkownika jako źródło wiedzy dla agenta nadzorującego trening. Punktem wyjścia było siedem polskojęzycznych materiałów z Arkadiuszem Czerwem: sześć rozmów (z Pawłem Albrechtem, Dawidem Olszewskim lub Robusiem Pasjonatem) oraz jeden materiał treningowy. Transkrypcje przygotowano wcześniej z nagrań za pomocą lokalnego workflow MLX Whisper, poprawiono redakcyjnie i uzupełniono o przypisanie mówców. Pełne transkrypcje nie są dołączone do tego publicznego repozytorium; repo zawiera syntezę tematyczną, identyfikatory źródeł, linki i timestampy.

Na podstawie tych materiałów przygotowano:

- `references/knowledge_base_hipertrofia.md` — tematyczną syntezę, zasady operacyjne, zastrzeżenia i odnośniki do fragmentów źródłowych;
- `references/knowledge_base_hipertrofia.json` — ustrukturyzowaną wersję bazy do wyszukiwania i dopasowywania reguł;
- `SKILL.md` — instrukcje określające, kiedy i jak agent ma korzystać z syntezy i źródeł.

Synteza kładzie nacisk na monitorowanie trendów i zachowanie ciągłości procesu, zamiast pochopnego zmieniania całego planu po pojedynczym słabszym treningu. Zalecenia są ostrożnymi, indywidualizowanymi hipotezami do monitorowania. Skill uwzględnia też granice bezpieczeństwa: nie diagnozuje, nie zaleca dopingu ani leków i kieruje sygnały alarmowe do odpowiedniego specjalisty.

## Podstawa źródłowa

Linki prowadzą do materiałów pierwotnych. S1–S4 to rozmowy Pawła Albrechta z Arkadiuszem Czerwem, S5 to rozmowa Dawida Olszewskiego z Arkadiuszem, S6 to materiał treningowy Arkadiusza, a S7 to rozmowa Arkadiusza z Robusiem Pasjonatem. Pełne transkrypcje nie są publikowane w tym repozytorium.

| ID | Temat | Nagranie |
|---|---|---|
| S1 | Redukcja tkanki tłuszczowej | [YouTube](https://youtu.be/bpSubkCA168) |
| S2 | Budowanie masy mięśniowej i hipertrofia | [YouTube](https://youtu.be/XLTbnKL_fwk) |
| S3 | Układanie planu treningowego | [YouTube](https://youtu.be/IIi8e4i6pZE) |
| S4 | Dieta i kaloryczność | [YouTube](https://youtu.be/ySgq9XysjD0) |
| S5 | Programowanie planu treningowego — Dawid Olszewski i Arkadiusz Czerw | [YouTube](https://youtu.be/h2Vj5ai9Ang) |
| S6 | Praktyczny trening, progresja i objętość — Arkadiusz Czerw | [YouTube](https://youtu.be/blaB3aBrf1o) |
| S7 | Programowanie treningu, wysiłek, przerwy, regeneracja i żywienie — Arkadiusz Czerw i Robuś Pasjonat | [YouTube](https://youtu.be/Xb2y18_B0QY) |

Synteza wskazuje identyfikatory źródeł i znaczniki czasu, aby można było sprawdzić kontekst konkretnej wypowiedzi w nagraniu. Gdy potrzebny jest dokładny cytat, szerszy kontekst albo porównanie wypowiedzi, należy sprawdzić oryginalne nagranie.

Uwaga redakcyjna do S7: oryginalna transkrypcja automatyczna miała globalnie zamienione etykiety mówców. Atrybucję w syntezie sprawdzono i poprawiono; pełna transkrypcja nie jest publikowana.

## Ważne ograniczenie

Repozytorium dokumentuje wiedzę przekazaną w wymienionych rozmowach. Umieszczenie wypowiedzi w bazie nie oznacza, że zostały niezależnie sprawdzone w literaturze naukowej. Konkretne liczby, prognozy tempa zmian oraz szerokie twierdzenia fizjologiczne należy traktować jako wypowiedzi rozmówców lub praktyczne hipotezy, a nie gwarantowane prawa ani spersonalizowaną poradę medyczną.

## Zawartość

```text
coach-arek/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
└── references/
    ├── knowledge_base_hipertrofia.json
    └── knowledge_base_hipertrofia.md
```

## Korzystanie ze skilla

Folder `coach-arek/` jest kompletnym publicznym skillem Codex opartym na syntezie źródeł. Instrukcje działania znajdują się w `SKILL.md`, synteza MD/JSON w katalogu `references/`, a metadane interfejsu w `agents/openai.yaml`. Pełne transkrypcje nie są częścią publicznej paczki.
