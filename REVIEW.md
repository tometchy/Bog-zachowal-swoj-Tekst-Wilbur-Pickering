# Review tłumaczenia „God Has Preserved His Text!”, wydanie 4

## Wynik i zakres

**Zakończono pierwsze pełne porównanie tłumaczenia z oryginałem — 2026-10-11.** Sprawdzono wszystkie 50 plików w `chapters/`, w tym oba pliki z prefiksem `09`. Poniżej znajdują się uwagi do kompletności, wierności, terminologii i formy. **Nie poprawiono tekstu książki ani plików wynikowych.** Raport jest listą do rozpatrzenia, nie informacją, że książka jest już wolna od błędów.

**Aktualizacja 2026-10-12:** zakończono weryfikację dodatkowego raportu `review-calej-ksiazki.md`. Sekcja „Uzupełnienie po porównaniu z drugim raportem” zawiera nowe uwagi U-001–018, decyzję U-T01, noty U-S01–03 oraz mapę duplikatów i sugestii odrzuconych. Rozszerzono też P3-T01. Pozostałe wcześniejsze ustalenia zachowano.

- Podstawa porównania: commit `4d35b43d4dd9868d5a600c1f4b9c88128f58010c` z 2026-10-09. Praca rozpoczęta 2026-10-10.
- Uwzględniona późniejsza zmiana użytkownika na `origin/master`: `17c80ef81abe5df94d90d197c896db41e615dd3f` dodaje bold do `XII` w `chapters/19-czesc-2-datowanie-kr-ponownie-rozwazone.md:3`. Tego miejsca **nie zalicza się do otwartych usterek**. Pozostałe uwagi odnoszą się do bazy wskazanej wyżej.
- Wzorzec: [God-Has-Preserved-His-Text-4th.pdf](God-Has-Preserved-His-Text-4th.pdf), 331 stron pliku. Strony drukowane 1–323 odpowiadają stronom PDF 9–331 (+8); przedmowa iii / PDF 3, podziękowania iv / PDF 4. Druk 260 / PDF 268 jest pusty. `neway/` nie jest niezależnym wzorcem poprawności.
- Zapis `20:104` lub `chapters/20:104` oznacza plik w `chapters/` o prefiksie `20-`, wiersz 104. Numery wierszy dotyczą bazy przeglądu; cytowane fragmenty pozwalają odnaleźć miejsca po przesunięciach. Oba pliki `09` rozróżniono nazwami/kontekstem. Numery stron polskiego PDF-u oznaczają strony pliku, liczone od 1.
- Nie oceniano prawdziwości argumentacji autora i nie zastępowano cytatów biblijnych gotowym polskim przekładem. Wyraźnie oznaczone dodatki tłumacza rozróżniono od tekstu Pickeringa.
- Brak osobnej uwagi przy danym akapicie oznacza, że nie wykryto problemu w wykonanym przeglądzie, nie stanowi gwarancji bezbłędności.

## Najważniejsze rzeczy do poprawy

| Priorytet | Problem | Identyfikatory uwag |
| --- | --- | --- |
| Wysoki — kompletność | Opuszczony cały akapit we „Wczesnym rozpoznaniu” oraz przypis objaśniający statystykę w rozdziale 34 | P1-017, P3-005 |
| Wysoki — dane | Brak świadka `bo` przy Rz 5,1, brak Lesbos w tabeli miejsc, zgubione diagnostyczne `**` w profilach | P5-001, P4-001, P3-002, P3-003 |
| Wysoki — znaczenie | Odwrócony kierunek prawdopodobieństwa, pomylona przyczyna zaślepienia, twierdzenie autora zmienione w pytanie | P1-031, P5-002, P5-003 |
| Wysoki — składnia Markdown | Literalne gwiazdki stają się kursywą; znikają oznaczenia, a całe zdanie trafia do indeksu górnego | P3-008, G-P1-001, G-P1-002 |
| Wysoki — eksport | `<br>` znika w PDF, skleja greckie odczyty i nazwy; tabela wychodzi poza stronę | G-001, P3-009 |
| Wysoki — diagram | Stemma w rozdziale 20 traci w PDF połączenia i figury, a końcowa etykieta przechodzi na następną stronę | P5-007 |
| Istotny — forma niosąca informację | Podkreślono niewłaściwe fragmenty greckich wariantów; brak widocznego podziału tabeli na bloki przywoływane w wywodzie | P4-004, P5-008 |
| Dalsza korekta | Pozostałe zmiany sensu, ustalone odpowiedniki, wielkość liter cytatów, bold/kursywa/podkreślenia, nawiasy i drobne usterki językowe | Szczegółowe uwagi poniżej |

Priorytety porządkują pracę, nie zastępują pełnej listy. Jedna uwaga może obejmować kilka lub kilkadziesiąt miejsc. Zagadnienia terminologiczne i problemy oryginału nie są automatycznie potwierdzonymi błędami przekładu.

## Jak czytać raport

- **Treść / kompletność / dane**: pominięcie, dodanie albo zmiana znaczenia, liczby, odniesienia lub toku wnioskowania.
- **Terminologia**: zgodność z `AGENTS.md` i zachowanie istotnych rozróżnień źródła. Proponowane odpowiedniki wymagające decyzji są tak oznaczone.
- **Forma**: pogrubienie, kursywa, podkreślenie, indeks, siglum, przypis, nagłówek, tabela, lista lub diagram. Różnice czysto typograficzne mają mniejszą wagę niż te, które zmieniają dane.
- **Problem źródła / decyzja redakcyjna**: nie poprawiać autora po cichu. Rozbieżność już obecna w oryginale nie jest pomyłką tłumacza.
- „Kierunek” to propozycja późniejszej poprawki, **nie wykonana zmiana**. Zachować istniejące identyfikatory przypisów.
- Numery P1–P5 oznaczają partie pracy, nie części książki. Dlatego uwagi P5 (pliki 18–21) umieszczono przed P2 (17, 22–30), a identyfikatorów nie zmieniano.

## Zakończone kontrole i ograniczenia

| Zakres | Strony drukowane oryginału | Wykonana kontrola |
| --- | --- | --- |
| Wstęp tłumacza, tytuł i nota wydawnicza | tytuł, ii | Rozróżnienie adaptacji i źródła, terminologia, literówki |
| Pliki 02–16, w tym oba 09 | iii–iv, 1–66 | Cała treść i przypisy, struktura, liczby, sigla, wyróżnienia, diagram |
| Pliki 18–21 | 84–110 | Cała treść, przypisy, tabele, kombinacje świadków, wyróżnienia i stemma |
| Pliki 17, 22–30 | 66–83, 110–182 | Cała treść i przypisy, duże profile i tabele, greka, liczby oraz wyróżnienia |
| Pliki 31–37 | 183–260 | Cała treść i przypisy, profile, wykazy i tabele, wyróżnienia |
| Pliki 38–49 | 261–323 | Cała treść i przypisy, wykazy, wszystkie tabele, wyróżnienia |
| Cały zbiór | — | Parser Pandoca, przypisy, obrazy, tabele, literalne gwiazdki i surowy HTML |

Metoda: porównanie tekstu z ekstrakcją `pdftotext -layout`, kontrola bold/kursywy w XML z `pdftohtml`, podkreśleń przez geometrię i glify `mutool draw -F trace`, a następnie obrazy stron rozstrzygające różnice. Nie utożsamiano ekstrakcji z oględzinami. Wszystkie strony źródłowe zakresu 18–21 oraz dodatków 38–49 obejrzano; w pozostałych zakresach stosowano analizę całego zakresu wyróżnień i oględziny stron, w tym miejsc wymagających rozstrzygnięcia wizualnego.

Wybrane kontrole danych i wyniki dodatnie:

- Profil 17: porównano wszystkie 658 zestawów wariantów, także maszynowo po normalizacji ekstrakcji; nie stwierdzono pominiętej pozycji. Źródłowe `etc.` przy Obj 3,2 / 3,18b jest zawinięte, nie dopisane w PL.
- Rozdział 20: sprawdzono dziewięć liczebności grup oraz sto kombinacji i liczebności. Rozdział 21: 74 wiersze danych pierwszej tabeli, sumy, 12 pozycji podsumowania i siedem wierszy tabeli w przypisie. Rozbieżności arytmetyczne samego źródła opisano w P5-S02.
- Profil 22: 180 zestawów, także porównanie maszynowe; jedyna wykryta różnica w porównaniu danych 180 zestawów to separator P2-017. Rozdział 23: trzy tabele po 10, 12 i 18 wierszy. Rozdział 24: wszystkie 32 zestawy. Rozdział 26: obie tabele (34 i 46 manuskryptów) bez stwierdzonych zmian liczb.
- Rozdział 27: wszystkie 49 pozycji wraz z komentarzami i przypisami. Tabela 28: wszystkie 114 wierszy sprawdzone także maszynowo, bez rozbieżności.
- Rozdziały 31–35: profile, wykazy i tabele poświadczeń porównano wraz z przypisami; w 35 wszystkie 119 pozycji i sumy są zachowane. W 36 porównano również cztery tabele kombinacji świadków, w 37 wykaz manuskryptów 1 Listu Jana.
- Rozdział 38: wszystkie 136 pozycji, dodatkowo maszynowa kontrola greki i 54 pogrubionych numerów. Rozdział 41: wszystkie 88 podkreślonych oznaczeń rankingu zgodne ze źródłem, zweryfikowane na obrazach o wyższej rozdzielczości.
- Rozdział 49: 78 wierszy dużej tabeli, 14 wierszy podsumowania i pięć wierszy zestawienia rękopisów kursywnych. Zidentyfikowane problemy opisano oddzielnie.
- Diagram `images/Rysunek_A.jpg`, użyty w części I i dodatku 48: oznaczenia, daty, kontury, strzałka i relacje zachowane w porównaniu z drukiem 50 / PDF 58.
- Globalnie: **380 definicji i 380 użytych identyfikatorów przypisów**, bez powtórzeń definicji, niezdefiniowanych odsyłaczy ani nieużytych przypisów. To nie wykrywa przypisu pominiętego w całości wraz z odsyłaczem — taki problem jest w P3-005.
- Pandoc `--from=markdown-smart -t json` dla połączonego zbioru: brak ostrzeżeń, 380 obiektów przypisu, **93 tabele**, pięć odwołań do istniejących obrazów. 92 tabele zapisano kreskami, jedną jako tabelę prostą w przypisie rozdziału 21; ta ostatnia parsuje się prawidłowo. W tabelach kreskowych liczby komórek są spójne.
- Jedyne surowe wstawki w strukturze Pandoca to **69 znaczników HTML `<br>`**. Poprawne parsowanie nie gwarantuje ich zachowania w PDF — patrz G-001.
- Przypis `12:69–70` jest poprawnie rozpoznawany mimo braku wcięcia drugiej linii. Odsyłacz `unia-hipostatyczna` w 05:46 jest użyty; następujący po nim dwukropek nie czyni go definicją ani przypisem osieroconym.

**Ograniczenie:** polski wynikowy PDF oglądano punktowo w miejscach problemów eksportu (m.in. strony 125–126, 341, 348, 368 i 390), nie wykonano pełnej korekty typograficznej każdej strony polskiego PDF-u ani wizualnej kontroli całych EPUB/DOCX. Pełny przegląd dotyczy zawartości i oznaczeń Markdown w porównaniu z oryginałem. Po przyszłych poprawkach potrzebne będą ponowny eksport i kontrola składu. Nie uruchamiano `make pdf`, bo w tym zadaniu nie zmieniono książki.

Do wspólnej decyzji terminologicznej pozostają zwłaszcza `exemplar` (P2-001, P3-001, P5-T03), szczególne użycie `not yet extant` (P3-T01, P4-T01), rozróżnienie `Catholic Epistles / General Epistles` (P3-T02, P4-T02, P5-T02) oraz `singular reading` (U-T01). Nie stosować globalnej zamiany bez rozstrzygnięcia znaczenia.

## Uwagi ogólne

### G-001 — Forma / eksport: `<br>` znika w PDF i skleja różne odczyty oraz dane tabel

- Lokalizacja: `chapters/40-dodatek-podgrupy-f35-w-listach-ogolnych.md:7–20,158–159`; także `chapters/49-dodatek-przedstawienie-dowodow-przez-alanda.md:111` (klasyfikacje `E++<br>E+<br>E` itp. tracą rozdzielenie). Ten sam zapis występuje w `32` (konkretne przypadki w P3-009).
- Źródło: druk 275–276, 280 / PDF 283–284, 288. Odczyty i nazwy są rozdzielone wierszami.
- Dowód: przy ustawieniach wejściowych Makefile (`markdown-smart`) polecenie `pandoc chapters/40-dodatek-podgrupy-f35-w-listach-ogolnych.md --from=markdown-smart -t latex` daje m.in. `εχειεχη`, `αλλαλλα`, `γινωσκοντεςγινωσκοντας`. Zapis `Konstamonitu<br>Kutlumusiu<br>Filotheu` staje się jednym ciągiem.
- Skutek widoczny także w **istniejącym** polskim PDF-ie: strona pliku 341 zawiera sklejone odczyty, a na 348 nazwy w tabeli rozmieszczenia zachodzą na sąsiednie kolumny i wychodzą za prawy brzeg strony. To utrata rozdzielenia danych, nie tylko kosmetyka.
- Do poprawy w przyszłym etapie: użyć podziału komórek/wierszy obsługiwanego przez Pandoca we wszystkich formatach albo jawnej konwersji podziałów przed eksportem. Po zmianie konieczna kontrola PDF, EPUB i DOCX. W tym review nic nie zmieniono.

### G-P1-001 — Forma / uszkodzone sigla i całe zdanie w indeksie górnym

- Lokalizacja: `chapters/49-dodatek-przedstawienie-dowodow-przez-alanda.md:136`, oba wystąpienia `P^66*^` w zdaniu od „Okoliczność, że niektóre odczyty bizantyjskie…”. Źródło: s. 318 / PDF 326. Istniejący polski PDF: s. 390 / PDF 390, obejrzany render.
- Obie literalne gwiazdki łączą się w znaczniki kursywy, a znaczniki `^` przestają wyznaczać dwa odrębne indeksy. `pandoc --from=markdown-smart -t latex` tworzy `P\textsuperscript{66\emph{\^{} poprawiono na odczyty egipskie, a niektóre odczyty egipskie w P\^{}66}}`. W gotowym PDF-ie większość tego zdania jest drobnym, kursywnym indeksem górnym, oba istotne oznaczenia `*` znikają, zaś daszki stają się widoczne.
- Kierunek: zabezpieczyć oba literalne asteriski (`\*`) i sprawdzić, że oba sigla mają wyłącznie `66*` w indeksie, a całe zdanie między nimi jest zwykłym tekstem. Nie zmieniać oznaczeń autora ani rozróżnienia rąk/korekt.

### G-P1-002 — Forma / utracona gwiazdka w numerze strony i przesunięta kursywa

- Lokalizacja: `chapters/47-dodatek-metoda-genealogiczna-oparta-na-spojnosci.md:9`, „(s. 18*), podobnie jak uczynili dwadzieścia lat wcześniej w *ECM*…”. Źródło: s. 296 / PDF 304. Istniejący polski PDF: s. 368 / PDF 368, obejrzany render.
- Gwiazdka po `18` otwiera kursywę zakończoną gwiazdką przed `ECM`. Pandoc zwraca `18\emph{), podobnie jak uczynili dwadzieścia lat wcześniej w }ECM*`. Numer strony staje się błędnym `18` zamiast `18*`, obcy fragment otrzymuje kursywę, a przy `ECM` pozostaje nieuprawniona literalna gwiazdka. To nie tylko różnica typograficzna, ale również uszkodzone odesłanie.
- Kierunek: zapisać literalne gwiazdki numeracji stron jako `\*`, zachować osobną kursywę skrótu *ECM*. Numery `28*` w w.5 i `11*` w w.9 obecnie przechodzą do LaTeX prawidłowo, ale warto zastosować jednolite zabezpieczenie literalnych znaków.

### G-002 — Drobne literówki we wstępie tłumacza

- `chapters/01-od-tlumacza.md:7`: `zazaczone` → `zaznaczone`.
- `chapters/01-od-tlumacza.md:47`: `prze licencjodawcę` → `przez licencjodawcę`.
- Uwaga językowa do dodatku tłumacza, bez odpowiednika w angielskim źródle.

### G-S01 — Nota licencyjna jest adaptacją, nie przekładem strony ii

- `chapters/01-od-tlumacza.md:35–49`, źródło ii / PDF 2.
- PDF podaje CC BY-SA **3.0 Unported**, nota polska CC BY-SA **4.0 Międzynarodowa** i inne rozwinięcie warunków. Ponieważ rozdział jest wyraźnie „Od tłumacza”, nie jest to automatycznie pominięcie w tekście Pickeringa. Warto rozróżnić oznaczenie licencji oryginału i decyzję dotyczącą przekładu. To stwierdzenie różnicy pomiędzy dokumentami, nie ocena prawna dopuszczalności licencji.

### G-T01 — Decyzja tytułowa: preservation jako „ochrona”

- `metadata.yml:3`: podtytuł „Boża ochrona Nowego Testamentu”, źródłowa strona tytułowa / PDF 1: `The Divine Preservation of the New Testament`.
- W książce *preservation* jest zasadniczo „zachowaniem”, a *protection* „ochroną”. Warto potwierdzić, czy odmienny podtytuł jest świadomą decyzją redakcyjną; dla zgodności terminologicznej naturalnym odpowiednikiem byłoby „Boże zachowanie Nowego Testamentu”. Nie zmieniać automatycznie zatwierdzonej okładki/tytułu.

### Zakres sprawdzenia i powiązania

