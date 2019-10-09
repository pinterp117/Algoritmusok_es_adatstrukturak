darab = int(input("Kérem a sorozat hosszát: "))
elozo = int(input("Kérem az első elemet: "))
aktualis = int(input("Kérem az következő elemet: "))
differencia = aktualis - elozo
eredmeny = True
for i in range(darab-2):
    elozo = aktualis
    aktualis = int(input("Kérem az következő elemet: "))
    if aktualis - elozo != differencia:
        eredmeny = False
if eredmeny:
    print("Számtani sorozat.")
else:
    print("Nem számtani sorozat.")