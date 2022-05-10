'''
6. Scrie o functie care converteste litrii in metri cubi.
'''

def cube_volume(edge):
    """Calculate cube volume in liters."""
    return edge ** 3 * 1000

def convert_to_m3(liters):
    """Convert liters in m3."""
    return liters / 1000

edge = int(input("Muchia: "))

print("Volumul cubului: ", convert_to_m3(cube_volume(edge)), "m3")