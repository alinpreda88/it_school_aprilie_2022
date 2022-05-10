'''
Scrieti o functie care printeaza primele 10 numere. care sa le printeze in modul:
0
===
1
===
2
===
'''

def b_range(stop, sep="+", sep_c=10):
    """Function wich print the first 10 caracter"""
    for i in range(stop):
        print(i, end='')
        print(sep * sep_c)

b_range(10)

#b_range(10, "=", 3)
#b_range(15, "=", 3)
#b_range(5, "=", 3)

b_range(5,sep_c=20)