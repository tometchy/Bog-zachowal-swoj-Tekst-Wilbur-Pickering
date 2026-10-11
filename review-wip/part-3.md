# Przegląd roboczy — część 3 (chapters/31–37)

Źródło: `God-Has-Preserved-His-Text-4th.pdf`. Numery stron: druk/PDF (PDF = druk + 8). Kontrola wyłącznie odczytowa książki; zapisuję tylko uwagi, bez korekt tekstu.

## Checkpoint

- Rozpoczęto: 2026-10-10.
- Przydzielony zakres: chapters/31–37, druk 183–260 / PDF 191–268.
- Zakończone: rozdziały 31–33, tekst główny, przypisy, liczby, trzy profile greckie, dwie tabele poświadczeń, wykazy manuskryptów oraz formatowanie według XML PDF; istotne gwiazdki sprawdzone wizualnie (druk 193–194).
- Zakończone także: rozdziały 34–35, druk 197–214, całość tekstu i przypisów, oba wykazy 26/52 manuskryptów, tabela lokalizacji, siedem zestawień greckich (119 odczytów) z liczbami i znakami; podkreślenia rozdziału 34 sprawdzone wizualnie (druk 200, 203).
- Zakończono także tekstowe porównanie całości 36–37, druk 215–259 / PDF 223–267, wraz ze wszystkimi przypisami, czterema tabelami kombinacji świadków w 36 i pełnym wykazem manuskryptów 1 Listu Jana. Druk 260 / PDF 268 jest pusty.
- Rozdział 35: 28 + 42 + 13 + 26 + 7 + 3 = 119. Wszystkie pozycje zestawień i sumy sprawdzone, bez rozbieżności (dawne P3-S05 było wynikiem pozytywnym, nie problemem źródła).
- Zakończono wyróżnienia 36–37: XML całości dla pogrubień/kursywy, wektorowe podkreślenia całego zakresu z `mutool draw -F trace`, następnie obrazy wszystkich miejsc zgłoszonych poniżej. Obrazy: `/tmp/pickering-review-lbPxWh/source-p3finish-223.png` do `source-p3finish-268.png`.
- Po tym zakresie recenzent przejmuje 18–21 do osobnego `review-wip/part-5.md`.
- Narzędzia pomocnicze: `/tmp/pickering-review-lbPxWh/source-layout.txt`, `source.xml`; dla formatowania źródłem rozstrzygającym jest PDF.

## Uwagi potwierdzone

### P3-001 — terminologia: niejednoznaczność odwołań do wzorców kopii (do decyzji)

- PL: `chapters/31-czesc-3-czy-f35-jest-starozytna.md:7` i dalej w. 9–11: „egzemplarze 35 i 2723”, „Egzemplarz 1897”, „Egzemplarz 2587”.
- EN: druk 183–184 / PDF 191–192: „the exemplars **of** 35 and 2723”, „The exemplar **of** 1897”, „the exemplar **of** 2587”.
- Problem: *exemplar* oznacza tu wzorzec, z którego przepisano dany manuskrypt. „Egzemplarz” może funkcjonować jako ustalony termin techniczny, dlatego nie oznaczam każdego jego wystąpienia jako błędu. Konkretna konstrukcja „egzemplarz 1897” łatwo jednak oznacza sam zachowany manuskrypt 1897, podczas gdy EN mówi o jego wzorcu. Argument polega na cofnięciu się o kolejne pokolenie; niejednoznaczna składnia może je zgubić.
- Kierunek do decyzji: np. „egzemplarz będący wzorcem manuskryptu 1897” albo wyjaśnienie technicznego znaczenia „egzemplarza”; zachować rozróżnienie wzorca i kopii także w dalszych odwołaniach. Nie zmieniać datowania ani argumentu autora.

### P3-002 — forma/dane: brak oznaczeń diagnostycznych w profilu M^6^ (ważne)

- PL: `chapters/33-czesc-3-o-tekscie-pericope-adulterae.md:74` i w. 76, zestawy 27 i 29: `(και μηδενα...)`, `(αυτη) γυναι`.
- EN: druk 193 / PDF 201: `**(και μηδενα θεασαμενος πλην της γυναικος)` oraz `**(αυτη) γυναι`.
- Obie pary gwiazdek są widoczne w PDF. To literalne znaczniki wariantów, do których odsyła zdanie o dziesięciu wariantach tworzących „kręgosłup”. W polskiej tabeli zostało tylko osiem oznaczonych wierszy.
- Kierunek: przywrócić literalne `\*\*` przed nawiasami w obu komórkach, tak jak w pozostałych wierszach.

