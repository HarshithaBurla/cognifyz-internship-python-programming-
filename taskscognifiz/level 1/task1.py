#Task:String Reversal
def reverse(string):
    rev_str=''.join(list(reversed(string)))
    return rev_str #return string[::-1]
string=input("Enter String:")
rev_string=reverse(string)
print("Reversed String:",rev_string)

#output
##======================= RESTART: C:\taskscognifiz\level 1\task1.py =======================
##Enter String:python programming
##Reversed String: gnimmargorp nohtyp
