'''
1. Scrieti o functie care verifica daca un nr este par. Daca este par retuneaza True, altef False.
Functia are un argument
'''

def is_even(n):
    """Check if number is even"""
    if n % 2 ==0:
        return True
    else:
        return False

'''
for i in range (101):
    if is_even(i):
        print("**")
    else:
        print("--")
'''
for i in range(10):
    if is_even(i):
        print(i, "este par")
    else:
        print(i, "este impar")
