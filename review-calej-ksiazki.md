---
WhereTo: "0"
---
# Review polskiego przekładu *God Has Preserved His Text*

## Zakres i podstawa przeglądu

Przegląd dotyczy całego stanu repozytorium `tometchy/Bog-zachowal-swoj-Tekst-Wilbur-Pickering` w commicie `b0c5bc165a97d8de32faed076f7c16b461d7ecd3`.

Porównano 50 plików z katalogu `chapters` z angielskim wydaniem czwartym (*God Has Preserved His Text*, PDF liczący 331 stron). Kontrola objęła:

- kompletność struktury i zgodność kolejności rozdziałów,
- wierność sensu i toku argumentacji,
- terminologię krytycznotekstową,
- nazwy ksiąg biblijnych,
- przypisy i identyfikatory przypisów,
- Markdown i zgodność z Pandokiem,
- tabele, symbole, grekę oraz dane liczbowe,
- rozróżnienie błędów przekładu od problemów znajdujących się już w źródle.

## Werdykt

Książka jest **kompletna strukturalnie** i technicznie znajduje się w dobrym stanie. Nie stwierdziłem pominięcia rozdziału ani sekcji źródła. Wszystkie pliki rozdziałów są poprawnie parsowane przez Pandoca, przypisy są domknięte, obrazy istnieją, a rozbudowane tabele z części II, III i dodatku zostały na ogół odtworzone z dużą starannością.

Przekład **nie jest jednak jeszcze gotowy do wydania bez korekty**. Najważniejsze przyczyny są trzy:

1. W części pierwszej występuje kilka zmian sensu, jedna błędna referencja biblijna, nieustabilizowana terminologia i sporo usterek językowych.
2. Pierwsza część zawiera rozbudowaną warstwę dopowiedzeń tłumacza, niekiedy polemizującą z autorem albo wprowadzającą informacje spoza źródła. Jest to sprzeczne z przyjętą zasadą tłumaczenia bez interpretowania i dopowiadania.
3. W rozdziale 33 pominięto cztery znaczniki `**` należące do danych profilu *PA*. To najpoważniejszy błąd w późniejszej części, ponieważ zmienia informację niesioną przez tabelę.

Ogólna różnica jakościowa jest wyraźna: pliki 16–49 są znacznie bardziej konsekwentne terminologicznie i bliższe źródłu niż pliki 01–15. Późniejsza część wymaga przede wszystkim punktowej korekty, natomiast pierwsza część — pełnej redakcji porównawczej ze źródłem.

## Skala ważności

- **Krytyczny** — zmienia twierdzenie autora, dane lub identyfikację cytowanego miejsca.
- **Poważny** — zaciera istotne rozróżnienie techniczne albo istotnie zniekształca zdanie.
- **Redakcyjny** — błąd językowy, niekonsekwencja, odstępstwo od ustalonego słownika lub formatu, bez zasadniczej zmiany argumentu.
- **Problem źródła** — niespójność występuje już w angielskim wydaniu i nie powinna być po cichu „naprawiana” w przekładzie.

## Najważniejsze poprawki

