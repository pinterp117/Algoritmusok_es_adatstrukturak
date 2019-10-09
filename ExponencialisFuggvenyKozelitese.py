import math
x = float(input("Kérem az x-et: "))
pontossag = float(input("Kérem a pontosságot: "))
lepes = 1
aktualis = x
ertek = 1 + aktualis
while abs(aktualis) >= pontossag:
    lepes = lepes + 1
    aktualis = aktualis * x / lepes
    ertek = ertek + aktualis
print("Lépésszam: ", lepes)
print("A közelítőérték: ", ertek)
print("A 'pontos' érték: ", math.exp(x))