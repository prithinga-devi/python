import random
random_integer=random.randint(1,10)
print(random_integer)

random_number_0_to_1=random.random()*10
print(random_number_0_to_1)

         #this is the game "heads" or "tails"

random_heads_or_tails=random.randint(0,1)
if random_heads_or_tails==0:
     print("Heads")
else:
   print("Tails")

#now this the "lists" of data 
states_of_america=["delaware","pennsylavanai","new jersay"]
print(states_of_america[2])
#i am changing the data from the first data
states_of_america=["delaware","pennsylavanai","new jersay"]
states_of_america[1]="pencilvanai"

#1)append is the end of the list
states_of_america.append("pri")

#2)this list add the 2 list
states_of_america.extend(["apple","ball","cat"])
print(states_of_america)


#who to pay the bill in the business

import random
friends=["alice","bob","charlie","david","emanuel"]
# 1 option
print(random.choice(friends))
# 2nd option
random_index=random.randint(0,4)
print(friends[random_index])


states_of_america=["delaware","pennsylavanai","new jersay"]
print(len(states_of_america))
num_of_states=len(states_of_america) #50 -> 49
print(states_of_america[num_of_states-1])

dirty_dozon=["Strawberries","Spinach","Kale","Nectarines","Apples","Grapes","Peaches"]


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][1])