| Ważność | Miejsce | Ustalenie |
|---|---|---|
| **Krytyczny** | `10...ostrozni.md`, w. 9 | Podano **Dzieje Apostolskie 21,28–31**, choć źródło odsyła do **Dziejów Apostolskich 20,28–31**. |
| **Krytyczny** | `12...normalnie.md`, w. 19 | Odwrócono kierunek argumentu statystycznego. Źródło mówi, że szybkie rozpowszechnienie dobrych kopii czyniło szanse uzyskania szerokiej akceptacji przez formy aberracyjne skrajnie małymi; polskie zdanie mówi dosłownie o podniesieniu szans wystąpienia takich okoliczności. |
| **Krytyczny** | `33...pericope-adulterae.md`, w. 74, 76, 92, 113 | Brakuje czterech źródłowych znaczników `**`: M6/27, M6/29, M5/05 i M5/26. Ponieważ gwiazdki oznaczają elementy profilu, nie jest to tylko formatowanie. |
| **Poważny** | `09...autografy.md`, w. 18 | `sat under his ministry` oddano jako „osiadło podczas jego posługi”. Sens dotyczy pozostawania pod nauczaniem/posługą Piotra, nie osiedlenia się. |
| **Poważny** | `04...preambula.md`, w. 51 | `it is one thing He cannot do` stało się „to jedyna rzecz, której nie może uczynić”. Autor mówi „jest to jedna rzecz, której nie może uczynić”, nie twierdzi tu, że jest jedyna. |
| **Poważny** | `10...ostrozni.md`, w. 29 | `the wording of Luke and Paul’s Epistles` oddano jako „sformułowania Listów Łukasza i Pawła”. Chodzi o **Ewangelię Łukasza i Listy Pawła**. |
| **Poważny** | `09...autografy.md`, w. 11–14 | `master copy` przetłumaczono jako „oryginalny egzemplarz”, co zaciera rozróżnienie między egzemplarzem wzorcowym a autografem. |
| **Poważny** | `02-przedmowa.md`, w. 10–13 | Dodany przypis tłumacza stwierdza, że oryginały zaginęły i krytyka tekstu jest konieczna. Nie pochodzi to od autora i bezpośrednio wchodzi w spór z tezą książki. |
| **Poważny** | `02-przedmowa.md`, w. 4 i 8 | `preserved original wording` uproszczono do „zachował oryginalny tekst”, a wcześniej użyto „dokładne oryginalne brzmienie”. Gubi to konsekwentnie używane pojęcie „oryginalnych sformułowań”. |
| **Poważny** | `05...natchnienie.md`, w. 15 | Źródło wskazuje Rzymian 14,24–25, polski nagłówek podaje tylko 14,24 i nie oznacza drugiego wersetu. |
| **Poważny** | `15-uwagi-koncowe.md`, w. 25 | Techniczne `recension` oddano jako „opracowanie krytyczne”, mimo że to samo zdanie później używa „recenzji”. Pierwszy człon również powinien zachować termin „recenzja”. |
| **Poważny** | `25...starannosci-kopisty.md`, w. 137 | Zdanie „Pierwszy jest jawnym nonsensem, niezależnymi przypadkami itacyzmu” jest niegramatyczne i nie przekazuje relacji ze źródła: pierwszy przypadek jest nonsensem, natomiast pozostałe to niezależne przypadki itacyzmu. |
| **Poważny** | `27...najlepszy-kompletny...md`, w. 57 | `None of this was a delay to Gallio` oddano jako „Żadna z tych rzeczy nie była dla Galliona zwłoką”. Zdanie wymaga ponownego przełożenia z uwzględnieniem kontekstu reakcji Galliona. |
| **Poważny** | `44...skolacjonowane-manuskrypty...md`, w. 53 | `I have not checked Hoskier’s collation ... in this connection` zmieniono na przyczynowe „W związku z tym nie sprawdziłem...”. Sens to „w tym zakresie/w odniesieniu do tej kwestii”. |
| **Poważny** | `48...czy-krytyka...jest-nauka.md`, w. 97 | `officiousness` oddano jako „wścibstwo”. W kontekście ingerencji w tekst trafniejsze jest „wtrącanie się”, „nadgorliwość” albo podobny termin, a nie ciekawska wścibskość. |
| **Redakcyjny** | `04...preambula.md`, w. 23 | `complete fossil` oddano jako „kompletny szkielet”. Skamieniałość i szkielet nie są tu tym samym. |

## Część pierwsza i materiały wstępne — przegląd plik po pliku

### `01-od-tlumacza.md`

- Literówki: „zazaczone”, „prze licencjodawcę”.
- „gospodarując dla niego czas” brzmi nienaturalnie; sensowniejsze byłoby „wygospodarowując na nie czas”.
- Jest zbędna spacja na początku jednego akapitu.
- Informacja licencyjna wymaga wyjaśnienia. Angielski PDF deklaruje **CC BY-SA 3.0 Unported**, natomiast ten plik i `metadata.yml` podają **CC BY-SA 4.0**. Może to być świadoma licencja polskiego opracowania, ale powinno być jasno rozdzielone, która licencja dotyczy źródła, a która przekładu.

### `02-przedmowa.md`

- Wiersz 4 zawiera fragment zdania: „Włącznie ze stanowiskiem...”.
- „dokładne oryginalne brzmienie” narusza ustalony odpowiednik `original wording` → „oryginalne sformułowania”.
- „wraz z żoną rozpoczęli” ma niezgodę podmiotu z orzeczeniem; podmiotem zdania jest dr Pickering.
- Opis kopii doskonałych manuskryptów/archetypu jest składniowo niejednoznaczny.
- Najważniejszy problem redakcyjny to dodany przypis o krytyce tekstu, który przedstawia jako fakt stanowisko odrzucane przez autora.

### `03-podziekowania.md`

- „okładka i formatowanie nie zostało” powinno mieć orzeczenie w liczbie mnogiej.
- Poza tym rozdział nie wykazuje materialnych odstępstw.

