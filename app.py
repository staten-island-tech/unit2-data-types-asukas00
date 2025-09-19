""" x = 3
y = float(3)
print(x,y)
 """
""" values = [1,2,23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

print(values[0])
print(values[3])
 """
"test"
["t","e","s" "t"]

""" x = "This is a thing"
y = x.split()
z = y[3]
print(y)
print(z) """

""" day_of_week = input("what day is it? ")
if day_of_week == "Monday":
    print("correct")
else:
    print("incorrect") """

""" x = "test"
print(f"hello {x}") """

""" temp = 75
if temp > 68:
    print("Warm")
elif temp == 68:
    print("Perfect")
else:
    print("Cold")
#Printed Warm because the temp was above 68 """

""" def check_odd_even(x):
    if x % 2 == 0:
        print("Even")
    else:
        print("odd")

values = [1,2,3,4,5,6,7,8,9,10]
print(values) 
for i in values:
    print(i, check_odd_even(i)) """


""" bill = input("How was the service")
if bill == ("bad"):
    print("0%")
elif bill == ("okay"):
    print("15%")
elif bill == ("good"):
    print("20%")
elif bill == ("great"):
    print("25%)"""

""" def factors(x):
    for y in range(1,x+1):
        if x % y == 0:
            print(f"{y} is a factor of {x}")
factors(4000) """

common_factors = []
def gcf(x,y):

    for a in range(1,x+1):
        if x % a == 0 and y % a == 0:
            common_factors.append(a)
gcf(2480 , 422)
print(max(common_factors))