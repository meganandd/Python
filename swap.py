mylist = [2, 5, 8, 9, 14, 20, 34]

def average (num1, num2): #numbers
    avg = ((num1 + num2) / 2) #average of the numbers divided by 2
    avg = int(avg)
    return(avg)

def binary_search (item, mylist): #defines binary_search
    right = len(mylist) - 1 # length of the list
    left = 0 #left equals 0
    mid = average (left, right) #midlle average
    while left <= right:
        if item == mylist[mid]:
            return mid
        elif mylist[mid] > item:
            right = mid - 1
            mid = average (left, right)
        elif mylist[mid] < item:
            left = mid + 1
            mid = average (left, right)
    return -1

mylist = [2, 5, 8, 9, 14, 20, 34]
position = binary_search (34, mylist)
print (position)