- Potwierdzono także opisany już w P3-008 problem `chapters/32:93`: 20 gwiazdek w wyliczeniu znika, tworząc 10 przypadkowych fragmentów kursywy. Nie tworzyć drugiej niezależnej uwagi o tym samym błędzie.
- Gwiazdki w pojedynczych komórkach tabel 32 oraz pojedyncze `P^66*^` w 38:65 nie wykazały tego błędu parsowania. Zatem nie każda niezabezpieczona gwiazdka już dziś powoduje usterkę; problem ujawnia się przy parowaniu z następną gwiazdką w obrębie tego samego fragmentu tekstu.
- Audyt dotyczył interpretacji literalnych gwiazdek przy numerach i siglach, nie zastępuje pełnej kontroli poprawności danych merytorycznych pozostałych rozdziałów. Nie zmieniano książki ani nie generowano jej ponownie.

## Pliki 02–16 — uwagi P1

### P1-001 — Treść / tytuły naukowe

- Lokalizacja: `chapters/02-przedmowa.md:4`, „Posiada tytuł magistra i doktora lingwistyki”. Źródło: s. iii / PDF 3.
- EN: „He has a ThM and a PhD in Linguistics.” PL przypisuje obu tytułom lingwistykę; `ThM` jest odmiennym stopniem i w źródle pozostaje osobno.
- Kierunek: zachować `ThM` albo oddać jako magister teologii, a doktorat z językoznawstwa przypisać tylko do `PhD`.

### P1-002 — Terminologia / original wording

- Lokalizacja: `chapters/02-przedmowa.md:4,8`, „oryginalne brzmienie”, „oryginalny tekst”, „zachować oryginał”. Źródło: s. iii / PDF 3.
- EN: „precise original wording”, „preserved the original wording”, „preserve that wording”.
- Kierunek: konsekwentnie „(dokładne) oryginalne sformułowania”; obecne trzy odpowiedniki zacierają powtórzenie tego samego terminu. Przypis tłumacza o krytyce tekstu jest wyraźnie oznaczonym dodatkiem, nie pominięciem źródła.

### P1-003 — Treść / zakres porównania

- Lokalizacja: `chapters/02-przedmowa.md:8`, „nie różni się znacząco od innych «dobrych» greckich tekstów”. Źródło: s. iii / PDF 3.
- EN: „not seriously different from **some of** the other ‘good’ Greek texts”.
- Problem: pominięto „niektórych”, rozszerzając porównanie na wszystkie pozostałe dobre teksty. Kierunek: przywrócić ograniczenie.

### P1-004 — Forma / granica kursywy tytułu

- Lokalizacja: `chapters/02-przedmowa.md:8`, `_The Sovereign Creator Has Spoken: Objective Authority for Living, Second Edition_`. Źródło: s. iii / PDF 3, XML.
- EN kursywą obejmuje sam tytuł do „Living”; „Second Edition” jest zwykłym tekstem poza tytułem.
- Kierunek: zakończyć kursywę po `Living`, a informację o wydaniu podać osobno.

### P1-005 — Treść / dodane objaśnienie i ograniczenie liczbowe

- Lokalizacja: `chapters/04-czesc-1-preambula.md:13,35`, „za pomocą 350”, „linię nachylenia (klin)”. Źródło: s. 2–3 / PDF 10–11.
- EN: „with **up to** 350 information ‘bits’”; „they form a **cline**”.
- Problem: przy 350 opuszczono „do”, a „klin” jest nieobecnym w źródle dopowiedzeniem, które myli *cline* z innym pojęciem. Kierunek: oddać ograniczenie „do 350”; usunąć dopisane objaśnienie i wiernie oddać nachyloną linię. Nie dotyczy to oceny prawdziwości argumentacji naukowej autora.

### P1-006 — Treść / „jedna rzecz” zmieniona na „jedyna rzecz”

- Lokalizacja: `chapters/04-czesc-1-preambula.md:51`, „to jedyna rzecz, której nie może uczynić”. Źródło: s. 5 / PDF 13.
- EN: „it is **one thing** He cannot do”.
- Problem: PL dodaje wyłączność nieobecną w EN. Kierunek: „to jedna rzecz, której nie może uczynić” lub równoważnie, bez „jedyna”.

### P1-007 — Cytaty biblijne / wielkość liter

- Lokalizacja: `chapters/04-czesc-1-preambula.md:41,51`, „na swój obraz”, „samemu sobie”. Źródło: s. 4–5 / PDF 12–13.
- EN: „in **His** own image”; „He cannot deny **Himself**”.
- Kierunek: zachować wielkie litery autora również w polskich zaimkach („Swój”, „Sobie”); nie importować innego przekładu. W drugim cytacie polskie zdanie może obejść brak jawnego odpowiednika `He`, ale istniejący odpowiednik `Himself` ma zachować wielkość litery.

### P1-008 — Cytaty biblijne / liczba i wielkość liter

- Lokalizacja: `chapters/05-czesc-1-wprowadzenie-natchnienie.md:9,11,34,36,50`, „niebo”, „Słowo swoje”, „Słowo Twoje”, „Słowo, PANA”, „Księga Prawa”, „przeze Mnie”, „Otrzymałem od Pana”. Źródło: s. 6–9, 11 / PDF 14–17,19.
- EN: Rdz 1,1 „the **heavens**”; Ps 138,2 „Your **word**”; Ps 119,89 „Your **word**”; 1 P 1,25 „the **word** of the LORD”; Joz 1,8 „Book of the **law**”; J 14,6 „through **me**”; 1 Kor 11,23 „I **received** from the Lord”.
- Problemy: liczba mnoga niebios została zmieniona; kilkakrotnie małe `word/law/me` stały się wielkim „Słowo/Prawa/Mnie”; w Ps 138,2 wielkie `Your` stało się małym „swoje”; przecinek po „Słowo” rozdziela dopełniacz od rzeczownika. W 1 Kor poprawić jedynie nieuzasadniony przecinek w „przekazałem, wam” (wielkość liter jest tam prawidłowa).
- Kierunek: przejrzeć wskazane cytaty znak po znaku według cytowanego EN, zachować liczbę i wielkość liter autora; usunąć dwa przypadkowe przecinki.

### P1-009 — Treść / nazwa podsekcji zmienia odniesienie

- Lokalizacja: `chapters/05-czesc-1-wprowadzenie-natchnienie.md:44`, `_Natura Tekstu_`. Źródło: s. 10 / PDF 18.
- EN: „Its nature” pod nadrzędnym „Inspiration”; następuje opis procesu natchnienia.
- Problem: PL wprowadza „Tekst”, którego nie ma w nagłówku, i przenosi odniesienie z natchnienia na Tekst. Kierunek: „Jego natura” albo jednoznaczne „Natura natchnienia”.

### P1-010 — Cytat / opuszczony numer wersetu

- Lokalizacja: `chapters/05-czesc-1-wprowadzenie-natchnienie.md:15`, „ale teraz ujawnionej”. Źródło: s. 7 / PDF 15, potwierdzone renderem.
- EN: „**25** but now revealed”. Cytat podpisany jest w źródle „Romans 14:24”, ale obejmuje też jawnie oznaczoną kontynuację wersetu 25.
- Kierunek: przywrócić numer 25 w cytacie; nie zmieniać samodzielnie nietypowego adresu autora na numerację innego wydania Biblii.

### P1-011 — Treść / utrata celu działania

- Lokalizacja: `chapters/05-czesc-1-wprowadzenie-natchnienie.md:34`, „rozważać w niej dniem i nocą, czego masz przestrzegać, zgodnie ze wszystkim”. Źródło: s. 8 / PDF 16, Joz 1,8.
- EN: „meditate in it day and night, **that you may observe to do** according to all that is written in it”.
- Problem: w PL ginie relacja celu („abyś…”) i czynienia według zapisanej treści. Kierunek: przywrócić cel rozważania oraz czynne przestrzeganie/zastosowanie zapisanych słów.

### P1-012 — Forma / podkreślenie zamienione na pogrubienie

- Lokalizacja: `chapters/05-czesc-1-wprowadzenie-natchnienie.md:11`, `**tylko wieczny Byt mógł wydać wieczne Słowo**`. Źródło: s. 7 / PDF 15, potwierdzone renderem.
- EN ma podkreślenie, nie pogrubienie, na „only an eternal Being could produce an eternal word”.
- Kierunek: zdecydować konsekwentnie o odwzorowaniu podkreśleń w Pandocu. To zmiana rodzaju wyróżnienia, nie dodane wyróżnienie; nie usuwać akcentu autora. Wewnątrz EN „word” pozostaje małą literą.

### P1-013 — Treść / liczebnik porządkowy

- Lokalizacja: `chapters/08-czesc-1-historyczne-dowody.md:9`, „aby trzysta pokoleń mogło je wszystkie przestrzegać”. Źródło: s. 15 / PDF 23.
- EN: „for **the three hundredth generation** to obey them all”.
- Problem: trzechsetne pokolenie zastąpiono trzystoma pokoleniami. Kierunek: „aby trzechsetne pokolenie mogło przestrzegać ich wszystkich”.

### P1-014 — Cytat biblijny / osoba i liczba

- Lokalizacja: `chapters/08-czesc-1-historyczne-dowody.md:9`, „A co do mnie”, „w twoje usta”. Źródło: s. 15 / PDF 23, Iz 59,21.
- EN: „As for **Me**”; „which I have put in your **mouths**”, następnie „from your **mouth**”.
- Problem: PL gubi wielką literę `Me` i rozróżnienie liczby mnogiej oraz pojedynczej słuchaczy (samo polskie „usta” ma tylko formę mnogą, więc wymaga kontroli zaimka). Kierunek: zachować „Mnie” i oddać pierwsze `your mouths` przez „wasze usta”, zachowując dalsze „twoich ust”. Nietypowego przejścia liczby w oryginale nie normalizować po cichu.

### P1-015 — Nazwa księgi niezgodna z ustaleniem

- Lokalizacja: `chapters/08-czesc-1-historyczne-dowody.md:9`, „Księga Objawienia 22,18-19”. Źródło: s. 15 / PDF 23.
- EN: „Revelation 22:18-19”. Kierunek: ustalone „Objawienie Jana”.

### P1-016 — Drobna korekta językowa

- Lokalizacja: `chapters/05-czesc-1-wprowadzenie-natchnienie.md:38`, „człowiek chciałaby napisać”. Źródło: s. 9 / PDF 17, „the human being would wish to write”.
- Problem: błąd zgody rodzaju. Kierunek: „człowiek chciałby”. Nie zmienia sensu ani argumentacji autora.

### Noty o źródle i dodatkach w zakresie 02–08

- `chapters/04:23,84`: w źródle s. 3 / PDF 11 występuje pisownia „lapidodendron”; polski tekst ją zachowuje, a przypis tłumacza podaje „Lepidodendron”. To rozbieżność w źródle / świadomie oznaczonym przypisie, nie powód do cichej normalizacji.
- `chapters/04` zawiera liczne jawnie oznaczone przypisy tłumacza i zdjęcia tłumacza; nie uznano ich za nieuprawnione dopiski autora. Nie oceniano prawdziwości argumentów kreacjonistycznych ani teologicznych.
- `chapters/05:76` zawiera jawnie oznaczone dodatkowe uwagi o przekładach polskich; zachować odrębność od przypisu Pickeringa.
- `chapters/06` i `03`: porównanie pełnej treści nie wykazało istotnych pominięć względem źródła; dodatki tłumacza są oznaczone.
- `chapters/07:11`: angielskie „the grandson makes clear that ben Sirach was simply a wise man and he was simply translating” zawiera niejednoznaczne `he`. PL („ben Sirach był … i zajmował się … tłumaczeniem”) rozstrzyga odniesienie na ben Siracha; wymaga świadomego rozważenia, ponieważ kontekst wskazuje raczej na wnuka jako tłumacza. Nie zaliczono tego do bezspornego błędu bez zaznaczenia niejednoznaczności samego EN.

### P1-017 — Treść / opuszczony akapit

- Lokalizacja: `chapters/09-czesc-1-historyczne-dowody-wczesne-rozpoznanie.md:5–7`, przejście od cytatu Horta do „Okres apostolski”. Źródło: s. 20 / PDF 28.
- EN: „Rather than take Hort’s word for it, prudence calls for a review of the premises. The place to start is at the beginning, when the apostles were still penning the Autographs.”
- W PL cały akapit jest nieobecny. Kierunek: przetłumaczyć i przywrócić pomiędzy cytatem Horta a podtytułem, bez zmiany kolejności.

### P1-018 — Treść / błędnie oddany idiom

- Lokalizacja: `chapters/09-czesc-1-historyczne-dowody-autografy.md:18`, „osiadło podczas jego posługi”. Źródło: s. 17 / PDF 25.
- EN: „had sat under his ministry until the persecution under Saul…”.
- Problem: chodzi o korzystanie z posługi/nauczania Piotra, nie osiedlenie się podczas jego posługi. Kierunek: zachować relację przywódców do nauczania Piotra oraz granicę czasową prześladowania.

### P1-019 — Treść / draft

- Lokalizacja: `chapters/09-czesc-1-historyczne-dowody-autografy.md:24`, „wstępnego konspektu listu”. Źródło: s. 18 / PDF 26.
- EN: „initial draft of the letter”.
- Problem: konspekt jest planem tekstu, nie jego pierwszą zapisaną wersją, na której opiera się argument o kolejnych egzemplarzach. Kierunek: „pierwszej wersji listu” / „pierwotnego szkicu listu”.

### P1-020 — Nazwy ksiąg i literówki

- Lokalizacja: `chapters/09-czesc-1-historyczne-dowody-autografy.md:20,28`: „Objawienie”, „Księga Objawienia”; `chapters/09-czesc-1-historyczne-dowody-wczesne-rozpoznanie.md:19,65,67`: te same formy i „Księga Objawnienia”, „Justin”. Źródło: s. 17,19,22,27 / PDF 25,27,30,35.
- EN: Revelation; Justin. Kierunek: ustalone „Objawienie Jana”, usunąć dodatkowe `n` w „Objawnienia”, zachować polską formę „Justyn” stosowaną w sąsiednich akapitach.

### P1-021 — Treść / zmieniony podmiot w zdaniu o Ignacym

- Lokalizacja: `chapters/09-czesc-1-historyczne-dowody-wczesne-rozpoznanie.md:45`, „Ignacy mówi, że są **one** wspomniane we «wszystkich listach Pawła»”. Źródło: s. 25 / PDF 33.
- EN: „in his own letter to the Ephesians Ignatius says **they** are mentioned in ‘all the epistles of Paul’”.
- Problem: PL „one” wskazuje pisma/listy, podczas gdy adresatami odniesienia są Efezjanie. Kierunek: jawnie przywrócić „Efezjanie są wspomniani” lub równoważne odniesienie osobowe.

### P1-022 — Treść / składnia cytatu Barnaby

- Lokalizacja: `chapters/09-czesc-1-historyczne-dowody-wczesne-rozpoznanie.md:39`, „bądźmy ostrożni, aby nie, jak jest napisane, to powinno być z nami znalezione, że…”. Źródło: s. 24 / PDF 32.
- EN: „let us be careful **lest**, as it is written, **it should be found with us** that…”.
- Problem: polska kalka nie tworzy logicznego zdania i zaciera ostrzeżenie „aby nie okazało się o nas…”. Kierunek: odtworzyć poprawną konstrukcję warunkowo-ostrzegawczą bez modyfikowania cytatu końcowego.

### P1-023 — Forma / utracone oznaczenie cytatu blokowego

- Lokalizacja: `chapters/09-czesc-1-historyczne-dowody-wczesne-rozpoznanie.md:25,81`. Źródło: s. 22–23,28 / PDF 30–31,36.
- EN: blok Łk 1,1–4 od „Given that many…” oraz cytat Barry’ego od „His testimony to the authority…” są osobnymi wciętymi blokami. PL podaje oba jako zwykłe akapity bez `>`.
- Kierunek: przywrócić status cytatu blokowego. Szczególnie wiersz 81 wygląda teraz jak własny akapit Pickeringa, choć źródło wyróżnia przytoczenie innego autora.

### P1-024 — Forma / utracona kursywa greki i transkrypcji

- Lokalizacja: `chapters/09-czesc-1-historyczne-dowody-autografy.md:40–41`, `mneme`, `poieo`, `μνήμη`, `ποιέω`; `chapters/09-czesc-1-historyczne-dowody-wczesne-rozpoznanie.md:27`, `ανωθεν`, `απ αρχης`. Źródło: s. 18,23 / PDF 26,31, XML.
- EN wyróżnia wskazane wyrażenia kursywą, PL nie. Kierunek: przywrócić kursywę na wyrażeniach autora, zachowując odrębność komentarzy tłumacza. Źródło greckie ma `μνημη`, `ποιεω` bez akcentów; PL wprowadza akcenty, co należy rozważyć jawnie zamiast przypisywać zmianę autorowi.

### P1-025 — Forma / utracona kursywa tytułów i jednego słowa

- Lokalizacja: `chapters/09-czesc-1-historyczne-dowody-wczesne-rozpoznanie.md:21` („ważne”); `61` (dwa skrócone „Tryfonie/Tryfona”); przypisy `89,91,93,107,109,123,125,131,138` (tytuły książek).
- Źródło: s. 20,22,25–28 / PDF 28,30,33–36, XML. EN ma *valid*, *Trypho* oraz kursywę tytułów *The Identity…*, *What is…*, *The New Testament…*, *The Apostolic Fathers*, *The Fathers of the Church*, *The New Testament in the Apostolic Fathers*, *The Ante-Nicene Fathers*, *Early Christian Fathers*, *The Inspiration…*.
- Kierunek: odtworzyć kursywę w tych miejscach; zastąpienie kursywy cudzysłowami w części przypisów nie zachowuje wyróżnienia źródła.

### P1-026 — Forma / brak lub zmiana podkreśleń, zakres 04–09

