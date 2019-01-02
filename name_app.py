name = input("Enter your name: ");
print("Hello " + name)

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# better to convert to float since user might enter float
# result = int(num1) + int(num2)
result = float(num1) + float(num2)
print("The sum is " + str(result))
