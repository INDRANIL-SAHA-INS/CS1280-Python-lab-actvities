def calculator ():
    print("Simple Calculator")
    num1=float(input("Enter first number:"))
    num2=float(input("Enter second number:"))
    print("select operation :")
    print("1.Add")
    print("2.Divide")
    print("3.Multiplication")
    print("4.Subtraction")
    print("5.Modulus")
    print("6.Floor Division")
    print("7.Exponent")
    choice=input("Enter choice(1/2/3/4/5/6/7):")
    if choice=="1":
        print(f"Result:{num1}+{num2}={num1+num2}")
    elif choice =='2':
        if num2!=0:
            print(f"Result:{num1}/{num2}={num1/num2}")
        else:
            print("Error! Division by zero .")
            
    elif choice=='3':
        print(f"Result : {num1} * {num2} = {num1*num2}")
    elif choice=='4':
        print(f"Result : {num1} - {num2} = {num1-num2}")
    elif choice=='5':
        print(f"Result : {num1} % {num2} = {num1%num2}")
    elif choice=='6':
        if num2!=0:
            print(f"Result : {num1} // {num2} = {num1//num2}")
    elif choice=='7':
        print(f"Result : {num1} ^ {num2} = {num1**num2}")
    else:
        print("Invalid Input")
            
calculator()
