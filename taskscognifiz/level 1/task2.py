#Temperature conversion
valid_input=True
while valid_input:
        temp=int(input("Enter a temperature:"))
        unit=input("Enter unit of measurement:")
        if(unit=='c' or unit=='C'):
            f=9*temp/5+32
            print("converted temperature:"+format(f,'.3f')+"°F")
        elif(unit=='f' or unit=='f'):
            c=5/9*(temp-32)
            print("converted temperature:"+format(c,'.3f')+"°C")
        else:
            print("Invalid unit")
        ch=input("If you want to stop type 'n'")
        if(ch=='n'):
            valid_input=False
#output
##======================= RESTART: C:\taskscognifiz\level 1\task2.py =======================
##Enter a temperature:100
##Enter unit of measurement:c
##converted temperature:212.000°F
##If you want to stop type 'n'f
##Enter a temperature:200
##Enter unit of measurement:f
##converted temperature:93.333°C
##If you want to stop type 'n'e
##Enter a temperature:300
##Enter unit of measurement:
##Invalid unit
##If you want to stop type 'n'n

        
    

    
