# Ohjelmistotekniikka, harjoitustyö

Sovelluksen avulla on mahdollista seurata omaa henkilökohtaista kalenteria sekä lisätä sinne tulevia tapahtumia.

[Harjoitustyön vaatimusmäärittely](/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](/dokumentaatio/tuntikirjanpito.md)

[Changelog](/dokumentaatio/changelog.md)

[Arkkitehtuuri](/dokumentaatio/arkkitehtuuri.md)

## Asennus
1. Asenna riippuvuudet:
```bash
poetry install
```
2. Suorita vaadittavat alustustoimentpiteet:
```bash
poetry run invoke build
```   
3. Käynnistä sovellus:
```bash
poetry run invoke start
```
## Komentorivikomennot

### Testaus

Testit voi suorittaa komennolla:
```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```
Raportti generoituu _htmlcov_-hakemistoon

### Pylint

Tiedoston [.pylintrc](/.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
