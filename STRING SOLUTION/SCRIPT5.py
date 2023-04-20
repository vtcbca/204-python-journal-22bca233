#WAS to create 2 udf input() to take input string and call strSymmetric() by passing inputted string.
#strSymmetric() check string is symmetric or not. A string is said to be symmetrical if both the halves of the string are the same.
#Example:
#Enter string : KhoKho
#String is Symmetrical.


def symmetric(n):
    half=(len(n)//2)
    first=n[:half]
    second=n[half:]
    if first==second:
        print(f"String {n} is symmetric!!!!")
    else:
        print(f"String {n} is not symmetric!!!")

def input1():
     a=input("Enter a string:")
     symmetric(a)
     
input1()     
