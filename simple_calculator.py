#progarm to perform arithmetic operations

def user_menu():
    user_input = input("""
                    Welcome to calculator program:
                    Please press
                    >> "1" for addition
                    >> "2" for subtraction
                    >> "3" for multiplication
                    >> "4" for division
                    >> any key for exit
    """)
    
    return user_input

while True:

    #Taking user input for calulator operation
    operation = user_menu()

    #logic to perform arithmetic operations

    #Addition
    if operation == '1':
        #Taking two numbers as input from user
        number_1 = int(input("Enter number 1: "))
        number_2 = int(input("Enter number 2: "))

        print(number_1 + number_2)

    #Subtraction
    elif operation == '2':
        #Taking two numbers as input from user
        number_1 = int(input("Enter number 1: "))
        number_2 = int(input("Enter number 2: "))

        if number_1 > number_2:
            print(number_1 - number_2)
        else:
            print(number_2 - number_1)
    
    #Multiplication
    elif operation == '3':
        #Taking two numbers as input from user
        number_1 = int(input("Enter number 1: "))
        number_2 = int(input("Enter number 2: "))

        print(number_1 * number_2)
    
    #Division
    elif operation == '4':
        #Taking two numbers as input from user
        number_1 = int(input("Enter number 1: "))
        number_2 = int(input("Enter number 2: "))

        if number_2 == 0:
            print("Divisor can't be 0. Try again!")
            continue
        else:
            print(number_1 / number_2)

    else:
        print("Thanks for using calculator!")
        exit()



