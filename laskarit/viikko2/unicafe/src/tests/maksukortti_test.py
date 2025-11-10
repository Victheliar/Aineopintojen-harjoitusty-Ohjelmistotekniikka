import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
        
    def test_kortin_saldo_on_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 1000)
    
    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(self.maksukortti.saldo, 1500)
        
    def test_saldo_vahenee_oikein_jos_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(self.maksukortti.saldo, 500)
    
    def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(2000)
        self.assertEqual(self.maksukortti.saldo, 1000)
    
    def test_rahat_riittaa(self):
        testi = self.maksukortti.ota_rahaa(500)
        self.assertEqual(testi, True)
    
    def test_rahat_eivat_riita(self):
        testi = self.maksukortti.ota_rahaa(2000)
        self.assertEqual(testi, False)
        
    def test_saldo_euroina(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
    
    def test_str(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")   
