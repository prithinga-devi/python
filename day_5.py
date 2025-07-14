# 1
fruits=["apple","banana","peach"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
    print(fruits)
print(fruits)

# 2
student_score=[150,142,185,120,171,184,149,24,59,68,199,78,65,89,20,60,30,445]
print(max(student_score)) #this line print the max number output:445 

total_exam_score=sum(student_score) #total sum
print(total_exam_score)

sum=0
for score in student_score:
    sum+=score
print(sum)

max_score=0
for score in student_score:
    if(score>max_score):
        max_score=score
print(max_score)

# 3
for i in range(1,11,3):
    print(i) #output:1 4 7 10
sum=0
for number in range(1,101,1):
    sum+=number
print(sum) #output:5050

# game 
for number in range (1,101):
    if(number%3==0):
        print("Fizz")
    elif(number%5==0):
        print("Buzz")
    elif(number%3==0 and number%5==0):
        print("FizzBuzz")
    else:
        print(number)