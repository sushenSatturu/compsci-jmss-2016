my_list = [1,2,3,5]
'''
try:
    x = my_list[5]
    print(x)
except IndexError:
    print("Out of Range")
'''

notNum = True
while notNum:
    try:
        x = input("Please enter a number ")
        x = int(x)
        notNum = False
    except ValueError:
        print("Plz enter a integer numeric, i.e 1, 2, 3, 4 etc")

