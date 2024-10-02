dict = {}
num = int(input("Enter the number: "))

for x in range(1, num+1):
    num2 = x**2
    dict[x] = num2
print(dict)