magic_numbers = [2.3, 4.6, 46.6, 29.29, 8.22, 23.3]
#                 0     1    2     3     4      5

for index in range(0, len(magic_numbers), 2):
    print(index, magic_numbers[index])
print("=" * 10)
for index in range(len(magic_numbers) - 1, -1, -1):
    print(index, magic_numbers[index])


#for number in magic_numbers:
 #   print(number * 10)