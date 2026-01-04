class Tier:
    def __init__(self):
        self.name = "Tiername"

    def fressen(self):
        print("Ich esse alles")


class Lebewesen:
    def __init__(self):
        self.gewicht = 3.0


class Hund(Tier, Lebewesen):
    def __init__(self):
        Tier.__init__(self)
        Lebewesen.__init__(self)

    def fressen(self):
        print("Ich fresse nur Hundefutter")


class Katze(Tier):
    def fressen(self):
        print("Ich fresse nur Katzenfutter")


mein_hund = Hund()
print(mein_hund.name)
mein_hund.fressen()
print(mein_hund.gewicht)

mein_katze = Katze()
mein_katze.fressen()
