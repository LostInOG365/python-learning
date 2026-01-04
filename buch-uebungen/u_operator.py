a = 0.18
b = 0.22
c = 0.26

d = "ledig"
f = "verheiratet"

print("Geben Sie Ihr Gehalt in Euro ein: ")

x = int(input())

print("Bitte geben Sie Ihren Famielienstand ein: ")
z = str(input())

y = float(x)
q = str(z)

if x >= 4000 and d:
    print(f"Es ergibt sich eine Steuer von {y * c} €")
if x > 4000 and f:
    print(f"Es ergibt sich eine Steuer von {y * b} €")
elif x <= 4000 and d:
    print(f"Es ergibt sich eine Steuer von {y * b} €")
elif x <= 4000 and f:
    print(f"Es ergibt sich eine Steuer von {y *a} €")
