import sys

readmessage = open ("input.txt", "r")
linemessage = readmessage.readline()
linemessage = linemessage.rstrip("\n")

alphabet = "abcdefghijklmnopqrtsuvwxyz"

def caesar(word):
    encoded = ""
    for ch in word:
        index = alphabet.find(ch)
        index = ord(index)
        nextIndex = (index + 3) % 26
        print(nextIndex)
        '''encoded += chr(nextIndex)'''
    return encoded

def salad(word):
    encoded = ""
    for ch in word:
        index = alphabet.find(ch)
        index = ord(index)
        nextIndex = (index - 3) % 26
        print(nextIndex)
        '''encoded += chr(nextIndex)'''
    return encoded

if sys.argv[1] == "-e":
    ciphertext = caesar(linemessage)
    f = open ("output.txt", "w")
    f.write(ciphertext)
    f.close()
if sys.argv[1] == "-d":
    ciphertext = salad(linemessage)
    f = open ("output.txt", "w")
    f.write(ciphertext)
    f.close()
