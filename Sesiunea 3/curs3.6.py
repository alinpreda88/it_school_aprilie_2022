#el if

a = input("Introduceti primul numar: ")
b = input("Introduceti al doilea numar: ")

a = int(a)
b = int(b)

if a > b:
    #print("A este mai mare decat B")
    if b < a - b:
        print("Numarul B este mai mic decat jumatatea lui A")
elif b == a-b:
    print("B este jumatatea lui A")
else:
    print("B este mai mare decat A")    
    