szam = int(input("Kérek egy számot: "))
oszto = 2
while (szam % oszto != 0):
    oszto = oszto + 1
print("Legkisebb osztó: ", oszto)