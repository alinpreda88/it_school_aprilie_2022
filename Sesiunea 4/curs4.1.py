'''
print("*")
print("**")
print("***")
print("****")
print("*****")
print("******")
'''
#n = input("Introduceti un numar: ")
#n = int(n)
n = 3
k = 1

while k <= n:
    print("*" * k, "+" * (n - k), sep='')
    k = k + 1
