osszes = int(input("Kérem az adatok számát: "))
adat = float(input("Kérem az aktuális számot: "))
novo = True
elozo = adat
for i in range(1, osszes):
    adat = float(input("Kérem az aktuális számot: "))
    if adat < elozo:
        novo = not novo
    elozo = adat
if novo:
    print("Monoton növekvők.")
else:
    print("Nem monoton növekvők.")