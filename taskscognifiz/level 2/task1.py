from random import randint
valid_input=True
while valid_input:
    rand_num=randint(1,100)
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
##======================= RESTART: C:\taskscognifiz\level 2\task1.py =======================
##Game Started
##Guess the number:23
##Too low.Try to guess another number...
##Guess the number:34
##Too low.Try to guess another number...
##Guess the number:45
##Too low.Try to guess another number...
##Guess the number:56
##Too low.Try to guess another number...
##Guess the number:67
##Too low.Try to guess another number...
##Guess the number:78
##Too High.Try to guess another number...
##Guess the number:75
##Too High.Try to guess another number...
##Guess the number:73
##Too low.Try to guess another number...
##Guess the number:74
##Congratulations!! you guessed the number correctly
##Game Ended
##do you want to continue if no type 'n' or 'N':n
