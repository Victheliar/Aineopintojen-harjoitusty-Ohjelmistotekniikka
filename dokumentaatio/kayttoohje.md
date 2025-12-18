# Käyttöohje
Lataa ensin projektin viimeisimmän [releasen](https://github.com/Victheliar/Aineopintojen-harjoitusty-Ohjelmistotekniikka/releases) lähdekoodi. Tämä onnistuu valitsemalla _Assets_-osion alta _Source code_.

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
Sovellus käynnistyy automaattisesti kirjautumisnäkymään. Kirjautuminen tapahtuu kirjoittamalla olemassaoleva käyttäjätunnus ja salasana syötekenttiin ja painamalla "Login".

## Tapahtuman lisääminen kalentetiin
Onnistuneen kirjautumisen jälkeen käyttäjä pääsee näkemään kalenterinsa. Kalenteriin voi lisätä uuden tapahtuman. Tämä onnistuu painamalla jotakin päivää kalenterista, minkä jälkeen avautuu tapahtuman luontinäkymä. Tapahtumalle voi kirjoittaa nimen ja kuvauksen, minkä jälkeen tapahtuma tallentuu painamalla "Create".