- Źródło sprawdzone geometrycznie w oryginalnym PDF, dodatkowo render s. 7 / PDF 15. Brak podkreślenia / odpowiednika wyróżnienia w:
  - `chapters/04:37`: „co godzinę” — EN *hour*, s. 4 / PDF 12.
  - `chapters/06:3`: „nie jest w stanie” — EN *cannot*, s. 12 / PDF 20.
  - `chapters/07:9`: „ustnie”, „forma pisemna” — EN *orally*, *writing*, s. 14 / PDF 22.
  - `chapters/08:3,7,11`: „zrobił/uczynił”, „ani jedna” — EN *did*, *not one*, s. 14–16 / PDF 22–24.
  - `chapters/09-czesc-1-historyczne-dowody-autografy.md:5`: „przed swobodną edycją” — EN *protecting against free editing*, s. 16 / PDF 24.
  - `chapters/09-czesc-1-historyczne-dowody-wczesne-rozpoznanie.md:21`: „teraz” w 1 P 1,12 — EN *now*, s. 22 / PDF 30; `87`: „ich” stosunek — EN *their*, s. 29 / PDF 37.
- Zmienione na pogrubienie podkreślenia: `09-wczesne:9` pierwsze „teraz” (s. 20 / PDF 28), `13` oba „teraz” (s. 21 / PDF 29), `25` „poznać” (s. 23 / PDF 31), `33` „nie znajduje się w Starym Testamencie” (s. 24 / PDF 32), `73` zdanie „Zwróć następnie uwagę…” (s. 27–28 / PDF 35–36).
- Kierunek: przyjąć konsekwentne odwzorowanie oryginalnych podkreśleń i przywrócić brakujące zakresy; nie traktować występującego bold jako nowego akcentu autora. Wskazane w P1-012 podkreślenie należy do tego samego problemu.

### P1-027 — Treść / powtórzenie wielkiej litery istotnej dla argumentu

- Lokalizacja: `chapters/09-czesc-1-historyczne-dowody-wczesne-rozpoznanie.md:27`, „przetłumaczyłem «wszystko z góry»”. Źródło: s. 23 / PDF 31.
- EN: „I rendered ‘everything from **Above**’”, podczas gdy objaśniane znaczenie słownikowe dalej brzmi małą literą „from **above**”. PL cytatu w w.25 używa „Góry”, lecz omawiając własny przekład gubi tę wielką literę.
- Kierunek: zachować „wszystko z Góry” w cytowaniu dokonanego przekładu i małe „z góry” przy znaczeniu słownikowym.

### Noty o źródle i kompletności w zakresie 09

- Przypisy autora porównano w całości, w tym przenoszone między stronami. Definicja `unia-hipostatyczna` z 05 ma rzeczywiste użycie w w.46 i nie jest osierocona.
- Nazwa „majority text” w 09-autografy występuje w źródle małymi literami i w cudzysłowie; nie zgłaszano automatycznego podniesienia wielkości liter bez rozpoznania użycia opisowego.
- Źródło s. 22 / PDF 30 ma `1 Peter 1:12,,` oraz `Mathew`; w PL nie powielono tych oczywistych usterek. Źródło s. 20 / PDF 28 celowo podaje Rz16,24–25 i wyjaśnia alternatywne umiejscowienie w przypisie, więc nie traktować adresu jako polskiej pomyłki.

### P1-028 — Treść / błędny adres i przypisanie gatunku księdze

- Lokalizacja: `chapters/10:9`, „Dzieje Apostolskie 21,28-31”; `10:29`, „Listów Łukasza i Pawła”. Źródło: s. 30,32 / PDF 38,40.
- EN ma `Acts 20:28-31` oraz `Luke and Paul’s Epistles`. Kierunek: przywrócić rozdział 20 oraz odróżnić Ewangelię Łukasza od Listów Pawła; PL przypisuje Łukaszowi listy.

### P1-029 — Forma / brak cytatów blokowych

- Lokalizacja: `chapters/10:39` (cały akapit od „W celu zapewnienia”), `10:47` (słowa Tertuliana od „kościołów apostolskich”), `chapters/12:37–39` (oba akapity Kilpatricka). Źródło: s. 33–34,47 / PDF 41–42,55.
- EN oznacza te fragmenty osobnymi wciętymi cytatami. PL ma zwykłe akapity. Szczególnie 10:39 jest w całości przytoczeniem Metzgera, nie tylko zawartą w nim wypowiedzią Ireneusza. Kierunek: przywrócić granice cytatów i ich `>`.

### P1-030 — Terminologia / objętość manuskryptu

- Lokalizacja: `chapters/11:19`, „manuskryptem Nowego Testamentu o dowolnej wielkości”. Źródło: s. 37 / PDF 45.
- EN `extant NT manuscript of any size` odnosi się do manuskryptu znaczniejszej objętości, a nie dowolnego rozmiaru; autor zaraz precyzuje, że zawiera większość Jana. Ten sam problem występuje w dodatku 39 (uwaga P4-002), podczas gdy 48 używa „o znacznej objętości”. Kierunek: ujednolicić wierny odpowiednik.

### P1-031 — Treść / odwrócony kierunek prawdopodobieństwa

- Lokalizacja: `chapters/12:19`, „podniosłoby do absolutnie zaporowych poziomów szanse wystąpienia okoliczności, w których…”. Źródło: s. 45 / PDF 53.
- EN `raise ... the chances against an opportunity for aberrant text forms to gain ... widespread acceptance` mówi o wzroście szans **przeciw** rozpowszechnieniu zniekształconych form. PL mówi o zwiększeniu szans ich rozpowszechnienia, odwracając wniosek. Kierunek: oddać wzrost nieprawdopodobieństwa / przeszkody dla takiego rozpowszechnienia, bez zmieniania argumentacji autora.

### P1-032 — Treść / wspólny zakres zamieniony w sumę

- Lokalizacja: `chapters/12:37`, „Łącznie zachowało się w nich około siedemdziesięciu wersetów”. Źródło: s. 47 / PDF 55.
- EN `They are together extant for about seventy verses` i następne porównanie 73 różnic dotyczą około 70 wersetów zachowanych **w obu** papirusach, nie sumy ich objętości. Kierunek: przywrócić wspólny zakres, na którym opiera się porównanie.

### P1-033 — Terminologia, wielkość liter i drobna korekta językowa

- `chapters/10:41,43`: powtarzające się „Księga Objawienia” — ustalone „Objawienie Jana”; w `11:31` samo „Objawienie” (EN Revelation; s. 33,38 / PDF 41,46).
- `chapters/10:43`: EN `the original reading` → „jak brzmiał oryginalny tekst”; przywrócić techniczny „oryginalny odczyt” (s. 33 / PDF 41).
- `chapters/11:13`, „tekstu Nowego Testamentu”: EN `NT Text`; `12:31`, „tekstowi Nowego Testamentu”: EN `NT Text` — przywrócić wielkie `Tekst` (s. 36,46 / PDF 44,54).
- `chapters/11:47`, „Sam zestawiłem”: EN `Having myself collated` — rozważyć ustalone „skolacjonowałem”, nie tracąc nazwy wykonywanej operacji (s. 41 / PDF 49).
- `chapters/10:19`: „słyszą słów” → „słyszą słowa”, „nie zwróci szczególną uwagę” → „nie zwróci szczególnej uwagi”; `10:13`: „zaprzeczając Właściciela” wymaga poprawnej konstrukcji „wypierając się Właściciela” (EN denying the Owner); `12:47`: „zmienić tekst” → „zmienić tekstu”.

### P1-034 — Forma / utracona kursywa, zakres 10–12

- `chapters/10:27`: tytuł „Apologia I” (EN *Apol.*); `10:41`: oba greckie zapisy liczby χξς̓ / χις̓. Źródło s. 32–33 / PDF 40–41, XML.
- `chapters/11:65,67,69,88`: tytuły *The Early Versions of the New Testament*, *The Bible in Modern Scholarship*, *The Text of the New Testament*, *The Last Twelve Verses of Mark*, *The Four Gospels: A Study of Origins*. Źródło s. 38,42 / PDF 46,50.
- Kierunek: odtworzyć zakresy kursywy. Kontrola pozostałych wyróżnień jest zakończona; dalsze uwagi znajdują się w P1-046 i P1-047.

### P1-035 — Forma / numer przypisu włączony do treści

- Lokalizacja: `chapters/12:72`, początek definicji `[^jw-burgon-revision-323-324]: 3 J.W. Burgon`. Źródło s. 46 / PDF 54.
- Cyfra `3` jest numerem przypisu oryginalnego PDF-u, nie częścią bibliografii. Kierunek: usunąć ją z treści definicji, pozostawiając jej identyfikator.

### P1-036 — Treść / liczba manuskryptów zamieniona na liczbę odczytów

- Lokalizacja: `chapters/13:22`, „tylko dziewięć odczytów zawiera inne słowo. Spośród tych dziewięciu odczytów…”. Źródło: s. 52 / PDF 60.
- EN mówi o dziewięciu **manuskryptach** wobec około 600, po czym rozróżnia trzy odczyty indywidualne i sześć manuskryptów zgodnych co do „kto”. PL przenosi liczebność świadków na liczbę odczytów i zaciera podstawę porównania procentowego. Kierunek: w obu miejscach przywrócić manuskrypty.

### P1-037 — Treść / utrata jednej linii zamieniona na utratę obu

- Lokalizacja: `chapters/13:69`, „ani linia krzyżowa, ani kreska skrótu nie są już zauważalne”. Źródło: s. 53 / PDF 61.
- EN `either the cross-line or the contracting-bar is no longer discernible` mówi o niewidoczności jednej lub drugiej linii. PL opisuje niewidoczność obu, podczas gdy następne zdanie źródła właśnie **odróżnia** rzadkie zniknięcie obu linii. Kierunek: przywrócić alternatywę, nie zmieniać rozumowania autora.

### P1-038 — Terminologia / odrębne typy świadków

- Lokalizacja: `chapters/13:53,57`, „minuskuł/minuskuły”, `13:65`, „kursywę 365”; `13:75`, „najwcześniejszą wersją… jest manuskrypt gotycki”. Źródło: s. 52–54 / PDF 60–62.
- EN w pierwszych miejscach konsekwentnie używa `cursive(s)`, nie `minuscule(s)`. Zgodnie z ustaleniem zachować „rękopis kursywny / rękopisy kursywne”; „kursywa 365” myli rękopis z rodzajem wyróżnienia pisma. W drugim przypadku `earliest version ... the gothic` oznacza wersję/przekład gocki, a nie jeden manuskrypt. Kierunek: zachować rozróżnienie wersji językowej i jej świadków.

### P1-039 — Terminologia / recenzja i rewizja

- Lokalizacja: `chapters/13:14`, „typów tekstowych i opracowań krytycznych”; `13:20`, „opracował poprawkę”; `chapters/15:25`, „nie jest opracowaniem krytycznym, nie powstała później niż Autografy wskutek recenzji”. Źródło: s. 51–52,61 / PDF 59–60,69.
- EN rozróżnia techniczne `recensions` i `revision`, a w 15 stwierdza: `is not a recension, was not created at some point subsequent to the Autographs`. „Opracowanie krytyczne” jest szersze od recenzji tekstu, zaś „poprawka” może sugerować pojedynczą korektę zamiast postulowanej rewizji. Dopisane w 15 „wskutek recenzji” zawęża drugie stwierdzenie, którego źródło nie ogranicza takim warunkiem.
- Kierunek: utrzymać precyzyjne nazwy działań tekstologicznych i niezależność obu twierdzeń 15:25; nie dokonywać cichego ujednolicenia dwóch różnych terminów angielskich.

### P1-040 — Dodatek tłumacza / utożsamienie odrębnych świadków

- Lokalizacja: `chapters/13:36`, objaśnienia „papirus 45 z kodeksu W” oraz „papirus 75 z kodeksu B”. Źródło s. 51 / PDF 59.
- Autor wymienia pary osobnych świadków `P45, W` i `P75, B`, co widać także po odrębnych punktach diagramu. Dopiski tłumacza przedstawiają je jako papirus pochodzący z danego kodeksu. To uwaga do jawnie oznaczonego dodatku, nie zarzut dopisania słów autorowi. Kierunek: wyjaśnić relację jako parę świadków wiązanych przez autora, bez utożsamiania oznaczeń.

### P1-041 — Treść / zakres wyłączności pisma uncjalnego

- Lokalizacja: `chapters/14:5`, „Pismo uncjałowe było stosowane wyłącznie do IX wieku”. Źródło s. 56 / PDF 64.
- EN `The uncial script was exclusively used until the ninth century` mówi, że **do IX wieku stosowano wyłącznie to pismo**, nie że używano go tylko do IX wieku. PL sugeruje koniec jego stosowania w IX wieku, co koliduje nawet z zestawieniem uncjałów do XI wieku w następnym akapicie. Kierunek: przenieść wyłączność na rodzaj używanego pisma.

### P1-042 — Problem źródła i dodatek tłumacza / nazwa języka

- Lokalizacja: `chapters/14:25`, „Skrócona lista rękopisów Nowego Testamentu w języku griesh”. Źródło s. 56 / PDF 64.
- Źródłowy tytuł bibliograficzny ma błędny zapis `Grieshischen`; PL zachowuje go, lecz dodatkowo tworzy z niego nazwę języka „griesh”. Kontekst jednoznacznie dotyczy wykazu greckich manuskryptów. Kierunek: wyraźnie odnotować usterkę źródłowego tytułu i poprawić objaśnienie tłumacza, bez cichego przypisywania poprawionej bibliografii autorowi.

### P1-043 — Treść / odesłanie do niewłaściwej książki

- Lokalizacja: `chapters/15:45`, „zajmuje rozdział 2 tej części”. Źródło s. 60 / PDF 68.
- EN `occupies Chapter 2 of that book` odsyła do właśnie wymienionej *The Identity of the New Testament Text IV*, nie do obecnej części *God Has Preserved His Text*. Kierunek: przywrócić „tej książki”; następne odesłania do rozdziałów 3, 4 i 6 należą do tej samej publikacji.

### P1-044 — Treść / idiom „to be sure”

- Lokalizacja: `chapters/16:5`, „jak zresztą musi, aby być pewnym”. Źródło s. 63 / PDF 71.
- EN `as they must, to be sure, since...` używa wtrącenia potwierdzającego („rzecz jasna”), nie celu działania „aby być pewnym”. Kierunek: przywrócić funkcję wtrącenia, bez osłabiania oskarżenia autora.

### P1-045 — Ustalone odpowiedniki i konsekwencja terminologiczna, 14–16

- `chapters/14:3`: `original wording` → „oryginalne brzmienie”; ma być „oryginalne sformułowania” (s. 55 / PDF 63).
- `chapters/14:17`: trzy wystąpienia „Objawienia/Objawieniem” bez Jana; zachować ustaloną nazwę „Objawienie Jana” (s. 57 / PDF 65).
- `chapters/14:31,34,36,42,44`, `15:35`, `16:19,51`: nazwa czynności `collate/collation` występuje jako „zebrał”, „zestawienie”, „analiza”, „zebrane dane”, „porównania”, „porównywanie”, „zestawione”; warto utrzymać ustalone „kolacjonowanie” zwłaszcza tam, gdzie źródło odróżnia je od `compare/comparison` (14:31 `collated and compared`; s. 57–59,61,64 / PDF 65–67,69,72).
- `chapters/16:7`: „Uwagi o Prawdzie” → ustalone „Notatki prawdy”; w 16:27 jest już właściwy odpowiednik (s. 63,65 / PDF 71,73).
- `chapters/16:9`: „punkt wyjścia” dla `steppingstone` → „punkt pośredni”; w 16:25 autor jawnie komentuje użycie właśnie tego terminu, więc niespójność zaciera odesłanie (s. 63–64 / PDF 71–72).
- Drobne literówki: `15:33` „Ksiega”, `15:45` „Wetcotta”, `16:5` „narazie”, `16:25` „ogólnikow”, `16:37` „z zachowanych greckich manuskryptach” (błędna fleksja).

### P1-046 — Forma / kursywa i dodatkowe wyróżnienia, 12–16

- Brak kursywy: `12:82` *Neutestamentliche Aufsatze* (s. 48 / PDF 56); `13:61` *theta* (s. 53 / PDF 61); `13:83` *Identity IV* (s. 54 / PDF 62). Kursywa *Pericope Adulterae* w tytule referatu `14:44` jest zachowana i nie wymaga poprawki.
- Zmieniona kursywa: `15:41` siedem kryteriów „wielkość”, „niezależność”, „wiek”, „rozmieszczenie geograficzne”, „profil”, „staranność”, „zakres” — źródło ma bold i podkreślenie, PL bold i kursywę (s. 62 / PDF 70, także render); `16:7` *Tekst Większościowy* — EN `Majority Text` jest zwykłym tekstem (s. 63 / PDF 71).
- Kierunek: odtworzyć oryginalne zakresy i rodzaje wyróżnień. Pozostałe różnice wynikające z podkreśleń są opisane w P1-047.

### P1-047 — Forma / brak lub zmiana podkreśleń, zakres 10–16

