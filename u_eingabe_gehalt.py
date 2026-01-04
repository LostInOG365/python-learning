# Schreiben Sie ein Programm zur vereinfachten Berechnung der Steuern. 
# Nach dem Aufruf des Programms wird man dazu ausfegfordert, sein monatliches Gehalt einzugeben.
# Anschließend werden 18% dieses Betrages berechnet und ausgegeben.

a = 0.18

print("Geben Sie Ihr Gehalt in Euro ein: ")
x = input()

y = float(x)
print(f"Es ergibt sich eine Steuer von {y * a} €")