import csv

# Basisklasse
class Tier:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
        self.art = "Unbekannt"

    def sprich(self):
        return "Ich bin ein Tier"

    def beschreibung(self):
        return f"{self.name} ist {self.alter} Jahre alt und gehört zur Art: {self.art}"

    def __str__(self):
        return f"{self.art} namens {self.name}, Alter: {self.alter}"


# Kindklassen
class Löwe(Tier):
    def __init__(self, name, alter):
        super().__init__(name, alter)
        self.art = "Löwe"

    def sprich(self):
        return "Ich brülle"


class Papagei(Tier):
    def __init__(self, name, alter, flugfähig=True):
        super().__init__(name, alter)
        self.art = "Papagei"
        self.flugfähig = flugfähig

    def sprich(self):
        return "Ich spreche wie ein Mensch"

    def __str__(self):
        flug = "flugfähig" if self.flugfähig else "nicht flugfähig"
        return f"{self.art} namens {self.name}, Alter: {self.alter}, {flug}"


class Elefant(Tier):
    def __init__(self, name, alter, gewicht=None):
        super().__init__(name, alter)
        self.art = "Elefant"
        self.gewicht = gewicht  # in Tonnen

    def sprich(self):
        return "Ich trompete"

    def __str__(self):
        gewicht_str = f", Gewicht: {self.gewicht} Tonnen" if self.gewicht else ""
        return f"{self.art} namens {self.name}, Alter: {self.alter}{gewicht_str}"


# Zoo-Verwaltung
class Zoo:
    def __init__(self):
        self.tiere = []

    def tier_hinzufuegen(self, tier):
        self.tiere.append(tier)

    def alle_tiere_zeigen(self):
        for tier in self.tiere:
            print(tier.beschreibung())
            print(tier.sprich())

    def suche_nach_art(self, art):
        gefundene_tiere = [t for t in self.tiere if t.art.lower() == art.lower()]
        for tier in gefundene_tiere:
            print(tier)


# CSV einlesen
def lese_tiere_aus_csv(dateipfad):
    tiere = []
    with open(dateipfad, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for zeile in reader:
            name = zeile["name"]
            alter = int(zeile["alter"])
            art = zeile["art"].lower()
            if art == "löwe":
                tiere.append(Löwe(name, alter))
            elif art == "papagei":
                tiere.append(Papagei(name, alter))
            elif art == "elefant":
                tiere.append(Elefant(name, alter))
    return tiere


# Hauptprogramm
if __name__ == "__main__":
    zoo = Zoo()

    # Optional: manuelles Hinzufügen
    zoo.tier_hinzufuegen(Löwe("Simba", 5))
    zoo.tier_hinzufuegen(Papagei("Polly", 2, flugfähig=True))
    zoo.tier_hinzufuegen(Elefant("Dumbo", 10, gewicht=5))

    # Aus CSV-Datei lesen (Datei muss existieren)
    try:
        tiere_aus_csv = lese_tiere_aus_csv("tiere.csv")
        for tier in tiere_aus_csv:
            zoo.tier_hinzufuegen(tier)
    except FileNotFoundError:
        print("Hinweis: CSV-Datei 'tiere.csv' wurde nicht gefunden.")

    print("\nAlle Tiere im Zoo:")
    zoo.alle_tiere_zeigen()

    print("\nNur Papageien im Zoo:")
    zoo.suche_nach_art("Papagei")
