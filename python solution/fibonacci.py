#python script to print fibonacci series
#0 1 1 2 3 5 8 13
#f3=f1+f2;    f0=0 and f1=1
n=int(input("Enter a number :"))
sum=0
f0=0
f1=1
i=0
while(i<n):
    print(f0)
    sum=f0+f1
    f0=f1
    f1=sum
    i=i+1
 
    
