todos = ["Apfel", "Banane"]

for _ in range(100000):
    newitem = input("Was möchtest du hinzufügen? ")
    todos.append(newitem)
    print("Meine Liste hat diese Elemente:")

    for todo in todos:
        print(f"- {todo}")

print("Programm beendet.")