class Musikinstrument():


    def __init__(self,p_modell="Standardinstrument"): # Konstruktor
        self.__modell = p_modell #privat


    def set_modell(self,neues_modell): # Schreibe-Methode, public Methode

        if neues_modell == "Hallo": # hier wird Kontrolle ausgeführt
            print("Hallo darf ich hier nicht reinschreiben")

        else:
            self.__modell = neues_modell # hier wird in dass private Attribut reingeschrieben, wenn es nicht "Hallo" ist


    def get_modell(self): # Lesemethode
        return self.__modell  # Rückgabe des Wertes vom privaten Attribut __modell

meine_trompete = Musikinstrument("Trompete") # Konstruktoraufruf


print(meine_trompete.get_modell())
meine_trompete.set_modell("Gitarre")
print(meine_trompete.get_modell())

meine_trompete.set_modell("Hallo")
print(meine_trompete.get_modell())

meine_trompete.set_modell("Oboe")
print(meine_trompete.get_modell())









#print(type(meine_trompete))


