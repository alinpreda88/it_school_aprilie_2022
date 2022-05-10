'''
# 2. Scrie un program care citeste de la tastatura un numar 
# natural, reprezentand raza unui cerc, si afiseaza perimetrul
# cercului insotit de mesajul "Perimetru cercului = <valoare>".
# Daca numarul citit este mai mare decat 100 se va calcula si aria
# cercului. Aceasta se va afisa insotita de mesajul "Aria cercului = <valoare>".
'''

raza = input("Raza cercului: ")
raza = int(raza)
pi = 3.14

print("Perimetrul cercului este: ", raza * pi * 2)

if raza > 100:
    print("Aria cercului este: ", pi * raza ** 2)
else:
    print("Numarul este mai mic decat 100")