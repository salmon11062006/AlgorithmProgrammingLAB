num1 = int(input("Enter Number: "))
def factorial(num):
    num2 = 1 
    for x in range(1, num+1):
        num2*=x
    print(num2)

factorial(num1)