# Przegląd części 1 — chapters/02–16

Stan: ukończony przydzielony zakres 02–16. Weryfikacja względem `God-Has-Preserved-His-Text-4th.pdf`, wydanie czwarte, 331 stron. Numery stron drukowanych od części I odpowiadają numerom stron PDF minus 8.

## Postęp

- Przydzielony zakres: `02-przedmowa.md`, `03-podziekowania.md`, `04`–`16`, w tym oba pliki `09`; źródło s. iii–iv (PDF 3–4) oraz s. 1–65 (PDF 9–73).
- Przejrzana treść: `02`–`08`, oba pliki `09`, całość; źródło iii–iv, s. 1–29 (koniec Wczesnego rozpoznania na początku s. 29).
- Przejrzana forma: `02`–`09`: struktura, przypisy, XML pogrubień/kursywy; render PDF 15 oraz geometria podkreśleń z `mutool draw -F trace` dla PDF 3–4,9–37.
- Kontynuacja 2026-10-11 po resecie limitu: przeczytano pełną treść i przypisy `10`–`16`, źródło s. 29–66 (rozdział 16 kończy się na początku PDF 74, przed profilem rodziny). Sprawdzono wszystkie wskazania bold/italic z XML dla tego zakresu.
- Diagram `images/Rysunek_A.jpg` porównany wizualnie z oryginałem s. 50 / PDF 58: oznaczenia, daty, kontury, strzałka i relacje zachowane; nagłówki i etykiety przetłumaczone. Nie stwierdzono pominięcia. Jest to ten sam plik ilustracji co w dodatku 48.
- Zakończona kontrola podkreśleń `10`–`16`: geometria cienkich prostokątów i sąsiadujących glifów `mutool draw -F trace` na PDF 37–74; dodatkowo ogląd renderów PDF 38,39,43,70,74 oraz diagramu PDF58. Rozpoznano też podkreślone adresy WWW i linie separatorów przypisów, których nie traktowano jako odrębnych akcentów autora.
- Przeprowadzony test Pandoca potwierdza, że definicja przypisu `12:69–70` jest poprawnie rozpoznawana pomimo braku wcięcia w drugim wierszu — nie zgłaszać tego jako uszkodzenia przypisu. Nie zmieniano treści, artefaktów książki ani gita.
- Zakres 02–16 obejmuje całe teksty główne i przypisy, listy/liczby/sigla, strukturę, bold/italic i podkreślenia oryginału. Zakończono również dodatkowy audyt globalnych gwiazdek: skan `chapters/`, analiza węzłów `Emph` w JSON Pandoca dla wszystkich plików, kontrola podejrzanych wyników LaTeX i renderów istniejącego polskiego PDF-u. Wyniki G-P1-001/002 poniżej uzupełniają P3-008; nie trzeba powtarzać tego audytu.
- Podstawa: oryginalny PDF; ekstrakcja `pdftotext -layout` do porównania treści, XML `pdftohtml` do kontroli wyróżnień, renderowanie podejrzanych stron. Pomocnicza transkrypcja `neway` nie jest wzorcem.
- Nie zmieniano tekstu książki.

## Potwierdzone uwagi

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
- Zmienione na pogrubienie podkreślenia: `09-wczesne:9` pierwsze „teraz” (s.20/PDF28), `13` oba „teraz” (s.21/PDF29), `25` „poznać” (s.23/PDF31), `33` „nie znajduje się w Starym Testamencie” (s.24/PDF32), `73` zdanie „Zwróć następnie uwagę…” (s.27–28/PDF35–36).
- Kierunek: przyjąć konsekwentne odwzorowanie oryginalnych podkreśleń i przywrócić brakujące zakresy; nie traktować występującego bold jako nowego akcentu autora. Wskazane w P1-012 podkreślenie należy do tego samego problemu.

### P1-027 — Treść / powtórzenie wielkiej litery istotnej dla argumentu

- Lokalizacja: `chapters/09-czesc-1-historyczne-dowody-wczesne-rozpoznanie.md:27`, „przetłumaczyłem «wszystko z góry»”. Źródło: s. 23 / PDF 31.
- EN: „I rendered ‘everything from **Above**’”, podczas gdy objaśniane znaczenie słownikowe dalej brzmi małą literą „from **above**”. PL cytatu w w.25 używa „Góry”, lecz omawiając własny przekład gubi tę wielką literę.
- Kierunek: zachować „wszystko z Góry” w cytowaniu dokonanego przekładu i małe „z góry” przy znaczeniu słownikowym.

