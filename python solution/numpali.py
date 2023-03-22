#python script to check number is palindrome or not
a=int(input("Enter any number :"))
temp=a
pali=0
while(a>0):
    rem=a%10
    pali=pali*10+rem
    a=a//10
if(pali==temp):
    print("The number is palindrome !")
else:
    print("The number is not palindrome !")
