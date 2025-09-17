""" #floats
bill = 31.56 """

#Boolean or true/false

""" x = True
y = False """
""" x= 10
# == is evaluation
if x == 10:
    print("x is 10")
elif x > 10:
    print("x is greater than 10")
else: 
    print("x is not 10")
 """

students = ["Sean", "Olivia", "Ayaan","Youssef"]
students.append("Mia")
""" # print(students[0])
for student in students:
    print(student) """
""" if "Olivia" in students:
    print("she's kinda lame")
else:
    print("she's still kinda lame but not in this class") """
""" if "Cadee" in students:
    print("she's kinda lame")
else:
    print("she's still kinda lame but not in this class") """
""" found = False
for student in students:

    if student == "Mia":
        print("mia is here")
    else:
        print("Mia not here")
name = "Andy"
print(len(name))
 """

""" print(4 % 2) """

""" money = True
friend = True

def movie():
    if money and friend:
        print("movies")
movie() """

""" hw = True

def movies():
    if not hw:
        print("Movie time")
    else: 
        print("Russian hw bro")
movies() """

def factors(x):
    for y in range(1,x+1):
        if x % y == 0:
            print(f"{y} is a factor of {x}")
factors(10000)