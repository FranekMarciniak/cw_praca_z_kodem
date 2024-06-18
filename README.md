# Automatyzacja testów API z wykorzystaniem curl

## Opis

Skrypt `test_api.py` automatycznie testuje różne endpointy PokeAPI przy użyciu narzędzia curl.

## Użycie

1. Zainstaluj Python 3.
2. Uruchom skrypt: `python3 test_api.py`.

## Testowane endpointy

- https://pokeapi.co/api/v2/pokemon/1 - Sprawdza informacje o Pokemonie Bulbasaur.
- https://pokeapi.co/api/v2/type/1 - Sprawdza informacje o typie Normal.
- https://pokeapi.co/api/v2/ability/1 - Sprawdza informacje o zdolności Stench.


Makefile docs:

By zainstalować dependencje:

```bash
make deps
```

By uruchomić testy:

```bash
make test
```

By uruchomić skrypt:

```bash
make run
```