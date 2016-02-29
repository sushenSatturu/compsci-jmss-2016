# write a program that reads in 10 numbers, then prints the sum of those
list = []
total = 0

for i in range(10):
    ask = input("Enter your number")
    ask = int(ask)
    list.append(ask)
    total = total + ask


print(total)
