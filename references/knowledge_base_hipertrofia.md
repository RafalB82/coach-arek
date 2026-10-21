# Źródło wiedzy: nadzór treningu hipertroficznego

Wersja: 1.6
Zakres: trening siłowy, hipertrofia, masa, redukcja, kaloryczność  
Źródła: siedem rozmów z Arkadiuszem Czerwem i jeden jego materiał treningowy

## Zasada nadrzędna

To redakcyjna zasada pracy agenta, a nie dosłowny wniosek z podcastu: monitoruj proces, sprawdzaj wykonanie i kontekst przed korektą oraz preferuj małe, mierzalne zmiany. Nie przypisuj rozmówcom reguły „nie zmieniaj planu po jednym słabszym treningu”.

## Jak czytać tę bazę

- **„Zasady operacyjne" (A–E)** to skrót operacyjny: co agent ma robić. **„Rozszerzona mapa" (1–6)** to ta sama wiedza z kotwicami, kontekstem i zastrzeżeniami — to ją cytuj i weryfikuj. Ta sama myśl pojawia się w obu miejscach; **kanonem jest mapa**, skrót w A–E służy tylko do szybkiego odczytu.
- **Każda liczba z bazy jest w tabeli „Wszystkie liczby w bazie"** — z kontekstem, źródłem i ryzykiem nadużycia. Nie podawaj liczby bez jej kontekstu (np. „10 serii" znaczy 10 serii tygodniowo na grupę, a nie 10 serii na trening).
- **„Kto jest kim"** rozróżnia gospodarzy rozmów; zanim przypiszesz wypowiedź, sprawdź, czy to ta sama osoba.
- **„Granice wiedzy"** mówi, czego źródła nie poruszają. Poza tymi obszarami odpowiadaj „źródła tego nie mówią", zamiast dopisywać własne wnioski.
- Wariant ustrukturyzowany (JSON) ma te same zasady plus pola `kind` (wypowiedź rozmówcy vs dodatek autora) i `confidence`; zasadę uznaj za wypowiedź rozmówcy tylko wtedy, gdy `kind` = `podcast_paraphrase`. Pola `applies_when` i `not_for` to **ramka operacyjna autora**, nie treść nagrań — mówią, kiedy regułę stosować, a kiedy odpuścić. Tablica `quantitative_claims` w JSON jest tym samym co tabela „Wszystkie liczby w bazie" w tym pliku; `knowledge_limits` odpowiada sekcji „Granice wiedzy", a `people` — „Kto jest kim".

## Kto jest kim

