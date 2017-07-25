import random

list1 = []
for count in range (1 ,101):
    x = random.randint(10, 99)
    list1.append(x)

print(list1)

for count in range (0, 100):
    if list1[count] % 5 == 0:
        print(list1[count])
