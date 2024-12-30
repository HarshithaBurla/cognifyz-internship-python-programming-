#Task:Number Guesser
up_bound,lw_bound=eval(input("Enter bounds:"))
from random import randint
valid_input=True
while valid_input:
    rand_num=randint(up_bound,lw_bound)
    print("Game Started")
    user=int(input("Guess the number:"))
    while not(user==rand_num):
        if(user<rand_num):
            print("Too low.Try to guess another number...")
        else:
            print("Too High.Try to guess another number...")
        user=int(input("Guess the number:"))
    print("Congratulations!! you guessed the number correctly")
    print("Game Ended")
    ch=input("do you want to continue if no type 'n' or 'N':")
    if(ch=='n' or ch=='N'):
        valid_input=False
#output
##======================= RESTART: C:\taskscognifiz\level 2\task2.py =======================
##Enter bounds:1,100
##Game Started
##Guess the number:34
##Too low.Try to guess another number...
##Guess the number:56
##Too low.Try to guess another number...
##Guess the number:67
##Too low.Try to guess another number...
##Guess the number:89
##Too High.Try to guess another number...
##Guess the number:75
##Too low.Try to guess another number...
##Guess the number:78
##Too low.Try to guess another number...
##Guess the number:82
##Too low.Try to guess another number...
##Guess the number:84
##Too High.Try to guess another number...
##Guess the number:83
##Congratulations!! you guessed the number correctly
##Game Ended
do you want to continue if no type 'n' or 'N':n
