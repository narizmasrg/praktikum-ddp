class Gempa:
  #member1 variabel
  lokasi = ""
  skala = 0
  #member2 konstruktor
  def __init__(self, lokasi, skala):
    self.lokasi = lokasi
    self.skala = skala
  #member3 method
  def dampak(self):
    if(self.skala < 2):
      ket = 'Tidak terasa'
    elif(self.skala >= 2 and self.skala < 4):
      ket = 'Bangunan retak-retak'
    elif(self.skala >= 4 and self.skala <6):
      ket = 'Bangunan pada roboh'
    else:
      ket = 'Berpotensi tsunami'
    print('Telah terjadi gempa di' , self.lokasi,
          ' dengan skala',self.skala,'richter'
          'berdampak', ket)
    
#from Gempa import *
#buat object
g1 = Gempa('Banten',1.2)
g2 = Gempa('Palu',6.1)
g3 = Gempa('Cianjur',5.6)
g4 = Gempa('Jayapura',3.3)
g5 = Gempa('Garut',4.0)

#panggil funsi di class Gempa
g1.dampak()
g2.dampak()
g3.dampak()
g4.dampak()
g5.dampak()
