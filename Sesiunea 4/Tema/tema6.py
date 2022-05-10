'''
6. Intr-o cutie se află 300 de bile, numerotate cu numere începând de la unu, 
din trei în trei. Toate bilele cărora le corespund numere pare sunt verzi. 
Să se afle câte bile verzi sunt.

'''
i = 0
nr_pe_bile = 1
bile_verzi = 0

while i <= 300:
    if nr_pe_bile % 2 == 0:
        bile_verzi += 1
    i += 1
    nr_pe_bile += 3 
print ("Bile verzi= ",bile_verzi)