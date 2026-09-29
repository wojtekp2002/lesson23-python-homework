# Verification

Projekt został sprawdzony testami jednostkowymi:

```bash
python3 -m unittest discover -s tests
```

Sprawdzone są między innymi:

- ignorowanie interpunkcji i wielkości liter w analizatorze tekstu,
- liczenie znaków, słów i zdań,
- obsługa pustego tekstu,
- dodawanie, wyszukiwanie, edycja i usuwanie kontaktu,
- unikalne ID kontaktów,
- walidacja błędnych danych kontaktu.
