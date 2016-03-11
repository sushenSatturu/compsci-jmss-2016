datafile = open("data.txt")


#print(line)
#lineList = line.split()

#work through every word in the line to find the word random and
#replace it with ticklish



for line in datafile:
    lineList = line.split()
    finalLine = ""
    for i in range(len(lineList)):
        if lineList[i] == "my":
            lineList[i] = "ticklish"
    finalLine += lineList[i] + " "
    print(finalLine)

