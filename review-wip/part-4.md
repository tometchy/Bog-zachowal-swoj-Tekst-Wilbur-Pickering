# Roboczy raport: dodatki 38–49 i kontrola globalna

## Postęp do wznowienia

- Oceniany commit: `4d35b43d4dd9868d5a600c1f4b9c88128f58010c`.
- Przeczytano w całości i porównano tekst oraz przypisy rozdziałów 39–47 (druk 273–296, PDF 281–304).
- Porównano zawartość tabel 40–41, wykazy 44–45 oraz b/i z XML. Wizualnie sprawdzono PDF 288 (tabela miejsc), 290–291 (wszystkie podkreślenia rankingu), 301 (greckie odczyty). Ranking 41 ma 88 podkreślonych oznaczeń, zgodnych z obejrzanym źródłem; podkreślenia niosą informację o rodzinie.
- Obejrzano polski istniejący PDF, stronę pliku 348: tabela z rozdziału 40 ma zlane i nachodzące na siebie nazwy.
- Kontrola globalna: 380 definicji i 380 użytych identyfikatorów przypisów; brak powtórzonych definicji, niezdefiniowanych odsyłaczy i nieużytych przypisów. Skorygowano fałszywy alarm skanera dla odsyłacza, po którym stał dwukropek. 92 ciągi tabel kreskowych; w każdym spójna liczba komórek, co samo w sobie nie dowodzi poprawności ich zawartości.
- Rozdział 48: porównano cały tekst i wszystkie przypisy, także ostatni akapit na druk 313; obejrzano wszystkie strony PDF 305–321. Diagram Rysunek_A jest współdzielony z częścią I, tam kontrolowany przez recenzenta.
- Rozdział 49: porównano cały tekst i wszystkie przypisy, 78 wierszy dużej tabeli, 14 wierszy tabeli podsumowującej i pięć wierszy zestawienia rękopisów kursywnych. Obejrzano wszystkie strony PDF 321–331, sprawdzono b/i w XML.
- Rozdział 38: pełna treść i oba przypisy przeczytane, wszystkie 136 pozycji porównane; greckie ciągi i zbiór 54 pogrubionych numerów sprawdzone dodatkowo skryptem. Wszystkie strony PDF 269–281 obejrzane. Nie znaleziono pominiętej pozycji wykazu ani zmiany odczytu greckiego.
- Zakończono kontrolę wizualną wszystkich stron PDF 269–331: komplet zakresu 38–49. Zestaw 290–291 (ranking) i 301 (grecki cytat) dodatkowo oglądany w większej rozdzielczości. Pozostała konsolidacja oraz kontrola globalna.
- Globalny test parsera Pandoca (`--from=markdown-smart -t json`) całego połączonego zbioru 50 plików: brak ostrzeżeń, 380 obiektów przypisu, 93 tabele, pięć odwołań do istniejących obrazów. 92 tabele zapisane kreskami i jedna innego typu w rozdziale 21. Jedyne surowe wstawki to 69 znaczników HTML `<br>` (G-001). Nie generowano ani nie nadpisywano plików wynikowych książki.

## Potwierdzone uwagi

### G-001 — Forma / eksport: `<br>` znika w PDF i skleja różne odczyty oraz dane tabel

