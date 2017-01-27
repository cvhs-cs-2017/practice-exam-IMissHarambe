"""Use the range function to print the numbers from 1-20"""
def count():
    y = 0
    for i in range (20):
        y = y + 1
        print (y)

print (count())



"""Repeat the exercise above counting by 2's"""
def count2():
    y = 0
    for i in range (10):
        y = y + 2
        print (y)

print (count2())



"""Print all the multiples of 5 between 10 and 200 in DECENDING order"""
def count3():
    x = 200
    while x > 0:
        if x % 5 == 0:
            print (x)
        x = x-1
print (count3())