| Osoba | Rola | Źródła | Kanał / nagranie | Jak się o nim mówi w nagraniach |
|---|---|---|---|---|
| Arkadiusz Czerw | trener i zawodnik kulturystyki, gość | S1–S8 | wszystkie | „Arek", „Arku" |
| Paweł Albrecht | gospodarz rozmów z Arkadiuszem | S1–S4 | własne nagrania („trenerów kopiuj w klej") | „Paweł" |
| Dawid Olszewski | gospodarz rozmowy o programowaniu planu | S5 | HSS Podcast, kanał `@dawidolszewski` | „Dawid" |
| Robuś Pasjonat | gospodarz rozmów dla portalu treningowego | S7, S8 | KFD.pl | „Robert", „Robuś" |

Uwaga: **S5, S7 i S8 to trzy różne nagrania, ale tylko dwaj gospodarze** — S5 prowadzi Dawid Olszewski, S7 i S8 Robuś Pasjonat. Nie łącz rozmów z S5 z S7/S8 i nie przypisuj wypowiedzi z jednej rozmowy drugiemu gospodarzowi. Materiał S6 to monolog samego Arkadiusza (bez gospodarza).

## Źródła

| ID | Temat | Link |
|---|---|---|
| `S1` | redukcja tkanki tłuszczowej | https://youtu.be/bpSubkCA168 |
| `S2` | budowanie masy mięśniowej | https://youtu.be/XLTbnKL_fwk |
| `S3` | układanie planu treningowego | https://youtu.be/IIi8e4i6pZE |
| `S4` | dieta i kaloryczność | https://youtu.be/ySgq9XysjD0 |
| `S5` | programowanie planu treningowego — rozmowa Dawida Olszewskiego z Arkadiuszem Czerwem | https://youtu.be/h2Vj5ai9Ang |
| `S6` | praktyczny trening, progresja i liczenie objętości — materiał Arkadiusza Czerwa | https://youtu.be/blaB3aBrf1o |
| `S7` | programowanie treningu, wysiłek, przerwy, regeneracja i żywienie — rozmowa Arkadiusza Czerwa z Robusiem Pasjonatem | https://youtu.be/Xb2y18_B0QY |
| `S8` | trening siłowy, redukcja tkanki tłuszczowej, cardio i autoregulacja — rozmowa Arkadiusza Czerwa z Robusiem Pasjonatem | https://youtu.be/54BCbUZaHo0 |

Uwaga do `S5`: nagranie z kanału HSS (@dawidolszewski), gospodarz to Dawid Olszewski — to ta sama osoba, której Arkadiusz w rozmowie nazywa „Dawid”. W dołączonej transkrypcji etykiety mówców są poprawne.

Uwaga do `S7`: nagranie z kanału KFD.pl, gospodarz to Robuś Pasjonat. W dołączonej transkrypcji etykiety mówców są poprawne (oryginał z globalnie zamienionymi etykietami nie jest w repozytorium, więc nie da się go tu sprawdzić). Z nagrania usunięto klauzulę kanałową (0:00–0:25), reklamę w intro (1:05–1:19) i promocyjną przyśpiewkę na outro (1:08:39–1:08:59); cięcia odtwarza `transkrypcja.sh --rebuild`. Automatyczne rozpoznawanie miejscami skleja fragmenty montażu, dlatego te fragmenty i dokładną atrybucję w razie potrzeby weryfikuj z nagraniem.

Uwaga do `S8`: nagranie z kanału KFD.pl, gospodarz to Robuś Pasjonat. Pierwsza minuta zawiera montaż zapowiedzi i reklamę — w dołączonej transkrypcji pozostawiony w całości, z poprawnymi etykietami (oryginał z globalnie zamienionymi etykietami nie jest w repozytorium). ASR miejscami skleja lub zniekształca wypowiedzi, więc liczby i szczegóły zdrowotne weryfikuj w nagraniu, a nieczytelnych fragmentów nie cytuj.

## Zasady operacyjne agenta

### A. Ocena planu

1. Zapytaj o poprzedni plan, jego czas trwania i wykonanie.
2. Nie obniżaj automatycznie objętości przy zmianie planu.
3. Zachowuj większość wspólnych ćwiczeń, aby można było porównać progres.
4. Oceniaj osobno: objętość, dobór ćwiczeń, progresję, regenerację i preferencje.

Źródło: `S3`, [01:04](https://youtu.be/IIi8e4i6pZE?t=64) (kontynuacja planu, wspólne ćwiczenia, nieobniżanie objętości), [12:01](https://youtu.be/IIi8e4i6pZE?t=721) (dobór ćwiczeń).

### B. Objętość i progresja

- Objętość praktycznie monitoruj przede wszystkim jako liczbę trudnych serii roboczych w tygodniu.
- Nie dodawaj od razu całego dodatkowego treningu. Najpierw rozważ jedną serię roboczą w tygodniu.
- W pierwszych seriach zostawiaj zapas, aby kolejne serie nadal były produktywne.
- Stosuj małe przyrosty obciążenia, gdy duży skok ciężaru utrudnia ocenę progresu.

Źródło: `S3`, [03:00](https://youtu.be/IIi8e4i6pZE?t=180), [38:33](https://youtu.be/IIi8e4i6pZE?t=2313), [51:46](https://youtu.be/IIi8e4i6pZE?t=3106), [58:12](https://youtu.be/IIi8e4i6pZE?t=3492).

### C. Dobór ćwiczeń

- Preferencje użytkownika są ważne, jeśli ćwiczenie pozwala realizować cel i progresować.
- Dla pełnego rozwoju grupy mięśniowej może być potrzebne więcej niż jedno ćwiczenie.
- Ćwiczenia globalne, wielostawowe i izolowane mogą pełnić różne funkcje; nie zakładaj automatycznej wyższości jednej kategorii.

Źródło: `S3`, [12:01](https://youtu.be/IIi8e4i6pZE?t=721), [58:12](https://youtu.be/IIi8e4i6pZE?t=3492).

### D. Masa mięśniowa i kalorie

- Wzory na zapotrzebowanie są punktem startowym, nie pomiarem prawdy.
- Kaloryczność oceniaj na podstawie trendu masy ciała i wykonania planu.
- W rozmowie jako praktyczny zakres nadwyżki pada 250–300 kcal, ale należy traktować to jako hipotezę do indywidualnej obserwacji, nie uniwersalną receptę.
- Tempo zmian oceniaj na podstawie powtarzalnych danych o masie ciała i wykonaniu planu; transkrypcje nie formułują reguły o pomiarach obwodów.

Źródła: `S2`, [01:08](https://youtu.be/XLTbnKL_fwk?t=68); `S4`, [01:01](https://youtu.be/ySgq9XysjD0?t=61), [02:34](https://youtu.be/ySgq9XysjD0?t=154).

### E. Redukcja

- Trend masy ciała jest istotny dla interpretacji kalorii. Średnia tygodniowa to praktyczna metoda operacyjna dodana przez autora skilla, nie zalecenie przypisane rozmówcom.
- W rozmowie pojawia się zakres około 0,5–1% masy ciała tygodniowo jako zdroworozsądkowy punkt odniesienia.
- Arkadiusz Czerw wskazuje trening siłowy i odpowiednią podaż białka jako warunki ograniczające ryzyko utraty mięśni; to parafraza jego wypowiedzi, nie gwarancja. (`S1` [02:23](https://youtu.be/bpSubkCA168?t=143))
- Zbyt agresywny deficyt grozi utratą masy mięśniowej (przy niedostatecznej podaży białka) oraz pogorszeniem przestrzegania planu; to wypowiedź Pawła Albrechta, nie Arkadiusza. Regeneracji źródła nie poruszają.

Źródło: `S1`, [01:58](https://youtu.be/bpSubkCA168?t=118) (Paweł Albrecht: mięśnie i psychika przy zbyt dużym deficycie), [06:14](https://youtu.be/bpSubkCA168?t=374) (Arkadiusz: 0,5–1% masy ciała tygodniowo).

## Rozszerzona mapa wiedzy z transkrypcji

Poniższe punkty opisują treść rozmów. Liczby i uogólnienia rozmówców nie są automatycznie zaleceniami dla każdego użytkownika. Przy decyzjach zdrowotnych lub żywieniowych agent ma sprawdzać aktualne, wiarygodne źródła.

### 1. Konstrukcja i ocena planu

- Przed zmianą planu zbierz poprzedni plan, okres jego realizacji, wykonanie, progres oraz powód zmiany. Paweł Albrecht wskazuje, że zmiana powinna wynikać z niezrealizowanego celu, nie z samej potrzeby nowości (04:13); Arkadiusz mówi, że kolejny plan ma być konsekwencją poprzedniego (01:04) i że planu, który działa, nie zmienia się bez powodu (04:45). (`S3` [01:04](https://youtu.be/IIi8e4i6pZE?t=64), [03:42](https://youtu.be/IIi8e4i6pZE?t=222), [04:13](https://youtu.be/IIi8e4i6pZE?t=253), [04:45](https://youtu.be/IIi8e4i6pZE?t=285))
- Trzy praktyczne kryteria dobrego planu: użytkownik go lubi, plan jest realistyczny do wykonania i elastyczny wobec zmian w grafiku. Te kryteria powtarzają się w S2 i S5; nie są nową, odrębną regułą. (`S2` [19:09](https://youtu.be/XLTbnKL_fwk?t=1149), [33:19](https://youtu.be/XLTbnKL_fwk?t=1999); `S5` [52:17](https://youtu.be/h2Vj5ai9Ang?t=3137))
- Nie ma jednego obowiązkowego podziału treningowego. Wybór full body, góra/dół lub split ma uwzględniać preferencje, czas i możliwość regularnego wykonania. S7 dodaje przykład Arkadiusza: przygotowywał się czasem przy trzech, a czasem mniejszej liczbie treningów tygodniowo, kierując się sumaryczną objętością i jej rozkładem. To opis jego praktyki, nie gwarancja, że każda częstotliwość będzie równie skuteczna dla każdej osoby. Mikrocykl nie musi pokrywać się z kalendarzowym tygodniem. (`S3` [06:16](https://youtu.be/IIi8e4i6pZE?t=376), [08:34](https://youtu.be/IIi8e4i6pZE?t=514), [09:15](https://youtu.be/IIi8e4i6pZE?t=555); `S7` [12:27](https://youtu.be/Xb2y18_B0QY?t=747), [12:42](https://youtu.be/Xb2y18_B0QY?t=762), [12:46](https://youtu.be/Xb2y18_B0QY?t=766))
- Zachowaj różnicę akcentów: S3 Arkadiusz zaleca każdą grupę minimum dwa razy w tygodniu; S2 mówi, że 2× nie jest obligatoryjne, jeśli ogranicza je czas, a raz w tygodniu nadal ma sens. W S7 Arkadiusz również preferuje 2×, gdy można tak rozłożyć objętość i utrzymać jakość serii, ale podkreśla, że kluczowa jest całkowita objętość. Praktycznie wybierz częstotliwość możliwą do utrzymania i adekwatną do objętości. (`S3` [07:20](https://youtu.be/IIi8e4i6pZE?t=440); `S2` [14:22](https://youtu.be/XLTbnKL_fwk?t=862); `S7` [24:44](https://youtu.be/Xb2y18_B0QY?t=1484))
- Warto utrzymywać ćwiczenie kontrolne dla grupy mięśniowej i nie zmieniać często wszystkich ćwiczeń. Arkadiusz opisuje stosowanie jednego głównego, złożonego ćwiczenia jako punktu porównania „w skali całego roku" (`S2` [21:14](https://youtu.be/XLTbnKL_fwk?t=1274)) oraz praktykę niezmieniania tego ćwiczenia przez 12 miesięcy, a nawet przez 6 (`S5` [43:42](https://youtu.be/h2Vj5ai9Ang?t=2622)); pozostałe ćwiczenia uzupełniające mogą być mniej złożone, maszynowe lub izolowane. To jego model, nie obowiązkowa architektura planu. (`S2` [21:14](https://youtu.be/XLTbnKL_fwk?t=1274), [21:34](https://youtu.be/XLTbnKL_fwk?t=1294); `S3` [09:42](https://youtu.be/IIi8e4i6pZE?t=582); `S5` [43:42](https://youtu.be/h2Vj5ai9Ang?t=2622); `S7` [33:32](https://youtu.be/Xb2y18_B0QY?t=2012), [33:50](https://youtu.be/Xb2y18_B0QY?t=2030), [34:46](https://youtu.be/Xb2y18_B0QY?t=2086))
- Ćwiczenie kontrolne nie oznacza testowania maksa co tydzień. Zaawansowany użytkownik może progresować wolniej; brak cotygodniowego wzrostu ciężaru sam w sobie nie dowodzi, że plan nie działa. (`S2` [22:53](https://youtu.be/XLTbnKL_fwk?t=1373))
- Arkadiusz opisuje programowanie jako planowane manipulowanie zmiennymi treningu w celu zarządzania zmęczeniem i wspierania adaptacji; periodyzację odróżnia jako planowanie w szerszej perspektywie czasu. To jego rama pojęciowa, nie jedyna obowiązująca definicja. (`S5` [02:46](https://youtu.be/h2Vj5ai9Ang?t=166))
- Nie zmieniaj planu wyłącznie dlatego, że minął arbitralny cykl. Arkadiusz opisuje utrzymywanie ćwiczeń bazowych przez lata, jeśli pozwalają trenować i monitorować postępy; zmiany wprowadza m.in. z powodu monotonii. To jego praktyka, nie nakaz utrzymania każdego planu bez końca. (`S5` [40:39](https://youtu.be/h2Vj5ai9Ang?t=2439), [43:42](https://youtu.be/h2Vj5ai9Ang?t=2622))
- S6 przedstawia powrót Arkadiusza po drobnym wypadku, na tyle poważnym, że przez pierwszy tydzień–dwa nie mógł trenować: najpierw rehabilitacja, utrwalanie wzorców ruchowych i stabilizacja, potem stopniowe dokładanie ćwiczeń. To opis jego indywidualnego przypadku, a nie gotowy protokół leczenia ani zalecenie do samodzielnej rehabilitacji. (`S6` [01:11](https://youtu.be/blaB3aBrf1o?t=71), [01:31](https://youtu.be/blaB3aBrf1o?t=91), [01:48](https://youtu.be/blaB3aBrf1o?t=108))
- S8 wyraźniej rozdziela osobę początkującą z otyłością, której plan trzeba dopasować do czasu i możliwości, od osoby zaawansowanej robiącej redukcję sylwetkową, u której punktem wyjścia jest poprzedni plan i wytrenowana tolerancja. To rama do indywidualizacji, nie odrębne prawa treningowe dla kategorii osób. (`S8` [01:25](https://youtu.be/54BCbUZaHo0?t=85), [01:56](https://youtu.be/54BCbUZaHo0?t=116), [02:45](https://youtu.be/54BCbUZaHo0?t=165))
- Wspólny wątek S8 i S7: plan ma być możliwy do wykonania, a krótka lub częściowa sesja może być lepsza niż opuszczenie treningu z powodu perfekcjonizmu. W S8 przykład klienta, który po opóźnieniu wykonał tylko część planu, opisuje Robuś Pasjonat (1:07:58), a Arkadiusz kwituje to „Done is better than perfect" (1:08:58) i wcześniej „zrób to zmęczony" (1:06:14); traktuj to jako strategię przestrzegania planu, nie obowiązek trenowania mimo choroby, bólu czy niebezpiecznego przemęczenia. (`S8` [1:07:58](https://youtu.be/54BCbUZaHo0?t=4078), [1:08:58](https://youtu.be/54BCbUZaHo0?t=4138))

### 2. Ćwiczenia, kolejność, technika i odpoczynek

- Dobór ćwiczeń ma uwzględniać preferencje, możliwość konsekwentnego wykonywania i pokrycie funkcji/obszarów danej grupy mięśniowej. Pojedyncze ćwiczenie może nie obejmować całej grupy; w rozmowie podano przykłady czworogłowych i dwugłowych uda. (`S3` [09:42](https://youtu.be/IIi8e4i6pZE?t=582), [12:01](https://youtu.be/IIi8e4i6pZE?t=721))
- Nie przedstawiaj ćwiczeń wielostawowych jako zawsze lepszych od izolowanych. Mogą pełnić różne role i być dobierane do celu oraz tolerancji ćwiczącego. (`S3` [13:25](https://youtu.be/IIi8e4i6pZE?t=805), [58:12](https://youtu.be/IIi8e4i6pZE?t=3492))
- Rozmówca proponuje zaczynać od ruchów bardziej złożonych i wymagających skupienia, a następnie wykonywać ćwiczenia izolowane. To praktyczna konwencja, nie bezwzględne prawo. (`S3` [28:14](https://youtu.be/IIi8e4i6pZE?t=1694))
- Zakres ruchu powinien być możliwie duży, o ile można zachować kontrolę i komfort stawów. Nie forsuj głębokości, jeśli pojawia się ból, utrata stabilnej pozycji lub kompensacja. (`S3` [23:37](https://youtu.be/IIi8e4i6pZE?t=1417), [24:48](https://youtu.be/IIi8e4i6pZE?t=1488))
- S7 omawia trening przy wydłużonej pozycji mięśnia i częściowe powtórzenia, ale rozmowa nie daje podstaw, by uznać je za obowiązkowo lepsze od pełnego, kontrolowanego zakresu. Dobieraj zakres do ćwiczenia, tolerancji i celu; nie forsuj rozciągnięcia pod obciążeniem. (`S7` [36:42](https://youtu.be/Xb2y18_B0QY?t=2202), [36:52](https://youtu.be/Xb2y18_B0QY?t=2212) — Arkadiusz o „hipertrofii pośredniczonej rozciąganiem"; [36:11](https://youtu.be/Xb2y18_B0QY?t=2171) i [39:08](https://youtu.be/Xb2y18_B0QY?t=2348) to wypowiedzi Robusia o badaniach nad częściowymi powtórzeniami)
- Przerwa zależy od ćwiczenia i gotowości do kolejnej jakościowej serii. W S3 pada co najmniej 2 minuty jako punkt odniesienia, a w S7 Arkadiusz Czerw opowiada się za minimum 2 minutami także przy izolacjach. To zbieżny punkt odniesienia, nie sztywna norma dla każdego. (dodatek autora: nie skracaj odpoczynku kosztem celu serii.) (`S3` [30:52](https://youtu.be/IIi8e4i6pZE?t=1852), [32:48](https://youtu.be/IIi8e4i6pZE?t=1968); `S7` [46:19](https://youtu.be/Xb2y18_B0QY?t=2779), [46:27](https://youtu.be/Xb2y18_B0QY?t=2787) — potwierdzenie „także przy izolacjach")
- Waga na maszynie nie zawsze jest porównywalna między sprzętami lub siłowniami. Śledź wynik w tym samym ćwiczeniu, na tym samym urządzeniu i przy podobnej technice. (`S4` [56:02](https://youtu.be/ySgq9XysjD0?t=3362))
- Arkadiusz opisuje technikę i dobór ćwiczenia z uwzględnieniem ograniczeń własnego ciała; w jego przykładzie ustawienie nóg na ławce ograniczało pogłębianie lordozy i możliwy dyskomfort. To modyfikacja konkretnej osoby, nie standardowa technika wyciskania. Przy bólu lub urazie nie kopiuj jej bez oceny specjalisty. (`S6` [04:05](https://youtu.be/blaB3aBrf1o?t=245))

### 3. Objętość, wysiłek i progresja

- Objętość można opisywać na różne sposoby; dla praktycznego monitorowania rozmówca wskazuje tygodniowe serie robocze, a nie sam tonaż. Zapisuj serie osobno dla grup mięśniowych; o ćwiczeniach wielostawowych mówi Arkadiusz w `S6` [08:52](https://youtu.be/blaB3aBrf1o?t=532) — triceps i przednia część deltoidów pracują razem z klatką, ale to klatka jest czynnikiem limitującym. (`S3` [03:00](https://youtu.be/IIi8e4i6pZE?t=180))
- W S6 Arkadiusz opisuje własną metodę przypisywania serii wielostawowych: za główną serię dla danej partii uznaje ją wtedy, gdy ta partia jest czynnikiem limitującym; samo współuczestnictwo mięśnia pomocniczego nie oznacza równoważnej serii bezpośredniej. To praktyczny model liczenia, nie uniwersalny sposób wyceny każdej serii. (`S6` [08:10](https://youtu.be/blaB3aBrf1o?t=490), [08:52](https://youtu.be/blaB3aBrf1o?t=532))
- Zachowaj różnicę akcentów: S2 Arkadiusz wprost rekomenduje 10 serii tygodniowo na grupę jako punkt startowy niezależnie od poziomu; S3 mówi, by szukać indywidualnego minimum (33:58), a powrót do skutecznej objętości z poprzedniego planu to osobna wypowiedź (01:04). W S7 Arkadiusz najpierw akcentuje minimum stymulujące adaptację i analizę poprzedniego planu, a później sam podaje 10 serii tygodniowo jako punkt odniesienia w porównaniu z 5 seriami. To różne konteksty tej samej rozmowy, nie spójna uniwersalna recepta. (`S2` [06:46](https://youtu.be/XLTbnKL_fwk?t=406); `S3` [01:04](https://youtu.be/IIi8e4i6pZE?t=64), [33:58](https://youtu.be/IIi8e4i6pZE?t=2038); `S7` [16:09](https://youtu.be/Xb2y18_B0QY?t=969), [16:34](https://youtu.be/Xb2y18_B0QY?t=994), [17:20](https://youtu.be/Xb2y18_B0QY?t=1040), [20:02](https://youtu.be/Xb2y18_B0QY?t=1202))
- Seria powinna być dostatecznie wymagająca. Rozmówca opisuje spowolnienie fazy koncentrycznej mimo intencji szybkiego ruchu jako praktyczny sygnał dużego wysiłku; nie jest to precyzyjny pomiar RIR. (`S2` [10:51](https://youtu.be/XLTbnKL_fwk?t=651))
- Nie trzeba doprowadzać każdej serii każdego ćwiczenia do upadku. W rozmowie zaleca się zachować zapas w początkowych seriach, a ewentualny upadek rozważać ostrożniej w ostatniej serii/ćwiczeniu dla grupy. Dostosuj to do bezpieczeństwa, ćwiczenia i doświadczenia. (`S3` [47:43](https://youtu.be/IIi8e4i6pZE?t=2863), [51:46](https://youtu.be/IIi8e4i6pZE?t=3106))
- S3 przedstawia szeroki zakres 5–35 powtórzeń jako potencjalnie skuteczny, gdy serie zbliżają się do upadku; jednocześnie sugeruje praktycznie ok. 6–8 powtórzeń dla złożonych ruchów z wolnym ciężarem, ok. 10 dla złożonych maszynowych i ok. 12 dla izolacji. Uzasadnieniem jest m.in. komfort i zmęczenie. Nie przekształcaj tych przykładów w sztywne normy ani nie pomijaj ich kontekstu. (`S3` [40:35](https://youtu.be/IIi8e4i6pZE?t=2435), [43:32](https://youtu.be/IIi8e4i6pZE?t=2612))
- W S7 Arkadiusz opisuje własną preferencję trenowania zwykle do 10 powtórzeń i wyjaśnia ją kosztem zmęczenia; zgadza się jednak wyjść poza ten zakres u klienta po urazie tylnej części uda. To osobisty punkt odniesienia, który sam rozmówca dopasowuje do przypadku, nie ogólny limit hipertrofii. (`S7` [31:27](https://youtu.be/Xb2y18_B0QY?t=1887), [32:14](https://youtu.be/Xb2y18_B0QY?t=1934) — wyjście poza 10 powtórzeń u klienta po urazie tylnej części uda; [31:59](https://youtu.be/Xb2y18_B0QY?t=1919) to pytanie Robusia)
- W S2 Arkadiusz mówi, że 6 powtórzeń może wystarczyć do uznania serii za efektywną, a dalsza odpowiedź przechodzi w omawianie wyciskania. Czytaj to razem z szerszą wypowiedzią S3 o 5–35 powtórzeniach; źródła różnią się akcentem, nie wyprowadzaj z krótkiego, urwanego fragmentu uniwersalnego górnego limitu. (`S2` [29:30](https://youtu.be/XLTbnKL_fwk?t=1770); `S3` [40:35](https://youtu.be/IIi8e4i6pZE?t=2435))
- Progresuj przez ciężar, powtórzenia lub niewielkie zwiększenie objętości. Porównuj przy tej samej technice i podobnym wysiłku; sam większy ciężar przy znacznie mniejszej liczbie powtórzeń nie przesądza o progresie. Mikroobciążenia mogą ułatwić stopniowe zwiększanie ciężaru. (`S2` [21:34](https://youtu.be/XLTbnKL_fwk?t=1294) (mikroobciążenia), [36:26](https://youtu.be/XLTbnKL_fwk?t=2186) (ciężar kosztem powtórzeń); `S3` [38:33](https://youtu.be/IIi8e4i6pZE?t=2313) (niewielki przyrost objętości), [54:40](https://youtu.be/IIi8e4i6pZE?t=3280) (obciążenie, powtórzenia albo spadek odczuwanego wysiłku), [58:12](https://youtu.be/IIi8e4i6pZE?t=3492) (mikroobciążenia))
- Progres nie musi oznaczać natychmiastowego dodania ciężaru: może obejmować więcej powtórzeń, lepszą jakość ruchu lub ten sam wynik przy niższym odczuwanym wysiłku. Nie zwiększaj ciężaru kosztem powtórzeń, techniki ani innych parametrów, które chcesz utrzymać. W S6 Arkadiusz opisuje podwójną progresję jako osobistą metodę. (`S5` [35:53](https://youtu.be/h2Vj5ai9Ang?t=2153), [39:24](https://youtu.be/h2Vj5ai9Ang?t=2364); `S6` [06:08](https://youtu.be/blaB3aBrf1o?t=368), [06:59](https://youtu.be/blaB3aBrf1o?t=419))
- Nie traktuj „efektywnych powtórzeń” jako precyzyjnie zmierzonej, oficjalnej kategorii. Arkadiusz mówi, że w przeglądanych przez niego publikacjach nie spotkał takiej definicji; to relacja z jego lektury, a nie samodzielny przegląd literatury przez skilla. W tej samej rozmowie praktycznie odwołuje się do bliskości upadku i RIR, więc nie należy zamieniać tej uwagi w zaprzeczenie znaczenia wysiłku. (`S5` [1:10:47](https://youtu.be/h2Vj5ai9Ang?t=4247), [1:12:23](https://youtu.be/h2Vj5ai9Ang?t=4343))
- W S5 Arkadiusz podaje 2–3 powtórzenia w zapasie jako przykład dla wcześniejszego, złożonego ćwiczenia, a upadek rozważa ostrożniej przy ćwiczeniach izolowanych i jeśli pozwala na to regeneracja. Podkreśla, że bliskość upadku zwiększa zarówno bodziec, jak i koszt zmęczeniowy; nie rób z tego obowiązkowego schematu dla wszystkich. (`S5` [33:07](https://youtu.be/h2Vj5ai9Ang?t=1987))
- Jego praktyczny wybór do 12 powtórzeń wynika z osobistych preferencji i problemów z koncentracją lub ograniczeniem serii przez zmęczenie metaboliczne. Nie jest to ogólne twierdzenie, że wyższe zakresy są nieskuteczne; oddziel tę preferencję od szerszego zakresu 5–35 omawianego w S3. (`S5` [1:06:45](https://youtu.be/h2Vj5ai9Ang?t=4005), [1:08:09](https://youtu.be/h2Vj5ai9Ang?t=4089))
- S6 podaje ok. 10 serii roboczych na partię w jednej jednostce jako granicę efektywnej objętości i argument za rozłożeniem większej objętości na więcej treningów. Traktuj tę liczbę jako twierdzenie rozmówcy do weryfikacji; nie mieszaj jej z 10 seriami tygodniowo, które S2 podaje jako punkt startowy. (`S6` [09:40](https://youtu.be/blaB3aBrf1o?t=580), [10:06](https://youtu.be/blaB3aBrf1o?t=606))
- Przy braku progresu najpierw sprawdź wykonanie, porównywalność, regenerację i czas obserwacji. Dopiero po utrzymującym się zastoju rozważ mały bodziec, np. jedną serię roboczą tygodniowo. (`S3` [03:42](https://youtu.be/IIi8e4i6pZE?t=222), [38:33](https://youtu.be/IIi8e4i6pZE?t=2313) („jedna seria robocza w skali tygodnia"); `S2` [24:58](https://youtu.be/XLTbnKL_fwk?t=1498) („dokładamy jedną serię roboczą albo kolejne ćwiczenie"))
- Atrybucja do S2 [15:29](https://youtu.be/XLTbnKL_fwk?t=929): Arkadiusz mówi, że wynik gorszy niż poprzednio oznacza potrzebę większej ilości czasu na regenerację; wynik powtórzony ma, według niego, oznaczać pełną regenerację. To twierdzenie rozmówcy, a nie potwierdzona reguła diagnostyczna. Zasada, by nie zmieniać całego planu po jednym słabszym treningu, jest ostrożnością operacyjną autora skilla, nie treścią tego cytatu.
- Sen został wskazany w rozmowie jako ważny element regeneracji; nie wyciągaj jednak wniosków o przyczynie z samego wyniku treningu. (`S2` [46:59](https://youtu.be/XLTbnKL_fwk?t=2819))
- S7 rozszerza zalecenie notowania postępów: Arkadiusz proponuje zapisywać ciężar, powtórzenia, subiektywny wysiłek i długość przerw. To użyteczny zestaw porównawczy, nie wymóg używania konkretnej skali wysiłku. Nie wyciągaj z jego wypowiedzi wniosku, że hipertrofia zaczyna się dopiero po zatrzymaniu progresu siłowego — rozmówca tak interpretuje adaptacje, ale nie jest to potwierdzona reguła diagnostyczna. (`S7` [47:14](https://youtu.be/Xb2y18_B0QY?t=2834), [48:20](https://youtu.be/Xb2y18_B0QY?t=2900) — Arkadiusz o zapisie i o interpretacji zastoju; [47:02](https://youtu.be/Xb2y18_B0QY?t=2822) to pytanie Robusia)
- Arkadiusz opisuje reaktywny deload, gdy utrzymujący się problem dotyczy konkretnego ćwiczenia: rozważa lokalne zmniejszenie objętości lub intensywności; jako swoją częstą praktykę wymienia obniżenie ciężaru. Transkrypcja pytania o zachowanie liczby serii jest uszkodzona, więc nie zakładaj, że zawsze pozostawia serie bez zmian. (`S7` [50:19](https://youtu.be/Xb2y18_B0QY?t=3019), [51:01](https://youtu.be/Xb2y18_B0QY?t=3061))
- S7 przedstawia przerwę od siłowni jako indywidualną decyzję: Arkadiusz relacjonuje kilkumiesięczne przerwy po sezonie startowym, a Robuś mówi o sugerowaniu klientom rekreacyjnym około dwóch tygodni wolnego rocznie; Arkadiusz potwierdza, że również zaleca klientom formę roztrenowania. To przykłady praktyki rozmówców, nie obowiązkowy harmonogram. (`S7` [51:26](https://youtu.be/Xb2y18_B0QY?t=3086), [53:50](https://youtu.be/Xb2y18_B0QY?t=3230), [54:14](https://youtu.be/Xb2y18_B0QY?t=3254))
- Arkadiusz preferuje utrzymanie jednego ćwiczenia bazowego jako punktu porównawczego przez dłuższy okres i dopuszcza wymianę ćwiczeń uzupełniających dla świeżości. To rozwija istniejącą zasadę ciągłości, ale opisuje jego metodę, nie uniwersalny podział ćwiczeń. (`S7` [33:32](https://youtu.be/Xb2y18_B0QY?t=2012), [49:49](https://youtu.be/Xb2y18_B0QY?t=2989) — wymiana ćwiczeń pomocniczych dla świeżości; [49:16](https://youtu.be/Xb2y18_B0QY?t=2956) to pytanie Robusia)
- S7 zawiera opinię Arkadiusza, że periodyzacja w popularnym modelu zmniejszania objętości na rzecz intensywności może być nieefektywna dla hipertrofii. Jest to jego stanowisko wobec konkretnego modelu, nie uniwersalny konsensus; zestaw je z jego rozróżnieniem programowania i periodyzacji w S5. (`S7` [55:18](https://youtu.be/Xb2y18_B0QY?t=3318), [55:31](https://youtu.be/Xb2y18_B0QY?t=3331))

### 4. Redukcja i utrzymanie mięśni

- Rozmówcy wskazują orientacyjnie 0,5–1% masy ciała tygodniowo jako zakres do rozważenia, a jednocześnie mówią, by nie przekraczać 1% jako typowego celu. Nie przedstawiaj tego jako bezpiecznej normy dla wszystkich; dostosowanie zależy od kontekstu i stanu zdrowia. (`S1` [06:14](https://youtu.be/bpSubkCA168?t=374), [39:43](https://youtu.be/bpSubkCA168?t=2383); `S4` [08:52](https://youtu.be/ySgq9XysjD0?t=532), [09:38](https://youtu.be/ySgq9XysjD0?t=578) (tygodniowa skala))
- Ustal konkretny cel i horyzont, a następnie dobierz umiarkowany, możliwy do utrzymania deficyt. Zbyt ambitny cel może utrudniać konsekwencję; zbyt łagodny może nadmiernie wydłużać proces. (`S1` [39:43](https://youtu.be/bpSubkCA168?t=2383), [42:15](https://youtu.be/bpSubkCA168?t=2535))
- Trening siłowy w redukcji ma przede wszystkim pomagać zachować mięśnie i wyniki, a nie służyć do „spalania” jak największej liczby kalorii. Nie traktuj wskazań zegarka jako dokładnej miary wydatku treningowego (o wiarygodności wskazań mówi Paweł Albrecht, o ograniczeniu wydatku treningowego Arkadiusz). (`S1` [17:36](https://youtu.be/bpSubkCA168?t=1056), [22:09](https://youtu.be/bpSubkCA168?t=1329), [22:36](https://youtu.be/bpSubkCA168?t=1356))
- W S3 Arkadiusz mówi, że plan zasadniczo ma pozostać ten sam na masie i redukcji; u zaawansowanych rozważa optymalizację stosunku bodźca do zmęczenia przez mniej powtórzeń lub stabilniejsze ćwiczenia maszynowe przy zachowaniu względnej intensywności. Spadek wyniku na wyciskaniu podczas redukcji przedstawia jako częsty, a częściowo wynikający z niższej masy ciała. Link do wyjaśnienia to [1:07:23](https://youtu.be/IIi8e4i6pZE?t=4043), nie 1:07:54 (gdzie transkrypcja ma rozdzielone, urwane segmenty). (`S3` [1:04:01](https://youtu.be/IIi8e4i6pZE?t=3841), [1:06:08](https://youtu.be/IIi8e4i6pZE?t=3968), [1:07:23](https://youtu.be/IIi8e4i6pZE?t=4043))
- W S5 Arkadiusz mówi, by na redukcji w miarę możliwości utrzymać zbliżony bodziec/objętość zamiast automatycznie ją zwiększać. Rozróżnia też zachowanie bodźca od obowiązku utrzymania wyników siłowych; są to wypowiedzi rozmówcy, nie gwarancja zachowania mięśni ani indywidualna recepta. (`S5` [46:07](https://youtu.be/h2Vj5ai9Ang?t=2767), [47:01](https://youtu.be/h2Vj5ai9Ang?t=2821), [51:19](https://youtu.be/h2Vj5ai9Ang?t=3079))
- Szybki spadek masy po ograniczeniu węglowodanów może obejmować glikogen, wodę i treść pokarmową; nie utożsamiaj zmiany wagi z utratą tłuszczu. Ten fragment rozmowy jest uproszczony i wymaga ostrożnej interpretacji. (`S4` [14:35](https://youtu.be/ySgq9XysjD0?t=875))
- Po redukcji S1 sugeruje wrócić do oszacowanego zapotrzebowania, uwzględniając aktualną masę i adaptacje. W S7 Arkadiusz rozróżnia sytuację osoby, która nadal chce poprawić poziom tkanki tłuszczowej, od zawodnika po sezonie startowym: opisuje stopniowe zwiększanie jedzenia w pierwszym kontekście oraz powrót w okolice utrzymania po sezonie. To opis jego praktyki, nie uniwersalny wymóg „reverse dieting”; szczegóły indywidualizuj i weryfikuj. (`S1` [49:42](https://youtu.be/bpSubkCA168?t=2982), [49:55](https://youtu.be/bpSubkCA168?t=2995); `S7` [56:46](https://youtu.be/Xb2y18_B0QY?t=3406))
- Kontroluj spontaniczną aktywność (NEAT); kroki mogą być jej użytecznym wskaźnikiem. Arkadiusz podaje anegdotyczny przykład spadku z ok. 10 tys. do 5 tys. kroków po wejściu w deficyt. To ilustracja z jego doświadczenia, nie typowa prognoza. (`S1` [07:33](https://youtu.be/bpSubkCA168?t=453), [10:01](https://youtu.be/bpSubkCA168?t=601))
- W redukcji Arkadiusz preferuje możliwie małą dawkę treningu siłowego jako bodziec podtrzymujący mięśnie, kontrolę kroków i dietę; odradza traktowanie siłowni jako narzędzia do tworzenia deficytu. Wypowiada też opinię o ograniczeniu cardio, z wyjątkiem niektórych przygotowań zawodniczych. To stanowisko rozmówcy, nie uniwersalna recepta; dobór cardio zależy od osoby, celu, zdrowia i aktualnych zaleceń. (`S1` [17:36](https://youtu.be/bpSubkCA168?t=1056))
- S8 rozwija praktyczną kolejność autoregulacji redukcji opisaną przez Arkadiusza: najpierw ogranicz koszt zmęczeniowy ćwiczeń (np. stabilniejszy wariant maszynowy zamiast wolnego ciężaru), rozważ umiarkowane obniżenie zakresu powtórzeń przy zachowaniu wymagającego, ale nie skrajnego wysiłku, a objętość zmniejszaj dopiero, gdy obserwowany trend i regeneracja tego uzasadniają. Jako przykład rozmówca opisuje odjęcie jednej serii roboczej, a nie automatyczne cięcie o stały procent. To jego podejście, nie zwalidowany algorytm; nie stosuj go sztywno ani nie wyciągaj wniosków z jednej słabszej sesji. (`S8` [04:50](https://youtu.be/54BCbUZaHo0?t=290), [12:39](https://youtu.be/54BCbUZaHo0?t=759), [14:15](https://youtu.be/54BCbUZaHo0?t=855), [14:58](https://youtu.be/54BCbUZaHo0?t=898), [1:10:08](https://youtu.be/54BCbUZaHo0?t=4208))
- W S8 Arkadiusz mówi, by odróżniać pojedynczy gorszy trening od utrzymującego się trendu; przykładowo, powtarzający się spadek powtórzeń może być sygnałem do sprawdzenia regeneracji, podczas gdy utrzymanie wyniku na redukcji może być akceptowalne. Nie podaje uniwersalnego progu spadku, a zmiana masy ciała może wpływać na wynik niektórych ćwiczeń. Nie używaj samego wyniku siłowego do diagnozowania utraty mięśni. (`S8` [20:29](https://youtu.be/54BCbUZaHo0?t=1229) („nie wyciągać pochopnych wniosków na podstawie jednego dnia"), [23:12](https://youtu.be/54BCbUZaHo0?t=1392), [23:48](https://youtu.be/54BCbUZaHo0?t=1428); [24:15](https://youtu.be/54BCbUZaHo0?t=1455) to uwaga Robusia o utrzymaniu wyniku na redukcji)
- S8 przedstawia cardio jako możliwe narzędzie dla zdrowia i zwiększania wydatku, ale nie jako obowiązkowy ani główny sposób redukcji. Arkadiusz wskazuje, że jego nadmierna intensywność może pośrednio obniżyć jakość treningu siłowego; nie podaje bezpiecznego „maksimum” cardio. Przykłady HIIT, czasu rozdzielenia cardio i siłowni ([28:53](https://youtu.be/54BCbUZaHo0?t=1733), wypowiedź Robusia Pasjonata) oraz bardzo niskiej podaży kalorii są wypowiedziami rozmówców, nie zaleceniami skilla; szczególnie nie wyprowadzaj z nich limitu kalorii ani protokołu cardio. (`S8` [25:03](https://youtu.be/54BCbUZaHo0?t=1503), [28:00](https://youtu.be/54BCbUZaHo0?t=1680), [28:53](https://youtu.be/54BCbUZaHo0?t=1733), [35:42](https://youtu.be/54BCbUZaHo0?t=2142))
- Dla osoby początkującej z ograniczonym czasem S8 omawia full body przy 2–3 sesjach tygodniowo i większą gęstość treningu, w tym serie łączone albo aktywny odpoczynek. Są to warianty do rozważenia w określonym kontekście, nie powód do skracania przerw kosztem jakości każdej serii hipertroficznej. (`S8` [10:27](https://youtu.be/54BCbUZaHo0?t=627) (Robuś Pasjonat o osobach z otyłością), [46:27](https://youtu.be/54BCbUZaHo0?t=2787) (Arkadiusz o objętości), [47:24](https://youtu.be/54BCbUZaHo0?t=2844) (Robuś Pasjonat o krótkich przerwach), [1:09:07](https://youtu.be/54BCbUZaHo0?t=4147) (Robuś Pasjonat w podsumowaniu))
- W S8 pojawiają się dwie praktyki korekty zastoju: Arkadiusz mówi o skompensowaniu brakującego wydatku przez dietę albo aktywność, a Robuś opisuje zwiększenie kroków o ok. 20% przed zmianą kalorii. Nie są to zgodne, uniwersalne protokoły; przed korektą sprawdź trend i realizację planu, a przykładu procentowego nie stosuj automatycznie po jednym tygodniu. (`S8` [55:57](https://youtu.be/54BCbUZaHo0?t=3357), [56:39](https://youtu.be/54BCbUZaHo0?t=3399), [57:17](https://youtu.be/54BCbUZaHo0?t=3437))

### 5. Kalorie, makroskładniki i zachowania żywieniowe

- Zero kaloryczne z kalkulatora jest estymacją. Kalibruj je na podstawie regularnego spożycia i trendu masy ciała; zapotrzebowanie zmienia się wraz z aktywnością, masą i spontanicznym ruchem. (`S4` [01:01](https://youtu.be/ySgq9XysjD0?t=61), [02:34](https://youtu.be/ySgq9XysjD0?t=154), [06:11](https://youtu.be/ySgq9XysjD0?t=371))
- W kolejności ważności omawianej przez rozmówców: całkowita kaloryczność, białko, proporcje tłuszczów i węglowodanów, a potem timing posiłków. Jest to hierarchia praktyczna rozmówców, nie kompletna ocena żywienia. (`S4` [31:42](https://youtu.be/ySgq9XysjD0?t=1902), [32:56](https://youtu.be/ySgq9XysjD0?t=1976))
- Rozmówca podaje 2–3 g białka/kg masy ciała i sugeruje wyższy zakres przy głębszej redukcji. To konkretne twierdzenie wymaga sprawdzenia względem aktualnych wytycznych, składu ciała, zdrowia i rodzaju masy użytej w przeliczeniu; agent nie powinien podawać go automatycznie jako indywidualnego celu. W S7 Arkadiusz powtarza zakres 2–3 g/kg, ale odmawia podawania konkretnych liczb drugiej osobie i krytykuje przesadę w ilości białka — to powtórzenie, nie nowa podstawa. (`S4` [19:22](https://youtu.be/ySgq9XysjD0?t=1162), `S7` [59:46](https://youtu.be/Xb2y18_B0QY?t=3586))
- W tym samym fragmencie Arkadiusz podaje 0,5–1 g tłuszczu/kg, a resztę kalorii rozdziela między węglowodany i preferencje/etap. Traktuj to jako jego praktyczną propozycję do weryfikacji, nie uniwersalny cel makro. (`S4` [19:22](https://youtu.be/ySgq9XysjD0?t=1162))
- Węglowodany mogą wspierać jakość wysiłku, ale rozmówca nie traktuje ich jako obowiązkowych do hipertrofii, jeśli użytkownik może wykonać równie dobry trening przy innych proporcjach makro. Jeśli spada wydolność treningowa, sprawdź całkowitą podaż energii, regenerację i rozkład jedzenia (dodatek autora; w źródle pada tylko spadek zdolności wysiłkowych). (`S4` [22:36](https://youtu.be/ySgq9XysjD0?t=1356), [24:25](https://youtu.be/ySgq9XysjD0?t=1465))
- Jeśli węglowodany są używane pod kątem treningu, rozmówca rozważa posiłek przed treningiem; po treningu pilność zależy m.in. od czasu do następnej jednostki. Białko w posiłku przed/po treningowym uznaje za istotne. Konkretne timingowe wskazówki są drugorzędne wobec całodziennego bilansu. (`S4` [24:57](https://youtu.be/ySgq9XysjD0?t=1497), [27:59](https://youtu.be/ySgq9XysjD0?t=1679), [28:48](https://youtu.be/ySgq9XysjD0?t=1728))
- Arkadiusz sugeruje, że węglowodany proste w trakcie treningu mogą podnieść zdolności wysiłkowe w konkretnym przypadku rozmówcy, który nie jadł przed treningiem; podaje przykład 20 g odżywki Carbo. Nie uogólniaj tej sytuacyjnej sugestii na każdego. (`S4` [35:09](https://youtu.be/ySgq9XysjD0?t=2109))
- Liczbę posiłków dopasuj do kaloryczności, dostępności czasu i preferencji (w źródle: kaloryczność, czas, preferencje; apetytu źródło nie wymienia). Rozmówca kwestionuje konieczność jedzenia białka co 2,5–3 godziny jako sztywnej reguły. (`S4` [29:13](https://youtu.be/ySgq9XysjD0?t=1753))
- Przy redukcji objętość posiłków, produkty sycące i własne upodobania mogą wspierać przestrzeganie planu. Smakowitość jedzenia może utrudniać kontrolę apetytu u niektórych osób; traktuj to indywidualnie. (`S1` [36:58](https://youtu.be/bpSubkCA168?t=2218); `S4` [39:52](https://youtu.be/ySgq9XysjD0?t=2392), [47:31](https://youtu.be/ySgq9XysjD0?t=2851))
- Jeśli deklarowane spożycie i trend masy nie pasują, sprawdź jakość pomiaru, porcje, dodatki, napoje i kompletność zapisu bez oskarżania użytkownika. Arkadiusz omawia „misreporting” jako często nieświadome pomijanie. Wagę kuchenną i dokładne ważenie zaleca Paweł, nie Arkadiusz. (`S4` [51:45](https://youtu.be/ySgq9XysjD0?t=3105), [54:16](https://youtu.be/ySgq9XysjD0?t=3256))
- Nie klasyfikuj produktów wyłącznie jako „dobre/złe”. Rozmówca akcentuje całkowite spożycie i nadmierną masę ciała, ale jego szerokie twierdzenia zdrowotne są streszczeniem wypowiedzi, nie indywidualną poradą medyczną. (`S4` [44:56](https://youtu.be/ySgq9XysjD0?t=2696), [45:52](https://youtu.be/ySgq9XysjD0?t=2752))
- Rozmówca proponuje na wakacjach elastyczność i przerwę od ścisłego liczenia, a w podróży logistyczne przygotowanie jedzenia. To opcje, nie nakaz; zależą od celu, historii użytkownika i relacji z jedzeniem. (`S4` [57:03](https://youtu.be/ySgq9XysjD0?t=3423), [58:19](https://youtu.be/ySgq9XysjD0?t=3499))

### 6. Twierdzenia wymagające szczególnej ostrożności

- Szacunki przyrostu masy mięśniowej na miesiąc/rok oraz ich spadku wraz ze stażem to uogólnienia rozmówcy, nie prognoza dla konkretnej osoby. (`S2` [02:12](https://youtu.be/XLTbnKL_fwk?t=132))
- Przelicznik kilokalorii na kilogram tłuszczu jest przybliżeniem; nie przeliczaj go wprost na gwarantowane tempo zmiany wagi. (`S1` [00:57](https://youtu.be/bpSubkCA168?t=57), `S4` [10:14](https://youtu.be/ySgq9XysjD0?t=614))
- Wypowiedzi o braku górnej granicy tempa redukcji są kontrowersyjne i nie powinny być używane jako zalecenie. Bezpieczeństwo i możliwość utrzymania tempa są ważniejsze. (`S1` [00:57](https://youtu.be/bpSubkCA168?t=57))
- W rozmowach pojawia się doping i środki farmakologiczne. Agent nie ma przekładać tych fragmentów na rekomendacje, dawkowanie ani optymalizację użycia. Kieruje pytania o leki do lekarza.

## Wszystkie liczby w bazie

Każda liczba występująca w tej bazie, z kontekstem i ryzykiem nadużycia. Podawaj liczbę **wraz z kontekstem**; jeśli kontekst nie pasuje do użytkownika, nie podawaj jej w ogóle.

### Dieta i kalorie

| Wartość | Co oznacza | Warunki | Źródło | Ryzyko nadużycia |
|---|---|---|---|---|
| 250–300 kcal | nadwyżka nad „zerem kalorycznym" | hipoteza praktyczna do indywidualnej obserwacji | `S2` [01:08](https://youtu.be/XLTbnKL_fwk?t=68) | traktowanie jako uniwersalnej recepty |
| 2–3 g/kg m.c. | białko; wyższy zakres przy głębszej redukcji | do weryfikacji względem aktualnych wytycznych, składu ciała i rodzaju masy użytej do przeliczenia | `S4` [19:22](https://youtu.be/ySgq9XysjD0?t=1162), `S7` [59:46](https://youtu.be/Xb2y18_B0QY?t=3586) | podanie jako indywidualnego celu |
| 0,5–1 g/kg m.c. | tłuszcz; reszta kalorii na węglowodany | propozycja rozmówcy, nie cel makro | `S4` [19:22](https://youtu.be/ySgq9XysjD0?t=1162) | jak wyżej |
| 0,5–1% m.c./tydz. | zakres tempa redukcji | „rozsądny punkt wyjściowy", nie norma bezpieczeństwa | `S1` [06:14](https://youtu.be/bpSubkCA168?t=374), `S4` [08:52](https://youtu.be/ySgq9XysjD0?t=532) | uniwersalizowanie procentu |
| 1% m.c./tydz. | sugerowana górna granica typowego celu | kontekst rozmówcy, nie bezpieczny limit | `S1` [39:43](https://youtu.be/bpSubkCA168?t=2383) | traktowanie jako zakazu redukcji powyżej 1% |
| 0,5 kg tłuszczu/tydz. | efekt deficytu 500 kcal/dzień przy przeliczniku ~7 tys. kcal/kg | przeliczenie przybliżone, nie prognoza | `S1` [00:57](https://youtu.be/bpSubkCA168?t=57), `S4` [10:14](https://youtu.be/ySgq9XysjD0?t=614) | liczenie „gwarantowanego" tempa |
| 5–10% | adaptacje metaboliczne (spadek zapotrzebowania) po redukcji | obserwacja rozmówcy | `S1` [49:42](https://youtu.be/bpSubkCA168?t=2982) | stosowanie jako korekty kalorii u każdego |
| 20 g | węglowodany w trakcie treningu (odżywka Carbo) | tylko w konkretnym przypadku rozmówcy, który nie jadł przed treningiem | `S4` [35:09](https://youtu.be/ySgq9XysjD0?t=2109) | uogólnianie na każdy trening |

### Objętość i progresja

| Wartość | Co oznacza | Warunki | Źródło | Ryzyko nadużycia |
|---|---|---|---|---|
| 10 serii/tydz./grupę | punkt startowy | niezależnie od poziomu (S2), powtórzony jako punkt wyjściowy (S5) | `S2` [06:46](https://youtu.be/XLTbnKL_fwk?t=406), `S5` [1:20:26](https://youtu.be/h2Vj5ai9Ang?t=4826) | **pomylenie z 10 seriami na jednej sesji** |
| 10 serii na jednej sesji | granica „efektywnej objętości" wg rozmówcy | twierdzenie do weryfikacji, nie limit | `S6` [09:40](https://youtu.be/blaB3aBrf1o?t=580) | pomylenie z tygodniowym punktem startowym |
| 5 serii | w S7 przywołane jako połowa objętości 10 serii | porównanie, nie osobna norma | `S7` [20:02](https://youtu.be/Xb2y18_B0QY?t=1202) | traktowanie jako minimum |
| 5–35 powtórzeń | szeroki zakres przy zbliżaniu do upadku | koszt zmęczenia rośnie wraz z liczbą powtórzeń | `S3` [40:35](https://youtu.be/IIi8e4i6pZE?t=2435) | czytanie jako normy |
| 6–8 / ~10 / 12 powtórzeń | punkty startowe zależnie od złożoności ćwiczenia | złożone z wolnym ciężarem / maszyny / izolacje | `S3` [43:32](https://youtu.be/IIi8e4i6pZE?t=2612) | traktowanie jako sztywnych limitów |
| 6 powtórzeń | może wystarczyć do uznania serii za efektywną | wypowiedź S2 o innej ramie niż S3 | `S2` [29:30](https://youtu.be/XLTbnKL_fwk?t=1770) | wyprowadzanie limitu z krótkiego fragmentu |
| do 10 powtórzeń | osobista preferencja Arkadiusza w S7 | dostosowywana do przypadku (klient po urazie tylnej części uda) | `S7` [31:27](https://youtu.be/Xb2y18_B0QY?t=1887), [32:14](https://youtu.be/Xb2y18_B0QY?t=1934) | ogłaszanie górnego limitu hipertrofii |
| do 12 powtórzeń | osobista preferencja Arkadiusza w S5 | wynika z koncentracji i zmęczenia metabolicznego | `S5` [1:06:45](https://youtu.be/h2Vj5ai9Ang?t=4005) | jak wyżej |
| 0,25 kg | mikroobciążenie | ułatwia stopniowe zwiększanie ciężaru | `S3` [58:12](https://youtu.be/IIi8e4i6pZE?t=3492) | — |
| 4–6 tygodni | horyzont bez postępu, po którym S2 proponuje dołożyć serię | sam rozmówca prosi, by nie przywiązywać wagi do tego czasu | `S2` [24:58](https://youtu.be/XLTbnKL_fwk?t=1498) | sztywny próg zastoju |
| 2–4 tygodnie | okno ponownej oceny | **dodatek autora skilla, nie wypowiedź rozmówcy** | — | traktowanie jako reguły źródeł |

### Częstotliwość

| Wartość | Co oznacza | Warunki | Źródło | Ryzyko nadużycia |
|---|---|---|---|---|
| 2×/tydz. na grupę | mocna rekomendacja przy optymalizacji | S2 mówi, że 2× nie jest obligatoryjne, jeśli ogranicza czas | `S3` [07:20](https://youtu.be/IIi8e4i6pZE?t=440), `S2` [14:22](https://youtu.be/XLTbnKL_fwk?t=862) | wygładzanie konfliktu źródeł |
| 3–5 treningów/tydz. | praktyka Arkadiusza w S7 | kierowanie się sumaryczną objętością i jej rozkładem | `S7` [12:27](https://youtu.be/Xb2y18_B0QY?t=747), [12:42](https://youtu.be/Xb2y18_B0QY?t=762), [12:46](https://youtu.be/Xb2y18_B0QY?t=766) | uniwersalizowanie częstotliwości |
| 4–5 treningów/tydz. | dla początkującego, który ma czas | aspiracja, nie plan do wykonania | `S8` [39:08](https://youtu.be/54BCbUZaHo0?t=2348) | jak wyżej |
| 2–3 treningi/tydz. | dla osób odchudzających się | zalecenie Robusia w S8; podobnie w podsumowaniu | `S8` [40:45](https://youtu.be/54BCbUZaHo0?t=2445), [1:09:07](https://youtu.be/54BCbUZaHo0?t=4147) | mylenie z powyższym |
| 6 dni (3 góra + 3 dół) | indywidualny przypadek powrotu po przerwie i dysproporcji | nie jest to plan ogólny | `S6` [02:30](https://youtu.be/blaB3aBrf1o?t=150) | kopiowanie jako szablonu |
| 7 dni mikrocyklu | mikrocykl nie musi pokrywać się z tygodniem kalendarzowym | można rozłożyć na 8–10 dni | `S3` [09:15](https://youtu.be/IIi8e4i6pZE?t=555) | — |

### Ćwiczenia i odpoczynek

| Wartość | Co oznacza | Warunki | Źródło | Ryzyko nadużycia |
|---|---|---|---|---|
| ≥2 min | punkt odniesienia dla przerwy | zależna od ćwiczenia i gotowości do kolejnej serii; w S7 także przy izolacjach | `S3` [30:52](https://youtu.be/IIi8e4i6pZE?t=1852), `S7` [46:19](https://youtu.be/Xb2y18_B0QY?t=2779), [46:27](https://youtu.be/Xb2y18_B0QY?t=2787) | skracanie kosztem jakości serii |
| 6–12 miesięcy | niezmienianie ćwiczenia kontrolnego | w S5; w S2 mówi „w skali całego roku" | `S5` [43:42](https://youtu.be/h2Vj5ai9Ang?t=2622), `S2` [21:14](https://youtu.be/XLTbnKL_fwk?t=1274) | nakładanie sztywnego cyklu |
| 9 lat | jak długo Arkadiusz sam nie zmienia ćwiczeń bazowych | opis jego praktyki, nie zalecenie | `S5` [40:39](https://youtu.be/h2Vj5ai9Ang?t=2439) | jak wyżej |
| 4, 6, 12 tygodni | okresy, po których zmiana ćwiczenia znosi punkt odniesienia | kontekst rozmowy o utrzymaniu ćwiczenia kontrolnego | `S7` [33:50](https://youtu.be/Xb2y18_B0QY?t=2030) | — |

### Aktywność i cardio

| Wartość | Co oznacza | Warunki | Źródło | Ryzyko nadużycia |
|---|---|---|---|---|
| 10 tys. → 5 tys. kroków | anegdotyczny spadek spontanicznej aktywności po wejściu w deficyt | przykład z doświadczenia, nie prognoza | `S1` [10:01](https://youtu.be/bpSubkCA168?t=601) | generalizowanie |
| +20% kroków | praktyka Robusia przy stagnacji | przed zmianą kalorii; nie uzgodniony protokół | `S8` [56:39](https://youtu.be/54BCbUZaHo0?t=3399) | stosowanie po jednym tygodniu bez trendu |
| 8 h odstępu | odstęp między treningiem aerobowym a siłowym | sugestia rozmówcy | `S8` [35:42](https://youtu.be/54BCbUZaHo0?t=2142) | jako sztywny wymóg |
| do 2,5 h cardio/dzień | anegdota Robusia o „ekstremalnych" dawkach | nie jest limitem ani zaleceniem | `S8` [28:53](https://youtu.be/54BCbUZaHo0?t=1733) | wyprowadzanie limitów cardio |
| poniżej 1000 kcal/dzień | anegdota z materiału promocyjnego | **źródła nie formułują z tego żadnego zalecenia** | `S8` [26:44](https://youtu.be/54BCbUZaHo0?t=1604) | budowanie protokołu kalorycznego |

## Cykl nadzoru

### Codziennie

- zapisz ćwiczenia, serie, powtórzenia, ciężar i — jeśli użytkownik tym operuje — subiektywny wysiłek/proksymację upadku (RIR/RPE pojawiają się w S5; nie narzucaj ich jako koniecznego sposobu raportowania);
- zapisz ból, nietypowe zmęczenie lub problemy techniczne;
- ostrożnościowo nie zmieniaj całego planu na podstawie jednej słabszej sesji; to zasada procesu agenta, nie cytat z podcastu.

### Co tydzień

- obserwuj trend masy; średnia tygodniowa może ograniczyć wpływ pojedynczych wahań, ale jest to metoda operacyjna dodana przez autora, nie zasada przypisana rozmówcom;
- sprawdź trend obciążenia/powtórzeń;
- sprawdź wykonanie zaplanowanych serii;
- oceń sen, regenerację, głód i trudność utrzymania kalorii;
- zaproponuj najwyżej jedną główną zmianę.

### Ponowna ocena

- dobierz termin do celu, jakości danych, liczby wykonanych treningów i bezpieczeństwa; sztywne okno 2–4 tygodni było dodatkiem autora skilla, nie występowało w transkrypcjach;
- jeśli trend i progres są zgodne z celem: utrzymaj plan;
- jeśli brak progresu mimo dobrego wykonania: dodaj mały bodziec, np. jedną serię lub niewielkie obciążenie;
- jeśli pogarsza się regeneracja, ból lub wykonanie: zmniejsz obciążenie albo skieruj użytkownika do specjalisty;
- jeśli zmiana masy jest zbyt szybka: skoryguj kaloryczność małym krokiem.

## Format danych wejściowych

```json
{
  "goal": "hypertrophy|fat_loss|maintenance",
  "body_mass_kg": 0,
  "weekly_body_mass_avg_kg": 0,
  "calories_avg": 0,
  "protein_g_avg": 0,
  "training_age_years": 0,
  "sessions": [],
  "sleep_hours_avg": 0,
  "pain_or_symptoms": null,
  "notes": ""
}
```

## Format odpowiedzi agenta

```text
Obserwacja: co wynika z danych.
Interpretacja: co może być przyczyną, z poziomem pewności.
Rekomendacja: jedna najważniejsza zmiana lub brak zmiany.
Monitoruj: jakie dane zbierać dalej.
Ponowna ocena: konkretny termin lub liczba treningów.
Źródło: zasada i timestamp, jeśli dotyczy.
```

## Ograniczenia i bezpieczeństwo

- Transkrypcje są materiałem źródłowym, nie niezależną walidacją naukową.
- Twierdzenia o dokładnym tempie przyrostu mięśni, „braku górnej granicy” redukcji i konkretnych nadwyżkach kalorycznych wymagają dodatkowej weryfikacji.
- Agent nie diagnozuje urazów, chorób ani zaburzeń odżywiania.
- Przy bólu, objawach neurologicznych, omdleniach, znacznym pogorszeniu samopoczucia lub podejrzeniu kontuzji agent ma przerwać optymalizację planu i zalecić konsultację ze specjalistą.
- Agent nie rekomenduje dopingu ani leków.

### Granice wiedzy (czego źródła nie poruszają)

Poniższych obszarów **nie ma** w ośmiu nagraniach. Nie uzupełniaj ich własnymi wnioskami ani nie przedstawiaj ich jako ustaleń rozmówców — odpowiedz wprost, że źródła tego nie mówią, i odsyłaj do aktualnej wiedzy klinicznej lub specjalisty.

- dawki i skuteczność suplementów poza białkiem (kreatyna, BCAA, przedtreningówki) — jedyne wzmianki to oznaczenia produktów w reklamach;
- protokoły rehabilitacji, zakres ruchu w rehabilitacji, powrót po operacjach — S6 to opis indywidualnego przypadku Arkadiusza, nie protokół;
- programowanie treningu w ciąży i po porodzie, u osób starszych, z chorobami przewlekłymi, po amputacji;
- dieta wegetariańska/wegańska, dieta bezglutenowa, nietolerancje pokarmowe — poza ogólną zasadą „jakość produktów nie jest problemem, problemem jest nadwaga" (`S4` [44:56](https://youtu.be/ySgq9XysjD0?t=2696));
- suplementacja w redukcji kontra budowie masy poza kwestią białka i węglowodanów;
- trening w drużynach sportowych, na boisku, w formie online;
- rozstrzygnięcie, ile powtórzeń jest „optymalne" — każde źródło podaje własny zakres i są one niespójne (patrz tabela napięć);
- tętno, HRV, glukoza, ciśnienie jako kryteria intensywności;
- rozkład jazdy w treningu oporowym, trening izometryczny w dużym obciążeniu, kontuzje ścięgien;
- wpływ posiłku na tempo przyrostu masy w badaniach — jedyne liczby to szacunki rozmówców, nie wyniki badań;
- bezpieczne tempo redukcji u osób z otyłością olbrzymią, po leczeniu farmakologicznym otyłości, po otyłości chirurgicznej;
- rola snu w adaptacji — źródła wskazują go jako ważny element regeneracji (`S2` [46:59](https://youtu.be/XLTbnKL_fwk?t=2819)), ale nie podają zaleceń.

Ogólna zasada: te nagrania to **wypowiedzi praktyków**, nie przegląd literatury. Gdy użytkownik prosi o rozstrzygnięcie naukowe, powiedz, że materiał tego nie dostarcza, i wskaż kierunek poszukiwań.

## Pochodzenie reguł i napięcia między źródłami

Wiedza źródłowa powinna być odróżniana od procedur dodanych przez autora skilla. W JSON reguły z podcastów mają `kind: podcast_paraphrase` oraz autora wypowiedzi (`speaker`); ostrożnościowe procedury agenta są osobno oznaczone jako `author_addition`. Nie przypisuj tych drugich rozmówcom.

W transkrypcjach zdarzają się sklejone lub urwane segmenty ASR. Atrybucję rób na podstawie pełnego sąsiedniego kontekstu, a gdy mówcy nie da się ustalić, wpisz `speaker: uncertain` zamiast zgadywać. Cytuj pełniejszy kontekst, nie pojedynczy urwany fragment.

Najważniejsze różnice, których nie należy wygładzać:

- Częstotliwość: S3 [07:20](https://youtu.be/IIi8e4i6pZE?t=440) mocno rekomenduje minimum 2 sesje/grupę; S2 [14:22](https://youtu.be/XLTbnKL_fwk?t=862) mówi, że 2× nie jest obowiązkowe i raz w tygodniu też ma sens.
- Częstotliwość: w S8 Arkadiusz mówi o 4–5 treningach, jeśli początkujący ma czas i chce maksymalizować proces ([39:08](https://youtu.be/54BCbUZaHo0?t=2348)); Robuś Pasjonat zaleca początkującym odchudzającym się 2–3 sesje ([40:45](https://youtu.be/54BCbUZaHo0?t=2445)), a w podsumowaniu obaj rozważają full body przy 2–3 treningach ([1:09:07](https://youtu.be/54BCbUZaHo0?t=4147)). Zachowaj różnicę między aspiracyjną częstotliwością a wykonalnym planem dla konkretnej osoby.
- Objętość: S2 [06:46](https://youtu.be/XLTbnKL_fwk?t=406) zaleca start od 10 serii/grupę niezależnie od poziomu; S3 [33:58](https://youtu.be/IIi8e4i6pZE?t=2038) stawia na indywidualne minimum, a utrzymanie skutecznej objętości z poprzedniego planu opisuje osobno w [01:04](https://youtu.be/IIi8e4i6pZE?t=64). S7 [16:09](https://youtu.be/Xb2y18_B0QY?t=969) i [17:20](https://youtu.be/Xb2y18_B0QY?t=1040) podkreśla indywidualny punkt wyjścia, ale później [20:02](https://youtu.be/Xb2y18_B0QY?t=1202) wymienia 10 serii jako benchmark. Nie wygładzaj tej zmiany akcentu.
- Powtórzenia: S2 [29:30](https://youtu.be/XLTbnKL_fwk?t=1770) mówi, że 6 powtórzeń wystarczy do efektywnej serii; S3 [40:35](https://youtu.be/IIi8e4i6pZE?t=2435) dopuszcza 5–35 przy bliskości upadku, a [43:32](https://youtu.be/IIi8e4i6pZE?t=2612) podaje węższe zakresy praktyczne zależne od złożoności. Przedstawiaj oba poziomy jako różne akcenty, nie jako dowiedzioną sprzeczność o jednym sztywnym limicie.
- Objętość: S2 [06:46](https://youtu.be/XLTbnKL_fwk?t=406) mówi o 10 seriach tygodniowo jako punkcie startowym, S3 [33:58](https://youtu.be/IIi8e4i6pZE?t=2038) o minimum skutecznym dla danej osoby, a S6 [09:40](https://youtu.be/blaB3aBrf1o?t=580) o ograniczeniu efektywnej objętości pojedynczej sesji do ok. 10 serii. Tygodniowy punkt startowy i limit na sesję to różne twierdzenia; nie łącz ich w jedną liczbę.
- Częstotliwość: S3 [07:20](https://youtu.be/IIi8e4i6pZE?t=440) mocno rekomenduje minimum 2 sesje/grupę; S2 [14:22](https://youtu.be/XLTbnKL_fwk?t=862) podkreśla, że 2× nie jest obowiązkowe; S5 [55:41](https://youtu.be/h2Vj5ai9Ang?t=3341) ponownie rekomenduje 2× w kierunku optymalizacji, a S7 [24:44](https://youtu.be/Xb2y18_B0QY?t=1484) preferuje taki rozkład, jeśli pozwala utrzymać jakość serii. S6 [02:30](https://youtu.be/blaB3aBrf1o?t=150) opisuje 6 dni góra/dół w szczególnej sytuacji powrotu po przerwie i dysproporcji — nie jest to ogólny plan.
- Zakres powtórzeń: szerokie możliwości omawiane w S3 [40:35](https://youtu.be/IIi8e4i6pZE?t=2435) współistnieją z osobistą preferencją Arkadiusza, by zwykle nie programować sobie powyżej 12 powtórzeń w S5 [1:06:45](https://youtu.be/h2Vj5ai9Ang?t=4005). Nie przedstawiaj jego osobistej preferencji jako górnego limitu hipertrofii.
- Redukcja i objętość: S5 [47:01](https://youtu.be/h2Vj5ai9Ang?t=2821) odradza automatyczne zwiększanie objętości i opisuje jej stopniowe obniżanie w miarę ograniczeń energetycznych; S8 [04:50](https://youtu.be/54BCbUZaHo0?t=290) oraz [14:15](https://youtu.be/54BCbUZaHo0?t=855) przedstawia objętość jako późniejszą dźwignię, po korekcie kosztu zmęczeniowego i wysiłku. To różne poziomy szczegółowości, nie sprzeczność.
- Cardio na redukcji: S1 [17:36](https://youtu.be/bpSubkCA168?t=1056) i Arkadiusz w S8 [25:03](https://youtu.be/54BCbUZaHo0?t=1503) nie traktują treningu siłowego/cardio jako automatycznego narzędzia spalania; S8 jednocześnie dopuszcza cardio dla zdrowia lub zwiększenia wydatku i ostrzega przed wpływem wysokiej intensywności na jakość sesji siłowej ([28:00](https://youtu.be/54BCbUZaHo0?t=1680)). Nie zamieniaj tych opinii w uniwersalny zakaz ani obowiązek cardio.