### `04-czesc-1-preambula.md`

- `complete fossil` → „kompletny szkielet” oraz `one thing` → „jedyna rzecz” wymagają poprawy.
- `cline` oddano jako „linia nachylenia (klin)”; termin jest niepewny i powinien zostać sprawdzony w kontekście argumentu.
- Występuje błąd zgody rodzaju i nazwa „1 Kronik”, niezgodna z przyjętą konwencją nazw ksiąg.
- Zachowano źródłowe nawiasy kwadratowe tam, gdzie zasady projektu wymagają okrągłych.
- Dodano trzy obrazy oraz rozbudowane objaśnienia, źródła internetowe i komentarze tłumacza. Są jawnie oznaczone, lecz tworzą równoległą warstwę argumentacyjną, której nie ma u Pickeringa.

### `05-czesc-1-wprowadzenie-natchnienie.md`

- Błędny zakres Rzymian 14,24–25 i pominięte oznaczenie wersetu 25.
- „Słowo, PANA”, „człowiek chciałaby” oraz kilka innych usterek fleksyjnych i interpunkcyjnych.
- `Its nature` zmieniono na „Natura Tekstu”, przez co doprecyzowano referencję bardziej niż źródło.
- `canticles` oddano jako „kantyczek” i opatrzono komentarzem, który nie pomaga zachować sensu autora.
- Nazwy ksiąg są niekonsekwentne: występują formy skrócone typu „Mateusza”, „Rzymian”, „Hebrajczyków”, „Jakuba”.
- Rozdział zawiera liczne dopiski do przypisów autora, m.in. listy współczesnych przekładów.

### `06-czesc-1-wprowadzenie-oswiecenie.md`

- Przekład zasadniczo wierny.
- Pozostaje dodany przypis/odnośnik oraz skrócona nazwa „1 Kor”, niezgodna z przyjętym standardem nazw.

### `07-czesc-1-wprowadzenie-kanon.md`

- Przekład zasadniczo wierny.
- „1 Kronik” wymaga ujednolicenia.
- Dosłowne „zabronić utraty/wstawienia” jest niezręczne i wymaga ponownego spojrzenia na angielski czasownik w kontekście.

### `08-czesc-1-historyczne-dowody.md`

- `work back from what He did` skrócono do „zacząć od tego, co zrobił”, przez co znika idea wnioskowania wstecz od skutków.
- `corrupt the Text` oddano słabszym „naruszenie Tekstu”.
- Występuje „Księga Objawienia” zamiast ustalonego „Objawienie Jana”.
- Dodano informacje o polskich przekładach, których nie ma w źródle.

### `09-czesc-1-historyczne-dowody-autografy.md`

- `master copy` należy odróżnić od autografu; obecne „oryginalny egzemplarz” zaciera ten punkt argumentacji.
- `sat under his ministry` zostało błędnie oddane jako „osiadło podczas jego posługi”.
- `initial draft` jako „wstępny konspekt” może sugerować plan, a nie pierwszą wersję tekstu.
- W kilku miejscach zapisano „tekst większościowy” małymi literami.
- „Księga Objawienia” wymaga ujednolicenia do „Objawienie Jana”.
- Duży przypis o Rodzinie 35 używa `NT` bez rozwinięcia, „linii transmisji” zamiast „linii przekazu” i wprowadza zewnętrzną definicję oraz adresy internetowe.
- Są też usterki „stał by się”, „na samym na terytorium” i niegramatyczny komentarz tłumacza.
- Źródłowa proza została miejscami zamieniona w listę. Nie zmienia to automatycznie sensu, ale narusza zasadę zachowania struktury.

### `09-czesc-1-historyczne-dowody-wczesne-rozpoznanie.md`

- Kilka zdań ma uszkodzoną składnię, szczególnie cytat dotyczący Barnaby oraz akapity w końcowej części pliku.
- „Siedem listów... zawiera” wymaga liczby mnogiej.
- Nazwa `Revelation` jest różnie oddawana jako „Księga Objawienia”, „Księga Objawnienia” i „Objawienie Jana”.
- Imię Justin występuje jako „Justin”, choć polska forma to „Justyn”.
- Są błędy odmiany, podwójne odstępy i niekonsekwentna interpunkcja.
- Liczne dodane przypisy i odnośniki należy oddzielić od aparatu autora.

### `10-czesc-1-historyczne-dowody-czy-pierwsi-chrzescijanie-byli-ostrozni.md`

