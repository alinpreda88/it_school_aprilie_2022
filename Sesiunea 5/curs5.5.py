'''
3. Scrieti o functie care returneaza daca unu nr. (reprezentand un an) este
considerat an bisect.
'''
def leap_year(n):
    """Return a number if it is leap year"""
    if n % 4 == 0:
        return True
    else:
        return False

leap_year(2012)

leap_year(2007)


print(leap_year(2013))