# Arkkitehtuurikuvaus

## Rakenne
Ohjelman koodin perusrakenne toimii seuraavasti: Pakkauksessa _ui_ oleva koodi vastaa käyttöliittymästä, _services_ sovelluslogiikasta ja _repositories_ tietojen tallennuksesta. _entities_ puolestaan sisältää sovelluksen käyttämiä tietokohteita kuvastavia luokkia.

## Käyttöliittymä
Käyttölittymä sisältää kolme erillistä näkymää:

* Uuden käyttäjätilin luominen
* Kirjautuminen
* Kalenterinäkymä

Jokainen näkymä on toteutettu omaan luokkaan. Yksi näkymistä on aina kerrallaan näkyvänä. Näkymien näyttämisestä, vaihtamisesta ja poistamisesta vastaa [UI](../src/ui/ui.py)-luokka. Käyttöliittymä on pyritty eristämään sovelluslogiikasta mahdollisimman paljon.

## Sovelluslogiikka

Sovelluksen tietomallin muodostavat luokat [User](../src/entities/user.py), [Calendar](../src/entities/calendar.py) ja [Event](../src/entities//event.py). Luokat kuvaavat käyttäjiä, käyttäjän kalenteria ja kalenteriin lisättäviä tapahtumia:

```mermaid
    classDiagram
        Event "*" --> "1" Calendar
        Calendar "*" --> "1" User
        class User{
            username
            password
        }
        class Calendar{
            id
        }
        class Event{
            id
            content
        }
```
Luokka [CalendarService](../src/services/calendar_service.py) vastaa ohjelman toiminnallisista kokonaisuuksista. Luokka tarjoaa jokaiselle sisältämälleen käyttäjäliittymän toiminnolle oman metodin, joita ovat esim.

* create_user(username, password)
* login(username, password)
* create_calendar()

Kalenteriin lisättävien tapahtumien hallinta on eristetty omalle luokalleen [EventService](../src/services/event_service.py). Luokka tarjoaa mm. seuraavia metodeja:

* create_event(content, date)
* get_events()

Molemmat luokat pääsevät käsiksi käyttäjä- ja kalenteritietoihin tietojen tallentamisesta vastaavien luokkien [UserRepository](../src/repositories/user_repository.py), [CalendarRepository](../src/repositories/calendar_repository.py) ja [EventRepository](../src/repositories/event_repository.py) avulla. Luokkien toteutuksen injektoidaan sovelluslogiikasta vastaavaan koodiin konstruktorikutsun yhteydessä. 

## Tietojen tallennus
Pakkauksen _repositories_ sisältämät luokat ```UserRepository```, ```CalendarRepository``` ja ```EventRepository``` vastaavat tietojen pysyvästä tallentamisesta. Luokat ```CalendarRepository``` ja ```EventRepository``` tallentavat tiedot CSV-tiedostoon, kun taas ```UserRepository``` puolestaan SQLite-tietokantaan. Luokkia on tarpeen vaatiessa mahdollista uusilla toteutuksilla, jos tallennustapoja pitää vaihtaa. Testauksessa käytetään tiedostoon ja tietokantaan tallentavien olioiden sijaan keskusmuistiin tallentavia toteutuksia.

## Tiedostot
Sovellus tallettaa käyttäjien ja kalenterien tiedot erillisiin tiedostoihin. Sovelluksen juuressa sijaitseva konfiguraatiotiedosto [.env](/.env) määrittelee tiedostojen nimet.

CSV-tiedostoihin tiedot tallennetaan seuraavissa formaateissa:
1. calendar.csv:
```
1f3e111a-b2cb-4b86-9787-c1ab1ced4cde;vici
0b84df0c-bc62-427d-9894-56f223d600a1;kalle
```
Eli kalenterin id ja käyttäjän käyttäjätunnus.
2. 
```
55cda479-855d-4c35-b305-cd4d8f1d0ed0;lecture;2025-12-09;vici;1f3e111a-b2cb-4b86-9787-c1ab1ced4cde
```
Eli tapahtuman id, tapahtuman sisältö, tapahtuman päivämäärä, käyttäjän käyttäjänimi ja kalenterin id. Molemmissa tiedostoissa kenttien arvot erotellaan puolipisteellä (;).

Käyttäjien tiedot tallennetaan SQLite-tietokannan tauluus ```Users```, joka alustetaan [initialize_database.py](../src/initialize_database.py)-tiedostossa.

## Päätoiminnallisuudet
### Uuden käyttäjätunnuksen luominen
Uuden käyttäjätunnuksen voi luoda käyttäjän luomisnäkymässä syöttämällä käyttäjätunnus, joka ei ole vielä käytössä sekä salasana, joka on vähintään 3 merkkiä pitkä. Tämän jälkeen painamalla "Create" etenee sovellus seuraavasti:
```mermaid
sequenceDiagram
    actor User
    participant UI
    participant CalendarService
    participant UserRepository
    participant vici
    User->>UI: click "Create new account" button
    UI->>CalendarService: create_user("vici", "vici123")
    CalendarService->>UserReposiroty: find_by_username("vici")
    UserRepository-->>CalendarService: None
    CalendarService->>UserRepository: create(vici)
    UserRepository-->>CalendarService: user
    CalendarService-->>UI: user
    UI->>UI: show_calendar_view()
```
Tapahtumakäsittelijä kutsuu create_user-metodia, jonka parametreiksi annetaan luotavan käyttäjän käyttäjätunnus ja salasana. Tämän jälkeen sovelluslogiikka selvittää ```UserRepository```:n avulla, onko käyttäjätunnus vapaa. Jos on, käyttäjätunnuksen luomin onnistuu, jolloin sovelluslogiikka luo ```User```-olion ja tallentaa sen kutsumalla ```UserRepository```:n metodia ```create```. Uusi käyttäjä kirjataan automaattisesti sisään, jolloin käyttöliittymän näkymäksi tulee ```CalendarView```.

### Sisäänkirjautuminen
Käyttäjä voi kirjautua sovellukseen sisään syöttämällä kirjautumisnäkymän syötekenttiin käyttäjätunnuksensa ja salasanansa. Tämän jälkeen painamalla painiketta _Login_, etenee sovellus seuraavasti:
```mermaid
SequenceDiagram
    actor User
    participant UI
    participant CalendarService
    participant UserRepository
    User->>UI: click "Login" button
    UI->>CalendarService: login("vici", "vici123")
    CalendarService->>UserRepository: find_by_username("vici")
    UserRepository-->>CalendarService: user
    CalendarService-->>UI: user
    UI->UI: show_calendar_view()
```
Eli ```CalendarService```:n metodia login kutsutaan antaen sille parametriksi käyttäjätunnuksen ja salasanan. Tämän jälkeen sovelluslogiikka selvittää ```UserRepository```:n avulla, onko käyttäjätunnus olemassa ja täsmäävätkö salasanat. Jos molemmat asiat pitävät paikkaansa, sisäänkirjautuminen onnistuu, minkä seurauksena käyttöliittymän näkymäksi tulee ```CalendarView```, eli sovelluksen päänäkymä. Näkymälle renderöidään myös kirjautuneen käyttäjän kalenteriin lisätyt tapahtumat.

<!-- ![architecture](architecture.jpg) -->
<!-- ![sequence](sekvenssikaavio.jpg) -->