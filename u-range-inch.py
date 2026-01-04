# Schreiben Sie ein Programm, das die folgende Ausgabe erzeugt (Datei u_range_inch.py).
# 15 Inch = 38.1 cm
# 20 Inch = 50.8 cm
# 25 Inch = 63.5 cm
# 30 Inch = 76.2 cm
# 35 Inch = 88.9 cm
# 40 Inch = 101.6 cm
# Es handelt sich um eine regelmäßige Liste von Inch-Werten, 
# für die der jeweilige Zentimeter-Wert durch Umrechnung mit dem Faktor 2,54 ermittelt wird Inch zu Zentimeter Umrechnung

for inch in range(15, 45, 5):
    cm = inch * 2.54
    print(f"{inch} Inch = {cm} cm")