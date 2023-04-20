#Write a script to create dictionary from list which contain student id , name and percentage
#Take student id and name till user choise.

def dicto(n):
    dic={}
    for i in range(0,len(n),3):
        dic[n[i]]=n[i+1:i+3]

    print(dic)
def takeinput():
    a=[]
    i="y"
    while i=="y" or i=="Y":
        b1=int(input("Student id:"))
        a.append(b1)
        b2=input("Student name:")
        a.append(b2)
        b3=float(input("Student percentage:"))
        a.append(b3)
        i=input("Do you add more ?(y/Y):")
    print(a)
    dicto(a)

takeinput()
