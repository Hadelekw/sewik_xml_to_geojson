Prosty konwertor plików XML pobranych z [Systemu Ewidencji Wypadków i Kolizji (SEWIK)](https://sewik.pl/) na pliki typu GeoJSON.

Simple converter of the XML files downloaded from the Polish Accident and Collision Recording System (commonly known as SEWIK) into GeoJSON files. For the English version of this document, look into [README.en.md](README.en.md).

## Sposób użycia
Aby użyć konwertora należy wywołać następujące polecenie:
```
python main.py input_file_path.xml output_file_path.geojson
```
Domyślnie nazwy pól z pliku wsadowego są tłumaczone z języka polskiego pisanego w formacie pascal case and język angielski pisany snake case. Jest to robione, aby zachować standardy nazewnictwa zmiennych w języku Python. Jeżeli użytkownik nie będzie chciał tego formatowania, należy zmienić zmienną `FIELD_MAP` w pliku `settings.py` na jedno ze wcześniej przygotowanych mapowań lub `None` w przypadku zachowania domyślnych nazw pól. Pominięcie pola w mapowaniu oznacza pominięcie go w pliku wynikowym.
