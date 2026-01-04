# Nach dem Aufruf des Programms soll man sein monatliches Gehalt eingeben.
# Liegt es über 2500 Euro, sind 22% Steuern zu zahlen, ansonsten 18%.
# Es ist nur eine Eingabe erforderlich. Innerhalb des Programms soll anhand des Gehalts entschieden werden, welcher Steuersatz zur Anwendung kommt.

a = 0.18
b = 0.22

print("Geben Sie Ihr Gehalt in Euro ein: ")
x = int(input())

y = float(x)
if x <= 2500:
    print(f"Es ergibt sich eine Steuer von {y * a} €")
else:
    print(f"Es ergibt sich eine Steuer von {y * b} €")
    
