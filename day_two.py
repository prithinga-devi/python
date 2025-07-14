print("welcome to the tip calculator!")
a=float(input("what was the total bill? $"))
b=float(input("how much tip would you like to give? 10,12 or 15? "))
c=float(input("how many people to split the bill? "))
d=b/100
e=d+a/a
print("each person should pay:$",round(a * e / c,2))