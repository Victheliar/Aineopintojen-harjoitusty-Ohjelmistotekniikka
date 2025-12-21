# Testausdokumentti
Ohjelman testaus on toteutettu automatisoitujen yksikkötestien avulla unittestilla. Sen lisäksi on toteutettu manuaalisia järjestelmätason testejä.

## Yksikkötestaus
### Sovelluslogiikka
Sovelluslogiikasta vastaavia luokkia `CalendarService` ja `EventService` testataan testiluokilla [TestCalendarService](../src/tests/services/calendar_service_test.py) ja [TestEventService](../src/tests/services/event_service_test.py). Testauksessa luokille injektoidaan repositorio-oliot, jotka tallentavat tietoa muistiin pysyvän tallennuksen sijaan. Tähän tarkoitukseen on luotu luokat `FakeUserRepository`, `FakeCalendarRepository` ja `FakeEventRepository`. 

### Repositoriot
Repositoriot `CalendarREpository`, `UserRepository` ja `EventRepository` testataan testeissä käytössäolevilla tiedostoilla, joiden nimet on konfiguroitu _.env.test_-tiedostoon. 