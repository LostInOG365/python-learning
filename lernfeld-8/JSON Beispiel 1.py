#https://www.datacamp.com/de/tutorial/json-data-python
#https://hellocoding.de/blog/coding-language/python/json-verwenden

import json

# Beispiel-Daten, die in eine JSON-Datei geschrieben werden sollen
daten = {
    "name": "Max Mustermann",
    "alter": 31,
    "beruf": "Ingenieur",
    "interessen": ["Fussball", "Programmieren", "Reisen"]
}

# Daten in eine JSON-Datei schreiben
with open("daten.json", "w", encoding="utf-8") as json_datei:
    json.dump(daten, json_datei, ensure_ascii=False, indent=4)

print("Daten wurden in die Datei 'daten.json' geschrieben.")

# Daten aus der JSON-Datei lesen
with open("daten.json", "r", encoding="utf-8") as json_datei:
    gelesene_daten = json.load(json_datei)

print("Gelesene Daten aus der JSON-Datei:")
print(gelesene_daten)
