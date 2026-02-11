import math

print("Scientific Calculator")
print("Operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")
print("6. Square Root")
print("7. Sin")
print("8. Cos")
print("9. Tan")
print("10. Log")

choice = int(input("Enter choice (1-10): "))

if choice in [1,2,3,4,5]:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result:", num1 + num2)

elif choice == 2:
    print("Result:", num1 - num2)

elif choice == 3:
    print("Result:", num1 * num2)

elif choice == 4:
    print("Result:", num1 / num2)

elif choice == 5:
    print("Result:", num1 ** num2)

elif choice == 6:
    num = float(input("Enter number: "))
    print("Result:", math.sqrt(num))

elif choice == 7:
    num = float(input("Enter angle in degrees: "))
    print("Result:", math.sin(math.radians(num)))

elif choice == 8:
    num = float(input("Enter angle in degrees: "))
    print("Result:", math.cos(math.radians(num)))

elif choice == 9:
    num = float(input("Enter angle in degrees: "))
    print("Result:", math.tan(math.radians(num)))

elif choice == 10:
    num = float(input("Enter number: "))
    print("Result:", math.log10(num))

else:
    print("Invalid choice")
