## Tehtävä 2 - Sekvenssikaavio

```mermaid
 sequenceDiagram
   main -->> laitehallinto: HKLLaitehallinto()
   main -->> rautatietori: Lataajalaite()
   main -->> ratikka6: Lukijalaite()
   main -->> bussi 244: Lukijalaite()
   main -->> laitehallinto: lisaa_lataaja(rautatietori)
   main -->> laitehallinto: lisaa_lukija(ratikka6)
   main -->> laitehallinto: lisaa_lukija(bussi244)
   main -->> lippu_luukku: Kioski()
   main -->> lippu_luukku: osta_matkakortti("Kalle")
   lippu_luukku -->> kallen_kortti: Matkakortti("Kalle")
   main -->> lippu_luukku: lataa_arvoa(kallen_kortti, 3)
   lippu_luukku -->> kallen_kortti.kasvata_arvoa(3)
   main -->> ratikka6: osta_lippu(kallen_kortti, 0)
   ratikka6 -->> Lukijalaite: osta_lippu(kallen_kortti, 0)
   main -->> bussi244: osta_lippu(kallen_kortti, 0)
   ratikka6 -->> Lukijalaite: osta_lippu(bussi244, 0)
```