#Write a Python program to enter sentence of atleast 10 words. Take user input of lengtho of word. 
#Find the word in user inputed string which has >= length of word enter by user and creaet its directory where word is key and its length is value.

def makedict(n):
    dic={}
    c=int(input("Enter minimum word length:"))
    for i in n:
        if len(i)>=c:
            dic[i]=len(i)

    print(dic)

def input1():
    str=input("Enter sentence:")
    a=str.split(" ")
    makedict(a)

input1()    
