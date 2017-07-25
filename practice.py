def checkList(item, myList):
    length = len(myList)
    for count in range(length):
        if myList[count] == item:
            return True
        else:
            return False

sampleList = ["megan", "nicole", "andersen"]
samepleItem = "hello"

print(checkList(samepleItem, sampleList))
