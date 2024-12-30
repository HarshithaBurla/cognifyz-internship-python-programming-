#Task:calculator program
valid_input=True
while valid_input:
    a,b=eval(input("Enter two numbers:"))
    op=input("Enter an operator(+,-,*,/,%):")
    if(op=='+'):
        print("Addition:",a+b)
    elif(op=='-'):
        print("Subtraction:",a-b)    
    elif(op=='*'):
        print("Multiplication:",a*b)
    elif(op=='/'):
        print("Division:",a/b)
    elif(op=='%'):
        print("Modulus:",a%b)
    else:
        print("Invalid operator")
    ch=input("If you wanna stop type 'n' or 'N':")
    if(ch=='n' or ch=='N'):
        valid_input=False
#output
##======================= RESTART: C:\taskscognifiz\level 1\task4.py =======================
##Enter two numbers:1,2
##Enter an operator(+,-,*,/,%):+
##Addition: 3
##If you wanna stop type 'n' or 'N':r
##Enter two numbers:2,3
##Enter an operator(+,-,*,/,%):-
##Subtraction: -1
##If you wanna stop type 'n' or 'N':e
##Enter two numbers:3,4
##Enter an operator(+,-,*,/,%):*
##Multiplication: 12
##If you wanna stop type 'n' or 'N':g
##Enter two numbers:4,5
##Enter an operator(+,-,*,/,%):/
##Division: 0.8
##If you wanna stop type 'n' or 'N':g
##Enter two numbers:5,6
##Enter an operator(+,-,*,/,%):%
##Modulus: 5
##If you wanna stop type 'n' or 'N':r
##Enter two numbers:2,3
##Enter an operator(+,-,*,/,%):.
##Invalid operator
##If you wanna stop type 'n' or 'N':n
        
