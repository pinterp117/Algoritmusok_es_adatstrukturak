import math
#Másodfokú egyenlet megoldása
A = float(input("Kérek egy számot: "))
B = float(input("Kérek egy számot: "))
C = float(input("Kérek egy számot: "))
if A == 0:
    #Nem másodfokú eset
    if B == 0:
        #Nem elsőfokú eset
        if C == 0:
            print("Minden valós szám megoldás!")
        else: print("Nincs megoldás!")
    else: print("Elsőfokú:", -C / B)
else:
    #Másodfokú eset
    D = B * B - 4 * A * C
    if D > 0:
        #Két valós gyök
        X1 = (-B + math.sqrt(D)) / (2 * A)
        X2 = (-B - math.sqrt(D)) / (2 * A)
        print("Két valós gyök: ", X1, X2)
    elif D == 0:
        print("Másodfokú: ", -B / (2 * A))
    else:
        #Komplex gyökök
        V = -B / (2 * A)
        K = abs(math.sqrt(-D) / (2 * A))
        print("Egyik komplex gyök: ", V, '+', K, 'i')
        print("Másik komplex gyök: ", V, '-', K, 'i')