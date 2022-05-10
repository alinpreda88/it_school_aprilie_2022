'''
4. Scrieti o functie care returneaza volumul unui cub in litri. Aceasta va primi
un singur agument reprezentand muchia cubului in metri.
'''

muchia = input("Introduceti muchia cubului(in metrii): ")
muchia = int(muchia)

def volume_cube(l):
    """The volume of the cube in liter"""
    if l > 0:
        return True
    else:
        return False

volum = muchia ** 3
litrii = volum / 0.001

if volume_cube(muchia):
    print("Volumul cubului: ", volum, "m^3")
    print("Volumul cubului in litrii are valoarea: ", litrii, "litrii")
else:
    print("Nu ati introdus o valoare corecta!")