### P3-003 — forma/dane: brak oznaczeń diagnostycznych w profilu M^5^ (ważne)

- PL: `chapters/33-czesc-3-o-tekscie-pericope-adulterae.md:92` i w. 113, zestawy 05 i 26: `(προς αυτον)`, `(εως των εσχατων)`.
- EN: druk 194 / PDF 202: `**(προς αυτον)`, `**(εως των εσχατων)`.
- Gwiazdki potwierdzone wizualnie; pełnią tę samą rolę co w P3-002. Kierunek: przywrócić literalne `\*\*` przed nawiasami.

### P3-004 — forma: przesunięty zakres podkreślenia

- PL: `chapters/33-czesc-3-o-tekscie-pericope-adulterae.md:162`: podkreślenie obejmuje „również musieli być doskonali. Proszę zauważyć, że doskonała kopia czyni wszystkie”.
- EN: druk 196 / PDF 204: podkreślone tylko „all of its ‘ancestors’ had to be perfect as well” (potwierdzone na renderze strony).
- Kierunek: objąć podkreśleniem „wszyscy jej «przodkowie» również musieli być doskonali”, a usunąć je z początku następnego zdania. To błąd zakresu formatowania, nie tłumaczenia treści.

### P3-005 — kompletność: pominięty cały przypis objaśniający statystykę (ważne)

- PL: `chapters/34-czesc-3-kiedy-mamy-do-czynienia-z-recenzja.md:43`, po pierwszym `[2 podw.]` brakuje odsyłacza i treści przypisu.
- EN: druk 202 / PDF 210, przypis 2: „‘subs’ stands for sub-variants, which are included in the larger number. Where a ‘sub’ is also a singular I list it only as a singular—each variant is counted only once.”
- Kierunek: dodać tłumaczenie całego przypisu, z unikatowym opisowym identyfikatorem, i osadzić odsyłacz przy pierwszym użyciu skrótu „podw.”. Brakuje informacji, że podwarianty są już wliczone w podaną większą liczbę, a podwariant singularny liczy się tylko raz jako singularny.

### P3-006 — forma: dwa przesunięte podkreślenia

- PL: `chapters/34-czesc-3-kiedy-mamy-do-czynienia-z-recenzja.md:29`: podkreślono „kopia nadal tam jest, nie sporządzono jej, aby zrealizować zamówienie z miasta. Dlaczego więc”. EN druk 200 / PDF 208 podkreśla tylko „If the copy is still there,”, czyli „Jeśli kopia nadal tam jest,”.
- PL: ten sam plik w. 123, przypis `pelne-kolacjonowania-ujawniaja-odrebnosc`: podkreślono „tej rodziny, biorąc pod uwagę tylko manuskrypty, które sam skolacjonowałem, możemy powiedzieć, co następuje”. EN druk 203 / PDF 211 podkreśla tylko „within that family”, czyli „w obrębie tej rodziny”.
- Oba zakresy sprawdzone wizualnie; kierunek: przywrócić dokładny zakres podkreśleń autora.

### P3-007 — treść: niejasne „listy” zamiast wykazów manuskryptów

- PL: `chapters/34-czesc-3-kiedy-mamy-do-czynienia-z-recenzja.md:123`: „zarówno dla 2, jak i 3 Listu Jana [nie są to identyczne listy]”.
- EN: druk 203 / PDF 211: „for both 2 and 3 John (not identical lists)”. Autor mówi o dwóch wykazach manuskryptów; polskie „listy” tuż po nazwach listów biblijnych może znaczyć same księgi i zaciera informację.
- Kierunek: np. „[nie są to identyczne wykazy manuskryptów]”, zachowując zagnieżdżenie nawiasów.

## Problemy źródła / wymagające dalszej weryfikacji

### P3-S01 — niespójność autora: manuskrypt bizantyjski w pierwszej kolumnie

