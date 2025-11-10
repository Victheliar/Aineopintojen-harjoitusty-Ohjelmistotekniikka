import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        self.kortti = Maksukortti(10)
    
    def test_kassan_rahamaara_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_kassan_lounasmaara_oikein(self):
        self.assertEqual((self.kassapaate.edulliset + self.kassapaate.maukkaat), 0)
    
    def test_edullinen_lounas_ostettu_kateisella1(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        
    def test_edullinen_lounas_ostettu_kateisella2(self):
        vaihto = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihto, 60)
    
    def test_edullinen_lounas_ostettu_kateisella3(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_maukas_lounas_ostettu_kateisella1(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_maukas_lounas_ostettu_kateisella2(self):
        vaihto = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihto, 100)
        
    def test_maukas_lounas_ostettu_kateisella3(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        
    def test_kateismaksu_ei_onnistu_edullinen1(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kateismaksu_ei_onnistu_edullinen2(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        
    def test_kateismaksu_ei_onnistu_edullinen3(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kateismaksu_ei_onnistu_maukas1(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kateismaksu_ei_onnistu_edullinen2(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)
    
    def test_kateismaksu_ei_onnistu_edullinen3(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_edullisen_osto_kortilla1(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
    
    def test_edullisen_osto_kortilla2(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_maukkaan_osto_kortilla1(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
    
    def test_maukkaan_osto_kortilla2(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_rahamaara_ei_muutu1(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 10)
    
    def test_rahamaara_ei_muutu2(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 10)
    
    def test_lounaiden_maara1(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_lounaiden_maara2(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_osto_epaonnistuu1(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti), False)
    
    def test_osto_epaonnistuu2(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), False)

    def test_kassalla_oleva_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_lataa_rahaa_kortille1(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_lataa_rahaa_kortille2(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kassassa_rahaa_euroina(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)