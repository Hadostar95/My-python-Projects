import os

print(dir(os))

#f=open("StuList.txt","w")
#f.write("Welcome to Student list:")
#f.close()
listname=[]
print("Welcome to list:________________________________________________")
while True:
    choise=input("Do you wish to continue?  ")
    if choise=="n"or choise=="N":
        break
    elif choise=="y" or choise=="Y":
        wname=input("Please add first name to list:  ")
        wlname=input("Please enter lastname:         ")
        
        listname.append(wname+" "+wlname)

print(listname)

#listname=["Justin Eseigbe","Jack Holden","Ben Musker","Moe Green"]

# Used to add to text file
def ListAdder(name):
    f=open("StuList.txt","r")
    if name in f:
        #f=open("StuList.txt","r")
        print("Already in list")
    else:
        f=open("StuList.txt","a")
        f.write("\nStudent Name:  "+name)

for n in listname:
    ListAdder(n)
    
f=open("StuList.txt","r")
print(f.read())

#Use to remove file-----------------------
#os.remove("StuList.txt")