- PL: `chapters/32-czesc-3-znaczenie-obiektywnych-dowodow.md:128` i w. 148; EN druk 189–190 / PDF 197–198.
- Tabela ma `1827*` w pierwszej kolumnie, a gwiazdka oznacza manuskrypt sklasyfikowany jako bizantyjski. Następny akapit mówi jednak: „There are no Byzantine MSS in the 1st column” / „W pierwszej kolumnie nie ma manuskryptów bizantyjskich”.
- Polski wiernie oddaje niespójność oryginału. Nie poprawiać jej po cichu; ewentualna uwaga tłumacza poza argumentacją autora.

### P3-S02 — prawdopodobna literówka autora w odsyłaczu do wariantu

- PL: `chapters/33-czesc-3-o-tekscie-pericope-adulterae.md:130`; EN druk 195 / PDF 203: „in 8:9 it has κατεληφθη”.
- Odczyt dotyczy schwytania kobiety; według profili w tym rozdziale odpowiada miejscu 8,3 (zestaw 08), nie 8,9. Dalej autor mówi, że b) i c) różnią się od a) jedynie podobnie brzmiącą samogłoską, co może wskazywać jeszcze inną omyłkę w greckim zapisie c). Nie rozstrzygnięto zamierzonego tekstu autora. Polski wiernie zachowuje zapis źródła; nie zmieniać bez osobnej decyzji.

### P3-S03 — błędny odsyłacz wewnętrzny już w źródle

- PL: `chapters/34-czesc-3-kiedy-mamy-do-czynienia-z-recenzja.md:265`; EN druk 208 / PDF 216, przypis 2: „Concerning the Text of the Pericope Adulterae” wskazano „in Part II”. Rozdział znajduje się w części III (druk 191), co odpowiada `chapters/33-*`.
- Nie traktować jako błędu tłumaczenia. Ewentualne sprostowanie wymaga oznaczenia jako ingerencja redakcyjna/uwaga tłumacza.

### P3-S04 — liczba 44 już w źródle

- PL: `chapters/34-czesc-3-kiedy-mamy-do-czynienia-z-recenzja.md:241`; EN druk 207 / PDF 215: po omówieniu 30 manuskryptów spoza f^35^ i kolejnych 12 autor pisze „we now have 44 MSS”. Suma wskazanych grup wynosi 42.
- Zapis PL „44” jest wierny źródłu. Nie poprawiać autora po cichu.

### P3-S05 — niezamknięty nawias już w źródle

- PL: `chapters/36-czesc-3-concordia-discors-i-odczyty-mniejszosciowe-f35-w-listach-ogolnych.md:101`, końcowe „300)”. EN druk 220 / PDF 228 kończy analogicznie „year 300.)” bez odpowiadającego nawiasu otwierającego. Nie jest to błąd tłumaczenia; ewentualna korekta wymaga decyzji redakcyjnej.

## Uzupełnienia z kontynuacji 2026-10-11

### P3-008 — forma/dane: Pandoc usuwa gwiazdki klasyfikacji manuskryptów (ważne)

- PL: `chapters/32-czesc-3-znaczenie-obiektywnych-dowodow.md:93`, wyliczenie 43 manuskryptów od „A, C, 81, 104*” do „2818*”. EN druk 188 / PDF 196.
- Gwiazdki po numerach oznaczają manuskrypty bizantyjskie, ale są zapisane jako niewyescapowane znaczniki Markdown. Pandoc interpretuje kolejne pary jako kursywę: polecenie `pandoc chapters/32-czesc-3-znaczenie-obiektywnych-dowodow.md --from=markdown-smart -t latex` zwraca m.in. `104\\emph{, 436, 459}` i `467\\emph{, 607, 720}`. W rezultacie znikają ważne oznaczenia danych, a fragmenty wyliczenia otrzymują przypadkową kursywę.
- Kierunek: literalne gwiazdki zabezpieczyć jako `\*`, bez zmiany numerów ani klasyfikacji autora. Gwiazdki w pojedynczych komórkach tabel są osobną sprawą i w sprawdzonym wyjściu zachowują się prawidłowo.

### P3-009 — forma/eksport: utrata podziałów w nagłówkach tabel (część globalnego G-001)

