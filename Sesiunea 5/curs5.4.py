'''
2. Utilizati functia de la pct 1 pentru a afisa toate numerele impare in intervalul
[0, 50] si in intervalul [2000, 2100].
'''

def is_even(n):
    """Check if number is even in interval [0, 50], [2000, 2100]"""
    if n % 2 == 1:
        return True
    else:
        return False

for i in range(51):
    if is_even(i):
        print(i, end=' ')

for i in range(2000, 2100):
    if is_even(i):
        print(i, end=' ')

#De la un coleg
'''
for i in range(51):
    if not is_even(i):
        print(i, end = ' ')
for i in range(1999,2101):
    if not is_even(i):
        print(i, end = ' ')
'''