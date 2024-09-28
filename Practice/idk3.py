array = []
insert = input("enter 3 numbers: ").split()
for i in range(9):
    list = []

    for numbers in insert:
        list.append(int(numbers))

    array.append(list)

print(array)
