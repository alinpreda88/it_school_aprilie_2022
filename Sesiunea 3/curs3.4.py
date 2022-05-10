'''
Conditia ca un numar introdus de la tastatura sa afiseze par/impar
'''
numar = input("Introduceti numarul: ")

numar = int(numar)

if numar % 2 == 0:
    print("Numarul este par")
else:
    print("Numarul este impar")