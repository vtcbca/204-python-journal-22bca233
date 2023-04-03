#write a script to enter any sentence and print those word which is palindrome also print total number of palindrome word.
def palicount(a):
    b=a.split(" ")
    c=0
    d=[]
    for i in b:
        if (i==i[::-1]):
            c=c+1
            d.append(i)
    if c>0:
        print(f'The number of palindrome word in sentence is {c} and palindrome words are:{d}.')              
    else:
        print("There is no palindrome word in sentence!!!")    
a=input("enter a sentece:")
palicount(a)    