import csv

with open("csvtext.text") as csvfile:  # megnyitjuk az adott fájlt és becenevet adunk
    csvreader = csv.reader(csvfile,  # a csv.reader-el tudjuk kiolvasni az adatokat, aztán zárójelben a becenév,
                           delimiter=',')  # a delmimiter pedig az elválasztó
    next(csvreader)  # az első sort átugorjuk mert az a fejléc
    for row in csvreader:  # egy for ciklussal végigiterálunk rajta
        print(row)
