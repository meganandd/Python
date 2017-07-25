n = input("Please enter a number. ")
n = int(n)

def PrintStars(n):
    for line in range (0, n):
        for nextline in range (0, line + 1):
            print("* ",end="")
        print("\n")

PrintStars(n)
