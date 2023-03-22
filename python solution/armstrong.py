#python script to check armstrong or not
a=int(input("Enter a number :"))
sum=0
temp=a
while(a>0):
    b=a%10
    c=b*b*b
    a=a//10
    sum=sum+c
if(sum==temp):
    print("{} is armstrong !".format(temp))
else:
    print("Number is not armstrong !")
