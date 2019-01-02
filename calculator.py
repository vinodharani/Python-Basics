num1 = float(input("Enter number 1: "))
op = input("Enter operation :")
num2 = float(input("Enter number 2: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 + num2)
else:
    print("Enter a right operator")