- Lokalizacja: `chapters/40-dodatek-podgrupy-f35-w-listach-ogolnych.md:7–20,158–159`; także `chapters/49-dodatek-przedstawienie-dowodow-przez-alanda.md:111` (klasyfikacje `E++<br>E+<br>E` itp. tracą rozdzielenie). Ten sam zapis występuje w `32` (konkretne przypadki w raporcie części III).
- Źródło: druk 275–276, 280 / PDF 283–284, 288. Odczyty i nazwy są rozdzielone wierszami.
- Dowód: przy ustawieniach wejściowych Makefile (`markdown-smart`) polecenie `pandoc chapters/40-dodatek-podgrupy-f35-w-listach-ogolnych.md --from=markdown-smart -t latex` daje m.in. `εχειεχη`, `αλλαλλα`, `γινωσκοντεςγινωσκοντας`. Zapis `Konstamonitu<br>Kutlumusiu<br>Filotheu` staje się jednym ciągiem.
- Skutek widoczny także w **istniejącym** polskim PDF-ie: strona pliku 341 zawiera sklejone odczyty, a na 348 nazwy w tabeli rozmieszczenia zachodzą na sąsiednie kolumny i wychodzą za prawy brzeg strony. To utrata rozdzielenia danych, nie tylko kosmetyka.
- Do poprawy w przyszłym etapie: użyć podziału komórek/wierszy obsługiwanego przez Pandoca we wszystkich formatach albo jawnej konwersji podziałów przed eksportem. Po zmianie konieczna kontrola PDF, EPUB i DOCX. W tym review nic nie zmieniono.

### P4-001 — Treść: pominięte Lesbos w tabeli rozmieszczenia

- Lokalizacja: `chapters/40-dodatek-podgrupy-f35-w-listach-ogolnych.md:159`, komórka „Gdzie indziej / Tryb łączący”.
- Źródło: druk 280 / PDF 288; w kolejności `Karditsa, Leiden, Lesbos, London, Meteora, Sofia, Vallicelliana (Rome), Zittau`.
- PL: `Karditsa<br>Lejda<br>Londyn...` — brak **Lesbos** pomiędzy Lejdą i Londynem. Potwierdzono na obrazie strony źródłowej.
- Do poprawy: przywrócić pozycję Lesbos w odpowiedniej komórce, niezależnie od technicznego problemu G-001.

### P4-002 — Treść: „of any size” nie oznacza „o jakichkolwiek rozmiarach”

- Lokalizacja: `chapters/39-dodatek-ocena-podstawowej-zasady.md:19`, „naszym najwcześniejszym manuskryptom o jakichkolwiek rozmiarach (P^66^)”.
- Źródło: druk 274 / PDF 282, `our earliest MSS of any size (P66)`.
- Autor ogranicza twierdzenie do manuskryptów o znaczącej objętości, a nie do wszystkich, niezależnie od wielkości zachowanego fragmentu. Polski zapis zaciera to ograniczenie.
- Kierunek korekty: „naszym najwcześniejszym manuskryptom o większej objętości” lub równoważne wierne oddanie idiomu.

### P4-003 — Treść: „legitimate” w opisie oszczędzania pergaminu

- Lokalizacja: `chapters/43-dodatek-definiowanie-zachowania.md:13`, „każdy zgodny z prawem sposób oszczędzania”.
- Źródło: druk 287 / PDF 295, `any legitimate means of economizing those materials`.
- Kontekst dotyczy dopuszczalnych zabiegów kopisty, które nie zmieniają tożsamości słowa ani znaczenia. „Zgodny z prawem” wprowadza kryterium prawne, którego autor tu nie omawia.
- Kierunek korekty: „każdy uprawniony/dopuszczalny sposób oszczędzania tych materiałów”.

### P4-004 — Forma o znaczeniu merytorycznym: błędne zakresy podkreślenia w 1 Kor 8,2–3

- Lokalizacja: `chapters/46-dodatek-grzech-pokoleniowy.md:9`.
- Źródło: druk 293 / PDF 301, obejrzany render. W pierwszym greckim cytacie podkreślono oddzielnie **δε**, **ειδεναι**, **ουδεπω**, **ουδεν**, **εγνωκε**. W cytacie eklektycznym podkreślono **εγνωκεναι**, **ουπω**, **εγνω**.
- PL: nie ma podkreślenia przy pierwszych `δε` i `ειδεναι`, natomiast jedno podkreślenie obejmuje fragment od `ουδεπω` aż do `οὑτος`, w tym niekwestionowane słowa i początek kolejnego wersetu. W drugim cytacie podkreślono `εγνω καθως δει` zamiast samego `εγνω`.
- Następujące zdanie „Omawiane miejsca są podkreślone” powoduje, że zmiana formy podaje błędną informację o przedmiocie porównania.
- Do poprawy: odtworzyć dokładne zakresy podkreśleń ze źródła.

