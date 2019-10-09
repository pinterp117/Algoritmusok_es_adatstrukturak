szam = int(input("Kérek egy számot: "))
faktorialis = 1
for i in range(1, szam + 1):
    faktorialis = faktorialis * i
print(szam, '! = ', faktorialis)