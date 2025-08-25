#simple calculator with python
def calculator():
    print("simple calculator")
    print("choose operator:")
    print("1-Addition(+)")
    print("2-Subtraction(-)")
    print("3-Multiplcation(*)")
    print("4-Division(/)")
    choice=input("Enter choice(1/2/3/4)")
    num1=float(input("Enter first no:"))
    num2=float(input("Enter second no:"))
    if choice=='1':
        print(f"{num1}+{num2}={num1+num2}")
    elif choice=='2':
        print(f"{num1}-{num2}=={num1-num2}")
    elif choice=='3':
        print(f"{num1}*{num2}=={num1 * num2}") 
        if num2 != 0:
            print(f"{num1}/{num2}=={num1/num2}")
        else:
            print("Error!division by zero")
    else:
         print("Invalid input")
calculator()