'''dictionary = {
"dad" : {"spanish" : "padre", "french" : "papa"},
"mom" : {"spanish" : "madre", "french" : "maman"}
}

for key in dictionary:
    print(key)
user = input("What word would you like to translate? ")
for key in dictionary[user]:
    print(key)
user2 = input("What language would you like to translate to? ")
print(dictionary[user][user2])'''

def countLetters(word):
    letterdict={}
    for letter in word:
        letterdict[letter] = 0
    for letter in word:
        letterdict[letter] += 1
    return letterdict

user = input("Type in a word: ")
table = countLetters(user)

for key, val in table.items():
    print("Letter: " + key + "\tAppeared: " + str(val))
