def calculator():

    print("*********************  CALCULATOR ********************************")

    print("Select Operation: ")

    print("1.Add")

    print("2.Subtract")

    print("3.Multiplication")

    print("4.Division")

    operation = input("Enter Choice (1/2/3/4): ")

    if operation in ['1', '2', '3', '4']:

        num1 = float(input("Enter the first number : "))

        num2 = float(input("Enter the second number : "))

        if operation == '1':

            print(f"The Sum is : {num1 + num2}")

        elif operation == '2':

            print(f"The Difference is : {num1 - num2}")

        elif operation == '3':

            print(f"The Product is : {num1 * num2}")

        elif operation == '4':

            if num2 != 0:

                print(f"The Quotient is : {num1 / num2}")

            else:

                print("Error! Division by Zero.")

    else:

        print("Invalid input")


calculator()