### P4-005 — Forma: brak pogrubienia sumy manuskryptów

- Lokalizacja: `chapters/45-dodatek-bizantyjskie-manuskrypty-kr-rodziny-35.md:7`, `Łącznie = 364`.
- Źródło: druk 292 / PDF 300, `Total = 364` jest pogrubione (znacznik b w XML).
- Do poprawy: przywrócić bold tej pozycji.

### P4-006 — Forma / zgodność cytatów: wielkość liter i dopowiedzenie w przypisach 44

- Lokalizacja: `chapters/44-dodatek-skolacjonowane-manuskrypty-f35.md:61,63`.
- Źródło: druk 289 / PDF 297. W cytacie Marka: `whatever we (ημιν) may ask`; PL: „o co możemy Cię poprosić (ημιν)”. Dodano `Cię`, a nawias z oznaczeniem greckim przeniesiono od zaimka pierwszej osoby na koniec zdania, co osłabia widoczny kontrast z `ye (υμιν)`.
- W cytacie Łukasza źródło ma `upon him` małą literą; PL: „nad Nim”.
- Do poprawy: przełożyć cytat Marka bez dopowiadania zaimka drugiej osoby i umieścić oznaczenia obok odpowiadających im `my`/`wy`; zachować małe `nim` w cytacie Łukasza zgodnie z regułą 16.

### P4-007 — Forma: zagnieżdżone nawiasy w bibliografii 42

- Lokalizacja: `chapters/42-dodatek-precz-z-falszerstwem.md:3,11`.
- Źródło: druk 284–285 / PDF 292–293; w zewnętrznych nawiasach okrągłych autor używa wewnętrznych kwadratowych: `[New York: Harper,1953]`, `[actually sent out in the Spring, 1989]`.
- PL zmienia oba poziomy na okrągłe, np. `(*A History of Christianity* (New York: Harper, 1953), s. 231)`.
- Do poprawy: zgodnie z regułą nawiasów z AGENTS pozostawić wewnętrzne kwadratowe. To nie dotyczy składni przypisów i spanów Pandoca.

### P4-008 — Forma: dodatkowe pogrubienia siglów papirusów w rankingu

- Lokalizacja: `chapters/41-dodatek-ranking-wariantowy-manuskryptow-zawierajacych-list-judy.md:5,9,33,39,45`.
- Źródło: druk 281–283 / PDF 289–291: sigla P^72^, P^78^, P^74^ są pismem zwykłym, z indeksem górnym; pogrubione są wybrane komentarze i oznaczenie f^35^.
- PL dodatkowo pogrubia wymienione sigla P. Do ujednolicenia ze źródłem, jeżeli wymagane jest ścisłe zachowanie wszystkich zakresów wyróżnień. Nie zmieniać przy tym właściwych 88 podkreśleń manuskryptów rodziny.

### P4-009 — Forma: liczne zgubione lub przesunięte wyróżnienia w rozdziale 48

Wszystkie poniższe pozycje dotyczą `chapters/48-dodatek-czy-krytyka-tekstu-nowego-testamentu-jest-nauka.md` i zostały skonfrontowane z obrazem stron oryginału. Nie wystarczy dopisać jednego pogrubienia do całego akapitu: należy odtworzyć poszczególne zakresy.

