import csv
import os

# Basisklasse Tier
class Tier:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
        self.art = "Unbekannt"
    
    def sprich(self):
        return "Ich bin ein Tier"
    
    def beschreibung(self):
        return f"Name: {self.name}, Alter: {self.alter} Jahre, Art: {self.art}"
    
    def __str__(self):
        return f"{self.art} '{self.name}' ({self.alter} Jahre)"

# Kindklasse Löwe
class Loewe(Tier):
    def __init__(self, name, alter, maehnen_farbe="braun"):
        super().__init__(name, alter)
        self.art = "Löwe"
        self.maehnen_farbe = maehnen_farbe
    
    def sprich(self):
        return "Ich brülle"
    
    def jagen(self):
        return f"{self.name} jagt in der Savanne"
    
    def beschreibung(self):
        return f"{super().beschreibung()}, Mähnenfarbe: {self.maehnen_farbe}"

# Kindklasse Papagei
class Papagei(Tier):
    def __init__(self, name, alter, flugfaehig=True, farbe="bunt"):
        super().__init__(name, alter)
        self.art = "Papagei"
        self.flugfaehig = flugfaehig
        self.farbe = farbe
    
    def sprich(self):
        return "Ich spreche wie ein Mensch"
    
    def fliegen(self):
        if self.flugfaehig:
            return f"{self.name} fliegt durch die Luft"
        else:
            return f"{self.name} kann nicht fliegen"
    
    def beschreibung(self):
        flug_status = "flugfähig" if self.flugfaehig else "nicht flugfähig"
        return f"{super().beschreibung()}, Farbe: {self.farbe}, {flug_status}"

# Kindklasse Elefant
class Elefant(Tier):
    def __init__(self, name, alter, gewicht=5000):
        super().__init__(name, alter)
        self.art = "Elefant"
        self.gewicht = gewicht
    
    def sprich(self):
        return "Ich trompete"
    
    def baden(self):
        return f"{self.name} badet im Wasser"
    
    def beschreibung(self):
        return f"{super().beschreibung()}, Gewicht: {self.gewicht} kg"

# Zoo-Klasse
class Zoo:
    def __init__(self, name="Mein Zoo"):
        self.name = name
        self.tiere = []
    
    def tier_hinzufuegen(self, tier):
        self.tiere.append(tier)
        print(f"{tier.name} wurde zum Zoo hinzugefügt!")
    
    def alle_tiere_zeigen(self):
        print(f"\n=== Alle Tiere im {self.name} ===")
        if not self.tiere:
            print("Der Zoo ist leer.")
            return
        
        for i, tier in enumerate(self.tiere, 1):
            print(f"\n{i}. {tier}")
            print(f"   Beschreibung: {tier.beschreibung()}")
            print(f"   Laut: {tier.sprich()}")
    
    def suche_nach_art(self, art):
        gefundene_tiere = [tier for tier in self.tiere if tier.art.lower() == art.lower()]
        
        print(f"\n=== Suche nach Art: {art} ===")
        if not gefundene_tiere:
            print(f"Keine Tiere der Art '{art}' gefunden.")
            return
        
        for tier in gefundene_tiere:
            print(f"- {tier}")
            print(f"  {tier.beschreibung()}")
    
    def __str__(self):
        return f"Zoo '{self.name}' mit {len(self.tiere)} Tieren"

# Hilfsfunktionen für CSV-Verarbeitung
def csv_erstellen():
    """Erstellt eine CSV-Datei mit Beispieltieren"""
    tiere_daten = [
        ["Art", "Name", "Alter", "Besonderheit1", "Besonderheit2"],
        ["Löwe", "Simba", "8", "goldbraun", ""],
        ["Papagei", "Polly", "3", "True", "rot-grün"],
        ["Elefant", "Jumbo", "25", "6000", ""],
        ["Löwe", "Nala", "6", "hellbraun", ""],
        ["Papagei", "Koko", "12", "False", "blau-gelb"]
    ]
    
    with open("zoo_tiere.csv", "w", newline="", encoding="utf-8") as datei:
        writer = csv.writer(datei)
        writer.writerows(tiere_daten)
    
    print("CSV-Datei 'zoo_tiere.csv' wurde erstellt!")

def tiere_aus_csv_laden(zoo):
    """Lädt Tiere aus einer CSV-Datei in den Zoo"""
    if not os.path.exists("zoo_tiere.csv"):
        print("CSV-Datei nicht gefunden. Erstelle eine neue...")
        csv_erstellen()
    
    with open("zoo_tiere.csv", "r", encoding="utf-8") as datei:
        reader = csv.reader(datei)
        next(reader)  # Header überspringen
        
        for zeile in reader:
            art, name, alter, besonderheit1, besonderheit2 = zeile
            alter = int(alter)
            
            if art == "Löwe":
                tier = Loewe(name, alter, besonderheit1 if besonderheit1 else "braun")
            elif art == "Papagei":
                flugfaehig = besonderheit1.lower() == "true" if besonderheit1 else True
                tier = Papagei(name, alter, flugfaehig, besonderheit2 if besonderheit2 else "bunt")
            elif art == "Elefant":
                gewicht = int(besonderheit1) if besonderheit1 else 5000
                tier = Elefant(name, alter, gewicht)
            else:
                tier = Tier(name, alter)
            
            zoo.tier_hinzufuegen(tier)

# Hauptprogramm
def main():
    print("=== Zoo-Verwaltungssystem ===")
    
    # Zoo erstellen
    mein_zoo = Zoo("Karlsruher Tiergarten")
    print(f"\n{mein_zoo} wurde erstellt!")
    
    # Tiere manuell erstellen und hinzufügen
    print("\n--- Manuelle Tiererstellung ---")
    loewe1 = Loewe("König", 10, "dunkelbraun")
    papagei1 = Papagei("Charlie", 5, True, "rot-blau")
    elefant1 = Elefant("Dumbo", 15, 4500)
    
    mein_zoo.tier_hinzufuegen(loewe1)
    mein_zoo.tier_hinzufuegen(papagei1)
    mein_zoo.tier_hinzufuegen(elefant1)
    
    # Tiere aus CSV laden
    print("\n--- Tiere aus CSV laden ---")
    tiere_aus_csv_laden(mein_zoo)
    
    # Alle Tiere anzeigen
    mein_zoo.alle_tiere_zeigen()
    
    # Suche nach bestimmten Arten
    mein_zoo.suche_nach_art("Löwe")
    mein_zoo.suche_nach_art("Papagei")
    mein_zoo.suche_nach_art("Elefant")
    
    # Spezielle Methoden demonstrieren
    print("\n=== Spezielle Tier-Fähigkeiten ===")
    for tier in mein_zoo.tiere:
        if isinstance(tier, Loewe):
            print(f"- {tier.jagen()}")
        elif isinstance(tier, Papagei):
            print(f"- {tier.fliegen()}")
        elif isinstance(tier, Elefant):
            print(f"- {tier.baden()}")
    
    print(f"\n--- Zoo-Statistik ---")
    print(f"Gesamt: {len(mein_zoo.tiere)} Tiere")
    arten_count = {}
    for tier in mein_zoo.tiere:
        arten_count[tier.art] = arten_count.get(tier.art, 0) + 1
    
    for art, anzahl in arten_count.items():
        print(f"{art}: {anzahl}")

if __name__ == "__main__":
    main()