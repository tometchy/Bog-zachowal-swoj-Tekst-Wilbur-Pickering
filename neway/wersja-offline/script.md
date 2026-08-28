Nie — nie zaczęło od nowa. Stan i pliki zostały zachowane, więc dokończyłem poprzednią pracę.

Gotowe pliki:

* [pdf_page_to_markdown.py](sandbox:/workspace/scratch/2dd690abb72a/pickering-repo/pdf_page_to_markdown.py)
* [requirements-pdf-page.txt](sandbox:/workspace/scratch/2dd690abb72a/pickering-repo/requirements-pdf-page.txt)

Skrypt działa całkowicie lokalnie:

* PyMuPDF renderuje JPG i odczytuje fonty, indeksy oraz współrzędne;
* lokalny PyMuPDF4LLM analizuje układ zwykłych stron;
* własny parser obsługuje trudne tabele aparatu krytycznego;
* nie ma OpenAI API ani żadnego HTTP;
* telemetria ONNX Runtime jest jawnie wyłączona przez `ORT_DISABLE_TELEMETRY=1`.

Instalacja na Ubuntu/X13s:

```bash
sudo apt update
sudo apt install -y python3-venv

cd ~/Projects/Bog-zachowal-swoj-Tekst-Wilbur-Pickering

python3 -m venv .venv-pdf
.venv-pdf/bin/python -m pip install --upgrade pip
.venv-pdf/bin/pip install -r requirements-pdf-page.txt
```

Przykładowe użycie:

```bash
.venv-pdf/bin/python pdf_page_to_markdown.py 119
```

Powstaną:

```text
neway/119/119.jpg
neway/119/119.md
```

Można też przekazać ścieżkę:

```bash
.venv-pdf/bin/python pdf_page_to_markdown.py neway/119/119.pdf
```

Albo stronę z pełnego PDF-u:

```bash
.venv-pdf/bin/python pdf_page_to_markdown.py neway/plik.pdf --page 119
```

Nadpisanie istniejących wyników:

```bash
.venv-pdf/bin/python pdf_page_to_markdown.py 119 --force
```

Sprawdziłem wszystkie 331 stron:

* 331/331 przetworzonych bez wyjątku;
* pusta strona 268 prawidłowo daje pusty Markdown;
* brak nierozpoznanych glifów Private Use Area;
* poprawnie odtwarzane są m.in. `**f^35^**`, `**K^r^**`, `P^46^`, `ℵ`, greka i `\|\|`;
* wyniki stron 100 i 119 przeszły test renderowania przez Pandoc;
* zweryfikowałem dostępność gotowych paczek ARM64 dla Pythona 3.12 i 3.14.

Samo uruchamianie po instalacji może odbywać się całkowicie offline. PyMuPDF również oficjalnie deklaruje lokalne przetwarzanie bez usług chmurowych: [PyMuPDF FAQ](https://pymupdf.readthedocs.io/en/latest/faq/index.html).

Jedno uczciwe ograniczenie: tekst będący wyłącznie częścią rastrowej ilustracji nie trafi do Markdownu, ale pozostaje wiernie widoczny w wygenerowanym JPG. Zwykła warstwa tekstowa PDF, w tym pogrubienia, kursywy, indeksy, greka, przypisy i tabele, jest przetwarzana.


---

Bo na Twoim dysku został **pierwszy, błędny wariant korzystający z API**. Drugi link miał tę samą nazwę, więc najwyraźniej plik nie został zastąpiony. To mój błąd.

Pobierz jednoznacznie nazwane pliki:

* [](sandbox:/workspace/scratch/2dd690abb72a/pickering-repo/pdf_page_to_markdown_local.py)
* [](sandbox:/workspace/scratch/2dd690abb72a/pickering-repo/requirements-pdf-page-local.txt)

Umieść je w `~/Projects/BogZachowalSwojTekst`, a następnie:

```bash
cd ~/Projects/BogZachowalSwojTekst
.venv-pdf/bin/pip install -r requirements-pdf-page-local.txt
.venv-pdf/bin/python pdf_page_to_markdown_local.py 92 --force
```

Ta wersja:

* nie wymaga `OPENAI_API_KEY`;
* nie importuje biblioteki `openai`;
* nie wywołuje żadnego endpointu;
* działa lokalnie przez PyMuPDF i PyMuPDF4LLM.

Możesz to potwierdzić:

```bash
grep -nE 'OPENAI_API_KEY|import openai|from openai' pdf_page_to_markdown_local.py || echo "OK — brak OpenAI API"
```

Powinno wyświetlić:

```text
OK — brak OpenAI API
```
