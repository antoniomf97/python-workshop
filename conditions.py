"""
Python Conditions
"""

a = True
b = False

if a == True:
    print("A is True")
else:
    print("A is False")


"""
Grade:
A: 18-20
B: 15-18
C: 10-15
D:  0-10    
"""

grade = -1

if 0 <= grade < 10:
    print("D")
if 10 <= grade < 15:
    print("C")
if 15 <= grade < 18:
    print("B")
if 18 <= grade <= 20:
    print("A")


if 0 <= grade < 10:
    print("D")
else:
    if 10 <= grade < 15:
        print("C")
    else:
        if 15 <= grade < 18:
            print("B")
        else:
            if 18 <= grade <= 20:
                print("A")
            else:
                print("Invalid Grade")

if 0 <= grade < 10:
    print("D")
elif 10 <= grade < 15:
    print("C")
elif 15 <= grade < 18:
    print("B")
elif 18 <= grade <= 20:
    print("A")
else:
    print("Invalid Grade")