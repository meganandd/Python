class User:
    def __init__(self, name):
        self.name = name
        self.friendList = []
    def __str__(self):
        nameInfo = "Name: " + self.name
        friendInfo = "Friends: " + str(self.friendList)
        return nameInfo + "\t" + friendInfo
    def addFriend(self, friendname):
        (self.friendList).append(friendname)
    def getName(self):
        return self.name
    def getFriends(self):
        return self.friendList

class Network:
    def __init__(self):
        self.userList = []
    def __str__(self):
        empString = ""
        for count in range (len(self.userList)):
            empString = empString + "\nUser: " + (self.userList[count]).name + "\tFriends: " + str((self.userList[count]).friendList)
        return empString
    def getUser(self, name):
        for count in range (len(self.userList)):
            if name == (self.userList[count]).name:
                return self.userList[count]
        return None
    def addUser(self, name):
        for count in range (len(self.userList)):
            if name == (self.userList[count]).name:
                return False
        nextUser = User(name)
        self.userList.append(nextUser)
        return True
    def addFriendship(self, friend1, friend2):
        findFriends = 0 #keeps track of if they're in the network
        for count in range (len(self.userList)): #goes through the user list
            if friend1 == (self.userList[count]).name: #if the first friend is in the list
                findFriends = findFriends + 1 #add 1 to find friends
                posoffriend1 = count #sets position of where they are
            if friend2 == (self.userList[count]).name: #if the second friend is in the list
                findFriends = findFriends + 1 #add another 1 to find friends
                posoffriend2 = count #sets friend2's position
        if findFriends == 2: #if they are both in the user list
            #print("They exist!")
            #check if they are friends
            storeIfFriends = 0 #keeps track of if they're already friends
            #if storeIfFriends equals 1, then they're already friends
            for counter in range (len((self.userList[posoffriend1]).friendList)): #goes through friend list of friend one
                if (self.userList[posoffriend1]).friendList[counter] == friend2: #if other friend's name is in friend1's friend list
                    print("You're already friends!")
                    storeIfFriends= storeIfFriends+ 1 #store that they're friends
            if storeIfFriends == 0: #if they're not already friends
                #print("Friend2 isn't in Friend1's list.")
                (self.userList[posoffriend1]).addFriend(friend2) #add friend2 to friend1's list
                #print(self.userList[posoffriend1])
            storeIfFriends2 = 0
            for num in range (len((self.userList[posoffriend2]).friendList)):
                if (self.userList[posoffriend2]).friendList[num] == friend1:
                    print("You're already friends!")
                    storeIfFriends2 = storeIfFriends2 + 1
            if storeIfFriends2 == 0:
                (self.userList[posoffriend2]).addFriend(friend1)
        else: #if someone's not in the list, then give this message
            print("Something's wrong!")

def mainMethod(network1):
    while True:
        user = input("Type 'add' to add a new user. \nType 'friend' to add a friendship between two users. \nType 'view' to view info about a user. \nType 'network' to view info about the network. \nType 'quit' to quit. \n> ")
        if user == "add":
            askname = input("what is their name? ")
            network1.addUser(askname)
            print("You added " + askname + "!")
        elif user == "friend":
            askfriends = input("Enter the first friend you would like to add. ")
            askfriends2 = input("Enter the second friend you would like to add. ")
            network1.addFriendship(askfriends, askfriends2)
            print("They're friends now!")
        elif user == "view":
            askuser = input("what is their name? ")
            for counter in range (len(network1.userList)):
                if network1.userList[counter].name == askuser:
                    print(network1.userList[counter])
        elif user == "network":
            print(network1)
        elif user == "quit":
            print("Bye!")
            break
        else:
            print("Invalid command.")




ourNetwork = Network()
ourNetwork.addUser("Shriya")
ourNetwork.addUser("Megan")
ourNetwork.addFriendship("Shriya", "Megan")

mainMethod(ourNetwork)
