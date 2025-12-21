# Käyttöohje
Lataa ensin projektin viimeisimmän [releasen](https://github.com/Victheliar/Aineopintojen-harjoitusty-Ohjelmistotekniikka/releases) lähdekoodi (valitse _Assets_-osion alta kohta _Source code_).

## Konfigurointi
Tallennukseen käytetyt tiedostot luodaan _data-hakemistoon_. Tiedostojen nimet on kofiguroitu _.env_-tiedostossa, joka sijaitsee projektin juurihakemistossa. Tiedosto on muodoltaan seuraava:
```
DATABASE_FILENAME=database.sqlite
CALENDAR_FILENAME=calendar.csv
EVENT_FILENAME=event.csv
```
Halutessaan tiedostojen nimiä voi muokata.

## Ohjelman käynnistäminen
Ennen ohjelman käynnistämistä, asenna projektin riippuvuudet:
```bash
poetry install
```
Suorita tämän jälkeen vaadittavat alustustoimenpiteet:
```bash
poetry run invoke build
```
Käynnistä ohjelma:
```bash
poetry run invoke start
```
## Uuden käyttäjätunnuksen luominen
Kirjautumisnäkymästä voi siirtyä uuden käyttäjätunnuksen luomisnäkymään painamalla "Create new account". Uusi käyttäjä luodaan syöttämällä käyttäjätunnus ja salasana syötekenttiin ja painamalla "Create".

## Sisäänkirjautuminen
Sovellus käynnistyy automaattisesti kirjautumisnäkymään. Kirjautuminen tapahtuu kirjoittamalla olemassaoleva käyttäjätunnus ja salasana syötekenttiin ja painamalla "Login". Uloskirjautuminen onnistuu painamalla kalenterinäkymän ylänurkassa olevaa "Logout" painiketta. Uloskirjautumisen jälkeen käyttäjä palaa kirjautumisnäkymään.

## Tapahtuman lisääminen kalentetiin
Onnistuneen kirjautumisen jälkeen käyttäjä pääsee näkemään kalenterinsa. Kalenteriin voi lisätä uuden tapahtuman. Tämä onnistuu painamalla jotakin päivää kalenterista, minkä jälkeen avautuu tapahtuman luontinäkymä. Tapahtumalle voi kirjoittaa nimen ja kuvauksen, minkä jälkeen tapahtuma tallentuu painamalla "Create".
