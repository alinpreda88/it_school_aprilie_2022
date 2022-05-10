'''
3. Scrieti o functie care returneaza daca unu nr. (reprezentand un an) este
considerat an bisect.
'''
year = int(input("Introdu un an: "))

def is_bisect(n):
    """If an year is bisect or not"""
    if n % 4 == 0:
         return True
    else:
         return False

if is_bisect(year):
    print(year, "- este an bisect")
else:
    print(year, "- nu este an bisect")