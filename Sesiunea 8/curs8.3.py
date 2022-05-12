# Operatiuni pe liste

'''
list.append(x) - inserarea unui nou element in lista
list.remove(x) - va sterge prima aparitie a unui element din lista(pozitia 0)
list.count(x)  - returneaza numarul de aparitii in lista
list.reverse() - returneaza lista
min(list)
max(list)
len(list)
'''
user_id = [33, 455, 3, 32, 34, 12, 90, 32, 234]

leader_board = ['Alex', 'George', 'Ionut']

print(user_id)

# Lungimea listei
print("Lungimea listei:", len(user_id))

print("-" * 30)

# Maximul listei
print("Maximul listei:", max(user_id))
print(max(leader_board)) # pentru string/litera, aduce litera cea mai indepartata din alfabet

print("-" * 30)

# Minimul listei
print("Minimul listei:", min(user_id))
print(min(leader_board))

print("-" * 30)

# adaugare element nou - append (la cap de lista)
user_id.append(100)
print(user_id)
print("Lungimea listei:", len(user_id))

print("-" * 30)

# eliminare element

user_id.remove(3)
print("Dupa remove:")
print(user_id)

'''
# verificare daca valoarea face parte din lista
value_to_remove = int(input("Remove value: "))

if value_to_remove in user_id:
    user_id.remove(value_to_remove)
else:
    print("Valoarea nu exista in lista!")

print("=" * 20)
print(user_id)
'''

# numarul de aparitii al unui element
print("Elementul 33 apare de", user_id.count(33), "ori")
#print(user_id.count(33))
print("=" * 20)
# insert la index
user_id.insert(1, 0)
user_id.insert(-1, 0)
print("Dupa insert 0")
print(user_id)
print("=" * 20)

# gaseste indexul unei valori
index_magic = user_id.index(32)
user_id.insert(index_magic + 1, "X")

print("Dupa index magic")
print(user_id)
print("=" * 20)

# reversul listei  !! opereaza pe lista
print("Lista in stare initiala:")
print(user_id)

user_id.reverse()
print("Dupa reverse")
print(user_id)

print("=" * 20)


# List sliceing(a taia/a felia) 
# primele 3 elemente
top_three_users = user_id[:3]  # se creeaza o lista noua


print("user_id", user_id)
print("top_three_users", top_three_users)

# ultimul element
last_element = user_id[-3:]
print("last_element", last_element)
print("=" * 20)
# interval de elemente
print(user_id[1:4])
print("=" * 20)

# list copy

print("END")