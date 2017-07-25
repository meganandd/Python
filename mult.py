number = input("Enter a number: ")
number = int(number)

def multiply(number):
    for x in range (1, number + 1):
        for y in range (1, number + 1):
            print(x * y, end="\t")
        print()

multiply(number)
