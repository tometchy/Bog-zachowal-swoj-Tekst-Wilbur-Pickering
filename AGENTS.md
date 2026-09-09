Tłumaczę książkę Wilbura Pickeringa z angielskiego na polski. Zadaniem jest tłumaczyć je wiernie, bez interpretowania, poprawiania argumentacji autora ani dopowiadania od siebie.

Zasady tłumaczenia i formatowania:

1. Tłumacz wiernie sens i tok argumentacji autora.
   - Nie poprawiaj autora merytorycznie.
   - Nie „wygładzaj” jego argumentacji kosztem informacji.
   - Jeśli autor używa dwóch różnych terminów, zachowuj to rozróżnienie także po polsku.
   - Jeśli coś jest niejednoznaczne terminologicznie, nie normalizuj tego po cichu — zachowaj informację albo krótko zaznacz problem poza tłumaczeniem.

2. Zachowuj cały Markdown źródła:
   - `*kursywa*`
   - `**pogrubienie**`
   - indeksy górne, np. `**M^7^**`, `**f^35^**`
   - przypisy, np. `[^1]`, `[^x]`
   - nagłówki, listy, tabele itd.
   - Nie zmieniaj identyfikatorów przypisów.

3. Odpowiedź z tłumaczeniem zawsze podawaj jako SUROWY MARKDOWN w bloku kodu:
   ```markdown
   ...

Jest to ważne, ponieważ kopiuję tekst na Androidzie do aplikacji GitHub i przy kopiowaniu wyrenderowanego Markdownu giną gwiazdki.

4. Nazwy ksiąg biblijnych podawaj zgodnie z Biblią Toruńską. Przykład:

Revelation → Objawienie Jana

5. Ustalone odpowiedniki terminologiczne:

Majority Text → Tekst Większościowy

evidence → dowód / dowody / dowodów itd., odpowiednio fleksyjnie

MSS → manuskrypty

MS → manuskrypt

steppingstone → punkt pośredni

Notes of Truth → Notatki prawdy

original wording to oryginalne sformułowania, nie oryginalne brzmienie

NT → zawsze rozwiń jako Nowy Testament

Gdy autor używa nawiasu kwadratowego używaj okrągłego, chyba, że to nawiasy w nawiasach.

reading w kontekście krytyki tekstu → odczyt, nie „lekcja”

shared readings → wspólne odczyty

variant reading → wariantowy odczyt albo odczyt wariantowy, zależnie od składni

minuscule → minuskuł

cursive(s) → zachowuj jako odrębny termin, np. rękopis kursywny / rękopisy kursywne; nie sprowadzaj automatycznie do „minuskuł”

6. Gdy Pickering pisze Text wielką literą i chodzi mu o autograf / oryginalny tekst Biblii, tłumacz jako Tekst wielką literą.

Original Text → Tekst Oryginalny

Jeśli Text wielką literą oznacza w danym miejscu coś innego, rozpoznaj to z kontekstu i nie stosuj tej zasady mechanicznie.

7. Zachowuj symbole i oznaczenia krytycznotekstowe dokładnie np.:

**K^r^**

**K^x^**

**f^35^**

**M^5^**

**M^6^**

**M^7^**

**M^a-b^**

**M^c^**

**M^d-e^** Nie upraszczaj ich i nie zmieniaj zapisu.



8. Skróty takie jak PA mogą pozostać jako *PA*, jeśli autor używa ich jako skrótu wcześniej zdefiniowanego terminu, np. Pericope Adulterae.


9. W przypadku terminów technicznych z krytyki tekstu preferuj precyzję nad stylistycznym wygładzaniem. Przykładowo:

line of transmission → linia przekazu

text-type → typ tekstu

apparatus → aparat krytyczny

collation / collate → kolacjonowanie / kolacjonować, jeśli pasuje do kontekstu

attestation → poświadczenie

archetype → archetyp

common denominator → wspólny mianownik



10. Tabele:



domyślnie zapisuj jako zwykłe tabele Markdown z pionowymi kreskami |,

np.:


	opis

+++	około 20%
++--	około 25%
++	około 30%
+---	około 35%
+	około 40%


Nie używaj raw LaTeX do tabel.

Docelowo generuję z Markdownu PDF/EPUB/DOCX za pomocą Pandoca.


Zachowaj strukturę, pogrubienia, kursywę, symbole, przypisy i tabele w miarę możliwości,


11. Jeśli zauważysz rzeczywisty problem w źródle, literówkę, niejednoznaczność albo miejsce, gdzie polski odpowiednik może zatrzeć ważną informację:



Stosuj wierne tłumaczenie,
Nie zmieniaj samowolnie znaczenia tekstu.


14. Zachowuj także nawiasy autora, dopowiedzenia w nawiasach kwadratowych, em dash, Q.E.D. oraz łacińskie i greckie wyrażenia w kursywie, jeśli tak są zapisane w źródle. Ale preferuj nawiasy okrągłe, ale jak jest nawias w nawiasie to wtedy nawiasy kwadratowe w ś©odku.

15. Preferuj przecinki, jeśli to możliwe, nawet gdzie Pickering stosuje średniki.


**Ten prompt jest celowo dość restrykcyjny**, żeby nowy chat nie zaczął po kilku wiadomościach „ulepszać” terminologii po swojemu. Np. gdy są punkty o `Text`, `reading`, `cursive/minuscule`, `evidence` i surowym Markdownie.

Ogólnie całe tłumaczenie wcześniej robiłem paragraf po paragrafie. Wszystko to w pandoc, dodając kolejne rozdziały w katalogu chapters - https://github.com/tometchy/Bog-zachowal-swoj-Tekst-Wilbur-Pickering/tree/master/chapters

Zwróć uwagę, że przypisy, zeby nie miały konfliktujących numerków, to każdy przypis to kilku słowne podsumowanie jego treści.

Oryginał to plik pdf ten - https://github.com/tometchy/Bog-zachowal-swoj-Tekst-Wilbur-Pickering/blob/master/God-Has-Preserved-His-Text-4th.pdf

Przeanalizuj dobrze obecną sturkturę, żeby kontynuacja była dokładnie według tej samej struktury, tak jakbym to ja dalej robił, najlepiej też stosowane przez mnie odpowiedniki tłumaczeń też dalej konsekwentnie stosuj.

UWAGA! Już jest całość wstępnie przetłumaczona, teraz robię review i poprawki.

## Kończenie pracy

Po każdej zmianie w repozytorium utwórz pull request i zakończ odpowiedź bezpośrednim,
klikalnym linkiem do niego. Przed podaniem linku zweryfikuj za pomocą GitHub CLI lub
API, że pull request rzeczywiście istnieje, jest otwarty i prowadzi do właściwego
repozytorium oraz gałęzi. Nie traktuj samego przygotowania tytułu i opisu PR-a jako
jego utworzenia.
