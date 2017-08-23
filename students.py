class Student:
    def __init__(self, name, idnum, scores, averageScore):
        self.name = name
        self.idnum = idnum
        self.scores = scores
        self.averageScore = averageScore
    def __str__(self):
        nameInfo = "Name: " + self.name
        idInfo = "\nID Number: " + self.idnum
        scoreInfo = "\nScores: " + str(self.scores)
        avgInfo = "\nAverage: " + str(self.averageScore)
        return nameInfo + " " + idInfo + " " + scoreInfo + " " + avgInfo
    def addScore(self, score):
        (self.scores).append(score)

def averageScore(scores):
    sum = 0
    for count in range(len(scores)):
        sum = sum + scores[count]
    avg = sum / len(scores)
    return avg

def add(theRoster, theStudent):
    theRoster.append(theStudent)

def delete(theRoster, theStudent):
    theRoster.remove(theStudent)

def display(theRoster, studentname):
    for count in range(len(theRoster)):
        if theRoster[count].name == studentname:
            print(theRoster[count])


testScores = [0, 30, 43, 20, 99, 100]
coolguy = Student("Cool Guy", "1", testScores, averageScore(testScores))
print(coolguy)
'''coolguy.addScore(50)
print(coolguy)
coolguy.averageScore()

testScores2 = [60, 30, 49, 88, 99, 100]
niceguy = Student("Nice Guy", "2", testScores2)

testScores3 = [97, 89, 95, 90, 99, 100]
smartguy = Student("Smart Guy", "3", testScores3)

roster = [coolguy, niceguy, smartguy]
for count in range(len(roster)):
    print(roster[count].name)
delete(roster, smartguy)
for count in range(len(roster)):
    print(roster[count].name)
display(roster, coolguy.name)'''
