'''
# 4. Scrie un program care citeste de la tastatura doua numere,
# si calculeaza a / b daca a > b sau b / a daca a <= b. Afiseaza 
# rezultatul.
'''

a = input("Introduceti primul numar: ")
b = input("Introduceti al doilea numar: ")

a = int(a)
b = int(b)

if a > b:
    print("Calculeaza A / B: ", a / b)
elif a <= b:
    print("Calculeaza B / A: ", b / a)
else:
    print("Nu ati introdus un numar corect")