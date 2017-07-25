def stars (number):
    output = ""
    for count in range (0, number + 1):
        output = output + "*"
    return output

def spaces (number):
    output = ""
    for count in range (0, number + 1):
        output = output + " "
    return output

n = input("Please enter a number. ")
n = int(n)

a = n
what = ""
for count in range(0, n):
    what = spaces(a)
    what = what + stars(n - a)
    print(what)
    a = a - 1
