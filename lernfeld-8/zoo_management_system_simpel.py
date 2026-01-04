import csv

# Basisklasse Tier
class Tier:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
        self.art = "Tier"
    
    def sprich(self):
        return "Ich bin ein Tier"
    
    def beschreibung(self):
        return f"Name: {self.name}, Alter: {self.alter} Jahre"
    
    def __str__(self):
        return f"{self.art} {self.name} ({self.alter} Jahre)"

# Löwe
class Loewe(Tier):
    def __init__(self, name, alter):
        super().__init__(name, alter)
        self.art = "Löwe"
    
    def sprich(self):
        return "Ich brülle"

# Papagei
class Papagei(Tier):
    def __init__(self, name, alter):
        super().__init__(name, alter)
        self.art = "Papagei"
        self.flugfaehig = True
    
    def sprich(self):
        return "Ich spreche wie ein Mensch"

# Elefant
class Elefant(Tier):
    def __init__(self, name, alter):
        super().__init__(name, alter)
        self.art = "Elefant"
    
    def sprich(self):
        return "Ich trompete"

# Zoo
class Zoo:
    def __init__(self):
        self.tiere = []
    
    def tier_hinzufuegen(self, tier):
        self.tiere.append(tier)
    
    def alle_tiere_zeigen(self):
        print("\n=== Alle Tiere im Zoo ===")
        for tier in self.tiere:
            print(tier)
            print(f"  {tier.beschreibung()}")
            print(f"  {tier.sprich()}")
            print()
    
    def suche_nach_art(self, art):
        print(f"\n=== Suche nach: {art} ===")
        for tier in self.tiere:
            if tier.art == art:
                print(tier)

# CSV erstellen
def csv_erstellen():
    tiere = [
        ["Art", "Name", "Alter"],
        ["Löwe", "Simba", "8"],
        ["Papagei", "Polly", "3"],
        ["Elefant", "Jumbo", "25"],
        ["Löwe", "Nala", "6"],
        ["Papagei", "Koko", "12"]
    ]
    
    with open("tiere.csv", "w", newline="") as datei:
        writer = csv.writer(datei)
        writer.writerows(tiere)

# Tiere aus CSV laden
def tiere_laden(zoo):
    with open("tiere.csv", "r") as datei:
        reader = csv.reader(datei)
        next(reader)  # Header überspringen
        
        for zeile in reader:
            art, name, alter = zeile
            alter = int(alter)
            
            if art == "Löwe":
                tier = Loewe(name, alter)
            elif art == "Papagei":
                tier = Papagei(name, alter)
            elif art == "Elefant":
                tier = Elefant(name, alter)
            
            zoo.tier_hinzufuegen(tier)

# Hauptprogramm
def main():
    # Zoo erstellen
    zoo = Zoo()
    
    # Tiere manuell hinzufügen
    zoo.tier_hinzufuegen(Loewe("König", 10))
    zoo.tier_hinzufuegen(Papagei("Charlie", 5))
    zoo.tier_hinzufuegen(Elefant("Dumbo", 15))
    
    # CSV erstellen und laden
    csv_erstellen()
    tiere_laden(zoo)
    
    # Alle Tiere zeigen
    zoo.alle_tiere_zeigen()
    
    # Nach Art suchen
    zoo.suche_nach_art("Löwe")
    zoo.suche_nach_art("Papagei")
    zoo.suche_nach_art("Elefant")

if __name__ == "__main__":
    main()