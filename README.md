# Lesson 23 - Python homework

Projekt zawiera dwa proste programy konsolowe napisane w Pythonie:

1. `src/text_analyzer.py` - analiza tekstu podanego przez użytkownika.
2. `src/address_book.py` - prosta książka adresowa przechowująca kontakty w słowniku.

## Zadanie 1: analiza tekstu

Program przyjmuje tekst od użytkownika i wyświetla:

- liczbę znaków razem ze spacjami,
- liczbę znaków bez spacji i innych białych znaków,
- liczbę słów,
- liczbę zdań zakończonych `.`, `!` albo `?`,
- najdłuższe słowo,
- najczęściej występujące słowo lub słowa.

Przy liczeniu słów program ignoruje wielkość liter oraz znaki interpunkcyjne.

Uruchomienie:

```bash
python3 src/text_analyzer.py
```

Przykład:

```text
Analiza tekstu
Podaj tekst do analizy: Ala ma kota. Ala lubi Python!

Statystyki tekstu:
Liczba znaków (ze spacjami): 29
Liczba znaków (bez spacji): 24
Liczba słów: 6
Liczba zdań: 2
Najdłuższe słowo: python
Najczęściej występujące słowo/słowa: ala (2 razy)
```

## Zadanie 2: książka adresowa

Program udostępnia menu z opcjami:

- dodanie kontaktu,
- wyświetlenie wszystkich kontaktów,
- wyszukanie kontaktu po imieniu lub nazwisku,
- usunięcie kontaktu,
- edycja kontaktu,
- zakończenie programu.

Kontakty są przechowywane w słowniku, w którym kluczem jest unikalne ID kontaktu.
Program sprawdza podstawową poprawność danych: imię i nazwisko nie mogą być puste,
telefon musi składać się wyłącznie z cyfr, a email musi mieć podstawowy poprawny format.

Uruchomienie:

```bash
python3 src/address_book.py
```

## Testy

Testy jednostkowe sprawdzają najważniejsze funkcje obu programów.

```bash
python3 -m unittest discover -s tests
```

## Struktura projektu

```text
.
├── README.md
├── docs/
│   └── verification.md
├── src/
│   ├── address_book.py
│   └── text_analyzer.py
└── tests/
    ├── test_address_book.py
    └── test_text_analyzer.py
```
