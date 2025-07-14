print("welcome to python pizza deliveries!")
size=input("what size do you want ? s,m or l:")
pepperoni=input("do you want pepperoni on your pizza? y or n:")
extra_cheese=input("do you want extra cheese? y or n:")
bill=0
if (size =="s"):
    bill += 15
elif(size =="m"):
    bill += 20
elif(size =="l"):
    bill +=25
else:
    print("you typed the wrong input.")
if(pepperoni == "y" and size=="s"):
    bill += 2
else:
    bill +=3
if(extra_cheese == "y"):
    bill +=1
print(f"your final bill is: ${bill}.")
