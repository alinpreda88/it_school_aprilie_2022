'''
5. Scrieti un program care afiseaza toate litere (capitale) ale 
alfabetului englez, pe aceiasi linie despartite prin spatiu. 
**A se vedea tablelul ASCII. chr(65) -> A
'''
for i in range(64, 90):
    i = i +1
    print(chr(i), end=' ')
