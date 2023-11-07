# Scrapy-olx-2108107010017 MOTOR BEKAS

---
## Tujuan

Project ini bertujuan untuk melakukan web scraping pada situs web OLX sehingga mendapatkan informasi mengenai motor bekas yaitu nama brand, tahun, lokasi dan harga dari mobil bekas tersebut.

## Langkah-langkah

1. *Buat Environment*
```bash

   python -m venv env-scrapy
```
3. *Aktifkan Python virtual environment*
```bash
  source env-scrapye/bin/activate
```
4. *Install Scrapy*
```bash
    pip install scrapy
```
5. *Buat project Scrapy baru*
```bash
    scrapy startproject olx_scrapy
```
7. *Jalankan spider yang akan menghasilkan format output JSON*
```bash
    scrapy crawl myspider -o output.json
```