| Wiersz PL | Druk / PDF | Wyróżnienie w EN | Problem w PL / kierunek poprawy |
| --- | --- | --- | --- |
| 9 | 298 / 306 | Podkreślone `they simply were not in possession of a sufficient proportion of the relevant evidence` | Brak podkreślenia „po prostu nie posiadali wystarczającej części istotnych dowodów”. |
| 13 | 299 / 307 | `If` pogrubione i podkreślone; `Hopeless, totally hopeless` pogrubione; `worst` podkreślone | „Jeśli”, „Beznadziejne, całkowicie beznadziejne” i „najgorsze” nie mają odpowiadających wyróżnień. |
| 15 | 299 / 307 | Podkreślone `and reason` | Brak podkreślenia „i rozum”. |
| 159,161 | 299 / 307 | W przypisie: podkreślone `both` i końcowe `oldest equals worst`; pogrubione całe zdanie `No amount of subjective preference … objectively so` | Wyróżnień brak przy „oba się mylą”, „najstarsze naprawdę znaczy najgorsze” i zdaniu o subiektywnych preferencjach. |
| 165 | 300 / 308 | Podkreślone `always` w przypisie | Brak podkreślenia „zawsze”. |
| 27 | 301 / 309 | Podkreślone `not` w `is not lost` | Brak podkreślenia „nie” w „nie zaginęły”. |
| 29 | 301 / 309 | Pogrubione pierwsze zdanie od `By now it should be evident…` do `…wording of the NT` | Całe odpowiadające zdanie w PL ma pismo zwykłe. |
| 49 | 304 / 312 | Pogrubione `singular readings alone` i `not` | „w samych odczytach singularnych” oraz „Nie” w kolejnym zdaniu pozbawione pogrubienia. |
| 65 | 306 / 314 | Podkreślone tylko zdanie od `It is possible to assign…` do `…objective criteria` | PL obejmuje podkreśleniem także następne zdanie aż do „empirycznie rozpoznana”. Zakończyć zakres po „obiektywnych kryteriach”. |
| 67 | 306 / 314 | Kursywa obejmuje `INTF Text und Textwert` | PL pozostawia `INTF` poza kursywą. |
| 105 | 309 / 317 | Podkreślone tylko `statistically impossible` | PL podkreśla całe zdanie „statystycznie niemożliwe jest, by…”. Ograniczyć podkreślenie do dwóch wskazanych słów. |
| 111 | 310 / 318 | Podkreślone `the` przy `the archetypal form` | Nacisk na jedną określoną formę archetypalną znika. Potrzebna decyzja tłumaczeniowa, jak zachować go w języku bez rodzajników, bez dodawania argumentu. |
| 115 | 311 / 319 | Osobno podkreślone `fact` i `incredibly careful transmission` | Brak podkreślenia „faktem”, a drugi zakres rozciągnięty dodatkowo na „ich źródła, i to przez całe średniowiecze”. |
| 143 | 312 / 320 | Kursywą `every` w cytacie `by every word of God` | PL ma „każdym *słowem* Boga”. Kursywa powinna przypadać na „każdym”, nie „słowem”. |
| 151 | 313 / 321 | Podkreślone `theory` w `propound a theory of textual criticism` | Brak podkreślenia „teorię” przy „nadal głosić teorię krytyki tekstu”. |
| 199 | 309 / 317 | Nazwa *Textus Receptus* w przytoczonym fragmencie Metzgera nie jest kursywą; f¹/f¹³ wewnątrz cytatu nie są pogrubione | PL dodaje te wyróżnienia; odróżnić je od pogrubionych siglów w zdaniu autora poprzedzającym cytat. |

### P4-010 — Treść: „between them” jako łączna liczba błędów

- Lokalizacja: `chapters/48-dodatek-czy-krytyka-tekstu-nowego-testamentu-jest-nauka.md:57`, „między Alefem i B występuje ponad 3000 błędów”.
- Źródło: druk 305 / PDF 313, `Aleph and B have over 3,000 mistakes between them`.
- W tym zdaniu chodzi o błędy przypadające łącznie na oba manuskrypty; autor następnie przypisuje co najmniej 1000 manuskryptowi B. Polski zapis sugeruje raczej różnice pomiędzy manuskryptami i zaciera ten rachunek.
- Kierunek korekty: „Alef i B mają łącznie ponad 3000 błędów”. Nie korygować samego rachunku ani argumentu Pickeringa.

