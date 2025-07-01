#----------------------------------------------------

line='-'*45
print(line)
print("Welcome to The Simple Calculator")
print(line)

# Input numbers
num1=float(input("Enter The First Number:"))
num2=float(input("Enter The Second Number:"))

# Display the available operation
print("\nChoose an operation")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division(/)")
print("5. Modulus(%)")
print("6. Floor Division(//)")

# 📝 Taking user choice
choice=input("Enter Your Choice (1/2/3/4/5/6):")
print(line)

# 🧠 Perform calculation according to user choice
if choice=='1':
    result=num1+num2
    print(f"Result: {num1} + {num2} = {result}")
elif choice=='2':
    result=num1-num2
    print(f"Result: {num1} - {num2} = {result}")
elif choice=='3':
    result=num1*num2
    print(f"Result: {num1} * {num2} = {result}")
elif choice=='4':
    if num2==0:
        print("Error cannot divide by zero!")
    else:
        result=num1/num2
        print(f"Result: {num1} / {num2} = {result}")
elif choice=='5':
    result=num1%num2
    print(f"Result: {num1} % {num2} = {result}")
elif choice=='6':
    result=num1//num2
    print(f"Result: {num1} // {num2} = {result}")
else:
    print("Invalid choice! Please enter 1,2,3,4,5 or 6.")

print(line)
print("Thanks for using the calculator! 😊")
print(line)

#--------------------------------------------------
