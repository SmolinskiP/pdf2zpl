
# Skrypt do drukowania etykiet Zebra

Ten skrypt konwertuje plik PDF na format ZPL (Zebra Programming Language) i wysyła go do drukarki etykiet Zebra. Zawiera funkcje do:

- Konwersji PDF na obraz
- Zmiany rozmiaru obrazu do wymiarów etykiety
- Konwersji obrazu na format ZPL
- Wysyłania kodu ZPL przez Ethernet lub port szeregowy
- Zapisania kodu ZPL do pliku

## Wymagania

- Python 3.x
- Zainstaluj wymagane biblioteki używając:
  ```bash
  pip install pdf2image pillow pyserial
  ```
- Poppler dla Windows (dodaj do `PATH` lub wskaż `poppler_path`)

## Użycie

1. **Konwersja PDF i zapisanie ZPL do pliku**:
   ```python
   save_zpl_to_file(zpl_command, 'moja_etykieta.zpl')
   ```

2. **Wysyłanie ZPL do drukarki przez Ethernet**:
   ```python
   send_zpl_over_ethernet(zpl_command, '192.168.0.1')
   ```

3. **Wysyłanie ZPL do drukarki przez port szeregowy**:
   ```python
   send_zpl_over_serial(zpl_command, 'COM3')
   ```

## Wymiary Etykiety

- Domyślna szerokość etykiety: 10.16 cm (4 cale)
- Domyślna wysokość etykiety: 15.24 cm (6 cali)
- DPI: 300

Możesz dostosować te wymiary, zmieniając wartości `label_width_cm`, `label_height_cm` i `dpi` w skrypcie.

## Uwagi

- Upewnij się, że adres IP drukarki i konfiguracja portu szeregowego są poprawne przed wysyłaniem danych.
- Skrypt przetwarza tylko pierwszą stronę pliku PDF.

## Przykład

Konwertuj i wyślij etykietę PDF przez Ethernet:
```python
send_zpl_over_ethernet(zpl_command, '192.168.0.1')
```
