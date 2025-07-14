print("welcome to the rollercoaster!")
height=int(input("what is your height in cm?"))
bill=0
if(height>=120):
    print("you can ride the rollarcoster.")
    age=int(input("what is your age?"))
    if(age<12):
        bill=5
        print("child tickets are $5.")
    elif(age<=18):
        bill=7
        print("youth tickets are $7")
    elif(age>=45 and age<=55):
        print("everything is going to be ok.have a free ride on us!")
    else:
        bill=12
        print("adult tickets are $12.")
    wents_photo=input("do you want a photo taken? y or n.")
    if(wants_photo=="y"):
        bill+=3
    print(f"your final bill is ${bill}")
else:
    print("sorry you have to grow taller befour you can ride.")