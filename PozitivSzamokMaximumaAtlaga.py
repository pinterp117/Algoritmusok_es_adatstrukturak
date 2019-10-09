osszes = int(input("Kérem az adatok számát: "))
darab = 0
osszeg = 0
for i in range(osszes):
    szam = float(input("Kérek egy számot: "))
    if szam > 0:
        darab = darab + 1
        osszeg = osszeg + szam
        if darab == 1:
            max = szam
        elif szam > max:
            max = szam
if darab == 0:
    print("Nem volt pozitív szám.")
else:
    atlag = osszeg / darab
    print("A pozitív számok maximuma: ", max)
    print("A pozitív számok átlaga: ", atlag)