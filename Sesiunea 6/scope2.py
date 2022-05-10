# global scope
index = 1011
'''
# for loop variable leaking

for index in range(100, 20, -10):
    # local scope
    print(index)

print(index)
'''
n = 2
while n != 0:
    index = 1
    print(n)
    n -= 1


print(index)