number = input("enter a number")
number = int(number)

def Divide (number1, number2):
    return number1 % number2 == 0

if Divide (number, 3) and Divide (number, 5):
    print("fizzbuzz")

elif Divide (number, 3):
    print("fizz")

elif Divide (number, 5):
    print("buzz")

else:
    print(":(")

while True:
    user_input = input("Type STOP to stop the program. Type CONT to continue the program")
    if user_input == "STOP":
        break
    elif user_input == "CONT":
        number = input("enter a number")
        number = int(number)

        def Divide (number1, number2):
            return number1 % number2 == 0

        if Divide (number, 3) and Divide (number, 5):
            print("fizzbuzz")

        elif Divide (number, 3):
            print("fizz")

        elif Divide (number, 5):
            print("buzz")

        else:
            print(":(")
    else:
        print("Enter a valid response")
