szam = int(input("Kérek egy számot: "))
oszto = 2
while (szam > 1):
    if szam % oszto == 0:
        szam = szam / oszto
        if szam == 1:
            print(oszto)
        else:
            print(oszto, '*')
    else:
        oszto = oszto + 1