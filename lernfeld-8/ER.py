from graphviz import Digraph

# Create ER diagram
dot = Digraph(comment="ER-Modell Musiker-Veranstaltung")
dot.attr(rankdir='LR', size='10,6')

# Musiker entity
dot.node('Musiker', '''Musiker
-----------------
MusikerID (PK)
Künstlername/Bandname''', shape='box')

# Veranstaltung entity
dot.node('Veranstaltung', '''Veranstaltung
-----------------
VeranstaltungID (PK)
Bezeichnung
Datum
Ort
PLZ''', shape='box')

# Auftritt relationship (m:n Beziehung)
dot.node('Auftritt', '''Auftritt
-----------------
Beginn
Ende''', shape='diamond')

# Edges mit korrekten Kardinalitäten für m:n Beziehung
dot.edge('Musiker', 'Auftritt', label='n')
dot.edge('Auftritt', 'Veranstaltung', label='m')

# Alternative: Wenn Sie die Kardinalitäten an den Enden anzeigen möchten
# dot.edge('Musiker', 'Auftritt', taillabel='n', headlabel='1')
# dot.edge('Auftritt', 'Veranstaltung', taillabel='1', headlabel='m')

# Render - verwenden Sie einen lokalen Pfad oder aktuelles Verzeichnis
try:
    dot.format = 'png'
    file_path = 'er_modell_musiker_veranstaltung'  # Lokaler Pfad
    dot.render(file_path, cleanup=True)
    print(f"ER-Diagramm erfolgreich erstellt: {file_path}.png")
    
    # Diagramm auch als SVG speichern (oft besser für Anzeige)
    dot.format = 'svg'
    dot.render(file_path + '_svg', cleanup=True)
    print(f"SVG-Version erstellt: {file_path}_svg.svg")
    
except Exception as e:
    print(f"Fehler beim Erstellen des Diagramms: {e}")

# Optional: Diagramm direkt anzeigen (wenn in Jupyter Notebook)
# dot.view()

# Quellcode des Graphen anzeigen
print("\nGraphviz DOT-Code:")
print(dot.source)

