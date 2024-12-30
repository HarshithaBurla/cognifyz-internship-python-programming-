import string
password=input("Enter a password:")
up_bool=any(char in string.ascii_uppercase for char in password)
low_bool=any(char in string.ascii_lowercase for char in password)
digit_bool=any(char in string.digits for char in password)
punc_bool=any(char in string.punctuation for char in password)
len_bool=len(password)>=8 
if(len_bool and up_bool and low_bool and (digit_bool or punc_bool)):
    print("Strong password")
elif(len_bool and ((up_bool and low_bool) or (digit_bool and punc_bool))):
    print("Moderate password")
else:
    print("Weak password")
#output
##======================= RESTART: C:\taskscognifiz\level 2\task3.py =======================
##Enter a password:Aabc12334
##Strong password
##
##======================= RESTART: C:\taskscognifiz\level 2\task3.py =======================
##Enter a password:aabc
##Weak password
##
##======================= RESTART: C:\taskscognifiz\level 2\task3.py =======================
##Enter a password:aabcAAbc
##Moderate password
