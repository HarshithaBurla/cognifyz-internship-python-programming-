#Task:Palindrome checker
def palindrome(string):
    rev_str=''.join(list(reversed(string)))
    if(rev_str==string):
        print(string,"is a palindrome")
    else:
        print(string,"is not a palindrome")
valid_input=True        
while valid_input:
    string=input("Enter string:")
    palindrome(string)
    ch=input("If you wanna stop type 'n' or 'N':")
    if(ch=='n' or ch=='N'):
        valid_input=False
#output
##======================= RESTART: C:\taskscognifiz\level 1\task5.py =======================
##Enter string:sis
##sis is a palindrome
##If you wanna stop type 'n' or 'N':
##Enter string:sister
##sister is not a palindrome
##If you wanna stop type 'n' or 'N':n
