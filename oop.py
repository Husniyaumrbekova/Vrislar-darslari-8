class Talaba:
    def init(self,ism,familya,otasi,tyil):
        self.name = ism
        self.firstname = familya
        self.otasi= otasi
        self.tyil = tyil
    def FIO(self):
        return f"{self.firstname} {self.name} {self.otasi} "
    def yoshi(self):
        return f"{2026-self.tyil} - yoshda"
talaba1 = Talaba('Anvar','Murodov','Boburbekovich',2020)
talaba2 = Talaba("Xursandbek","O'ktamboyev","Bunyodovich",2011)
talaba3 = Talaba("Muhammadjon",'Mammatjumayev','Sherzodovich',2011)
talaba4 = Talaba("Asadbek",'Ruziboyev','Umirbekovich',1999)
print(talaba3.name, talaba3.tyil)
print(talaba3.yoshi())

class Mashinalar:
    def init(self, nomi, rangi, yili):
        self.nomi = nomi
        self.rangi = rangi
        self.yili = yili
    def data(self):
        return f"{self.nomi} {self.rangi} {self.yili}"
mashina1 = Mashinalar("Lacetti", "Qora", 2010)
mashina2 = Mashinalar("Nexia", "Oq", 2012)
mashina3 = Mashinalar("Damas", "Sariq", 2015)
print(mashina1.data())

class Moshinalar:
    def init(self, nomi, rangi, kampaniya_modeli, yili, otkuchi,orindiq):
        self.nomi = nomi
        self.rangi = rangi
        self.modeli = kampaniya_modeli
        self.yil = yili
        self.otkuchi = otkuchi
        self.orindiq = orindiq
    def data(self):
        return f"{self.modeli} kampaniyasining {self.nomi} nomli {self.rangi}, yili {self.yil}, {self.otkuchi} ot kuchli {self.orindiq} o'rindiqli avtamabili"
    
m1 = Moshinalar("Cobalt","Oq","GM",2020, 105, 5)
m2 = Moshinalar("M5","Qora",'BMW',2021,385,5)
m3 = Moshinalar("Carneval",'Oq','KIA',2026,215,7)
print(m3.data())