### Noty o źródle i kompletności w zakresie 09

- Przypisy autora porównano w całości, w tym przenoszone między stronami. Definicja `unia-hipostatyczna` z 05 ma rzeczywiste użycie w w.46 i nie jest osierocona.
- Nazwa „majority text” w 09-autografy występuje w źródle małymi literami i w cudzysłowie; nie zgłaszano automatycznego podniesienia wielkości liter bez rozpoznania użycia opisowego.
- Źródło s.22/PDF30 ma `1 Peter 1:12,,` oraz `Mathew`; w PL nie powielono tych oczywistych usterek. Źródło s.20/PDF28 celowo podaje Rz16,24–25 i wyjaśnia alternatywne umiejscowienie w przypisie, więc nie traktować adresu jako polskiej pomyłki.

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

- `chapters/10:41,43`: powtarzające się „Księga Objawienia” — ustalone „Objawienie Jana”; w `11:31` samo „Objawienie” (EN Revelation; s.33,38/PDF41,46).
- `chapters/10:43`: EN `the original reading` → „jak brzmiał oryginalny tekst”; przywrócić techniczny „oryginalny odczyt” (s.33/PDF41).
- `chapters/11:13`, „tekstu Nowego Testamentu”: EN `NT Text`; `12:31`, „tekstowi Nowego Testamentu”: EN `NT Text` — przywrócić wielkie `Tekst` (s.36,46/PDF44,54).
- `chapters/11:47`, „Sam zestawiłem”: EN `Having myself collated` — rozważyć ustalone „skolacjonowałem”, nie tracąc nazwy wykonywanej operacji (s.41/PDF49).
- `chapters/10:19`: „słyszą słów” → „słyszą słowa”, „nie zwróci szczególną uwagę” → „nie zwróci szczególnej uwagi”; `10:13`: „zaprzeczając Właściciela” wymaga poprawnej konstrukcji „wypierając się Właściciela” (EN denying the Owner); `12:47`: „zmienić tekst” → „zmienić tekstu”.

### P1-034 — Forma / utracona kursywa, zakres 10–12

- `chapters/10:27`: tytuł „Apologia I” (EN *Apol.*); `10:41`: oba greckie zapisy liczby χξς̓ / χις̓. Źródło s.32–33/PDF40–41, XML.
- `chapters/11:65,67,69,88`: tytuły *The Early Versions of the New Testament*, *The Bible in Modern Scholarship*, *The Text of the New Testament*, *The Last Twelve Verses of Mark*, *The Four Gospels: A Study of Origins*. Źródło s.38,42/PDF46,50.
- Kierunek: odtworzyć zakresy kursywy. Kontrola pozostałych wyróżnień jest zakończona; dalsze uwagi znajdują się w P1-046 i P1-047.

### P1-035 — Forma / numer przypisu włączony do treści

- Lokalizacja: `chapters/12:72`, początek definicji `[^jw-burgon-revision-323-324]: 3 J.W. Burgon`. Źródło s.46/PDF54.
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

- `chapters/14:3`: `original wording` → „oryginalne brzmienie”; ma być „oryginalne sformułowania” (s.55/PDF63).
- `chapters/14:17`: trzy wystąpienia „Objawienia/Objawieniem” bez Jana; zachować ustaloną nazwę „Objawienie Jana” (s.57/PDF65).
- `chapters/14:31,34,36,42,44`, `15:35`, `16:19,51`: nazwa czynności `collate/collation` występuje jako „zebrał”, „zestawienie”, „analiza”, „zebrane dane”, „porównania”, „porównywanie”, „zestawione”; warto utrzymać ustalone „kolacjonowanie” zwłaszcza tam, gdzie źródło odróżnia je od `compare/comparison` (14:31 `collated and compared`; s.57–59,61,64/PDF65–67,69,72).
- `chapters/16:7`: „Uwagi o Prawdzie” → ustalone „Notatki prawdy”; w 16:27 jest już właściwy odpowiednik (s.63,65/PDF71,73).
- `chapters/16:9`: „punkt wyjścia” dla `steppingstone` → „punkt pośredni”; w 16:25 autor jawnie komentuje użycie właśnie tego terminu, więc niespójność zaciera odesłanie (s.63–64/PDF71–72).
- Drobne literówki: `15:33` „Ksiega”, `15:45` „Wetcotta”, `16:5` „narazie”, `16:25` „ogólnikow”, `16:37` „z zachowanych greckich manuskryptach” (błędna fleksja).