- Brak wyróżnienia `false` → „fałszywi” w cytacie 2 P 2,1: `chapters/10:13`, źródło s. 30 / PDF 38.
- Zmiana podkreślenia na bold: `10:19` „mu” (s. 31 / PDF 39); `10:25` „wzburzony” (s. 32 / PDF 40); `10:58` całe „kluczową kwestią jest zachowanie jego Tekstu” (s. 35 / PDF 43); `12:70` „natchnionego Tekstu” (s. 46 / PDF 54); `13:38` „będą” (s. 51 / PDF 59); `15:45` „Tekstu” w tytule zastrzeżenia (s. 60 / PDF 68); `16:25` „wykazane” i `16:33` „nie może” (s. 65 / PDF 73); `16:33` zdanie od „Jeśli K^r^ jest wczesny i niezależny” do „Nowego Testamentu” (s. 66 / PDF 74). Następne zdanie o najlepszej linii jest w źródle rzeczywiście pogrubione, należy zachować to rozróżnienie.
- Brak podkreślenia przy zachowanym bold: końcówka liczby mnogiej `word**s**` → `sł**ów**` w `10:19` (s. 31 / PDF 39), `11:37` „IV wieku” (s. 40 / PDF 48).
- `10:72`, ostatnie „słowa” przed „prawdziwe i wierne”: źródło podkreśla końcówkę `s` (liczbę mnogą); PL nie zachowuje tego akcentu (s. 31 / PDF 39).
- Podkreślenia siedmiu kryteriów z `15:41` zamieniono na kursywę, jak w P1-046. Wszystkie wskazania pochodzą z geometrii oryginalnego PDF-u; reprezentatywne s. 30,31,35,62,66 potwierdzono również renderami.
- Kierunek: zastosować spójny sposób zapisu podkreśleń obsługiwany przez Pandoca, nie usuwać istniejącego akcentu i nie zgłaszać go jako całkowicie nowego pogrubienia autora.

### P1-048 — Treść / świadkowie tekstu a dowody jego istnienia

- Lokalizacja: `chapters/12:65`, „nie mamy zachowanych żadnych świadectw ich istnienia”. Źródło s. 45 / PDF 53.
- EN `we have no extant witness to them` odnosi się do braku zachowanych świadków zawierających omawiane odczyty. PL twierdzi szerzej, że brak jakichkolwiek zachowanych dowodów ich istnienia, choć autor w tym samym zdaniu odwołuje się do przedstawionych dowodów. Kierunek: zachować techniczny sens „nie mamy żadnego zachowanego świadka tych odczytów”, nie negować dowodów istnienia.

### P1-049 — Forma / nawiasy zagnieżdżone

- Lokalizacja: `chapters/13:67`, `(por. Fee…)` w całym akapicie ujętym w nawiasy; `chapters/15:35`, `(22)`, `(przypuszczalnie)`, `(4)`, `(Dzieje Apostolskie)` wewnątrz całej uwagi nawiasowej. Źródło s. 53,61 / PDF 61,69.
- W pierwszym miejscu EN ma wewnętrzne nawiasy kwadratowe; w drugim zewnętrzne EN są kwadratowe, a wewnętrzne okrągłe. Zamiana zewnętrznych na okrągłe w PL wymaga pozostawienia/zmiany wewnętrznych na kwadratowe zgodnie z AGENTS, zamiast nawiasów okrągłych wewnątrz okrągłych.

## Pliki 18–21 — uwagi P5

### P5-001 — dane: pominięty świadek bo w Rz 5,1 (ważne)

- PL: `chapters/19-czesc-2-datowanie-kr-ponownie-rozwazone.md:36`: po `ℵABCD,lat` następuje komentarz.
- EN druk 92 / PDF 100: przy εχωμεν wykaz brzmi `ℵABCD,lat,bo`.
- Kierunek: przywrócić `bo` po `lat`; nie zmieniać pozostałych danych wariantu.

### P5-002 — treść: odwrócony sens „blinded to the evidence” (ważne)

- PL: ten sam plik, w. 175: „Jeśli sam von Soden przyjął doktrynę Horta, dowody go zaślepiły”.
- EN druk 97 / PDF 105: „If von Soden himself had bought into Hort’s doctrine, then he was blinded to the evidence”.
- Źródło mówi o zaślepieniu **na dowody** wskutek przyjętego poglądu, PL czyni dowody przyczyną zaślepienia. Kierunek: „był ślepy na dowody” / „był zaślepiony i nie dostrzegał dowodów”.

### P5-003 — treść: twierdzenie zmienione w pytanie

- PL: `chapters/20-czesc-2-o-wzorcu-i-zaleznosci.md:104`: „Skoro wszystkie trzy zależą od Oryginału, czy możemy ustalić, która z nich jest najbardziej zależna, a zatem najbliższa Oryginałowi?”.
- EN druk 105 / PDF 113: „Since all three are dependent on the Original, we can determine which is most dependent, and therefore closest to the Original!”.
- Autor stwierdza możliwość ustalenia i kończy wykrzyknikiem, nie pyta o taką możliwość. Kierunek: „Skoro wszystkie trzy zależą od Oryginału, możemy ustalić, która z nich jest najbardziej zależna, a zatem najbliższa Oryginałowi!”.

### P5-004 — forma: braki pogrubień wieków w rozdziale 19

- PL: `chapters/19-czesc-2-datowanie-kr-ponownie-rozwazone.md`. EN druk 90–97 / PDF 98–105 wyróżnia pogrubieniem niżej wskazane rzymskie liczby wieków; PL ich nie wyróżnia.
- Druk 90 / PDF 98: w. 5 — `XIV`, `XI`, `XII`.
- Druk 91 / PDF 99: w. 15 — `X` oraz końcowe `IX`, `VIII` (nie wcześniejsze `IX` w cytacie „na długo przed IX wiekiem”, które jest zwykłe również w źródle); w. 17 — `IV`; w. 21 — `IV`.
- Druk 92 / PDF 100: w. 38 i 47 — `II/III`.
- Druk 93 / PDF 101: w. 83 — `IV`, `III`, `II`; w. 87, 89, 91 — `V`.
- Druk 94 / PDF 102: w. 103 — `V`; 107 — `IV`; 110 i 112 — `III`; 118 — `IV`; 120 — `II`; 122 — `III`.
- Druk 95 / PDF 103: w. 128 — `V`; 129 — `III`; 132 — `V`; 138 — `II`; 140 — `III`; 144 — `IV`; 151 — `V`.
- Druk 96 / PDF 104: w. 155 — `IV`; 158 — `III`; 160 — `II`; 163, 165 — `III`; początkowe `II` w w. 171 („Obiektywne dowody z II wieku”); w. 187 — `III`.
- Druk 97 / PDF 105: dalsze `II` i `III` w w. 171; `III` w w. 173.
- **Już naprawione, nie otwarty problem:** `XII` w w. 3 (druk 89 / PDF 97) ma pogrubienie w commicie użytkownika `17c80ef`.
- Nie pogrubiać mechanicznie wszystkich wieków w całym rozdziale: np. cytowany Robinson oraz końcowe akapity w. 175–177 mają zwykłe liczby również w źródle.

### P5-005 — forma: pozostałe zmiany wyróżnień w 18–21

| PL | Źródło druk / PDF | Różnica i kierunek |
|---|---|---|
| 18:69, przypis Goulburna | 85 / 93 | `Life of Dean Burgon` w EN zwykłym krojem, PL kursywą. Usunąć dodaną kursywę, chyba że użytkownik zatwierdzi osobno konsekwentną normalizację bibliografii. |
| 19:83, `Ewangelii Łukasza` w tytule wydania IGNTP | 93 / 101 | EN `Luke` kursywą; polski odpowiednik nie ma kursywy. |
| 19:177, całe końcowe zdanie WERSALIKAMI | 97 / 105 | W EN są wersaliki, ale nie pogrubienie; PL dodało również bold. |
| 20:3, `WSZYSTKIE` | 97 / 105 | EN bold + podkreślenie, PL tylko bold. |
| 20:35, końcowe zdanie `Sfabrykowana kopia jest bez znaczenia dla historii przekazywania Tekstu.` | 100 / 108 | EN podkreślenie bez bolda, PL bold bez podkreślenia. |
| 20:104, `nie` w `te trzy grupy nie są jednakowo niezależne` | 105 / 113 | EN `not` podkreślone, PL nie. |
| 20:126, `Trinity Journal`; 20:130, `The Profile Method for the Classification and Evaluation of Manuscript Evidence` | 100 / 108 | EN zwykły krój, PL dodana kursywa bibliograficzna. Do przywrócenia albo osobnej zgody na normalizację. |
| 21:3, `tekst` i `tekstu`; 21:104 i 110, `tekst` | 106 / 114; 109 / 117; 110 / 118 | Wszystkie cztery wystąpienia EN `text` są jednocześnie podkreślone i pogrubione. PL zachowuje tylko podkreślenie. |

Skrótu *PA* ani standardowego pogrubienia siglów nie uznano za błąd wyłącznie z powodu zastosowania kursywy/bolda: użytkownik osobno dopuszcza zapis *PA* oraz wymaga zachowania ustalonego zapisu symboli.

### P5-006 — forma: utracony pionowy układ dziewięciu grup

- PL: `chapters/20-czesc-2-o-wzorcu-i-zaleznosci.md:41` — wszystkie dziewięć par w jednym akapicie.
- EN druk 101 / PDF 109: dziewięć osobnych wierszy od `e—495` do `c—20`, każdy widoczny niezależnie. Wszystkie dane, kolejność i wyróżnienia liter zachowano, lecz układ listy zniknął.
- Kierunek: przywrócić osobne wiersze, np. prostą tabelą Markdown; nie zmieniać liczb (ich suma prawidłowo wynosi 2212).

### P5-007 — forma: stemma nie zachowuje połączeń, znaki i fragment diagramu giną w PDF (ważne)

- PL: `chapters/20-czesc-2-o-wzorcu-i-zaleznosci.md:108`, cały blok w. 109–115. EN druk 106 / PDF 114.
- Już w Markdownzie `O` i pionowa kreska mają sześć spacji wcięcia, a kwadrat `□` rozpoczyna się w pierwszej kolumnie: połączenie O → kwadrat nie trafia w węzeł. Źródło ma O dokładnie nad kwadratem `macro-C`; z kwadratu wychodzą gałęzie do c i do kółka `a,d`, z kółka do a i d.
- Potwierdzono na obrazach aktualnego `build/pdf/Bog-zachowal-swoj-Tekst-Wilbur-Pickering.pdf`, s. 125–126: kreski, rozgałęzienia, kwadrat i kółko są **niewidoczne**; pozostają jedynie rozrzucone etykiety. Końcowe `d` dodatkowo przeszło na następną stronę.
- Kierunek: zachować pełny czytelny diagram, właściwe przyłączenie O i nie dzielić go między stronami; sprawdzić czcionkę/grafikę we wszystkich formatach docelowych. Nie wystarczy zmiana samego wcięcia. Nie zmieniano książki ani nie regenerowano PDF na potrzeby tego review.

### P5-008 — forma: zniknęły bloki tabeli, do których odwołuje się wywód

- PL: `chapters/21-czesc-2-wczesne-poswiadczenie-f35-w-listach-ogolnych.md:13`, tabela w. 13–86. EN druk 107–108 / PDF 115–116.
- Źródło wizualnie oddziela wiersz samej rodziny i pięć grup według liczby towarzyszących uncjałów. PL łączy je w nieprzerwaną tabelę. Wywód w w. 106–108 mówi następnie o „pierwszym bloku”, „następnym bloku” itd., lecz granic bloków nie widać.
- Zachować wyróżnione grupy: w. 13 osobno; w. 14–20 — jeden uncjał (119); 21–35 — dwa (148); 36–59 — trzy (224); 60–76 — cztery (100); 77–86 — pięć (28). Dane i wszystkie sumy tych grup przeniesiono wiernie.
- Kierunek: przywrócić wizualne rozdzielenie bloków w przenośnym zapisie Pandoca, bez ingerowania w dane ani dopisywania argumentacji.

### P5-T01 — terminologia: Redeemer i Provider w cytacie Xaviera

- PL: `chapters/18-czesc-2-epistemologia.md:47`: „Stwórcą, Zbawicielem i Opiekunem”.
- EN druk 88 / PDF 96: „Creator, Redeemer and Provider”.
- *Redeemer* akcentuje odkupienie, nie jest tym samym terminem co *Savior*. *Provider* akcentuje zapewnianie potrzebnych środków, podczas gdy „Opiekun” jest ogólniejszy. Do decyzji terminologicznej: zachować te odrębne znaczenia, np. „Stwórcą, Odkupicielem i Tym, który zaspokaja potrzeby”. Nie zmieniać teologicznego argumentu cytowanego autora.

### P5-T02 — terminologia: Catholic Epistles w opisie bibliograficznym

- PL: `chapters/21-czesc-2-wczesne-poswiadczenie-f35-w-listach-ogolnych.md:112`, `Listy Ogólne`.
- EN druk 106 / PDF 114, przypis 1: tytuł tomu `Catholic Epistles`, podczas gdy w tekście głównym autor używa `General Epistles`.
- To kolejne miejsce globalnego zagadnienia z P3-T02: dwa różne określenia źródłowe zostały znormalizowane do jednego. Do decyzji, czy zachować w opisie bibliograficznym angielski tytuł albo odrębny odpowiednik; nie zmieniać po cichu całej terminologii.

### P5-T03 — terminologia: egzemplarz jako exemplar może zatrzeć relację wzorzec → kopia

- Konkretne miejsca: 19:5 („jeśli 35 jest kopią [...] jego egzemplarz musiał być starszy”, EN druk 90 / PDF 98); 19:15 („Jeśli są kopiami [...] ich egzemplarze musiały być starsze”, EN druk 91 / PDF 99); 21:106 („Jeśli są kopiami, ich egzemplarze były oczywiście wcześniejsze”, EN druk 109 / PDF 117).
- To kontynuacja P3-001, **nie teza, że każde tłumaczenie exemplar jako egzemplarz jest błędem**. „Egzemplarz” może funkcjonować jako termin techniczny, ale przy tych konkretnych zdaniach czytelnik może utożsamić go z omawianą zachowaną kopią, zamiast z jej starszą podstawą. Do uzgodnienia: konsekwentny termin jednoznacznie pokazujący, z czego przepisano kopię, albo objaśnienie przy pierwszym użyciu.

### P5-S01 — literówka Platinga jest w oryginale

- Rozdział 18, w. 29 ma poprawnie „Plantinga”, a w. 41 „Platinga”. Oryginał analogicznie druk 87–88 / PDF 95–96. To wiernie przeniesiona literówka źródła; nie traktować jako błąd tłumaczenia ani nie poprawiać po cichu.

### P5-S02 — własne sprzeczności liczbowe tabel rozdziału 21 (nie błędy przekładu)

- EN druk 107–109 / PDF 115–117; PL `chapters/21-czesc-2-wczesne-poswiadczenie-f35-w-listach-ogolnych.md`, w. 13–102. Każdy odczytany wiersz i każdą komórkę PL porównano ze źródłem: dane są przeniesione wiernie.
- W w. 87 suma sześciu podanych sum kolumn wynosi 610, nie 619. Zsumowanie poszczególnych komórek kolumny 1 Listu Piotra, bez wiersza „f35 sam”, daje 164, a podano 155. Pozostałe pięć sum kolumn zgadza się; wszystkie 73 sumy wierszy „z uncjałem” dają 619, a z wierszem „sam” 795. A zatem nie jest to w polskim tekście zgubione dziewięć danych.
- Zsumowanie wierszy zawierających poszczególne sigla daje kolejne rozbieżności wobec podsumowania, obecne także w EN: P81 — 7 wobec podanych 4 (w. 95), ℵ — 358 wobec 356 (w. 97), A — 361 wobec 356 (w. 98), 048 — 64 wobec 62 (w. 101). Pozostałe osiem pozycji podsumowania zgadza się. Przypis w. 114, twierdzący, że liczba 356 dla A jest poprawna, również pochodzi ze źródła.
- W. 80 (`f35 P72 ℵAB048`) ma liczbę 6 w kolumnie 2 i 3 Listu Jana także w EN druk 108 / PDF 116, chociaż tekst w. 7 mówi, że P72 obejmuje tylko 1 i 2 List Piotra oraz Judę (EN druk 107 / PDF 115). To kolejna wewnętrzna sprzeczność oryginału, nie przesunięcie kolumn wykonane przez tłumacza.
- Kierunek: nie poprawiać samowolnie danych ani wywodu autora. Ewentualna nota redakcyjna wymaga decyzji użytkownika. Wypowiedź autora z w. 9, że nie gwarantuje pełnej dokładności tabel, została zachowana.

## Pliki 17, 22–30 — uwagi P2

### P2-001 — decyzja terminologiczna / ryzyko niejednoznaczności: „exemplar” i „egzemplarz”

- Miejsce: `chapters/29-czesc-2-boskie-zachowanie-oryginalnych-sformulowan-listow-ogolnych.md:75`, także 79, 83–95 i nagłówek tabeli 25; `chapters/30-czesc-2-czy-archetypalny-tekst-f35-jest-autografem.md:11`.
- Źródło: s. 179–182 / PDF 187–190. EN: „their exemplars were also perfect; and the exemplars of the exemplars were also perfect”; „as do the exemplars of 35 and 2723, and as does 2723 itself”.
- PL: „ich egzemplarze również były doskonałe, a egzemplarze egzemplarzy także były doskonałe”; „podobnie jak egzemplarze 35 i 2723, a także praktycznie sam 2723”.
- Problem: argument wyraźnie rozróżnia zachowany manuskrypt i wcześniejszy manuskrypt, z którego go przepisano. „Egzemplarze 35 i 2723” brzmi jak te same zachowane manuskrypty i zaciera rozróżnienie szczególnie w 30:11.
- Kierunek: rozważyć „wzorce, z których przepisano 35 i 2723” w 30:11. Nie jest to automatyczny błąd każdego wystąpienia „egzemplarza”: jeżeli w książce wprowadzono go jako termin techniczny, można go zachować, ale w tym konkretnym zdaniu warto uniknąć utożsamienia go z samym 2723. Przed zmianą uzgodnić stały odpowiednik w całej książce.

### P2-002 — forma: zagnieżdżone nawiasy autora

