# Assoziation

class Maschine:

    def produziert(self):
        return Werkstueck() # return "Hallo"


class Werkstueck(): # Struktur

    def __init__(self): #Definition
        self.material = "Holz"
        self.hoehe = 2.0

#Idee: Maschine produziert Werkstück

# so "Normal"
w1 = Werkstueck() #Konstruktoraufruf
w2 = Werkstueck()
print(w1.hoehe)


#Jetzt über die Maschine:
m1 = Maschine()
w3= m1.produziert() # W3 ist ein Objekt vom Typ Werkstueck
print(w3.material)

#Aufgabe: Maschinennummer soll in Werkstück gespeichert werden


