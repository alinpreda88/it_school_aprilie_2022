'''
# 3. Scrie un program care citeste de la tastatura doua numere, a si b.
# Daca a > b sa se diferenta suma lor.
# Daca a == b sa se afiseze a la puterea b
# Altfel sa se afiseze suma lor.
'''

a = input("Introduceti primul numar: ")
b = input("Introduceti al doilea numar: ")

a = int(a)
b = int(b)

if a > b:
    print("Scaderea numerelor a-b: ", a - b)
elif a == b:
    print("A ridicat la puterea lui b: ", a ** b)
else:
    print("Suma numerelor: ", a + b)