- Miejsce: `chapters/29-czesc-2-boskie-zachowanie-oryginalnych-sformulowan-listow-ogolnych.md:75`.
- Źródło: s. 179 / PDF 187. EN: „(MS 664 has thirty … basic profile [the diagnostic variants …] …)”.
- PL: „(Manuskrypt 664 ma trzydzieści … podstawowy profil (warianty diagnostyczne …), …)”.
- Kierunek: wewnętrzne nawiasy przy objaśnieniu wariantów pozostawić kwadratowe zgodnie z regułą nawiasów w nawiasach.
- Analogicznie 27:9 (wewnętrzne `27/24`), 27:43 (wewnętrzne `57` oraz dłuższy nawias „Nie mam zwyczaju…”), źródło s. 163, 165 / PDF 171, 173. Procentów w nawiasach kwadratowych nie normalizować bezrefleksyjnie: w 27:137 autor wyraźnie odróżnia pochodzenie procentów oznaczonych nawiasami okrągłymi i kwadratowymi.
- Także 26:65: „(… są niestarannymi błędami (nieszczęśliwi mnisi))”, źródło s. 159 / PDF 167. Zachować zagnieżdżenie, stosując wewnątrz nawias kwadratowy.

### P2-003 — forma: zbyt szerokie podkreślenie cytatu Ehrmana

- Miejsce: `chapters/29-czesc-2-boskie-zachowanie-oryginalnych-sformulowan-listow-ogolnych.md:5`.
- Źródło: s. 175 / PDF 183, sprawdzone wizualnie. Podkreślone jest wyłącznie EN „must”.
- PL: podkreślono cały fragment „musi (wyróżnienie dodane) oznaczać jedną z trzech rzeczy — albo 1) Bóg”.
- Kierunek: ograniczyć `[...]{.underline}` do słowa „musi”; komentarz autora i resztę zdania pozostawić bez podkreślenia.

### P2-004 — terminologia gramatyczna: `mass noun` nie jest `collective noun`

- Miejsce: `chapters/28-czesc-2-glowne-podzialy-f35-w-ewangelii-mateusza.md:9`.
- Źródło: s. 170 / PDF 178. EN: „plural or singular; mass noun or not?”; PL: „liczba mnoga czy pojedyncza, rzeczownik zbiorowy czy nie?”.
- Kierunek: zachować termin autora jako „rzeczownik niepoliczalny” (ew. „masowy”). Nawet jeżeli `mass noun` autora w odniesieniu do tej konstrukcji budzi wątpliwość, nie zastępować po cichu innym terminem gramatycznym.
- Ten sam przypadek: 27:9, EN „whether the mass noun is viewed as singular or plural”, s. 163 / PDF 171.

### P2-005 — forma: pominięty tytuł tabeli wzorców

- Miejsce: `chapters/28-czesc-2-glowne-podzialy-f35-w-ewangelii-mateusza.md:138`.
- Źródło: s. 173 / PDF 181. EN: samodzielny, podkreślony nagłówek „PATTERNS” nad zestawieniem kombinacji.
- PL: od razu tabela `| 1 | 2 | 3 | 4 | 5 | ...`, bez tytułu.
- Kierunek: przywrócić podkreślony tytuł „WZORCE” nad tabelą; dodane opisowe nagłówki kolumn mogą pozostać.

### P2-006 — treść: `did not appreciate` jako „nie doceniał”

- Miejsce: `chapters/27-czesc-2-najlepszy-kompletny-nowy-testament-jaki-dotad-widzialem.md:57`, komentarz do Dz 18,17.
- Źródło: s. 166 / PDF 174. EN „did not appreciate the interruption”; PL „nie doceniał zakłócenia”.
- Problem: idiom wyraża niezadowolenie z przeszkadzania, a polski przekład sugeruje niedocenienie znaczenia zakłócenia.
- Kierunek: „nie był zadowolony, że mu przerwano” / „nie podobało mu się to zakłócenie”.

### P2-007 — forma: nadmiarowa kursywa w pozycji 48

- Miejsce: `chapters/27-czesc-2-najlepszy-kompletny-nowy-testament-jaki-dotad-widzialem.md:123`.
- Źródło: s. 169 / PDF 177. W pozycji 48 `μεγαν || 1 τον` nie ma kursywy, w odróżnieniu od otaczających pozycji (potwierdza XML).
- PL: `*μεγαν*` oraz `*τον*`.
- Kierunek: dla ścisłej zgodności formy usunąć tylko te dodatkowe kursywy. Niska waga; nie wpływa na odczyt.

### P2-008 — forma: urwane podkreślenie i brak podkreślenia „co najmniej”

- Miejsce: `chapters/26-czesc-2-niewiarygodnie-staranny-przekaz.md:65`.
- Źródło: s. 159 / PDF 167, sprawdzone wizualnie. Podkreślone jest EN „at least” oraz cały kursywny ciąg od „The implications of finding…” do „the creation of that text”.
- PL: „co najmniej” bez wyróżnienia; podkreślenie urywa się po „Wszystkie”, wraca dopiero przy „powstania tego tekstu”.
- Kierunek: przywrócić podkreślenie „co najmniej”; objąć nim także środek zdania „»kanony« krytyki tekstu stają się nieistotne dla każdego punktu późniejszego od”. Kursywa pozostaje na całym wyróżnionym fragmencie.

### P2-009 — forma: zmieniony zakres podkreślenia i brak bolda

- Miejsce: `chapters/26-czesc-2-niewiarygodnie-staranny-przekaz.md:128`.
- Źródło: s. 162 / PDF 170, sprawdzone wizualnie. Podkreślone są tylko EN „fact”, „incredibly careful transmission” i „all”; „all” jest również pogrubione.
- PL: podkreślono cały fragment od „niezależnie od tego” do „przez całe średniowiecze”; „wszystkie” jest tylko podkreślone.
- Kierunek: ograniczyć pierwsze podkreślenie do odpowiedników „fakt” i „niewiarygodnie staranny przekaz”, dodać pogrubienie słowu „wszystkie”.

### P2-010 — forma: pominięte podkreślenia w Postscriptum

- Miejsce: `chapters/25-czesc-2-wspolczynnik-starannosci-kopisty.md:331` i 333.
- Źródło: s. 156 / PDF 164, sprawdzone wizualnie. Podkreślone EN „text” oraz „size”, „independence”, „age”, „geographical distribution”, „profile”, „care”, „range”.
- PL: wszystkie odpowiedniki bez podkreślenia.
- Kierunek: przywrócić podkreślenie wskazanych słów i frazy. Nie podkreślać całego zdania, ponieważ źródło tego nie robi.

### P2-011 — jawność korekty źródła: zmienione dane w wierszu 2875

- Miejsce: `chapters/25-czesc-2-wspolczynnik-starannosci-kopisty.md:81`.
- Źródło: s. 142 / PDF 150, sprawdzone wizualnie. EN tabela ma `1x, 37, 2/, 1c, 5s, 1i` i lokalizację `Valopedi`.
- PL: `1x, 3y, 2/, 1c, 5s, 1i` i `Vatopedi`.
- Ocena: korekty prawdopodobnie trafnie usuwają literówki źródłowe, jednak nie są wiernym odtworzeniem wydrukowanej tabeli. Zgodnie z zasadą niepoprawiania źródła po cichu należy pozostawić odczyt źródłowy lub jawnie odnotować korektę redakcyjną (po decyzji tłumacza).

### P2-012 — terminologia: niepełne „aparat” zamiast ustalonego „aparat krytyczny”

- Miejsce: `chapters/25-czesc-2-wspolczynnik-starannosci-kopisty.md:5`, 11, 13, 173, 197.
- Źródło: m.in. s. 139–141, 148 / PDF 147–149, 156; EN `apparatus`, `full f35 apparatus`.
- PL: „w moim pełnym aparacie”, „w aparacie”, „dotyczy aparatu”.
- Kierunek: zastosować ustalone w instrukcji `apparatus → aparat krytyczny`. To kwestia konsekwencji terminologii, nie brak danych merytorycznych.

### P2-013 — treść: pominięta możliwość łącznego działania dwóch mechanizmów

- Miejsce: `chapters/25-czesc-2-wspolczynnik-starannosci-kopisty.md:260` (Rz 12,8).
- Źródło: s. 150 / PDF 158. EN „homoioarcton, and/or -teleuton”; PL „homoioarktonu lub homoioteleutonu”.
- Kierunek: zachować oba warianty relacji jako „homoioarktonu i/lub homoioteleutonu”. Niewielki szczegół, ale autor celowo dopuszcza również kombinację obu.

### P2-014 — cytat biblijny: „advantageous” zastąpione oceną właściwości

- Miejsce: `chapters/24-czesc-2-traktowanie-kr-przez-von-sodena.md:17`, Dz 6,2.
- Źródło: s. 126 / PDF 134. EN „It is not advantageous that we should forsake the Word of God to serve at tables”.
- PL „Nie jest rzeczą właściwą, żebyśmy zaniedbali Słowo Boże, aby usługiwać przy stołach”.
- Kierunek: zachować znaczenie „nie jest korzystne / nie przynosi korzyści”. „Właściwe” przesuwa wypowiedź w kierunku stosowności; instrukcja wymaga tłumaczyć dokładnie wariant przytoczony przez autora.

### P2-015 — forma: pominięte pogrubienia przy kontrolowaniu i niemożliwości rewizji

- Miejsce: `chapters/24-czesc-2-traktowanie-kr-przez-von-sodena.md:31`, 112.
- Źródło: s. 128 / PDF 136: w `controller` i `controlling` końcówki `er` i `ing` są jednocześnie pogrubione i podkreślone; s. 135 / PDF 143: `cannot` jest pogrubione i podkreślone. Obie strony obejrzane.
- PL: `[kontrolera]{.underline}`, `[kontrolowania]{.underline}`, `[nie może]{.underline}`, bez pogrubień.
- Kierunek: „nie może” oddać także pogrubieniem. Przy parze kontroler/kontrolowanie odtworzyć wyróżnienie znaczącej różnicy końcówek w sposób zrozumiały po polsku; obecnie znika bold i zmienia się zakres podkreślenia.

### P2-016 — oznaczenie krytycznotekstowe: znormalizowana wielkość litery

- Miejsce: `chapters/24-czesc-2-traktowanie-kr-przez-von-sodena.md:112`, „(**K^x^** Sodena)”.
- Źródło: s. 135 / PDF 143, w tym jednym wystąpieniu jest małe, pogrubione `k` z górnym `x`, choć dalej na stronie występuje `K^x^`.
- Kierunek: ponieważ instrukcja każe zachować dokładne oznaczenia, nie normalizować po cichu, ewentualnie uznać za literówkę źródłową i jawnie zaznaczyć decyzję redakcyjną. Niska waga.

### P2-017 — forma i dane aparatu: dodatkowy separator wariantu w Dz12:25

- Miejsce: `chapters/22-czesc-2-profil-rodziny-35-w-dziejach-apostolskich.md:84`.
- Źródło: s. 112 / PDF 120, potwierdzone wizualnie. Po `[60%]` stoją cztery pary pionowych kresek `||` (dwie w pierwszym wierszu i dwie w następnym). W całej pozycji jest pięć separatorów.
- PL: po `[60%]` pięć par, czyli sześć separatorów w pozycji.
- Kierunek: usunąć dodatkowy separator, chyba że tłumacz świadomie koryguje źródło — wówczas należy to jawnie odnotować. Nie uzupełniać aparatu samodzielnie na podstawie liczby wariantów wymienionej w przypisie.

### P2-018 — forma: podkreślenie bez źródłowego pogrubienia słowa „tekst”

- Miejsca: `chapters/22-czesc-2-profil-rodziny-35-w-dziejach-apostolskich.md:220`; `chapters/23-czesc-2-precz-z-kaczkami-dziennikarskimi.md:63` i 69.
- Źródło: s. 115 / PDF 123 oraz s. 120 / PDF 128, obejrzane. W trzech miejscach EN `text` jest jednocześnie pogrubione i podkreślone.
- PL: `[tekst]{.underline}`, bez pogrubienia.
- Kierunek: zachować oba wyróżnienia na samym słowie „tekst”, nie rozszerzać ich na resztę zdania.

### P2-019 — treść: „około 300 grup” zmienione na „ponad 300 grup/manuskryptów”

- Miejsce: `chapters/23-czesc-2-precz-z-kaczkami-dziennikarskimi.md:57`.
- Źródło: s. 119 / PDF 127: `the remaining 300+/- groups`.
- PL: „pozostałych 300+ grup/manuskryptów”.
- Problem: `+/-` oznaczające przybliżenie zastąpiono `+` sugerującym dolną granicę; autor w tym miejscu mówi tylko o grupach, nie alternatywnie o manuskryptach.
- Kierunek: „pozostałych około 300 grup”.

### P2-020 — forma: różnice wyróżnień w „Precz z kaczkami…”

- Miejsce: `chapters/23-czesc-2-precz-z-kaczkami-dziennikarskimi.md`.
- W. 3: źródłowe `Kr/M7` i `Kr` w cytatach profesorów (s. 115–116 / PDF 123–124) są zwykłą czcionką, PL dodaje bold. W. 112: końcowe zdanie WERSALIKAMI (s. 123–124 / PDF 131–132) w źródle nie jest pogrubione, PL dodaje bold. W. 110: źródłowe `Selah` jest zwykłą czcionką, PL dodaje kursywę.
- W. 25/42/75: pominięto podkreślenia nagłówków kolumn trzech tabel (`group/size/coherence` oraz `MS/Location/Content`), s. 118–119,121 / PDF 126–127,129. Markdown domyślnie pogrubiający nagłówki tabel nie odtwarza ich podkreślenia.
- W. 15: w źródłowym `the archetypal form` (s. 117 / PDF 125) podkreślono `the`. W PL nie ma śladu tego nacisku na określoną/jedyną formę. Uzgodnić, jak oddać nacisk po polsku, bez mechanicznego podkreślania całej frazy ani dodawania argumentu.
- Niska waga z wyjątkiem nacisku w argumentacji. Oględziny wszystkich wymienionych stron wykonano.

### P2-021 — treść: imiesłów po zaprzeczeniu może odwracać sens

- Miejsce: `chapters/23-czesc-2-precz-z-kaczkami-dziennikarskimi.md:124`, przypis `robinson-sprawdzil-okolo-1650-pa`.
- Źródło: s. 117 / PDF 125: `Robinson has yet to publish his collations, thus making them available to the public at large`.
- PL: „Robinson nie opublikował dotąd swoich kolacjonowań, udostępniając je tym samym ogółowi”.
- Problem: polski imiesłów sugeruje, że nieopublikowanie udostępniło kolacjonowania. Autor mówi o udostępnieniu, które nastąpiłoby poprzez publikację, wciąż oczekiwaną.
- Kierunek: „Robinson nie opublikował jeszcze swoich kolacjonowań i tym samym nie udostępnił ich ogółowi” albo równoważne zdanie zachowujące tę relację.

### P2-022 — forma: utracone indeksy górne określające wystąpienie słowa

- Miejsce: `chapters/17-czesc-2-profil-rodziny-35-dla-calego-nowego-testamentu.md:503`, 583, 602, 630, 832.
- Źródło: Dz22:20 `και⁴` (s. 76 / PDF 84), 1Kor6:11 i 2Kor7:11 `αλλ¹`, Flp2:1 `τι²` (s. 78 / PDF 86), Obj13:15 `ινα²` (s. 82 / PDF 90), wszystkie obejrzane.
- PL: `και4`, `αλλ1`, `αλλ1`, `τι2`, `ινα2`, cyfry w linii tekstu. W 2 Tm 3,14 poprawnie zachowano `οις^2^`, więc zapis jest też wewnętrznie niespójny.
- Kierunek: zapisać odpowiednio `και^4^`, `αλλ^1^`, `τι^2^`, `ινα^2^`. Cyfry są elementem aparatu, nie częścią greckiego słowa.

### P2-023 — drobne fragmenty pozostawione po angielsku

- Miejsce: `chapters/17-czesc-2-profil-rodziny-35-dla-calego-nowego-testamentu.md:36` oraz 690.
- Źródło: Mt10:19, s. 67 / PDF 75, `(1st)`; Hbr11:20, s. 79 / PDF 87, `(also 12:16)`.
- PL zachowuje `(1^st^)` i `(also 12:16)`.
- Kierunek: „(pierwsze wystąpienie)” / „(1.)” oraz „(także 12:16)”, zachowując powiązanie z danym odczytem.

### P2-024 — forma: podkreślenia zamienione na pogrubienia w profilach

- Miejsce: `chapters/17-czesc-2-profil-rodziny-35-dla-calego-nowego-testamentu.md`, wszystkie etykiety „Klucz” i nazwy ksiąg/grup wprowadzające tabele (wiersze 3,15,112,126,196,208,286,298,346,359,544,558,695,707,778,790,859,873); ponadto 885.
- Źródło: s. 66–83 / PDF 74–91. Etykiety i nazwy są podkreślone, nie pogrubione. `attention please` (s. 83 / PDF 91) również podkreślone, PL „proszę o uwagę” pogrubione.
- Kierunek: dla ścisłej zgodności przywrócić podkreślenia zamiast bolda. Pozostawić rzeczywiste źródłowe pogrubienia „Łącznie: 658”, „Rodzina 35” i „wszystkie” w zakończeniu.
- Analogicznie `chapters/22-czesc-2-profil-rodziny-35-w-dziejach-apostolskich.md:5` i 190: `Acts` oraz `Key` są podkreślone w źródle, bez bolda (s. 110,114 / PDF 118,122). W. 200 PL dodaje bold do „Łącznie: 180”, w. 204 do „Łączna liczba wystąpień każdego świadka”; w źródle obie etykiety są zwykłą czcionką. Ponadto w. 202 PL pogrubia **K^x^**, chociaż źródło w tym wystąpieniu ma zwykłe `K^x^`.
- W 17:90,96,108,657 źródłowe `pt` w `f35pt` jest niepogrubione przy pogrubionym `f35`, a w. 327 (J12:6) całe oznaczenie jest niepogrubione. PL wszystkie pięć oznaczeń pogrubia w całości. Ściśle odtworzyć zakres bolda, zachowując wszystkie indeksy.

