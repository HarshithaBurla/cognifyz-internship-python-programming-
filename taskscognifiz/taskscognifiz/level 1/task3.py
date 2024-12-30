#Task:Email validator
import re
def email_validator(email):
    pattern=re.compile(r'^[a-zA-z0-9_.+-]+@[a-zA-z0-9-]+\.[a-zA-z0-9-.]+$')
    return pattern.match(email)
valid_input=True
while valid_input:
    email=input("Enter email:")
    validity=email_validator(email)
    if(validity):
        print("Entered Email is valid")
    else:
        print("Entered Email is invalid")
    ch=input("If u want to stop type 'n' or 'N':")
    if(ch=='n' or ch=='N'):
        valid_input=False
#output
##======================= RESTART: C:\taskscognifiz\level 1\task3.py =======================
##Enter email:a@gmail.com
##Entered Email is valid
##If u want to stop type 'n' or 'N':e
##Enter email:a@
##Entered Email is invalid
##If u want to stop type 'n' or 'N':n        