- Błędna referencja Dzieje Apostolskie 21,28–31 zamiast 20,28–31.
- „słyszą słów” i „nie zwróci szczególną uwagę” są błędami gramatycznymi.
- „Listy Łukasza i Pawła” zniekształcają źródłowe „Łukasz i Listy Pawła”.
- Występuje „Księga Objawienia”, a `original wording` jest parafrazowane jako „jak brzmiał oryginalny tekst”.
- Przed listą brakuje pustego wiersza; jeden identyfikator przypisu zawiera literówkę.
- Dodano przypisy oparte m.in. na zewnętrznych serwisach o nierównej wiarygodności; nie należą one do argumentu autora.

### `11-czesc-1-historyczne-dowody-kto-mial-najlepsze kwalifikacje.md`

- Jedno zdanie nie ma pełnego orzeczenia, inne zawiera konstrukcję „a być może, że”.
- `collated` oddano jako „zestawiłem”; zgodnie ze słownikiem projektu powinno być „skolacjonowałem”.
- „Objawienie” nie zawsze ma pełną ustaloną nazwę.
- Kursywa w bibliografii jest niekonsekwentna.

### `12-czesc-1-historyczne-dowody-czy-przekazywanie-przebiegalo-normalnie.md`

- Najważniejszy błąd to odwrócenie sensu zdania o prawdopodobieństwie w wierszu 19.
- „Konstantyn zaprowadził ulgę” jest kalką; chodzi o przyniesienie kresu/ulgi w prześladowaniach.
- „nadać znaczenia” jest niegramatyczne.
- `'Majority' text` nie zostało powiązane z ustalonym „Tekstem Większościowym”.
- Śródtytuły są miejscami zwykłym tekstem, choć pełnią funkcję nagłówków.
- Zachowano źródłowe nawiasy kwadratowe; pojawiają się też „wariacje” zamiast wariantów i „warianty odczytów”.
- Na końcu przypisu pozostała samotna cyfra `3`.

### `13-czesc-1-historyczne-dowody-strumien-przekazywania.md`

- Błędy językowe: „dominujące strumień”, brak spacji i miejscami niewłaściwa zgoda.
- „trzech równych świadków” powinno zachować sens świadków równorzędnych.
- `cursive` utożsamiono w komentarzu z minuskułem, wbrew przyjętemu rozróżnieniu terminologicznemu.
- W jednym zestawie znaków źródłowe `O, OC, ΘC` zostało zmienione formatowaniem na `O, OC, *Θ*C`.
- Rozdział ma wyjątkowo dużo komentarzy tłumacza; część z nich rozszerza lub ocenia argumentację.

### `14-czesc-1-historyczne-dowody-jakie-sa-rzeczywiste-dowody.md`

- `original wording` występuje jako „oryginalne brzmienie”.
- „linie transmisji” należy zmienić na „linie przekazu”.
- Literówki: m.in. „języku griesh”, „byzantyjskiego”; są też brakujące spacje i uszkodzona składnia.
- „Objawienie” nie zawsze ma pełną ustaloną nazwę.
- Użycie `cursives (minuscules)` można zachować jako dwa terminy, ponieważ źródło samo podaje oba; nie należy jednak dalej ich utożsamiać.

### `15-czesc-1-uwagi-koncowe.md`

- „linia przekazywania” powinna być „linią przekazu”.
- Zdanie o „wspólnej mozaice odczytów” wymaga kontroli, aby nie zatrzeć technicznego sensu `shared mosaic of readings`.
- `recension` → „opracowanie krytyczne” jest terminologicznie błędne.
- `collating` oddano ogólnym „porównywaniem”; należy zachować „kolacjonowanie”.
- Literówki: „Ksiega”, „Wetcotta”; występuje też podwójny znak interpunkcyjny.
- Zagnieżdżone nawiasy nie są zgodne z regułą projektu.

## Część druga, trzecia i dodatek — przegląd plik po pliku

