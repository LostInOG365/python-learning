import csv
import os
print(os.getcwd())

#with open('./Speicherort/Daten.txt') as csvdatei:
with open('./Speicherort/Daten.txt', mode='r', encoding='utf-8') as csvdatei:
    csv_reader_object = csv.reader(csvdatei, delimiter=',')
    #print(csv_reader_object)
    '''for row in csv_reader_object:
        print(row)
    print("-------")'''
    # ohne erste Zeile
    zeilennummer = -1
    for row in csv_reader_object: # hier sind immer alle

        if zeilennummer == -1:
            print(f'Spaltennamen sind: {", ".join(row)}\n')
        else:
            print(f'- Nachname: {row[0]} \t| Vorname: {row[1]} \t| Geburtstag: {row[2]}.')
        zeilennummer += 1

    print(f'Anzahl Datensätze: {zeilennummer}')

    #