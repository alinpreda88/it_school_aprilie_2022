'''
4. Scrieti un program care citeste de la tastatura un nr natural "n", 
si afiseaza n! (factorial). 6! = 1 * 2 * 3 * 4 * 5 * 6
'''

n = input("Introduceti un numar natural: ")
n = int(n)

factorial = 1

if n < 0:
    print("Numarul introdus este negativ")
elif n == 0:
    print("Valoarea introdusa este egala cu 0")
else:
    for i in range(1, n + 1):
        factorial = factorial * i
    print("Valoarea factoriala a numarului", n, "este", factorial)