| Plik | Ocena i ustalenia |
|---|---|
| `16-czesc-2-czym-wlasciwie-jest-rodzina-35.md` | Początek późniejszej, ogólnie lepszej części. Tytuł „Najlepsza linia przekazywania” wymaga „linia przekazu”. `Notes of Truth` oddano jako „Uwagi o Prawdzie”, zamiast ustalonego „Notatki prawdy”. Są literówki „narazie”, „ogólnikow” oraz dosłowne `collated` → „zestawione”. |
| `17-czesc-2-profil-rodziny-35-dla-calego-nowego-testamentu.md` | **Bez materialnych błędów.** Zweryfikowano wszystkie 658 wierszy profilu. Sumy kategorii zgadzają się ze źródłem: `+++` 161, `++--` 144, `++` 153, `+--` 81, `+` 119. |
| `18-czesc-2-epistemologia.md` | Argument zachowany. Do korekty: „Platinga” zamiast Plantinga, niezręczne zdanie o dorobku Burgona, „poniższe wersy” oraz umieszczenie znacznika przypisu wewnątrz pogrubienia. Nazwa Księgi Koheleta wymaga sprawdzenia pod kątem dokładnej nomenklatury Biblii Toruńskiej. |
| `19-czesc-2-datowanie-kr-ponownie-rozwazone.md` | Przekład wierny. `1389` warto zapisać typograficznie jako `1 389`. „Well, well, well” przełożono jako „No, no, no”, co zmienia ton z „No proszę...” na zaprzeczenie. Jedno zdanie o świadectwie 35 kolacjonowań jest składniowo ciężkie. |
| `20-czesc-2-o-wzorcu-i-zaleznosci.md` | Sens zachowany. Należy ustalić jednolity odpowiednik `singular reading`: tu występuje „odczyt singularny”, wcześniej „odczyt pojedynczy”. Są dwa połączenia zdań samym przecinkiem i błąd „umniejsza jej wiarygodności”. |
| `21-czesc-2-wczesne-poswiadczenie-f35-w-listach-ogolnych.md` | **Bez materialnych błędów.** Dane i tok argumentu odpowiadają źródłu. |
| `22-czesc-2-profil-rodziny-35-w-dziejach-apostolskich.md` | **Bez materialnych błędów.** Tabele i obliczenia są spójne. |
| `23-czesc-2-precz-z-kaczkami-dziennikarskimi.md` | `lection(s)` oddano jako „lekcje”; w tym kontekście chodzi o liturgiczne „czytania”. `seriously off the mark` → „mija się z celem” osłabia sens „poważnie się myli”. Niezręczne są „od czasu do czasu rok” i „wygląda równie staro”. |
| `24-czesc-2-traktowanie-kr-przez-von-sodena.md` | Dane wierne. Powtarza się problem `lection` → „lekcja” (kilka miejsc); należy użyć „czytanie”. „Well, well, well” znów stało się „No, no, no”. Jest pleonazm „wystarczająco dobrą do praktycznie wszystkich celów praktycznych”. |
| `25-czesc-2-wspolczynnik-starannosci-kopisty.md` | Tabele odtworzono poprawnie. Poważnie uszkodzone jest zdanie w wierszu 137. `valid variant` jako „ważny wariant” nie oddaje sensu prawidłowego/zasadnego wariantu. Terminologia `singular` pozostaje niejednolita. |
| `26-czesc-2-niewiarygodnie-staranny-przekaz.md` | Przekład wysokiej jakości. „przedkładam, że” jest kalką i wymaga naturalniejszego odpowiednika. Rozbieżność dat 1874/1893 w prozie i 1876/1892 w tabeli pochodzi ze źródła. |
| `27-czesc-2-najlepszy-kompletny-nowy-testament-jaki-dotad-widzialem.md` | Ogólnie wierny. Zdanie o Gallionie wymaga ponownego przełożenia. „1 i 2 List Piotra” powinno mieć liczbę mnogą: „1 i 2 Listy Piotra”. |
| `28-czesc-2-glowne-podzialy-f35-w-ewangelii-mateusza.md` | **Bez materialnych błędów.** Struktura i dane zachowane. |
| `29-czesc-2-boskie-zachowanie-oryginalnych-sformulowan-listow-ogolnych.md` | Przekład wierny. Powtarza się kalka „przedkładam, że”. Zapis `16x,24` jest niejasny, ale został wiernie zachowany ze źródła i nie powinien być po cichu normalizowany. |
| `30-czesc-2-czy-archetypalny-tekst-f35-jest-autografem.md` | **Bez materialnych błędów.** Terminologia i argument odpowiadają źródłu. |
| `31-czesc-3-czy-f35-jest-starozytna.md` | **Bez materialnych błędów.** „jeszcze prostszym angielskim” jest niezręczne, lecz zachowuje intencję źródła. |
| `32-czesc-3-znaczenie-obiektywnych-dowodow.md` | **Bez materialnych błędów.** Dane i rozumowanie zachowane. |
| `33-czesc-3-o-tekscie-pericope-adulterae.md` | **Wymaga pilnej poprawki danych:** brakuje czterech znaczników `**` przy M6/27, M6/29, M5/05 i M5/26. Poza tym tabela i kolejność zestawów odpowiadają źródłu. |
| `34-czesc-3-kiedy-mamy-do-czynienia-z-recenzja.md` | Dane wierne. Zdanie „niektóre naprawdę znacznie” jest uszkodzoną kalką. `became extant in Sinai` oddano niezręcznie jako „stał się zachowanym manuskryptem na Synaju”; należy ponownie ustalić sens w kontekście pojawienia się/odnalezienia rękopisu. Występuje mała litera w nazwie Tekstu Większościowego. |
| `35-czesc-3-archetyp-w-listach-ogolnych-f35-tak-kx-nie.md` | **Bez materialnych błędów.** Dane porównawcze zachowane. |
| `36-czesc-3-concordia-discors-i-odczyty-mniejszosciowe-f35-w-listach-ogolnych.md` | Przekład wierny. Niedomknięcie/nadmiarowy nawias i przedwczesne odwołanie do 1 Listu Jana znajdują się już w źródle; nie są błędami tłumaczenia. |
| `37-czesc-3-podstawowa-przyczyna-ciaglego-odchodzenia-od-biblijnej-nieomylnosci.md` | **Bez materialnych błędów.** Pozostają jedynie długie, miejscami kalkowane konstrukcje i typograficzny zapis `1389`. |
| `38-dodatek-nagromadzone-bledy-czternastu-stuleci.md` | **Bardzo dobra zgodność danych.** Jest wszystkich 136 numerowanych pozycji; automatyczne porównanie potwierdziło zgodność identyfikatorów wersetów oraz wszystkich par greckich wariantów. Pozostaje decyzja o jednolitym odpowiedniku `singular reading`. |
| `39-dodatek-ocena-podstawowej-zasady.md` | **Bez materialnych błędów.** |
| `40-dodatek-podgrupy-f35-w-listach-ogolnych.md` | Tabele i liczby zachowane. W tabeli pozostawiono zwykły nawias kwadratowy `[1P 3,6]`, mimo ogólnej reguły używania nawiasów okrągłych. Źródło mówi o „kolejnych dwunastu” manuskryptach, choć tabela zawiera 15 pozycji — to problem źródła. |
| `41-dodatek-ranking-wariantowy-manuskryptow-zawierajacych-list-judy.md` | **Bardzo dobra zgodność danych:** 514 wpisów tabeli i 88 podkreślonych oznaczeń **f^35^**. Manuskrypt 1847 występuje w źródle w dwóch rangach, dlatego jest 514 wpisów, ale 513 unikatowych numerów; przekład wiernie zachowuje tę niespójność. |
| `42-dodatek-precz-z-falszerstwem.md` | **Bez materialnych błędów.** |
| `43-dodatek-definiowanie-zachowania.md` | Treść wierna. Konstrukcje „Nic tak jak rzeczywiste kolacjonowanie...” i cytowane „przeżuć” są bardzo dosłowne; warto je sprawdzić stylistycznie bez zmiany sensu. |
| `44-dodatek-skolacjonowane-manuskrypty-f35.md` | Dane zachowane. Wiersz 53 nadaje zdaniu nieobecną w źródle zależność przyczynową („W związku z tym”). Źródłowe „AG 586” zostało po cichu znormalizowane do „GA 586”; korekta jest prawdopodobna, lecz powinna być świadoma. |
| `45-dodatek-bizantyjskie-manuskrypty-kr-rodziny-35.md` | Lista zawiera dokładnie 364 manuskrypty, zgodnie ze źródłem. Kolejność `2673, 2669` jest nielogiczna, lecz taka sama w PDF-ie — to problem źródła. |
| `46-dodatek-grzech-pokoleniowy.md` | **Bez materialnych błędów.** |
| `47-dodatek-metoda-genealogiczna-oparta-na-spojnosci.md` | **Bez materialnych błędów.** |
| `48-dodatek-czy-krytyka-tekstu-nowego-testamentu-jest-nauka.md` | Ogólnie przekład wysokiej jakości. `officiousness` → „wścibstwo” wymaga zmiany. W końcowej części występuje mała litera w „tekstem większościowym”. |
| `49-dodatek-przedstawienie-dowodow-przez-alanda.md` | **Bez materialnych błędów.** Sumy wierszy i sumy kategorii między tabelami zostały sprawdzone i są zgodne. `decent` jako „dostateczne” można lepiej oddać „przyzwoite”. Wcięte bloki pod przypisami są poprawną kontynuacją przypisu w Pandocu, nie błędem Markdownu. |