- PL: ten sam plik, w. 9 i 103; EN druk 185–186 i 189 / PDF 193–194 i 197.
- `<br>` między numerem wersetu a greckim odczytem jest pomijane przez eksport LaTeX: nagłówki stają się np. `3,6και`, `5,11ο θεος ημιν`, `1,6περιπατουμεν`. Wymaga rozwiązania zgodnego z Pandokiem i sprawdzenia PDF/EPUB/DOCX; nie wystarczy poprawność podglądu GitHuba.

### P3-010 — treść: dokonane działanie w przeszłości zmienione w przyszłą możliwość

- PL: `chapters/36-czesc-3-concordia-discors-i-odczyty-mniejszosciowe-f35-w-listach-ogolnych.md:194`, cytat 1 Listu Piotra 4,3: „czas, który przeminął, wystarczy wam do pełnienia woli pogan”.
- EN druk 224 / PDF 232: „the time that has passed is plenty for you to have performed the will of the Gentiles”.
- Konstrukcja *to have performed* odnosi się do dotychczasowego spełniania tej woli. „Wystarczy wam do pełnienia” sugeruje możliwość/przeznaczenie czasu na przyszłe działanie. Zachować odniesienie do tego, co czytelnicy już czynili, tłumacząc cytat autora, a nie zapożyczając wersetu z innej Biblii.

### P3-011 — treść: zatarte „do wnętrza nas” w cytacie i przypisie

- PL: `chapters/37-czesc-3-podstawowa-przyczyna-ciaglego-odchodzenia-od-biblijnej-nieomylnosci.md:153` oraz przypis `moc-skierowana-do-wierzacych`, w. 213: „mocy skierowanej do nas”, „«Skierowanej do nas» — tak mówi Tekst”.
- EN druk 249 / PDF 257: „His power into us”, a przypis rozpoczyna się „«Into us»—that is what the Text says” i następnie objaśnia moc, którą Bóg „pours into us”.
- „Skierowana do” osłabia znaczenie kierunku do wnętrza i zaciera dokładnie ten element, który przypis wyróżnia. Kierunek: zachować w cytacie i przypisie sens „w nas / do naszego wnętrza”, z decyzją o naturalnej, lecz wiernej polskiej składni.

### P3-012 — treść: dokonane oświecenie zmienione w cel modlitwy

- PL: ten sam plik, w. 153: „aby oczy waszego serca zostały oświecone”, podobnie cytat w przypisie `rzeczywiste-poznanie-epignosis`, w. 211.
- EN druk 249 / PDF 257 w obu miejscach: „the eyes of your heart having been enlightened”.
- Forma dokonana podaje stan uprzednio zaistniały, podczas gdy „aby” włącza oświecenie do tego, o co dopiero się prosi. Kierunek: zachować czasową/logiczno-składniową relację cytatu Pickeringa, np. „gdy oczy waszego serca zostały już oświecone”.

### P3-013 — forma: brakujące i poszerzone wyróżnienia w rozdziale 36

Poniższe podkreślenia potwierdzono na obrazie oryginału. Lokalizacje PL dotyczą `chapters/36-czesc-3-concordia-discors-i-odczyty-mniejszosciowe-f35-w-listach-ogolnych.md`.

| PL wiersz | EN druk / PDF | Rozbieżność |
| --- | --- | --- |
| 47, 162, 252, 326 | 216/224, 222/230, 226/234, 229/237 | Wszystkie cztery podnagłówki *f35 minority readings* są kursywą, PL „Odczyty mniejszościowe…” bez kursywy. |
| 61 | 217/225 | Pogrubione i podkreślone jest tylko *no*, nie *absolutely*. PL obejmuje oboma wyróżnieniami „absolutnie żadnego”; ograniczyć do „żadnego”. |
| 63 | 217/225 | Brak podkreślenia „szesnaście” (*sixteen*). |
| 262 | 226/234 | Brak podkreślenia „nijakiego” (*neuter*). |
| 301–317 | 228–229/236–237 | Siglum f35 w tabeli dla 1 Listu Jana, poza pierwszym wierszem „f35 alone”, jest zwykłym drukiem, PL dodaje pogrubienie wszystkim wystąpieniom. Niskopriorytetowa różnica formy, nie danych. |
| 375 | 230/238 | Brak podkreślenia przeczenia „nie ma” w zdaniu o pokrywaniu się dwóch pierwszych kolumn (*no*). |
| 379 | 231/239 | Brak podkreślenia przeczenia „nie ma” w porównaniu z ιθυνοντος (*no*). |
| 383 | 231/239 | Brak podkreślenia „absolutnie nie” w zdaniu o zachowanych manuskryptach (*absolutely do not*). |
| 397 | 232/240 | Brak podkreślenia „wszystkich” (*all*). |

