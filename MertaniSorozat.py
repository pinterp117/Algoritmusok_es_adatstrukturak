darab = int(input("Kérem a sorozat hosszát: "))
elozo = int(input("Kérem az első elemet: "))
aktualis = int(input("Kérem az következő elemet: "))
kvociens = aktualis / elozo
eredmeny = True
for i in range(darab-2):
    elozo = aktualis
    aktualis = int(input("Kérem az következő elemet: "))
    if aktualis / elozo != kvociens:
        eredmeny = False
if eredmeny:
    print("Mértani sorozat.")
else:
    print("Nem mértani sorozat.")