## Problemy przekrojowe

### 1. Warstwa tłumacza jest zbyt rozbudowana

W repozytorium występują 84 tekstowe wystąpienia frazy `przyp. tłum.` na 67 wierszach (jedno wystąpienie należy do objaśnienia konwencji w pliku 01, więc liczba ta nie odpowiada dokładnie liczbie osobnych przypisów). Większość znajduje się w plikach 01–16; późniejsza część niemal całkowicie rezygnuje z takich ingerencji.

Same oznaczenia nie rozwiązują problemu wierności, ponieważ część dopisków:

- objaśnia argument autora za pomocą zewnętrznych źródeł,
- dodaje listy polskich przekładów,
- ocenia twierdzenia autora,
- poprawia lub uzupełnia jego argumentację,
- w jednym przypadku otwarcie przyjmuje stanowisko przeciwne tezie książki,
- korzysta z Wikipedii, CreationWiki, Grokipedii i innych stron o nierównym statusie.

Jeżeli celem jest edycja ściśle wierna, najlepszym rozwiązaniem jest usunięcie tych dodatków z tekstu głównego albo przeniesienie ich do osobnego, wyraźnie opisanego dodatku redakcyjnego. Trzy obrazy dodane w preambule również powinny zostać potraktowane jako materiał redakcyjny, nie część przekładu.

