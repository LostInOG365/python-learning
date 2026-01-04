# Beispiel für das Überschreiben



class Tier(): # Elternklasse

    def __init__(self):
        self.name = "Tiername" # public

    def fressen(self):
        print("Ich esse alles")


class Lebewesen():

    #def __init__(self):
    gewicht = 6.0

    def fressen(self):
        print("Fressen eines Lebewesens")



class Hund(Lebewesen,Tier): # Kindklasse, Hier wird geerbt, Mehrfachvererbung

    def fressen(self):
        print("Ich fresse nur Hundefutter")


class Katze(Tier): # Kindklasse
    def fressen(self):
        print("Ich fresse nur Katzenfutter")



mein_hund = Hund()
print(mein_hund.name)
mein_hund.fressen()
print(mein_hund.gewicht)

print(Hund.mro()) # MRO-Methode: Method Resolution Order