### P2-025 — forma: brak i nadmiar podkreślenia w pytaniu o Autograf

- Miejsce: `chapters/30-czesc-2-czy-archetypalny-tekst-f35-jest-autografem.md:3` i 5.
- Źródło: s. 181–182 / PDF 189–190, obejrzane. W pierwszym akapicie podkreślono `text` w zdaniu `the text of f35 is ancient and independent`; w następnym akapicie tylko `text` w `the f35 text is ancient (also independent)`.
- PL: w. 3 „tekst” bez podkreślenia; w. 5 podkreślono także „jest starożytny (a także niezależny)”.
- Kierunek: dodać podkreślenie „tekst” w. 3, usunąć nadmiarowe podkreślenie dalszej frazy w. 5. Podkreślenia listy cech w. 7 i obiektywnego autorytetu w. 13 są zgodne; 29:81 poprawnie podkreśla tylko „rzeczywistym”.

### P2-026 — forma: dalsze brakujące lub zbyt szerokie podkreślenia u von Sodena

- Miejsce: `chapters/24-czesc-2-traktowanie-kr-przez-von-sodena.md:5`, 15, 55, 88.
- W. 5: źródło s. 124 / PDF 132 podkreśla tylko `All`, PL całe zdanie „Wszystkie manuskrypty … pochodziły ze Wschodu”. Ograniczyć podkreślenie do „Wszystkie”.
- W. 15: źródło s. 126 / PDF 134 podkreśla `After` w cytacie Dz 13,15; PL „Po” jest bez podkreślenia.
- W. 55: źródło s. 131 / PDF 139 podkreśla `omit` w komórce M⁷, zestaw 03. PL „pominięcie” jest bez podkreślenia.
- W. 88: źródło s. 132 / PDF 140 podkreśla tylko `not one single time`; PL obejmuje też „nie łączą się przeciwko **7**”. Ograniczyć wyróżnienie do polskiego odpowiednika wyrażenia częstotliwości: „ani jeden jedyny raz”. Wszystkie strony potwierdzono wizualnie.

### P2-027 — forma: dalsze pominięcia podkreśleń we „Współczynniku staranności kopisty”

- Miejsce: `chapters/25-czesc-2-wspolczynnik-starannosci-kopisty.md`.
- W. 13: brak podkreślenia „w jednym rozdziale” w pytaniu o 34 odstępstwa; źródło s. 141 / PDF 149 podkreśla `in one chapter` właśnie w tym drugim wystąpieniu, po cyfrze 34.
- W. 28 i 203: oba tytuły tabel „f³⁵ … — dane surowe” są w źródle kursywne i podkreślone (s. 141,149 / PDF 149,157); PL zachowuje kursywę, ale nie podkreślenie.
- W. 127: brak podkreślenia całego zdania od „Na przestrzeni stuleci przekazu” do „zamierzone znaczenie Autografu” (s. 144 / PDF 152). Powtórzenie tego zdania w. 275 ma poprawne podkreślenie.
- W. 133: brak podkreślenia „dla nas” oraz „dla was (lm.)” w omawianym cytacie (s. 145 / PDF 153).
- W. 155: źródło podkreśla `for the whole book of Mark` (s. 147 / PDF 155). PL wyłącza „w całej” z podkreślenia; objąć nim także te słowa.
- W. 189, przypis: brak podkreślenia „jednym” w „w jednym!”; źródło s. 147 / PDF 155 podkreśla samo `one`.
- W. 245: brak podkreślenia całego zdania od „Zauważ, że zdecydowanie najgorszy” do „Kodeksu Alef” (s. 150 / PDF 158).
- Wszystkie wymienione strony obejrzano. Podkreślenie „współczynnika staranności kopisty” w. 315 jest zgodne; Postscriptum omówiono osobno w P2-010.

### P2-028 — forma: trzy brakujące podkreślenia w „Niewiarygodnie starannym przekazie”

- Miejsce: `chapters/26-czesc-2-niewiarygodnie-staranny-przekaz.md:67`, 126, 144.
- W. 67: źródło s. 159 / PDF 167 podkreśla `far` w `far better job`; PL „znacznie” bez podkreślenia.
- W. 126: źródło s. 161 / PDF 169 podkreśla `fact`; PL „faktu” bez podkreślenia.
- W. 144, przypis: źródło na tej samej stronie podkreśla tylko `all` w `all the books`; PL „wszystkich” bez podkreślenia.
- Przywrócić wyróżnienia wyłącznie wskazanych słów; strony obejrzano. Pozostałe rozbieżności podkreśleń rozdziału są w P2-008 i P2-009.

### P2-029 — treść: `valid variant` jako „ważny wariant”

- Miejsce: `chapters/25-czesc-2-wspolczynnik-starannosci-kopisty.md:139`, komentarz do trzeciego wariantu manuskryptu 789 (Mk 16,9).
- Źródło: s. 145 / PDF 153: `In any case, it is not a valid variant`.
- PL: „W każdym razie nie jest to ważny wariant”.
- Problem: w kontekście autor kwestionuje zakwalifikowanie oczywistego błędu jako rzeczywistego wariantu, nie tylko jego znaczenie lub doniosłość. „Ważny” zwykle sugeruje tutaj ocenę istotności, inaczej niż pobliskie „właściwy wariant”.
- Kierunek: „nie jest to prawidłowy wariant” lub równoważne sformułowanie zachowujące zakwestionowanie jego zasadności jako wariantu.

### P2-030 — forma: pominięte etykiety legend

- Miejsca: `chapters/25-czesc-2-wspolczynnik-starannosci-kopisty.md:15`, `chapters/26-czesc-2-niewiarygodnie-staranny-przekaz.md:44`, `chapters/29-czesc-2-boskie-zachowanie-oryginalnych-sformulowan-listow-ogolnych.md:15`.
- Źródło: odpowiednio s. 141,157,177 / PDF 149,165,185, wszystkie obejrzane. Przed objaśnieniami symboli stoi podkreślone `Key`.
- PL: od razu tabelki z kolumnami „Symbol” i „Znaczenie”, bez etykiety.
- Kierunek: dla ścisłej zgodności formy dodać podkreślony „Klucz” nad każdą legendą. Niska waga: zawartość legend zachowano.

### P2-031 — forma językowa: dwie usterki zgody gramatycznej

- `chapters/24-czesc-2-traktowanie-kr-przez-von-sodena.md:15`: „Zauważ, co mówi Dzieje Apostolskie 13,15” — uzgodnić liczbę („mówią Dzieje Apostolskie”) albo zastosować konstrukcję „co napisano w Dziejach Apostolskich”. Źródło s. 126 / PDF 134.
- `chapters/25-czesc-2-wspolczynnik-starannosci-kopisty.md:11`: „jako główni świadkowie wyłonili się sześć greckich manuskryptów” — uzgodnić konstrukcję liczebnikową, np. „sześć greckich manuskryptów wyłoniło się jako główni świadkowie”. Źródło s. 139 / PDF 147. Nie zmieniać listy sześciu świadków.

### Problemy źródła w plikach 17, 22–30 — nie poprawiać jako błędów przekładu

- Tabela 29, wiersz 664: ostatnia komórka `16x,24` (bez `/`) występuje także w źródle na s. 177 / PDF 185. Tłumaczenie wiernie ją odtwarza; ewentualną poprawkę należałoby jawnie potraktować jako korektę źródła.
- 26:65: numery 1874 i 1893 występują tak samo w źródle na s. 159 / PDF 167, choć tabele wymieniają odpowiednio 1876 i 1892. Nie traktować ich jako pomyłek tłumacza. Także `1` w wierszu 204 i `1x,1` w wierszu 1075 pierwszej tabeli są wierne źródłu (brak końcowego `/` jest już w PDF).
- 25:189: `11 × 16 = 171` jest błędem rachunkowym już w źródle, s. 147 / PDF 155 (powinno arytmetycznie być 176). Przekład wierny; nie poprawiać bez jawnego odnotowania.
- 25:268 i 301: określenia gramatyczne `Indicative/Subjunctive` i „person from plural to singular” są wiernie przetłumaczone, nawet gdy nie odpowiadają podanym greckim formom. To problem źródła, nie tłumaczenia.
- 24:142: tytuł `Grieshischen` (zamiast zwykłego `Griechischen`) pochodzi ze źródła s. 127 / PDF 135; nie jest błędem przepisania w PL.

## Pliki 31–37 — uwagi P3

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

### P3-S05 — nadmiarowy nawias zamykający już w źródle

- PL: `chapters/36-czesc-3-concordia-discors-i-odczyty-mniejszosciowe-f35-w-listach-ogolnych.md:101`, końcowe „300)”. EN druk 220 / PDF 228 kończy analogicznie „year 300.)” bez odpowiadającego nawiasu otwierającego. Nie jest to błąd tłumaczenia; ewentualna korekta wymaga decyzji redakcyjnej.

### P3-008 — forma/dane: Pandoc usuwa gwiazdki klasyfikacji manuskryptów (ważne)

- PL: `chapters/32-czesc-3-znaczenie-obiektywnych-dowodow.md:93`, wyliczenie 43 manuskryptów od „A, C, 81, 104*” do „2818*”. EN druk 188 / PDF 196.
- Gwiazdki po numerach oznaczają manuskrypty bizantyjskie, ale są zapisane jako niewyescapowane znaczniki Markdown. Pandoc interpretuje kolejne pary jako kursywę: polecenie `pandoc chapters/32-czesc-3-znaczenie-obiektywnych-dowodow.md --from=markdown-smart -t latex` zwraca m.in. `104\emph{, 436, 459}` i `467\emph{, 607, 720}`. W rezultacie znikają ważne oznaczenia danych, a fragmenty wyliczenia otrzymują przypadkową kursywę.
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

- Uzupełnienie 2026-10-12 po porównaniu drugiego raportu: `chapters/34-czesc-3-kiedy-mamy-do-czynienia-z-recenzja.md:117`, przypis `alef-wyniesiony-z-synaju`, „stał się zachowanym manuskryptem na Synaju”. EN druk 202 / PDF 210 ma `became extant in Sinai`; chodzi o pojawienie się w rozpoznanym zasobie świadków, nie o rozpoczęcie istnienia/przetrwania. Do tej samej decyzji należą także `23:124` i `33:164`, źródłowe `not yet ‘extant’` (druk 117 i 191 / PDF 125 i 199). Zachować szczególne użycie autora i uzgodnić czytelny polski odpowiednik, nie korygować po cichu jego terminologii.

### P3-T02 — terminologia: dwa powtarzające się odpowiedniki wymagające ujednolicenia z regułami

- Rozdział 36, w. 5 i rozdział 37, w. 37: *solitary evidence* w cytacie Burgona oddano jako „samotne świadectwo” (druk 215 i 235 / PDF 223 i 243), mimo ustalonego *evidence → dowód/dowody*. Rozważyć wierną składnię zachowującą przyjęty termin, nie mylić z osobnym *testimony*.
- Rozdział 36, w. 107: bibliograficzne *Catholic epistles* (druk 217 / PDF 225) oddano jako „Listy Ogólne”, identycznie jak *General Epistles*. To ten sam problem zachowania rozróżnień nazw co w innych rozdziałach, do decyzji globalnej, nie jako zarzut zmiany zawartości zbioru ksiąg.

## Pliki 38–49 — uwagi P4

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
- Druk 312, 298, 309 / PDF 320, 306, 317. W 145 zewnętrzne dopowiedzenie zamieniono zgodnie z preferencją na okrągłe, lecz pozostawiono także okrągłe w jego wnętrzu; w 157 i 199 wewnętrzne kwadratowe źródła również stały się okrągłymi.
- Do poprawy: zewnętrzne okrągłe, wewnętrzne kwadratowe, zgodnie z zasadami użytkownika.

### P4-T01 — Do decyzji terminologicznej: „not yet extant”

- Lokalizacja: `chapters/48-dodatek-czy-krytyka-tekstu-nowego-testamentu-jest-nauka.md:175,201`, „jeszcze «niezachowanych»”.
- Druk 302 i 310 / PDF 310 i 318. Autor sam umieszcza `extant` w cudzysłowie, następnie wyjaśnia: `not yet identified and catalogued`. Ma na myśli istniejące, lecz jeszcze nieodnalezione/nieskatalogowane manuskrypty.
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

### P4-S03 — Suma 44 w rozdziale 38 pochodzi z oryginału

- `chapters/38-dodatek-nagromadzone-bledy-czternastu-stuleci.md:11`, druk 261 / PDF 269: autor wymienia grupy 12, 17, 17, 15 i 12 odczytów, następnie pisze `six out of 44`.
- PL zachowuje „sześć z 44”. Wymienione liczby sumują się do 73, nie 44; tę rozbieżność zgłaszać jako problem źródła, nie błąd przekładu. Nie korygować po cichu.

### P4-S01 — „kolejnych dwanaście” przed tabelą z piętnastoma wierszami

- `chapters/40-dodatek-podgrupy-f35-w-listach-ogolnych.md:96–114`, druk 278 / PDF 286.
- Oryginał również mówi `another twelve`, choć następujący wykaz ma piętnaście wierszy (757–1899). Tłumaczenie zachowało rozbieżność wiernie. Nie „poprawiać” liczby w tekście autora bez oznaczonej uwagi redakcyjnej.

### P4-S02 — Przypis dotyczący 586 stoi przy GA 35 także w oryginale

- `chapters/44-dodatek-skolacjonowane-manuskrypty-f35.md:7,61`, druk 289 / PDF 297.
- Przypis po `GA 35 is complete` rozpoczyna się od `AG 586` i omawia wariant 586. To źródłowa niekonsekwencja, nie dowód przestawienia przypisu przez tłumacza. PL normalizuje `AG` do `GA`; tę oczywistą literówkę źródła warto odnotować poza tekstem autora, jeżeli ma być zachowana pełna dokumentacja interwencji.

## Uzupełnienie po porównaniu z drugim raportem — 2026-10-12

**Stan uzupełnienia: zakończone.** Sprawdzono wszystkie konkretne uwagi drugiego raportu i ich wystąpienia w sekcjach przekrojowych. Dodano 18 grup uwag U-001–018, jedną decyzję terminologiczną U-T01 oraz trzy noty o źródle U-S01–03. P3-T01 rozszerzono o trzy lokalizacje. Uwagi czysto językowe lub stylistyczne oznaczono jako takie; nie należy utożsamiać wszystkich nowych wpisów z błędami merytorycznymi. Nie zmieniono książki.

Porównano lokalny plik użytkownika `review-calej-ksiazki.md` (SHA-256: `db71b23f3322ccb910a5bd8c6cd679a15c629eefe8246be3e6f1bd97a4c02435`) z niniejszym raportem. Drugi raport opiera się na `b0c5bc165a97d8de32faed076f7c16b461d7ecd3`; różnica treści książki względem naszej bazy `4d35b43...` dotyczy tylko jednego fragmentu przypisu 18:81 i nie wpływa na sprawdzane zarzuty. Wejściowy plik użytkownika pozostawiono bez zmian.

Numery U oznaczają nowe, zweryfikowane ustalenia; U-S oznacza problemy lub cechy oryginału, nie błędy tłumaczenia. Uwaga obejmująca kilka lokalizacji pozostaje jedną grupą. Dawnych identyfikatorów P1–P5/G nie zmieniono.

### U-001 — Forma językowa: urwane zdanie w przedmowie

- Lokalizacja: `chapters/02-przedmowa.md:4`, „Włącznie ze stanowiskiem, że dokładne oryginalne brzmienie zostało zachowane…”.
- Źródło: druk iii / PDF 3: „This includes the position that the precise original wording has been preserved to our day and that we can know what it is.”
- Problem: zdanie EN ma orzeczenie, a polski fragment po kropce zaczyna się przyimkowym „Włącznie ze stanowiskiem…” i pozostaje bez zdania nadrzędnego. Jest to usterka składni, niezależna od odnotowanego już P1-002 problemu `original wording`.
- Kierunek: połączyć fragment z poprzednim zdaniem albo zachować pełne zdanie typu „Obejmuje to stanowisko, że…”, wraz z korektą terminu według P1-002.

### U-002 — Forma językowa: zgoda w przypisie tłumacza do podziękowań

- Lokalizacja: `chapters/03-podziekowania.md:7`: „Oryginalna okładka i formatowanie nie zostało wykorzystane…”.
- Źródło: brak odpowiednika — jawnie oznaczony przypis tłumacza do podziękowań z druku iv / PDF 4.
- Problem: podmiot szeregowy „okładka i formatowanie” wymaga liczby mnogiej orzeczenia; obecne „zostało wykorzystane” zgadza się jedynie z drugim składnikiem.
- Kierunek: „…nie zostały wykorzystane…”. To korekta językowa dodatku, nie zarzut jego obecności.

### U-003 — Treść: skamieniałość zawężona do szkieletu

- Lokalizacja: `chapters/04-czesc-1-preambula.md:23`: „kompletny szkielet dinozaura…”.
- Źródło: druk 3 / PDF 11: „a complete fossil of a dinosaur called ‘acrocanthasaurus’”.
- Problem: EN mówi o skamieniałości, nie o szkielecie. PL usuwa informację o skamienieniu i wprowadza konkretny typ znaleziska, którego to zdanie nie określa. Nie oceniamy tu prawdziwości twierdzeń autora o muzeum ani wieku znalezisk.
- Kierunek: „kompletna skamieniałość dinozaura…” (z dopasowaniem rodzaju dalszego zdania). Nie dodawać „szkieletu”, jeśli nie ma go w przytoczonym źródle.

### U-004 — Treść: utrata kierunku wnioskowania wstecz

