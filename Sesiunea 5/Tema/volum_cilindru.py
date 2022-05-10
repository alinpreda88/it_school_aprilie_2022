'''
5. Scrieti o functie care returneaza volumul unui cilintru in litri,
Aceasta va primi doua argumente reprezentand inaltimea si raza bazei in metri.
'''
r = input("Introduceti raza cilindrului(in metrii): ")
r = int(r)

h = input("Introduceti inaltimea cilindrului(in metrii): ")
h = int(h)

def volume_cylinder(l):
    """The volume of the cylinder in liter"""
    if l > 0:
        return True
    else:
        return False

pi = 3.14
volum = pi * r ** 2 * h
litrii = volum / 0.001

if volume_cylinder(r) and volume_cylinder(h):
    print("Volumul cilindrului: ", volum, "m^3")
    print("Volumul cilindrului in litrii are valoarea: ", litrii, "litrii")
else:
    print("Nu ati introdus o valoare corecta!")