### P4-011 — Forma: zagnieżdżone nawiasy w rozdziale 48

- Lokalizacja: `chapters/48-dodatek-czy-krytyka-tekstu-nowego-testamentu-jest-nauka.md:145,157,199`.
- Druk 312, 298, 309 / PDF 320, 306, 317. W 145 zewnętrzne dopowiedzenie zamieniono zgodnie z preferencją na okrągłe, lecz pozostawiono także okrągłe w jego wnętrzu; w 157 i199 wewnętrzne kwadratowe źródła również stały się okrągłymi.
- Do poprawy: zewnętrzne okrągłe, wewnętrzne kwadratowe, zgodnie z zasadami użytkownika.

### P4-T01 — Do decyzji terminologicznej: „not yet extant”

- Lokalizacja: `chapters/48-dodatek-czy-krytyka-tekstu-nowego-testamentu-jest-nauka.md:175,201`, „jeszcze «niezachowanych»”.
- Druk 302 i310 / PDF310 i318. Autor sam umieszcza `extant` w cudzysłowie, następnie wyjaśnia: `not yet identified and catalogued`. Ma na myśli istniejące, lecz jeszcze nieodnalezione/nieskatalogowane manuskrypty.
- Polski termin „niezachowane” może sugerować manuskrypty utracone. Nie normalizować po cichu nietypowego sformułowania autora: zachować cudzysłów i informację o jego użyciu, ewentualnie doprecyzować odpowiednik poza przekładem. To problem terminologiczny do rozstrzygnięcia, nie pominięty akapit.

### P4-012 — Treść: dodane uzasadnienie w przypisie o Kodeksie W

- Lokalizacja: `chapters/49-dodatek-przedstawienie-dowodow-przez-alanda.md:200`, przypis `aland-kodeks-w-data`.
- Źródło: druk 314 / PDF 322, przypis kończy się na `which would put the Byzantine Text in the second century`.
- PL dopisuje „ponieważ wykazuje wpływ bizantyjski”. Podobne uzasadnienie występuje w innym przypisie autora (druk 307 / PDF 315, rozdział 48), ale nie w tym miejscu.
- Kierunek: usunąć nieoznaczony dodatek albo wyraźnie oznaczyć go jako odrębne objaśnienie tłumacza. Nie przenosić argumentu między przypisami bez zaznaczenia.

### P4-013 — Forma: zgubiony odsyłacz gwiazdkowy i podkreślenia w rozdziale 49

- `chapters/49-dodatek-przedstawienie-dowodow-przez-alanda.md:105`, druk 316 / PDF 324: źródło ma `(*Aland shows ap, but gives no figures for a.)`, PL pomija `*`, choć w tabeli zachowano `p*` przy 048. Przywrócić powiązanie objaśnienia z oznaczeniem.
- Wiersze 109 i 115: nagłówki kategorii I–V (oraz „total” w drugiej tabeli) w źródle są podkreślone; w PL brak podkreśleń (druk 316–317 / PDF 324–325). Pogrubiony styl nagłówka tabeli nie jest tym samym wyróżnieniem.
- Wiersz 166, przypis `aland-stopniowe-oczyszczanie-strumienia-przekazu`, druk 321 / PDF 329: podkreślone tylko `based on the extant MSS`; PL rozciąga podkreślenie przez nawias i „zostało uznane przez wszystkich”. Zakończyć podkreślenie po „manuskryptach”.
- Wiersze 170–180: skrót PA w cytacie Robinsona w źródle jest pismem zwykłym, w PL dodano kursywę. Zachować kursywę samego *Pericope* i tytułu *Pericope Adulterae*, lecz nie rozszerzać jej na niewyróżnione źródłowo skróty.

### P4-T02 — Terminologia: Catholic Epistles a General Epistles