- Lokalizacja: `chapters/08-czesc-1-historyczne-dowody.md:3`: „Musimy zacząć od tego, co zrobił”.
- Źródło: druk 14 / PDF 22: „We must work back from what He did.”
- Problem: PL zachowuje punkt wyjścia, ale pomija `back`: autor proponuje rozumowanie wstecz od dokonanych działań do sposobu zachowania Tekstu. W w. 11 ten tok jest później objaśniony, co ogranicza wagę usterki, lecz nie przywraca brakującego elementu w zdaniu wprowadzającym.
- Kierunek: wyrazić wnioskowanie wstecz, np. „Musimy wnioskować wstecz na podstawie tego, co zrobił”. P1-026 osobno opisuje brak podkreślenia odpowiednika `did`; nie liczyć go drugi raz.

### U-005 — Forma językowa: dwie dalsze konkretne usterki interpunkcyjne w pliku 05

- Lokalizacja: `chapters/05-czesc-1-wprowadzenie-natchnienie.md:13`: „między Bogiem, a Jego spisanym Objawieniem”. Źródło: druk 7 / PDF 15, „the intimate connection between God and His written Revelation”. Przecinek rozdziela dwa człony konstrukcji „między X a Y”; należy go usunąć.
- Lokalizacja: ten sam plik, w. 40: „Zwróć, proszę uwagę, że…”. Źródło: druk 10 / PDF 18, „Please note that Jesus affirms…”. Wtrącone „proszę” otwarto przecinkiem, ale go nie zamknięto. „Zwróć, proszę, uwagę, że…” albo „Zwróć proszę uwagę, że…”.
- To konkretyzacja ogólnej uwagi drugiego raportu o dodatkowych usterkach interpunkcyjnych w 05, nie nowe zmiany sensu. Nie dublować przecinków po „Słowo” i „przekazałem”, które już obejmuje P1-008.

### U-006 — Terminologia: master copy jako egzemplarz wzorcowy, nie ogólnie „oryginalny”

- PL: `chapters/09-czesc-1-historyczne-dowody-autografy.md:11,13,14`, cztery wystąpienia „oryginalny egzemplarz / oryginalnego egzemplarza”.
- EN: druk 17 / PDF 25, cztery `master copy`: „the master copy may indeed have been done on parchment”; przechowywany „for quality control” i służący sporządzaniu dalszych kopii.
- Potwierdzona jest utrata wyraźnego określenia funkcji egzemplarza wzorcowego. Kierunek: konsekwentnie „egzemplarz wzorcowy” albo „egzemplarz-matka”.
- **Zastrzeżenie do diagnozy drugiego raportu:** nie dowiedziono, że Pickering wyklucza tu tożsamość egzemplarza wzorcowego z autografem; nie pisać, że PL na pewno utożsamia dwa dokumenty, które autor jednoznacznie rozdzielił. To precyzja terminologiczna, nie potwierdzona duża zmiana argumentacji.

### U-007 — Forma: w 09 dodano listę, a w 10 oryginalna lista nie parsuje się jako lista

- `chapters/09-czesc-1-historyczne-dowody-autografy.md:11–14`, druk 17 / PDF 25: EN ma ciągły akapit „for two reasons: if …; if …”; PL przekształca dwie części zdania w listę wypunktowaną. Treść zachowana, ale układ zmieniony; przy ścisłym zachowaniu formy wrócić do prozy. Widać na obrazie całej strony 25.
- `chapters/10-czesc-1-historyczne-dowody-czy-pierwsi-chrzescijanie-byli-ostrozni.md:53–56`, druk 34–35 / PDF 42–43: oryginał rzeczywiście zawiera trzy wypunktowane tezy. PL ma trzy linie `-`, lecz bez pustego wiersza po „następujące tezy:”. `pandoc --from=markdown-smart -t native` zwraca **jeden `Para` z `SoftBreak` i literalnymi `Str "-"`**, nie `BulletList`. Dodać pustą linię przed pierwszym punktem i sprawdzić eksport. To rzeczywisty problem parsowania, a nie tylko reguła estetyczna Markdownu. Obie strony źródła obejrzane.

### U-008 — Ustalone odpowiedniki pominięte w pierwszym raporcie: line of transmission i NT

- `chapters/14-czesc-1-historyczne-dowody-jakie-sa-rzeczywiste-dowody.md:42`, druk 58 / PDF 66: EN „the lines of transmission remained separate”, PL „linie transmisji pozostawały odrębne”. Zachować „linie przekazu”. Nie narzucać tej zamiany sąsiedniemu `textual transmission` → „transmisja tekstowa”, bo to inna konstrukcja.
- `chapters/15-czesc-1-uwagi-koncowe.md:11`, druk 60 / PDF 68: EN „resulted in lines of transmission”, PL „doprowadził do powstania linii przekazywania”. Ustalone „linii przekazu”.
- `chapters/16-czesc-2-czym-wlasciwie-jest-rodzina-35.md:1`, druk 63 / PDF 71: EN `The Best Line of Transmission`, PL `Najlepsza linia przekazywania`. Ustalone „Najlepsza linia przekazu”.
- `chapters/09-czesc-1-historyczne-dowody-autografy.md:32`, jawny dodatek tłumacza w przypisie `kolofony-datuja-wydanie`: „greckich rękopisów NT”, „każdej księgi NT” oraz „linię transmisji”. Naruszają własną konwencję projektu: „Nowego Testamentu” i „linię przekazu”. Cytowaną angielską nazwę „Family 35 NT” rozpatrywać osobno jako nazwę, nie mechanicznie przerabiać. Sam dodatek i jego adresy nie są przez to błędem przekładu Pickeringa.

### U-009 — Terminologia: variant reading / variation w rozdziale 12

- PL `chapters/12-czesc-1-historyczne-dowody-czy-przekazywanie-przebiegalo-normalnie.md:39`, druk 47 / PDF 55: „zastępuje jeden wariant odczytu innym … występowały wariacje”. EN „replacing one variant reading by another … there was variation at these points”.
- Pierwszy człon ma ustalony odpowiednik „jeden wariantowy odczyt innym”. Końcowe `variation` opisuje zróżnicowanie tekstu w tych miejscach; „wariacje” jest nietrafne w tym technicznym kontekście. Kierunek: „w tych miejscach istniało już zróżnicowanie” lub równie precyzyjna konstrukcja, nie zastępować automatycznie każdego `variation` rzeczownikiem `variant reading`.
- Ten sam ustalony termin w `12:65`, druk 45 / PDF 53: EN `a great many variant readings`, PL „bardzo wiele wariantów odczytów”; kierunek „bardzo wiele wariantowych odczytów”. P1-048 dotyczy innej, późniejszej części tego przypisu, więc może zostać uzupełniony lub dostać odsyłacz.

### U-010 — Drobne usterki językowe w obu plikach 09, dotąd nienotowane

`chapters/09-czesc-1-historyczne-dowody-autografy.md`:

- w. 7: „na samym na terytorium żydowskim” → „na samym terytorium żydowskim”; druk 16 / PDF 24, EN `just in the Jewish territory`.
- w. 40: „stał by się” → „stałby się”; druk 18 / PDF 26, EN `would doubtless have become`.
- w. 36, oznaczony przypis tłumacza: „ponieważ charakteryzowały się tam znaczące interakcje” jest niegramatyczne. Np. „ponieważ zachodziły tam znaczące interakcje”. Uwaga wyłącznie do języka dodatku, bez orzekania o historycznej prawdziwości dopisku.

`chapters/09-czesc-1-historyczne-dowody-wczesne-rozpoznanie.md`:

- w. 37: „wybrane księgi … (i obejmujących co najmniej pięciu różnych autorów)” → uzgodnić imiesłów z księgami, np. „obejmujące”; druk 24 / PDF 32, EN `a selection of New Testament books … (and involving at least five different authors)`.
- w. 45: aktualne „Siedem listów … zawierają” → **„Siedem listów … zawiera”**; druk 25 / PDF 33, EN `The seven letters … contain`. Drugi raport mówi odwrotnie i błędnie żąda liczby mnogiej; zweryfikowane ustalenie wymaga odwrócenia jego wskazówki.
- w. 45: „trochę hiperbola” → np. „to nieco hiperboliczne”; to samo EN `a bit of hyperbole`. Nie zmieniać przy okazji stopnia oceny autora.
- w. 55: „z możliwymi aluzjami do … List Judy i Objawienie Jana” → „Listu Judy i Objawienia Jana”; druk 26 / PDF 34, EN `with possible allusions to 2 Peter, Jude, and Revelation`.
- w. 75: podwójna spacja w „on  Ewangelię”; druk 28 / PDF 36.
- w. 79: „są mniej więcej równe pod względem objętości do dzieł” → poprawna rekcja, np. „mają mniej więcej taką samą objętość jak dzieła …”. Wtrącenie „jego główne dzieło … napisane około 185 r.” wymaga czytelnego składniowego oddzielenia od podmiotu. Druk 28 / PDF 36, EN `The surviving writings …, his major work … being written about 185, are about equal in volume to those of all the preceding Fathers put together`.
- w. 81: „trzy kościoły, tych z Lyonu, Azji Mniejszej i Rzymu” → np. „trzy kościoły: w Lyonie, Azji Mniejszej i Rzymie”; druk 28 / PDF 36, EN `three churches at least, those of Lyons, Asia Minor, and Rome`. Status cytatu już P1-023, ale nie opisywał on błędu składni.

### U-011 — Drobna korekta językowa w 11–14, dotąd nienotowana

