# Schreiben Sie ein Programmzur Eingabe und Unmrechnung von beliebigen Inch-Werten in Zentimeter.
# Der Umrechenfaktor soll wie in der Übung >>u_inch.py<< in einer Variablen gespeichert werden


a = 2.54 

print("Bitte geben Sie den Inch-Wert ein: ")
x = input()

y = float(x)
print(f"{x} Inch sind {y * a} cm")