### P3-014 — forma: rozbieżności wyróżnień w rozdziale 37

Wszystkie wymienione podkreślenia sprawdzono na renderach oryginału, pogrubienia i kursywę także w XML. Lokalizacje PL dotyczą `chapters/37-czesc-3-podstawowa-przyczyna-ciaglego-odchodzenia-od-biblijnej-nieomylnosci.md`.

| PL wiersz | EN druk / PDF | Rozbieżność |
| --- | --- | --- |
| 11 | 234–235/242–243 | Brak podkreślenia „najgorsze” (*worst*) oraz drugiego „oba” (*both*, w zdaniu „w których oba się mylą”). |
| 13 | 235/243 | Podkreślone tylko „i rozum” (*and reason*), a PL rozciąga podkreślenie na następne zdanie aż po „tylko”. |
| 23 | 237/245 | Brak podkreślenia „dzisiaj” (*today*). Pogrubione „musi” jest poprawne, odpowiada pogrubionemu *has* na następnej stronie. |
| 37 | 235/243 | Przypis o Burgonie: brak podkreślenia „najstarsze naprawdę znaczy najgorsze” (w EN podkreślono *oldest equals worst*, bez poprzedniego *Yes indeed*). |
| 79 | 239/247 | Przypis o miłości prawdy: brak podkreślenia „miłowali” (*love*). |
| 85 | 240/248 | Brak podkreślenia „ta” w „skąd pochodzi ta doktryna” (*that*). |
| 99 | 243/251 | EN podkreśla tylko hiperłącza, PL obejmuje wielozdaniowym podkreśleniem tekst od „Większość mojej twórczości” do „faktem”. Usunąć to rozszerzenie i zachować odrębne linki. |
| 123 | 246/254 | EN podkreśla wyłącznie zdanie „Można przypisać rodzinie współczynnik wiarygodności oparty na obiektywnych kryteriach”, PL także część następnego zdania do „rozpoznana”. |
| 125, 127, 279 | 247/255, 257/265 | Brak kursywy *INTF*: oba wystąpienia w omówieniu serii wydawniczych i w przypisie o kolacjonowaniach Robinsona. |
| 133 | 248/256 | Brak podkreślenia „nas” w „przyszłości, która obejmuje nas” (*us*). W cytacie Łk 10,19 EN podkreśla również *the* przed *authority* — sposób oddania emfazy rodzajnika wymaga decyzji, nie mechanicznego dodania słowa. |
| 155 | 250/258 | Źródło pogrubia i podkreśla tylko „daleko” (*far*), PL dodatkowo pogrubia „ponad”. |
| 163 | 251/259 | Brak podkreślenia „wam” w „co wam nakazałem” (*you*); podkreślenie „nie” przy 94% jest zachowane. |
| 185 | 253/261 | Brak podkreślenia „powinniśmy” (*should*). |
| 213 | 249/257 | Przypis o mocy: brak podkreślenia „nie” w „nie wykorzystujemy Jego mocy” (*not*). |
| 215 | 250/258 | Powtórny cytat Łk 10,19 podkreśla *the* przed *authority*; analogiczna decyzja co w w. 133. |
| 221 | 255/263 | Brak podkreślenia „którego tam nie było” (*who was not there*). |
| 225 | 255/263 | Brak podkreślenia „statystycznie niemożliwe” (*statistically impossible*). |
| 229 | 256/264 | Brak podkreślenia „Jednak” (*However*). Duże podkreślenie zdania o dostępie do przedstawiciela f35 na następnej stronie zachowano prawidłowo. |
| 231 | 257/265 | EN podkreśla *the* w *the archetypal form*; polski sposób zaznaczenia określoności wymaga decyzji. |
| 263 | 259/267 | Kursywa powinna obejmować „każdym” (*every*), a obejmuje „słowem”. |
| 271 | 259/267 | Podkreślone są osobno nazwy kryteriów: „liczebności”, „niezależności”, „wieku”, „rozmieszczenia geograficznego”, „profilu”, „staranności”, „zakresu”. PL podkreśla ciągły fragment razem z nawiasami/objaśnieniami do tytułu „Współczynnik staranności kopisty”, lecz pomija końcowy „zakres”. |
| 283 | 258/266 | W przypisie EN podkreśla wyłącznie *text* („tekst”); PL całe „tekst f35 jest starożytny (a także niezależny)”. |