- `chapters/11-czesc-1-historyczne-dowody-kto-mial-najlepsze kwalifikacje.md:11`, druk 36 / PDF 44: „dla List Judy” → „dla Listu Judy”; „a być może, że aż siedem” → „a być może aż siedem” (EN `possibly up to seven`).
- Tamże: zdania „Ewangelia Mateusza i List Jakuba albo przez Azję Mniejszą, albo Palestynę. List do Hebrajczyków przez Rzym lub Palestynę…” są urwanymi kontynuacjami orzeczenia wcześniejszego zdania. **Źródło też stosuje elipsę, lecz w jednym zdaniu rozdzielonym średnikami** (`Matthew and James by either Asia Minor or Palestine; Hebrews by Rome or Palestine`). Kierunek: zachować logiczne połączenie z „były … przechowywane” albo jawnie powtórzyć orzeczenie po kropce; nie dodawać nowego twierdzenia.
- `chapters/12-czesc-1-historyczne-dowody-czy-przekazywanie-przebiegalo-normalnie.md:3`, druk 42 / PDF 50: „Konstantyn zaprowadził ulgę” jest niezręczną kalką `Constantine started relief`. Kierunek „Konstantyn zaczął przynosić ulgę [prześladowanym]” lub podobnie, bez dopisywania definitywnego **końca wszystkich** prześladowań (drugi raport sugeruje również „kres”, co może być zbyt mocne).
- `12:17`, druk 44 / PDF 52: „aby nadać znaczenia” → „aby nadać znaczenie”; EN `to give currency to an aberrant text form` dotyczy nadania zasięgu/obiegu danej formie, więc przy poprawie warto oddać „upowszechnić odbiegającą od normy formę tekstu”, a nie jedynie znaczenie/prestiż. To także precyzja sensu `currency`.
- `chapters/13-czesc-1-historyczne-dowody-strumien-przekazywania.md:14`, druk 51 / PDF 59: „dominujące strumień przekazu” → „dominujący strumień przekazu”; EN `the dominant stream of transmission`.
- `13:71`, druk 53 / PDF 61: „Musiało to jednak być wczesna zmiana” → „Musiała to jednak być wczesna zmiana”; EN `it must have been an early development`.
- `chapters/14-czesc-1-historyczne-dowody-jakie-sa-rzeczywiste-dowody.md:5`, druk 56 / PDF 64: „Do XI wieku pismo kursywne zdominowało” nie domyka składni; EN `By the 11th century the cursive script had taken over`. Np. „Do XI wieku pismo kursywne zaczęło dominować”. P1-041 dotyczy innego zdania w tym akapicie.
- `14:11`, druk 56 / PDF 64: „wersetów(są” → „wersetów (są”.
- `14:13`, druk 56 / PDF 64: „kolejne 37 zawierają” → „kolejne 37 zawiera”.
- `14:31`, druk 57 / PDF 65: „byzantyjskiego” → „bizantyjskiego”.

### U-012 — Nawiasy: zwykłe wtrącenie źródłowe pozostawione w kwadratowych

- PL `chapters/12-czesc-1-historyczne-dowody-czy-przekazywanie-przebiegalo-normalnie.md:37`, druk 47 / PDF 55: `[ok. 200 r. n.e.]`; EN `[AD 200]`. Wokół całej wypowiedzi nie ma nadrzędnego nawiasu okrągłego, więc według konwencji projektu powinno być `(ok. 200 r. n.e.)`. Nie zgubiono treści.
- Dla kontrastu `12:70`, `[wiosna 1979]`, jest **wewnątrz** okrągłego nawiasu bibliograficznego i spełnia regułę zagnieżdżania. Nie obejmować go automatyczną zamianą.

### U-013 — Treść: zakres sprawdzenia Hoskiera zamieniony na przyczynę

- Lokalizacja: `chapters/44-dodatek-skolacjonowane-manuskrypty-f35.md:53`, druk 291 / PDF 299.
- EN: `I have not checked Hoskier’s collation of other MSS, in this connection.` PL: „W związku z tym nie sprawdziłem kolacjonowania innych manuskryptów dokonanego przez Hoskiera”.
- Końcowe `in this connection` ogranicza zakres zastrzeżenia do rozpatrywanej kwestii kompletności/doskonałości kopii i jej wzorca. Polskie „W związku z tym” na początku zdania sugeruje skutek wcześniejszych ustaleń.
- Kierunek: „Nie sprawdziłem pod tym względem kolacjonowania innych manuskryptów dokonanego przez Hoskiera”. Nie rozszerzać zastrzeżenia do twierdzenia, że autor w ogóle nie sprawdzał prac Hoskiera.

### U-014 — 18:31: „wersy” zamiast wierszy prozy

- `chapters/18-czesc-2-epistemologia.md:31`: „poniższe wersy odnoszą się wyłącznie…”. EN druk 87 / PDF 95: `the lines that follow refer exclusively…`, następnie proza i cztery numerowane przesłanki, nie poezja.
- Drobna usterka leksykalna: wers to jednostka utworu wierszowanego, tutaj chodzi o poniższe wiersze/fragment wywodu. Kierunek: „poniższe wiersze” albo „poniższy wywód”, bez zmiany argumentacji. Nie traktować jako opuszczenia treści.

### U-015 — 19:15: niejednoznaczna granica po numerze manuskryptu 35

- `chapters/19-czesc-2-datowanie-kr-ponownie-rozwazone.md:15`: „Oprócz świadectwa 35 kolacjonowania Robinsona wykazują…”.
- EN druk 91 / PDF 99: `Besides the witness of 35, Robinson’s collations demonstrate…`.
- Źródło rozdziela świadectwo manuskryptu 35 od kolacjonowań Robinsona. Polski ciąg może zostać odczytany jako liczba kolacjonowań, a nie numer świadka (drugi raport sam streszcza go nieprecyzyjnie jako „35 kolacjonowań”). Kierunek minimalny: „Oprócz świadectwa manuskryptu 35 kolacjonowania Robinsona wykazują…” lub przestawienie zdania tak, by numer nie zlewał się z następnym podmiotem. To uściślenie składni, nie nowy dowód.

### U-016 — 20:98: „umniejsza jej wiarygodności”

- `chapters/20-czesc-2-o-wzorcu-i-zaleznosci.md:98`: „pięć podgrup wraz z dalszym wewnętrznym pomieszaniem umniejsza jej wiarygodności jako linii przekazu”.
- EN druk 104 / PDF 112: `the five subgroups, plus further internal confusion, detract from its credibility as a line of transmission`.
- Błąd rekcji w polskim zdaniu twierdzącym: „umniejsza jej wiarygodność” albo „ujmuje jej wiarygodności”. Zachować podmiot i przyczynę, bez przerabiania dowodu autora. Rekcję z biernikiem potwierdzają połączenia w [WSJP PAN](https://wsjp.pl/haslo/podglad/73546/umniejszac).

### U-017 — 25:137: wadliwa polska składnia, ale NIE znaczenie przypisane jej przez drugi raport

- `chapters/25-czesc-2-wspolczynnik-starannosci-kopisty.md:137`: „Pierwszy jest jawnym nonsensem, niezależnymi przypadkami itacyzmu”.
- EN druk 145 / PDF 153 (sprawdzono także obraz): `The first one is manifest nonsense, independent instances of itacism.`
- Usterka polska jest rzeczywista: zdanie utożsamia singularny „pierwszy” z mnogimi „przypadkami”. Możliwy kierunek: „Pierwszy jest jawnym nonsensem — chodzi o niezależne przypadki itacyzmu”.
- **Nie przyjmować sugestii drugiego raportu, że „pierwszy przypadek jest nonsensem, natomiast pozostałe to niezależne przypadki itacyzmu”.** W angielskim nie ma „pozostałych”; omawiane są dwa miejsca (Mk 2,23 i 15,46), a pierwszy odczyt ma świadków 1251, 2554, 2765. Liczba mnoga `instances` odpowiada niezależnym wystąpieniom pierwszego błędu, nie przenosi komentarza na drugi wariant. Drugi autor odrębnie nazywa podziałem w rodzinie.
- Proponowana przez drugi raport „naprawa sensu” wprowadziłaby więc nowe zniekształcenie. Przydatna jest tylko uwaga o składni.

### U-018 — 34:95 i 237: niezgrabna elipsa z przysłówkiem „znacznie”

- `chapters/34-czesc-3-kiedy-mamy-do-czynienia-z-recenzja.md:95,237`: „Pozostałe manuskrypty bizantyjskie są wszystkie odmienne, niektóre naprawdę znacznie”.
- EN druk 203 i 207 / PDF 211 i 215: `The rest of the Byzantine MSS are all distinct, some really so`.
- Sugestia lekkiej korekty językowej, nie błąd danych ani sensu: odmienność zachowano, lecz „znacznie” wymaga tutaj domyślnego „różnią się”, a nie poprzedniego „są odmienne”. Kierunek: „wszystkie się różnią, niektóre naprawdę znacznie” lub odpowiednik zachowujący nacisk autora. Nie oceniać jako utraty argumentacji.

### U-T01 — Do decyzji: konsekwencja odpowiednika „singular reading”

- Potwierdzone odmienne odpowiedniki tego samego technicznego terminu: `11:23` „257 innych odczytów pojedynczych” (druk 38 / PDF 46), `13:40` „rygorystycznie wyeliminować odczyt pojedynczy” (druk 51 / PDF 59); w `20:5` „odczyt «singularny»” z definicją (druk 98 / PDF 106), a w `25:17` „odczyt singularny” w kluczu tabeli (druk 141 / PDF 149). Dalsze rozdziały używają „singularny”.
- Nie jest zasadne twierdzenie, że sam rozdział 25 błędnie miesza termin z „liczbą pojedynczą”: gramatyczne singular/plural to inne użycie (np. `25:173,301`). Nie wykonywać globalnej podmiany słowa „pojedynczy”.
- Uzgodnić konsekwentny odpowiednik dla `singular reading`, bez przedstawiania którejś z dwóch form jako zabronionej przez AGENTS (AGENTS nie ustala jej).

### U-S01 — Problem źródła: 1847 w dwóch rangach

- Lokalizacja: `chapters/41-dodatek-ranking-wariantowy-manuskryptow-zawierajacych-list-judy.md:13,35`, druk 281–282 / PDF 289–290; obie strony potwierdzone wizualnie.
- Manuskrypt `1847` jest w wierszach 29 oraz 4 wariantów także w oryginale. To niespójność źródła, nie powielenie wprowadzone w polskiej tabeli. Nie usuwać pozycji bez osobnej decyzji.
- Tabela ma 514 wpisów i 513 odrębnych oznaczeń. W takim zliczeniu trzeba zachować `205` i `205^abs^` jako odrębne sigla, a także odróżniać papirusy od minuskułów; samo wyciągnięcie cyfr daje mylący wynik.

### U-S02 — Cecha źródła: kolejność 2673, 2669

- Lokalizacja: `chapters/45-dodatek-bizantyjskie-manuskrypty-kr-rodziny-35.md:5`, druk 292 / PDF 300; potwierdzono na obrazie.
- Kolejność `2658, 2673, 2669, 2704` występuje również w EN. Odstępstwo od porządku rosnącego nie jest błędem przepisywania w PL. Lista ma 364 odrębne numery.
- Nie wymaga korekty przekładu. Zachowano tę uwagę osobno, aby przy późniejszej pracy nie „naprawić” po cichu danych autora.

### U-S03 — Zgodność źródłowa: wyprzedzające odwołanie do 1 Listu Jana

- `chapters/36-czesc-3-concordia-discors-i-odczyty-mniejszosciowe-f35-w-listach-ogolnych.md:288`: „Podobnie jak w Liście Jakuba, 1 Liście Piotra i 1 Liście Jana…”, po czym w. 290 dopiero rozpoczyna sekcję o 1 Liście Jana.
- EN druk 228 / PDF 236, obejrzana cała strona: identyczne `As in James, 1 Peter and 1 John…`, a bezpośrednio dalej nagłówek `1 John`.
- Jest to wyprzedzające odwołanie w układzie tego rozdziału, **nie** dowód pominięcia lub przestawienia polskiego tekstu. Sam brak słowa „powyżej” sprawia, że nie musi być błędem autora; w poprzednich rozdziałach 1 List Jana był już omawiany. Nie korygować nazw ksiąg ani kolejności.

### Duplikaty — bez ponownego numerowania

Przeanalizowano wszystkie sekcje drugiego raportu, także listę najważniejszych poprawek i uwagi przekrojowe. Powtarzające się tam zarzuty potraktowano łącznie. Poniższa mapa wskazuje najważniejsze ustalenia, które już były w niniejszym raporcie:

| Uwaga drugiego raportu | Wcześniejsze ustalenie |
| --- | --- |
| Literówki w 01 i różnica licencji | G-002, G-S01 |
| `original wording`, `cline`, `one thing` | P1-002, P1-005, P1-006 |
| Cytaty 05: przecinki, `Its nature`, numer 25, „chciałaby” | P1-008–010, P1-016 |
| Nazwy Objawienia Jana, Justin i literówki nazwy | P1-015, P1-020, P1-033, P1-045 |
| `sat under his ministry`, `initial draft`, cytat Barnaby | P1-018, P1-019, P1-022 |
| Dz 21 zamiast 20 oraz „Listy Łukasza i Pawła” | P1-028 |
| „słyszą słów”, „nie zwróci szczególną uwagę”, `collated` w 11 | P1-033 |
| Kursywa bibliografii 11, kierunek prawdopodobieństwa 12, samotne `3` | P1-034, P1-031, P1-035 |
| `cursive/minuscule`, `recension`, błędny dopisek o P45/W i P75/B | P1-038–040 |
| „griesh”, terminologia i literówki w 14–16, zagnieżdżone nawiasy 15 | P1-042, P1-045, P1-049 |
| Platinga | P5-S01 — usterka już w źródle |
| `valid variant` oraz `did not appreciate` u Galliona | P2-029, P2-006 |
| Numery 1874/1893 vs 1876/1892 oraz `16x,24` | „Problemy źródła w plikach 17, 22–30” |
| Cztery diagnostyczne pary gwiazdek w 33 i nawias w 36 | P3-002, P3-003, P3-S05 |
| „Dwanaście” przed 15 wierszami w 40 oraz AG/GA 586 w 44 | P4-S01, P4-S02 |

### Sugestie odrzucone albo wymagające innej diagnozy

Ta sekcja dokumentuje wynik weryfikacji, **nie dodaje poniższych zarzutów do listy błędów przekładu**.

| Sugestia / zakres | Wynik sprawdzenia |
| --- | --- |
| Usunąć rozbudowaną warstwę przypisów i ilustracji tłumacza | Sama obecność jawnie oznaczonych dodatków, których konwencję objaśnia 01, nie jest dowodem błędu. Oceniać konkretne dopiski. Nie przejęto zbiorczego postulatu usuwania ani ocen wiarygodności wszystkich cytowanych serwisów. |
| Przypis 02 o zaginięciu oryginałów przeczy tezie autora | Zaginięcie fizycznych dokumentów nie jest tym samym co zaginięcie oryginalnych sformułowań. Przypis jest jawnie oznaczony. Nie potwierdzono zarzutu bezpośredniej sprzeczności wyłącznie na tej podstawie. |
| 02 „wraz z żoną rozpoczęli”; 27 „1 i 2 List Piotra” | Pierwsza konstrukcja może podkreślać równorzędność uczestników (EN `he and his wife began`), druga dopuszcza elipsę wspólnego członu. Brak podstaw do bezwzględnego nakazu zmiany liczby. |
| 04 błąd rodzaju przy „Przyczynie”; wszystkie źródłowe nawiasy kwadratowe | Nie wskazano jednoznacznego błędu rodzaju; EN sam przechodzi od `That Cause` do `He`. Część nawiasów jest poprawnie zagnieżdżona albo oznacza dodatki tłumacza. Konkretny nowy wyjątek w 12:37 opisano w U-012. |
| Nagłówek Rz 14,24–25 w 05 | Raport niedokładnie cytuje źródło: EN ma nagłówek `Romans 14:24`, a 25 dopiero w cytacie. Brak numeru wewnątrz cytatu opisuje P1-010. Nie zmieniać nagłówka pod pozorem odtwarzania zapisu PDF-u. |
| 05 `canticles` → „kantyczki” | Nie potwierdzono bezspornego błędu samego odpowiednika. Dopisek 05:89 odwołujący się do kolęd/pastorałek może jednak sugerować inny gatunek niż poetyckie części Pieśni nad Pieśniami; to opcjonalna decyzja terminologiczna, nie podstawa do poprawiania tezy autora. Por. [WSJP: kantyczka](https://wsjp.pl/haslo/podglad/84709/kantyczka/5211354/piesn-religijna). |
| 07 „zabronić utraty/wstawek”; 08 „naruszenie Tekstu” | EN rzeczywiście używa `forbid`; niezręczność nie dowodzi błędnego odczytania czasownika. „Naruszenie” jest szersze od „skażenia”, lecz kontekst zachowuje zmianę formy i sensu Tekstu; nie potwierdzono nowego zniekształcenia argumentu. |
| Skróty nazw ksiąg, Kohelet, „1 Kronik” | Nie ma ogólnej reguły zakazującej skrótów. Drugi raport nie podaje autorytatywnego wykazu nazw BT uzasadniającego proponowane zmiany starotestamentowe. Jednoznacznie ustalone „Objawienie Jana” pozostaje osobnym, już opisanym problemem. |
| „Siedem listów … zawiera” wymaga liczby mnogiej | Wskazówka drugiego raportu jest odwrócona. Obecne PL ma „zawierają”, do poprawy na „zawiera” — U-010. |
| 13:69 `O, OC, *Θ*C` | Kursywą zapisano samo Θ także w źródle, druk 53 / PDF 61; potwierdzają XML i obraz. Nie usuwać poprawnego wyróżnienia. |
| 15 „wspólna mozaika odczytów” | EN ma `a shared mosaic of readings`, nie `a mosaic of shared readings`. Zakres przymiotnika jest zachowany. |
| Zawsze zmienić „tekst większościowy” na „Tekst Większościowy” | W 09-autografy, 12:21, 34:15 i cytacie TuT w 48:107 są użycia opisowe lub cytowane, z małymi literami/cudzysłowem już w EN. Nie stosować mechanicznej zamiany bez rozpoznania użycia terminu. |
| 12:33,53 utracone formatowanie śródtytułów | Źródło także ma zwykły krój i osobne akapity. Zmiana na nagłówki Pandoca może służyć nawigacji, lecz nie wykazano zgubienia pogrubienia/kursywy. |
| Literówka w ID przypisu 10 i brak spacji po `]:` w 13 | `slow-w-libczbie-mnogiej` jest spójne w definicji i odsyłaczu, a `]:Chociaż` jest poprawnie parsowane. Nie zmieniać identyfikatorów wbrew instrukcji ani zgłaszać niewidocznej spacji jako usterki publikacji. |
| 19/24 `Well, well, well` → „No, no, no” rzekomo zaprzecza | Polskie powtórzone „no” może wyrażać zdziwienie lub uznanie. „No proszę” jest opcją stylistyczną, nie konieczną korektą sensu. Por. [NCK](https://nck.pl/projekty-kulturalne/projekty/ojczysty-dodaj-do-ulubionych/ciekawostki-jezykowe/no--grzeczne-czy-niegrzeczne-) i [Poradnia UŁ](https://www.poradnia-jezykowa.uni.lodz.pl/szczegoly/powtorzone-no-a-interpunkcja). |
| 23/24 `lection` → „lekcja” rzekomo narusza ustalony słownik | Chodzi o czytanie liturgiczne, nie krytycznotekstowe `reading`. „Lekcja” jest poprawnym terminem religijnym; reguła `reading → odczyt` nie zakazuje tłumaczenia innego słowa `lection` w ten sposób. Por. [WSJP: lekcja podczas mszy](https://wsjp.pl/index.php/haslo/podglad/2573/lekcja/5162489/podczas-mszy). |
| 25:137 „pozostałe przypadki to itacyzmy” | Tego przeciwstawienia nie ma w EN. U-017 przyjmuje korektę składni, odrzuca dopisanie nowej relacji. |
| Gallion 27:57: „zwłoka” jako poważny błąd | Pickering sam podaje `None of this was a delay to Gallio` i objaśnia nietypową interpretację. Nie zastępować jej znanym przekładem biblijnym ani „nie obchodziło go”. Rzeczywista rozbieżność w dalszym komentarzu jest już w P2-006. |
| 23 `seriously off the mark` utraciło nacisk | PL ma „**poważnie** mija się z celem”, a drugi raport pomija w swoim cytacie „poważnie”. Nie potwierdzono osłabienia stopnia zarzutu. |
| 18:63 przypis wewnątrz bolda | Samo położenie znacznika w Markdown nie dowodzi zmiany wyglądu przypisu: kontrola istniejącego polskiego PDF-u, s. 108, nie wykazała pogrubionego numeru ani treści przypisu. Ewentualna higiena zapisu wymaga osobnej oceny innych eksportów. |
| 40 `[1P 3,6]` zamienić na zwykły nawias okrągły | Autor na druk 278 / PDF 286 jawnie objaśnia kwadratowy nawias jako oznaczenie szczególnego statusu kolumny. PL 40:116 to zachowuje. Zmiana samej tabeli zerwałaby odesłanie; nie traktować tego jak zwykłego wtrącenia w prozie. |
| 48 `officiousness` → „wścibstwo” musi być błędem | Możliwe stylistyczne doprecyzowanie do „nadgorliwego ingerowania”, lecz słownikowe zakresy `officious` i „wścibski” obejmują `interfering/meddlesome`. Nie potwierdzono zarzutu, że polski wyraz oznacza wyłącznie ciekawość. Por. [Cambridge: officious](https://dictionary.cambridge.org/us/dictionary/english/officious) oraz [Cambridge/PASSWORD: wścibski](https://dictionary.cambridge.org/dictionary/polish-english/wscibski). |
| 49:166 `decent` → „dostateczne” | EN druk 321 / PDF 329 ma `fair`, nie `decent`. „Dostateczne” zachowuje kontrast z `not good enough`; „przyzwoite” to opcja stylistyczna. |
| 36 wzmianka o 1 Liście Jana dowodzi źródłowego błędu kolejności | Wierne źródłu wyprzedzające odwołanie, bez słowa „powyżej”. Nie dowodzi błędu autora ani pominięcia polskiego tekstu — U-S03. |

Pozostałe ogólne sugestie stylistyczne („gospodarując czas”, ciężkie zdanie o dorobku Burgona, „od czasu do czasu rok”, „wygląda równie staro”, „przedkładam, że”, „jeszcze prostszym angielskim”, „Nic tak jak…” / „przeżuć”) nie wykazały nowych zmian sensu. Metafory i osobliwości obecne również w EN należy rozważać zgodnie z zasadą niepoprawiania stylu argumentacji autora. W 24:39 zastąpienie „praktycznie wszystkich celów praktycznych” przez „niemal wszystkich celów praktycznych” usuwa powtórzenie brzmieniowe, ale nie jest konieczną korektą danych lub sensu — `virtually` i `practical` pełnią odrębne funkcje.

Jedna początkowa spacja w 01 ani techniczna spacja po definicji przypisu nie psują składu. Nie odnaleziono konkretnego „podwójnego znaku interpunkcyjnego” w 15 odpowiadającego zarzutowi. Zapis `1389` zamiast `1 389` jest wyborem konwencji typograficznej, nie pomyłką liczby; nie wolno zmieniać w ten sposób identyfikatora manuskryptu. Samo połączenie zdań przecinkiem również nie dowodzi błędu polskiej interpunkcji.

Nie przejęto ogólnego zapewnienia drugiego raportu, że głównym ryzykiem nie jest format. Poprawne parsowanie i zgodne sumy tabel nie wykluczają usterek już potwierdzonych w G-001, G-P1-001/002, P3-008, P5-007 i U-007. Także liczby 1874/1893 w 26 są **numerami manuskryptów, nie datami**, jak określa je drugi raport.

## Dalsza praca i wznowienie po przerwie

1. Przegląd całości oraz uzupełniające porównanie z drugim raportem z 2026-10-12 są zakończone. Wszystkie przyjęte uwagi scalono tutaj; nie trzeba zaczynać ponownie ani szukać nieukończonego rozdziału w zapisach roboczych. Propozycje odrzucone i już wcześniej opisane mają osobną mapę rozstrzygnięć powyżej.
2. Przed dalszą pracą przeczytać `AGENTS.md`, sprawdzić `git status --short --branch` i porównać zmiany książki względem bazy przeglądu. Nie cofać późniejszych poprawek użytkownika. Numery wierszy mogą się przesunąć.
3. **Nie wdrażać automatycznie uwag bez zlecenia poprawek.** Uzgodnić zakres, zwłaszcza decyzje terminologiczne, korekty źródła, tytuł i notę licencyjną.
4. Przy poprawkach zachowywać identyfikatory P1–P5/G. Dopisywać status „poprawione”, commit oraz wynik kontroli, zamiast usuwać ślad ustalenia. Obecnie wyjątkiem już naprawionym jest tylko wymienione wyżej `XII` w 19:3, poza listą otwartych usterek.
5. Po zmianie treści książki wykonać `make pdf`, sprawdzić `test -s build/pdf/Bog-zachowal-swoj-Tekst-Wilbur-Pickering.pdf`, obejrzeć odpowiednie strony i uwzględnić zmieniony PDF w tym samym PR co Markdown. Problemy eksportu przenośnego wymagają także sprawdzenia EPUB/DOCX.
6. Pliki pomocnicze sesji były w `/tmp/pickering-review-lbPxWh/`. W razie utraty odtworzyć ekstrakcję przez `pdftotext -layout` oraz `pdftohtml -xml -hidden -i`, a obrazy przez `pdftoppm`. Raport nie zależy od przetrwania tego katalogu.
7. Cząstkowy checkpoint jest zachowany w historii gita, commit `1081341b940c3fe40f8995a3fcd81e93ce016f62`; końcowy raport zawiera również później ukończony zakres 18–21. Bieżącym miejscem zapisu wszystkich ustaleń jest wyłącznie `REVIEW.md`.