### 2. Terminologia krytycznotekstowa

Do globalnego wyszukania i ujednolicenia pozostają zwłaszcza:

| Źródło / pojęcie | Formy problematyczne | Forma docelowa |
|---|---|---|
| `original wording` | „oryginalne brzmienie”, „jak brzmiał oryginalny tekst”, „oryginalny tekst” | „oryginalne sformułowania” |
| `line of transmission` | „linia transmisji”, „linia przekazywania” | „linia przekazu” |
| `Notes of Truth` | „Uwagi o Prawdzie” | „Notatki prawdy” |
| `collate/collation` | „zestawić”, „porównywanie” | „kolacjonować/kolacjonowanie” |
| `recension` | „opracowanie krytyczne” | „recenzja” |
| `lection` | „lekcja” | „czytanie” (liturgiczne) |
| `singular reading` | „odczyt pojedynczy” / „odczyt singularny” | wybrać jedną formę i stosować konsekwentnie |
| `cursive` / `minuscule` | miejscami utożsamione | zachować jako dwa odrębne terminy |
| `Majority Text` | małe litery lub opisowy „tekst większościowy” | „Tekst Większościowy”, gdy chodzi o termin |

W przypadku `singular reading` sugeruję świadomą decyzję redakcyjną. „Odczyt pojedynczy” jest naturalniejszy, lecz „odczyt singularny” może być użyteczny jako węższy termin techniczny. Najważniejsze, by nie zmieniać odpowiednika bez powodu między rozdziałami.

### 3. Nazwy ksiąg biblijnych

Najwięcej niekonsekwencji znajduje się w części pierwszej. Występują m.in.:

- „1 Kronik” i „1 Ksiega Kronik”,
- „Mateusza”, „Rzymian”, „Hebrajczyków”, „Jakuba” bez pełnej nazwy,
- skróty `Mt`, `Łk`, `Ps`, `1 Kor`, `Dz`,
- „Księga Objawienia”, „Księga Objawnienia” i „Objawienie” zamiast konsekwentnego „Objawienie Jana”.

Skróty w technicznych tabelach można pozostawić, jeżeli pełne nazwy zaburzałyby tabelę, ale proza powinna zostać ujednolicona zgodnie z Biblią Toruńską.

### 4. Nawiasy i znaki

- W części pierwszej zachowano wiele źródłowych nawiasów kwadratowych, mimo reguły zamiany na okrągłe.
- Nie wolno mechanicznie zamieniać nawiasów będących składnią Pandoca, np. `[tekst]{.underline}` ani identyfikatorów przypisów `[^id]`.
- Późniejsza część na ogół dobrze zachowuje **f^35^**, **K^r^**, **K^x^**, oznaczenia profili i grekę.
- Cztery brakujące gwiazdki w rozdziale 33 są wyjątkiem o znaczeniu merytorycznym.

### 5. Język i interpunkcja

Pierwsza część ma zauważalnie więcej:

- błędów zgody podmiotu z orzeczeniem,
- literówek i brakujących spacji,
- kalek angielskiej składni,
- połączeń pełnych zdań samym przecinkiem,
- niekonsekwentnych półpauz i pauz,
- zdań urwanych albo pozbawionych orzeczenia.

