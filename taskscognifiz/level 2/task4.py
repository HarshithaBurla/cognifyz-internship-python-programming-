#Task:Fibnocci sequence
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input("Enter no of terms:"))
fib(n)
for i in range(0,n):
    print(fib(i))
#output
##======================= RESTART: C:\taskscognifiz\level 2\task4.py =======================
##Enter no of terms:5
##0
##1
##1
##2
##3
