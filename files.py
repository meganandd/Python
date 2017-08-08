f = open("myfile.txt", "w")
f.write("Megan\n")
f.write("Nicole\n")
f.write("Andersen\n")
f.close()

f = open("myfile.txt", "r")
for line in f:
    print(line.rstrip("\n"))
f.close()
