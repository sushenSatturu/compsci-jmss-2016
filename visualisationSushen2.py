data = open("blackburnMarch.csv")

headers = data.readline()

def Average (list):
    av = sum(list)/len(list)
    return av

mondayMentor = []
tuesdayMentor = []
wednesdayMentor = []
thursdayMentor = []
fridayMentor = []

mondayp1 = []
tuesdayp1 = []
wednesdayp1 = []
thursdayp1 = []
fridayp1 = []

mondayp2 = []
tuesdayp2 = []
wednesdayp2 = []
thursdayp2 = []
fridayp2 = []

mondayp3 = []
tuesdayp3 = []
wednesdayp3 = []
thursdayp3 = []
fridayp3 = []

mondayp4 = []
tuesdayp4 = []
wednesdayp4 = []
thursdayp4 = []
fridayp4 = []

i = 1

mentorStart = 1456735200 # 1456736100 1456736040

for line in data:
    line = line.strip()
    datalist = line.split(",")

    time = int(datalist[0])

    ## MONDAY
    if time >= mentorStart and time <= (mentorStart + 840) and i == 1:
        mondayMentor.append(datalist[3])
    elif time >= (mentorStart + 900) and time <= (mentorStart + 5400) and i == 1:
        mondayp1.append(datalist[3])
    elif time >= (mentorStart + 6900) and time <= (mentorStart + 11400) and i == 1:
        mondayp2.append(datalist[3])
    elif time >= (mentorStart + 11700) and time <= (mentorStart + 16200) and i == 1:
        mondayp3.append(datalist[3])
    elif time >= (mentorStart + 19200) and time <= (mentorStart + 23700) and i == 1:
        mondayp4.append(datalist[3])
    elif time >= (mentorStart + 23700) and i == 1:
        mentorStart += 86400
        i += 1

    ## TUESDAY
    if time >= mentorStart and time <= (mentorStart + 840) and i == 2:
        tuesdayMentor.append(datalist[3])
    elif time >= (mentorStart + 900) and time <= (mentorStart + 5400) and i == 2:
        tuesdayp1.append(datalist[3])
    elif time >= (mentorStart + 6900) and time <= (mentorStart + 11400) and i == 2:
        tuesdayp2.append(datalist[3])
    elif time >= (mentorStart + 11700) and time <= (mentorStart + 16200) and i == 2:
        tuesdayp3.append(datalist[3])
    elif time >= (mentorStart + 19200) and time <= (mentorStart + 23700) and i == 2:
        tuesdayp4.append(datalist[3])
    elif time >= (mentorStart + 23700) and i == 2:
        mentorStart += 86400
        i += 1


    ## WEDNESDAY
    if time >= mentorStart and time <= (mentorStart + 840) and i == 3:
        wednesdayMentor.append(datalist[3])
    elif time >= (mentorStart + 900) and time <= (mentorStart + 5400) and i == 3:
        wednesdayp1.append(datalist[3])
    elif time >= (mentorStart + 6900) and time <= (mentorStart + 11400) and i == 3:
        wednesdayp2.append(datalist[3])
    elif time >= (mentorStart + 11700) and time <= (mentorStart + 16200) and i == 3:
        wednesdayp3.append(datalist[3])
    elif time >= (mentorStart + 19200) and time <= (mentorStart + 23700) and i == 3:
        wednesdayp4.append(datalist[3])
    elif time >= (mentorStart + 23700) and i == 3:
        mentorStart += 86400
        i += 1

    ## THURSDAY

    if time >= mentorStart and time <= (mentorStart + 840) and i == 4:
        thursdayMentor.append(datalist[3])
    elif time >= (mentorStart + 900) and time <= (mentorStart + 5400) and i == 4:
        thursdayp1.append(datalist[3])
    elif time >= (mentorStart + 6900) and time <= (mentorStart + 11400) and i == 4:
        thursdayp2.append(datalist[3])
    elif time >= (mentorStart + 11700) and time <= (mentorStart + 16200) and i == 4:
        thursdayp3.append(datalist[3])
    elif time >= (mentorStart + 19200) and time <= (mentorStart + 23700) and i == 4:
        thursdayp4.append(datalist[3])
    elif time >= (mentorStart + 23700) and i == 4:
        mentorStart += 86400
        i += 1

    ## FRIDAY

    if time >= mentorStart and time <= (mentorStart + 840) and i == 5:
        fridayMentor.append(datalist[3])
    elif time >= (mentorStart + 900) and time <= (mentorStart + 5400) and i == 5:
        fridayp1.append(datalist[3])
    elif time >= (mentorStart + 6900) and time <= (mentorStart + 11400) and i == 5:
        fridayp2.append(datalist[3])
    elif time >= (mentorStart + 11700) and time <= (mentorStart + 16200) and i == 5:
        fridayp3.append(datalist[3])
    elif time >= (mentorStart + 19200) and time <= (mentorStart + 23700) and i == 5:
        fridayp4.append(datalist[3])
    elif time >= (mentorStart + 23700) and i == 5:
        mentorStart += 259200
        i = 1


mondayMentor = list(map(float, mondayMentor))
print("monday mentor" , Average(mondayMentor))

mondayp1 = list(map(float, mondayp1))
print("monday p1" , Average(mondayp1))

mondayp2 = list(map(float, mondayp2))
print("monday p2" , Average(mondayp2))

mondayp3 = list(map(float, mondayp3))
print("monday p3" , Average(mondayp3))

mondayp4 = list(map(float, mondayp4))
print("monday p4" , Average(mondayp4))



