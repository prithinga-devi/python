import random


rock='''                                 _____ 
        \                              /\| | | |
         \                            / /|_|_|_|
          \                           \        |
            (  ( ) ) ( )  )            \_______/
           ( ( ( ( )  )  ) )           /______/
          ( ( )) ) (   ) ( ( )        /       /
          ( (__.-.___.-.__) )        /       /
          / ---._.---._.---\        /       /
          \||    '/  '   ||/       /       /
            |||  (_     |||       /       /
             || ///\\\  ||\______/       /
        ___/ ||||\__/|||||/             /
       /   \   ||||||||  /             /
      /     \   ||||||  /        _____/
'''


paper='''   
8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88     
'''

scissor='''
   ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/
'''
game=[rock,paper,scissor]
a=int(input("what do you choose? type 0 for rock,1 for paper,2 for scissor\n"))
if(a>=0 and a<=2):
    print(game[a])
computer=random.randint(0,2)
print("computer chose:")
print(game[computer])
if(a>=3 or a<0):
    print("you typed an invalid number.you lose!")
elif(a==0 and computer==2):
    print("you win!")
elif(computer==0 and a==2):
    print("you lose!")
elif(computer>a):
    print("you lose!")
elif(a>computer):
    print("you win!")