- `chapters/49-dodatek-przedstawienie-dowodow-przez-alanda.md:9`, druk 313 / PDF 321: `c = Catholic Epistles` przełożono jako „c = Listy Ogólne”.
- Te same księgi w innych rozdziałach nazywane są `General Epistles`, również „Listami Ogólnymi”. Według zasady zachowywania różnych terminów warto rozstrzygnąć jawnie, czy tutaj oddać odrębną nazwę (np. „Listy Powszechne”), czy odnotować angielski wariant. Nie chodzi o zmianę zbioru ksiąg ani danych tabeli.

### P4-014 — Forma: zakresy wyróżnień w rozdziale 38

- `chapters/38-dodatek-nagromadzone-bledy-czternastu-stuleci.md:5`, druk 261 / PDF 269: brak podkreślenia `dated` — „datowanym”. Wyróżnienie odróżnia datowany manuskrypt od manuskryptu z datą szacowaną.
- Wiersz 295, druk 272 / PDF 280: podkreślone tylko `what` w `what happened, not where it happened`. PL podkreśla całą frazę „co się wydarzyło, a nie gdzie się wydarzyło”. Ograniczyć zakres do „co”.
- Wiersz 191 (pozycja 87), druk 268 / PDF 276: siglum `f35pt` w EN nie jest pogrubione; PL `**f^35pt^**` dodaje bold.
- Dodatkowa kursywa przy *homoioarcton/homoioteleuton* (np. w. 89, 149, 163, 175, 209, 221, 229, 265) nie występuje w źródłowym wykazie. To niska waga, lecz przy ścisłym zachowaniu wyróżnień należy ją odróżnić od właściwej źródłowej kursywy *epsilon/iota* (w. 83).
- Zapis przy adresach wersetów: litery `a/b/c` są w EN na linii bazowej (`1:40a`, `18:39c`), PL podnosi je do indeksu górnego. Nie mylić z rzeczywistymi indeksami przy greckich słowach i siglach, które trzeba zachować. Decyzja o konsekwentnej normalizacji adresów może być świadoma, nie jest to zmiana danych.

### P4-015 — Forma: pozostałe różnice wyróżnień w dodatkach 40–47

| Plik i wiersz | Druk / PDF | Problem / kierunek korekty |
| --- | --- | --- |
| `40-dodatek-podgrupy-f35-w-listach-ogolnych.md:22,24,78,156` | 276, 278, 280 / 284, 286, 288 | Zdanie „Dzielą się na dwie…” jest w EN zwykłym wprowadzeniem, PL tworzy dodatkowy nagłówek. Nazwy Grup 1 i 2 w EN są pogrubione i podkreślone; PL ma nagłówki bez podkreślenia. W tabeli końcowej podkreślone nagłówki „Indicative”, „Subjunctive”, „both” również tracą podkreślenie. Niska waga, odrębna od uszkodzenia danych tabeli G-001. |
| `42-dodatek-precz-z-falszerstwem.md:1` | 284 / 292 | W nagłówku podkreślone jest `forgery`, w PL „fałszerstwem” bez podkreślenia. |
| `43-dodatek-definiowanie-zachowania.md:11,21` | 287–288 / 295–296 | `nomina sacra` jest w EN w cudzysłowie, bez kursywy; PL zamienia cudzysłów na kursywę. `perfectly` i `completely` są podkreślone, PL „doskonale” i „kompletnie” kursywą bez podkreślenia. Przywrócić rodzaj wyróżnienia. |
| `45-dodatek-bizantyjskie-manuskrypty-kr-rodziny-35.md:3,5,15` | 291–292 / 299–300 | *Uncials* i *Minuscules* w EN są także podkreślone; PL zachowuje tylko kursywę. W bibliografii kursywa *Text und Textwert* nie obejmuje `(TuT)`, a PL obejmuje. Brak bolda sumy opisano osobno w P4-005. |
| `46-dodatek-grzech-pokoleniowy.md:13,21` | 294–295 / 302–303 | EN `he` jest podkreślone, ale nie kursywą; PL „on” ma oba wyróżnienia. EN `is` w `what God's word is!` jest podkreślone, PL „jest” bez podkreślenia. Błędy greckich zakresów opisano osobno w P4-004. |
| `47-dodatek-metoda-genealogiczna-oparta-na-spojnosci.md:5` | 296 / 304 | W zdaniu `The method is not empirical` podkreślono samo `method`. PL „Metoda nie jest empiryczna” nie ma podkreślenia. |