### P1-046 — Forma / kursywa i dodatkowe wyróżnienia, 12–16

- Brak kursywy: `12:82` *Neutestamentliche Aufsatze* (s.48/PDF56); `13:61` *theta* (s.53/PDF61); `13:83` *Identity IV* (s.54/PDF62). Kursywa *Pericope Adulterae* w tytule referatu `14:44` jest zachowana i nie wymaga poprawki.
- Zmieniona kursywa: `15:41` siedem kryteriów „wielkość”, „niezależność”, „wiek”, „rozmieszczenie geograficzne”, „profil”, „staranność”, „zakres” — źródło ma bold i podkreślenie, PL bold i kursywę (s.62/PDF70, także render); `16:7` *Tekst Większościowy* — EN `Majority Text` jest zwykłym tekstem (s.63/PDF71).
- Kierunek: odtworzyć oryginalne zakresy i rodzaje wyróżnień. Pozostałe różnice wynikające z podkreśleń są opisane w P1-047.

### P1-047 — Forma / brak lub zmiana podkreśleń, zakres 10–16

- Brak wyróżnienia `false` → „fałszywi” w cytacie 2 P 2,1: `chapters/10:13`, źródło s.30/PDF38.
- Zmiana podkreślenia na bold: `10:19` „mu” (s.31/PDF39); `10:25` „wzburzony” (s.32/PDF40); `10:58` całe „kluczową kwestią jest zachowanie jego Tekstu” (s.35/PDF43); `12:70` „natchnionego Tekstu” (s.46/PDF54); `13:38` „będą” (s.51/PDF59); `15:45` „Tekstu” w tytule zastrzeżenia (s.60/PDF68); `16:25` „wykazane” i `16:33` „nie może” (s.65/PDF73); `16:33` zdanie od „Jeśli K^r^ jest wczesny i niezależny” do „Nowego Testamentu” (s.66/PDF74). Następne zdanie o najlepszej linii jest w źródle rzeczywiście pogrubione, należy zachować to rozróżnienie.
- Brak podkreślenia przy zachowanym bold: końcówka liczby mnogiej `word**s**` → `sł**ów**` w `10:19` (s.31/PDF39), `11:37` „IV wieku” (s.40/PDF48).
- `10:72`, ostatnie „słowa” przed „prawdziwe i wierne”: źródło podkreśla końcówkę `s` (liczbę mnogą); PL nie zachowuje tego akcentu (s.31/PDF39).
- Podkreślenia siedmiu kryteriów z `15:41` zamieniono na kursywę, jak w P1-046. Wszystkie wskazania pochodzą z geometrii oryginalnego PDF-u; reprezentatywne s.30,31,35,62,66 potwierdzono również renderami.
- Kierunek: zastosować spójny sposób zapisu podkreśleń obsługiwany przez Pandoca, nie usuwać istniejącego akcentu i nie zgłaszać go jako całkowicie nowego pogrubienia autora.

### P1-048 — Treść / świadkowie tekstu a dowody jego istnienia

- Lokalizacja: `chapters/12:65`, „nie mamy zachowanych żadnych świadectw ich istnienia”. Źródło s.45/PDF53.
- EN `we have no extant witness to them` odnosi się do braku zachowanych świadków zawierających omawiane odczyty. PL twierdzi szerzej, że brak jakichkolwiek zachowanych dowodów ich istnienia, choć autor w tym samym zdaniu odwołuje się do przedstawionych dowodów. Kierunek: zachować techniczny sens „nie mamy żadnego zachowanego świadka tych odczytów”, nie negować dowodów istnienia.

### P1-049 — Forma / nawiasy zagnieżdżone

