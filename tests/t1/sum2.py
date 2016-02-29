# copy the code from sum1.py into this file, THEN:
# change your program so it keeps reading numbers until it gets a
# -1, then prints the sum of all numbers read

list = []
total = 0

'''
for i in range(10):
    ask = input("Enter your number")
    ask = int(ask)
    if ask != -1:
        list.append(ask)
        total = total + ask
    elif ask == -1:
        break
'''

i = 0
total = 0

while i == 0:
    ask = input("enter your number")
    ask = int(ask)
    if ask == -1:
        break
    total = total + ask


print(total)
