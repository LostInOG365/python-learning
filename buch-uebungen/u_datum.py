# Entwickeln Sie ein Programm zur Prüfung einer Datumsangabe. 
# Nach dem Aufruf des Programms sollen die drei Bestandteile eines Datums einzeln eingegeben werden. 
# Anschließend wird ermittelt, ob es sich um ein gültiges Datum handelt. Gehen Sie bei der Entwicklung wie nachfolgend beschrieben vor. Testen Sie Ihr Programm nach jedem Schritt:
# Untersuchen Sie den eingegebenen Wert für den Tag. 
# Ist er kleiner als 1 oder größer als 31, handelt es sich um ein ungültiges Datum.
# Untersuchen Sie den eingegebenen Wert für den Monat. 
# Ist er kleiner als 1 oder größer als 12, handelt es sich um ein ungültiges Datum.
# Geben Sie den Wert aus, den der letzte Tag des betreffenden Monats hat. 
# Denken Sie daran, dass es nur drei mögliche Fälle gibt: 28, 30 oder 31 Tage. Die Regeln für Schaltjahre werden noch nicht beachtet.
# Untersuchen Sie den eingegebenen Wert für den Tag. 
# Geben Sie aus, ob er kleiner als 1 oder größer als der letzte Tag des betreffenden Monats ist.
# Untersuchen Sie den eingegebenen Wert für das Jahr. 
# Geben Sie aus, ob es sich um ein Schaltjahr handelt. Die vereinfachte Regel für ein Schaltjahr lautet: Lässt sich der Wert ohne Rest durch 4 teilen, handelt es sich um ein Schaltjahr.
# Kombinieren Sie die bisherigen Schritte miteinander. 
# Ist der Wert für den Tag kleiner als 1 oder größer als der letzte Tag des betreffenden Monats (mit Berücksichtigung der Regel für ein Schaltjahr), handelt es sich um ein ungültiges Datum, ansonsten um ein gültiges Datum.
# Erweitern Sie das Programm. 
# Die vollständige Regel für ein Schaltjahr lautet: Lässt sich der Wert ohne Rest durch 4 teilen, aber nicht ohne Rest durch 100, handelt es sich um ein Schaltjahr. Es handelt sich aber auch um ein Schaltjahr, falls sich der Wert ohne Rest durch 400 teilen lässt

a = "Februar"
b = "4 or 6 or 9 or 11"

print("Geben Sie den Wert des Datums ein: ")

x = int(input())

if x<1 and x>31:
    print("ungültiges Datum")

print("Geben Sie den Monat des Datums ein: ")

y = int(input())


if y == a:
    print("Letzter Tag: 28")
elif y == b:
    print("Letzter Tag: 30")
else:
    print("Letzter Tag: 31")

if x < 1:
    print("Der eingegebene Wert ist kleiner als 1")
elif x <= 31:
    print("gültige Eingabe")
else:
    print("Der eingegeben Wert ist größer als der letzte Tag des Monates")

print("Geben Sie das Jahr des Datums ein: ")

z = int(input())
if z // 4 == 0:
    print("Schaltjahr")
else:
    print("Kein Schaltjahr")
