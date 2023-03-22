#check prime number between 1 to input number
a=int(input("Enter a number :"))
for i in range(2,a):
    isprime = True
    for j in range(2,i):
        if(i%j==0):
            isprime = False
    if isprime:
        print(i)
      
