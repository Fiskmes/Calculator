def plus(x, y):
    print(x + y)

def minus(x, y):
    print(x - y)

def multiply(x, y):
    print(x * y)

def divide(x, y):
    if num2 == 0:
        print("Error")
    else:
        print(x / y)

print("Välj vad du vill göra")
print("1. Plus")
print("2. Minus")
print("3. Multiply")
print("4. Divide")

val = input("Skriv in val (1/2/3/4): ")

num1 = int(input("Skriv det första numret "))
num2 = int(input("Skriv det andra numret "))



if val == '1':
    plus(num1, num2)

if val == '2':
    minus(num1, num2)

if val == '3':
    multiply(num1, num2)

if val == '4':
    divide(num1, num2)
