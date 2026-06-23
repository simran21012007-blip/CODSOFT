import math
print("======================= CALCULATOR ========================")

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square Root")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice=="8":
        print("Calculator Closed!")
        break
    elif choice in["1","2","3","4","5","6"]:

       num1 = float(input("Enter the first number: "))
       num2 = float(input("Enter the second number: "))

       if choice == "1":
          print("Result=",num1+num2)
       elif choice == "2":
          print("Result=",num1-num2)
       elif choice == "3":
          print("Result=",num1*num2)
       elif choice == "4":
          if num2!=0:
            print("Result=",num1/num2)
          else:
             print("Cannot be divided by zero")
       elif choice == "5":
          print("Result=",num1%num2)
       elif choice == "6":
          print("Result=",num1**num2)
    elif choice == "7":
        num=float(input("Enter a number:"))
        print("Result=",math.sqrt(num))
    else:
        print("Invalid choice!")