- Lokalizacja: `chapters/13:67`, `(por. Fee…)` w całym akapicie ujętym w nawiasy; `chapters/15:35`, `(22)`, `(przypuszczalnie)`, `(4)`, `(Dzieje Apostolskie)` wewnątrz całej uwagi nawiasowej. Źródło s.53,61/PDF61,69.
- W pierwszym miejscu EN ma wewnętrzne nawiasy kwadratowe; w drugim zewnętrzne EN są kwadratowe, a wewnętrzne okrągłe. Zamiana zewnętrznych na okrągłe w PL wymaga pozostawienia/zmiany wewnętrznych na kwadratowe zgodnie z AGENTS, zamiast nawiasów okrągłych wewnątrz okrągłych.

## Dodatkowy audyt globalny: literalne gwiazdki

### G-P1-001 — Forma / uszkodzone sigla i całe zdanie w indeksie górnym

- Lokalizacja: `chapters/49-dodatek-przedstawienie-dowodow-przez-alanda.md:136`, oba wystąpienia `P^66*^` w zdaniu od „Okoliczność, że niektóre odczyty bizantyjskie…”. Źródło: s.318/PDF326. Istniejący polski PDF: s.390/PDF390, obejrzany render.
- Obie literalne gwiazdki łączą się w znaczniki kursywy, a znaczniki `^` przestają wyznaczać dwa odrębne indeksy. `pandoc --from=markdown-smart -t latex` tworzy `P\textsuperscript{66\emph{\^{} poprawiono na odczyty egipskie, a niektóre odczyty egipskie w P\^{}66}}`. W gotowym PDF-ie większość tego zdania jest drobnym, kursywnym indeksem górnym, oba istotne oznaczenia `*` znikają, zaś daszki stają się widoczne.
- Kierunek: zabezpieczyć oba literalne asteriski (`\*`) i sprawdzić, że oba sigla mają wyłącznie `66*` w indeksie, a całe zdanie między nimi jest zwykłym tekstem. Nie zmieniać oznaczeń autora ani rozróżnienia rąk/korekt.

### G-P1-002 — Forma / utracona gwiazdka w numerze strony i przesunięta kursywa

- Lokalizacja: `chapters/47-dodatek-metoda-genealogiczna-oparta-na-spojnosci.md:9`, „(s. 18*), podobnie jak uczynili dwadzieścia lat wcześniej w *ECM*…”. Źródło: s.296/PDF304. Istniejący polski PDF: s.368/PDF368, obejrzany render.
- Gwiazdka po `18` otwiera kursywę zakończoną gwiazdką przed `ECM`. Pandoc zwraca `18\emph{), podobnie jak uczynili dwadzieścia lat wcześniej w }ECM*`. Numer strony staje się błędnym `18` zamiast `18*`, obcy fragment otrzymuje kursywę, a przy `ECM` pozostaje nieuprawniona literalna gwiazdka. To nie tylko różnica typograficzna, ale również uszkodzone odesłanie.
- Kierunek: zapisać literalne gwiazdki numeracji stron jako `\*`, zachować osobną kursywę skrótu *ECM*. Numery `28*` w w.5 i `11*` w w.9 obecnie przechodzą do LaTeX prawidłowo, ale warto zastosować jednolite zabezpieczenie literalnych znaków.

### Zakres sprawdzenia i powiązania

- Potwierdzono także opisany już w P3-008 problem `chapters/32:93`: 20 gwiazdek w wyliczeniu znika, tworząc 10 przypadkowych fragmentów kursywy. Nie tworzyć drugiej niezależnej uwagi o tym samym błędzie.
- Gwiazdki w pojedynczych komórkach tabel 32 oraz pojedyncze `P^66*^` w 38:65 nie wykazały tego błędu parsowania. Zatem nie każda niezabezpieczona gwiazdka już dziś powoduje usterkę; problem ujawnia się przy parowaniu z następną gwiazdką w obrębie tego samego fragmentu tekstu.
- Audit dotyczył interpretacji literalnych gwiazdek przy numerach i siglach, nie zastępuje pełnej kontroli poprawności danych merytorycznych rozdziałów pozostałych recenzentów. Nie zmieniano książki ani nie generowano jej ponownie.
