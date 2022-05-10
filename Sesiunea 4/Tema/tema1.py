'''
1. Scrieti un program care afiseaza numerele prime din intervalul [0 100].
'''
'''
# agoritm numere prime
n = input("Introduceti numarul natural n: ")
n = int(n)
prim = True

for i in range(1, n):
    if n % i == 0:
        prim = False
        break

if prim == True:
    print("Numar prim.")
else:
    print("Numarul nu este prim.")


prim = 0
for i in range (1, 101):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
            else:
                print("Afiseaza numarul prim:\n", i)
    prim = prim + 1
print("Total numere prime între {0} și {1} este {2}".format(1,101,prim))
'''
'''
n = int(input("Vă rugăm introduceți numărul de început: ")) 
m = int(input("Vă rugăm să introduceți numărul final: ")) 
prim = 0 
for i in range(n,m): 
    if i > 1: 
        for j in range(2,i/2): 
            if (i % j == 0): 
                break 
        else: 
            print(i) 
        prim = prim + 1 
print("Total numere prime între {0} și {1} sunt {2}".format(n,m,prim))
'''
for n in range(0, 100):
    prim = True
    for i in range(2, n):
        if n % i == 0:
            prim = False
            break
    if prim:
        print(n)