### P3-015 — forma: wielkość liter zaimków w cytatach biblijnych

- PL: rozdział 37, w. 149, 151, 153, 199, 201 (plik jak wyżej). EN druk 248–249 i 254 / PDF 256–257 i 262.
- W J 20,21 źródło ma *me*, PL „Mnie”; w Hbr 10,7 *your will*, PL „Twoją wolę”; w J 14,12 (cytat i jego powtórzenie) *into me*, PL „we Mnie”. Zgodnie z zasadą 16 zachować małe litery tych zaimków.
- W odwrotnym kierunku: Ef 2,4–6 ma *His great love*, PL „swojej wielkiej miłości”; Ef 1,16–21 ma *Himself* i *at His[F] right*, PL „samego siebie” i „po swojej[O] prawicy”. Tam, gdzie zaimek ma po polsku odpowiednik, zachować wyróżnienie wielką literą źródła.
- W w. 205 cytowane *you apostles* zmieniono na „wy, Apostołowie” (druk 255 / PDF 263); również zachować małą literę w cytacie.

### P3-016 — forma: zagnieżdżone nawiasy okrągłe zamiast wewnętrznych kwadratowych

- PL: rozdział 36, w. 379 i 383: `(3,4 (21%))`, `(3,2 (23%))`; EN druk 231 / PDF 239: `(3:4 [21%])`, `(3:2 [23%])`.
- PL: rozdział 37, w. 201 (Piotr zrobił kilka kroków…), 265 (22 / przypuszczalnie / 4 / Dzieje Apostolskie wewnątrz dużego nawiasu), 275 (tom towarzyszący UBS3 wewnątrz danych bibliograficznych). EN druk 254, 259, 256 / PDF 262, 267, 264.
- Zastosować regułę AGENTS: okrągły nawias zewnętrzny, kwadratowy wewnętrzny. Zachować całą treść dopowiedzeń.

### P3-T01 — terminologia: „niezachowany jeszcze” jako odpowiednik nieznanego świadectwa

- PL: rozdział 36, w. 121: P72 „niezachowany jeszcze w czasach Burgona”; rozdział 37, w. 143 i 279: manuskrypty „jeszcze «niezachowane»”. EN druk 220, 246, 257 / PDF 228, 254, 265: *wasn’t extant*, *not yet ‘extant’*.
- Autor używa *extant* w szczególnym sensie: nieznane / jeszcze niezidentyfikowane i nieskatalogowane (sam to objaśnia w przypisie druk 246). Po polsku „niezachowany” zwykle oznacza, że obiekt nie przetrwał, a „jeszcze niezachowany” daje sprzeczną sugestię czasową. Problem wymaga wspólnej decyzji terminologicznej z analogicznymi miejscami w dodatkach; nie prostować po cichu autora.

### P3-T02 — terminologia: dwa powtarzające się odpowiedniki wymagające ujednolicenia z regułami

- Rozdział 36, w. 5 i rozdział 37, w. 37: *solitary evidence* w cytacie Burgona oddano jako „samotne świadectwo” (druk 215 i 235 / PDF 223 i 243), mimo ustalonego *evidence → dowód/dowody*. Rozważyć wierną składnię zachowującą przyjęty termin, nie mylić z osobnym *testimony*.
- Rozdział 36, w. 107: bibliograficzne *Catholic epistles* (druk 217 / PDF 225) oddano jako „Listy Ogólne”, identycznie jak *General Epistles*. To ten sam problem zachowania rozróżnień nazw co w innych rozdziałach, do decyzji globalnej, nie jako zarzut zmiany zawartości zbioru ksiąg.
