#Task:File manipulation
text_file=input("Enter text file name:")
f=open(text_file,"w+")
f.write("This Is The Python Language Programming Language")
f.seek(0,0)
string=f.read()
str_split=string.split(' ')
str=sorted(set(str_split))
for i in str:
    if i in str_split:
        print(i,":",str_split.count(i))
f.close()
#output
##======================= RESTART: C:\taskscognifiz\level 2\task5.py =======================
##Enter text file name:demo.txt
##Is : 1
##Language : 2
##Programming : 1
##Python : 1
##The : 1
##This : 1
