#sum of digit
num=int(input("Enter a number:"))
sum=0
n=num
while(num>0):
    r=num%10
    sum=sum+r
    num=num//10
print("The sum of {} number is {}".format(n,sum))
    
    
        
