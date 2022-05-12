# Structuri de date buit-in
'''
list - Colectie ordonata de obiecte
tuple - Colectie ordonata de obiecte - Imutabil
str - Colectie ordonata de caractere - Imutabil
set - Colectie ordonata de obiecte unice
dict - Colectie neordonata de obiecte accesibile prin cheie
'''

###declarare###
#call_id = []
###alocare###
#call_id = [1, 2, 3, 4]
###apelare###
#call_id[1] - ia valoarea 2
###modificare###
#call_id[3] = 5
###stergerea###
#del call_id[-1]

# Definirea unei liste

leader_board = ['Alex', 'George', 'Ionut']
# indexarea porneste de la 0 ex: [0, 1, 2]
#leader_board = list() - sau asa

print(type(leader_board))
print(leader_board)

print("-" * 30)
#len(leader_board) - lungimea listei
print("Nr. castigatori:", len(leader_board))

print("Locul 1: ", leader_board[0])
print("Ultimul loc:", leader_board[-2])
print("-" * 30)

print("Locul 2 initial:", leader_board[1])

leader_board[1] = "Andrei"
print("Dupa modificare")
print("Locul 2:", leader_board[1])

print("STOP")
print(leader_board)

print("-" * 30)

del leader_board[-1]
print("Dupa stergerea ultimului element, lungiea este:", len(leader_board))
print(leader_board)

print("-" * 30)
print("Castigatorii sunt:")
for name in leader_board:
    print(name)

print("STOP")