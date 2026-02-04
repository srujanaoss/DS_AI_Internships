#Calculator 
num1 = int(input("Enter first number: "))
num2= int(input("Enter second number: "))

operand = input("Enter operation (+, -, *, /): ")

if operand == "+":
    print("Result =", num1 + num2)

elif operand == "-":
    print("Result =", num1 - num2)

elif operand == "*":
    print("Result =", num1 * num2)

elif operand == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Cannot divide by zero!")

else:
    print("Invalid operation!")

#concatinate
name = input("enter a name:")
print("welcome,",name + "!")

#fstring
age = input("enter your age:")
print(f"you are {age} years old!")

#type conversion
height = float(input("enter your height in meters:"))


