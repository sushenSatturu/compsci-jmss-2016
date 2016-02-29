# Write a program to read in words from the keyboard one at a time until
# the word "quit" is typed.
# Store them in a list then print them alphabetically

i = 0
list = []

while i == 0:
    ask = input("word plz")
    if "quit" in ask:
        break
    else:
        list.append(ask)


list.sort()
print(list)