## Problemy źródła / decyzje redakcyjne

### P4-S03 — Suma 44 w rozdziale 38 pochodzi z oryginału

- `chapters/38-dodatek-nagromadzone-bledy-czternastu-stuleci.md:11`, druk 261 / PDF 269: autor wymienia grupy 12, 17, 17, 15 i 12 odczytów, następnie pisze `six out of 44`.
- PL zachowuje „sześć z 44”. Wymienione liczby sumują się do 73, nie 44; tę rozbieżność zgłaszać jako problem źródła, nie błąd przekładu. Nie korygować po cichu.

### P4-S01 — „kolejnych dwanaście” przed tabelą z piętnastoma wierszami

- `chapters/40-dodatek-podgrupy-f35-w-listach-ogolnych.md:96–114`, druk 278 / PDF 286.
- Oryginał również mówi `another twelve`, choć następujący wykaz ma piętnaście wierszy (757–1899). Tłumaczenie zachowało rozbieżność wiernie. Nie „poprawiać” liczby w tekście autora bez oznaczonej uwagi redakcyjnej.

### P4-S02 — Przypis dotyczący 586 stoi przy GA 35 także w oryginale

- `chapters/44-dodatek-skolacjonowane-manuskrypty-f35.md:7,61`, druk 289 / PDF 297.
- Przypis po `GA 35 is complete` rozpoczyna się od `AG 586` i omawia wariant 586. To źródłowa niekonsekwencja, nie dowód przestawienia przypisu przez tłumacza. PL normalizuje `AG` do `GA`; tę oczywistą literówkę źródła warto odnotować poza tekstem autora, jeżeli ma być zachowana pełna dokumentacja interwencji.

### G-S01 — Nota licencyjna jest adaptacją, nie przekładem strony ii

- `chapters/01-od-tlumacza.md:35–49`, źródło ii / PDF 2.
- PDF podaje CC BY-SA **3.0 Unported**, nota polska CC BY-SA **4.0 Międzynarodowa** i inne rozwinięcie warunków. Ponieważ rozdział jest wyraźnie „Od tłumacza”, nie jest to automatycznie pominięcie w tekście Pickeringa. Warto rozróżnić oznaczenie licencji oryginału i decyzję dotyczącą przekładu. To stwierdzenie różnicy pomiędzy dokumentami, nie ocena prawna dopuszczalności licencji.

### G-002 — Drobne literówki we wstępie tłumacza

- `chapters/01-od-tlumacza.md:7`: `zazaczone` → `zaznaczone`.
- `chapters/01-od-tlumacza.md:47`: `prze licencjodawcę` → `przez licencjodawcę`.
- Uwaga językowa do dodatku tłumacza, bez odpowiednika w angielskim źródle.

### G-T01 — Decyzja tytułowa: preservation jako „ochrona”

- `metadata.yml:3`: podtytuł „Boża ochrona Nowego Testamentu”, źródłowa strona tytułowa / PDF 1: `The Divine Preservation of the New Testament`.
- W książce *preservation* jest zasadniczo „zachowaniem”, a *protection* „ochroną”. Warto potwierdzić, czy odmienny podtytuł jest świadomą decyzją redakcyjną; dla zgodności terminologicznej naturalnym odpowiednikiem byłoby „Boże zachowanie Nowego Testamentu”. Nie zmieniać automatycznie zatwierdzonej okładki/tytułu.