Późniejsza część jest pod tym względem znacznie stabilniejsza. Wymaga korekty językowej, ale nie ponownego tłumaczenia całości.

## Kontrola techniczna i kompletność

| Kontrola | Wynik |
|---|---|
| Liczba plików w `chapters` | 50 |
| Łączna objętość | 6572 wiersze, ok. 141 151 słów |
| Zgodność ze spisem treści źródła | wszystkie części i sekcje obecne |
| Parsowanie Pandoc | wszystkie pliki przechodzą z `--fail-if-warnings` |
| Przypisy | każdy znacznik występuje w prawidłowej parze; brak zduplikowanych definicji |
| Obrazy | wszystkie odwołania wskazują istniejące pliki |
| Uszkodzone znaki | brak `U+FFFD` |
| Pozostałości robocze | brak `<mark>` i surowych tabel LaTeX |
| Rozdział 17 | 658 wierszy i zgodne sumy profilu |
| Rozdział 38 | 136 pozycji; identyfikatory i greckie warianty zgodne ze źródłem |
| Rozdział 41 | 514 wpisów, 88 oznaczeń **f^35^** |
| Rozdział 45 | 364 numery manuskryptów |
| Rozdział 49 | sumy wierszy i kategorii spójne |

To oznacza, że głównym ryzykiem nie jest utrata rozdziałów ani awaria formatu, lecz kilka punktowych zmian sensu oraz niejednorodność pierwszej części.

## Niespójności obecne już w angielskim źródle

Poniższych miejsc nie należy po cichu poprawiać tak, jakby były błędami tłumacza. Można je zachować i ewentualnie opisać krótką notą poza przekładem:

1. **Rozdział 26:** proza podaje lata 1874 i 1893, natomiast tabela 1876 i 1892.
2. **Rozdział 29:** zapis `16x,24` jest niejasny, ale występuje w źródle.
3. **Rozdział 36:** w źródle jest nadmiarowy/niedomknięty nawias; podsumowanie wspomina też 1 List Jana, zanim zostaje on omówiony.
4. **Rozdział 40:** tekst mówi o „kolejnych dwunastu” manuskryptach, lecz następująca tabela ma 15 wierszy.
5. **Rozdział 41:** manuskrypt 1847 pojawia się w dwóch różnych rangach; stąd 514 wpisów, ale 513 unikatowych numerów.
6. **Rozdział 45:** lista źródłowa ma kolejność `2673, 2669`.

## Zalecana kolejność prac

1. **Naprawić błędy krytyczne:** referencję Dz 20,28–31, odwróconą logikę w rozdziale 12 i cztery znaczniki `**` w rozdziale 33.
2. **Naprawić pozostałe zmiany sensu:** `sat under his ministry`, `one thing`, Łukasz i Listy Pawła, `master copy`, zdanie o Gallionie, zdanie w rozdziale 25, `officiousness` i `in this connection`.
3. **Oddzielić warstwę tłumacza od tekstu autora:** szczególnie przypisy polemiczne, źródła internetowe, listy współczesnych przekładów i dodane ilustracje.
4. **Przeprowadzić globalne ujednolicenie terminów:** `original wording`, `line of transmission`, `collation`, `recension`, `lection`, `singular reading`, `Majority Text`, `cursive/minuscule`.
5. **Ujednolicić nazwy ksiąg według Biblii Toruńskiej.**
6. **Wykonać korektę językową części pierwszej**, a następnie lżejszą korektę plików 16–49.
7. **Ponownie uruchomić testy Pandoca i kontrolę danych**, szczególnie rozdziałów 17, 33, 38, 41, 45 i 49.

## Konkluzja

Najważniejszy pozytywny wynik przeglądu jest taki, że książka została doprowadzona do końca, jej struktura odpowiada źródłu, a najbardziej pracochłonne tabele i zestawienia w późniejszych rozdziałach są w ogromnej większości kompletne i dokładne. Nie ma potrzeby tłumaczyć drugiej połowy od nowa.

Przed publikacją potrzebna jest jednak ukierunkowana korekta merytoryczna oraz pełna redakcja części pierwszej. Po usunięciu kilkunastu wskazanych zmian sensu, przywróceniu czterech znaczników w rozdziale 33, rozdzieleniu komentarzy tłumacza od tekstu Pickeringa i ujednoliceniu terminologii przekład powinien osiągnąć spójny standard w całej książce.
