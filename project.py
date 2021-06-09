import pytest

import re

nonacroom=[1,2,3,4,5]
acroom=[6,7,8]
specialroom=[9,10]
cusid=[]
aname=[]
aage=[]
aaddress=[]
aphno=[]
checkin=[]
checkout=[]

i=0


def Admin():
    password="Admin123"
    passwd=input("Enter Password :")
    if(passwd==password):
        return status()

def Sum(a,b):
    return a+b        
    

def status():
    print("Admin Mode")
    print('1 to check availablitiy')
    print('2 Display Records')
    z=int(input("\nEnter your choice:"))
    if(z==1):
        return adminroom()
    
    elif(z==2):
        return record()


    

def bookingdetails():
    print("Welcome to Room Booking Details ") 
    roomtypefunction()
    
    
 #   room=input("\:")
def cnfbook(cusid):
    print('Booking confirmed Your customer Id is :- ')
    print(cusid)
    main()

    

def nonacavailability():
    cin=str(input("Check-In: "))
    checkin.append(cin)
    cout=str(input("check-out:")) 
    checkout.append(cout)
    if nonacroom!=[]:
         cusi=nonacroom[-1]
         cusid.append(cusi)
         nonacroom.pop()
         print(cusi)
         cnfbook(cusi)
    else:
        print("No NON AC Rooms found")
        roomtypefunction()


def acavailability():
    cin=str(input("Check-In: "))
    checkin.append(cin)
    cout=str(input("check-out:")) 
    checkout.append(cout)
    if acroom!=[]:
        cusi=acroom[-1]
        cusid.append(cusi)
        acroom.pop()
        print(cusi)
        cnfbook(cusi)
     
    else:
        print("No AC Rooms found")
        roomtypefunction()

def splacavailability():
    cin=str(input("Check-In: "))
    checkin.append(cin)
    cout=str(input("check-out:")) 
    checkout.append(cout)
    
    if specialroom!=[]:
        cusi=specialroom[-1]
        cusid.append(cusi)
        specialroom.pop()
        print('printing cid')
        print(cusi)
        cnfbook(cusi)
    else:
        print("No Special Rooms found")
        roomtypefunction()

def adminroom():
     print(' '.join(map(str, nonacroom))) 
     print(' '.join(map(str, acroom))) 
     print(' '.join(map(str, specialroom))) 
     print('are available')
     main()



def roomtypefunction():
    print("\t\t\t 1 NON-AC---RS 1000\n")
    print("\t\t\t 2 AC---RS 1500\n")
    print("\t\t\t 3 Suite SpeciaL---RS 3000\n") 
    print("\t\t\t 0 Go back\n") 
    romty=int(input("->"))
      
    if romty == 1:
        print(" NON AC ROOM")
        nonacavailability()
        

    elif romty == 2:
        print(" AC")
        acavailability()
      
    elif romty == 3:
        print(" SPECIAL ")
        splacavailability()
    elif romty == 0:
        main()
    

def user():
    print('Welcome to Take a break')
    Userbooking()

def Userbooking():
   # print('Welcome to take a break')
    name=input("\nEnter your name:")
    age =int(input("\nEnter your age:"))
    address=input("\nEnter your address:")
    phno=input("\nEnter phno:")
    aname.append(name)
    aage.append(age)
    aaddress.append(address)
    
    
        

    def isValid(phno):
        Pattern = re.compile("[6][7][8][9][0-9][0-9][0-9][0-9][0-9][0-9]")
        return Pattern.match(phno)
        
    if (isValid(phno)):
        print ("correct")
        aphno.append(phno)   
        bookingdetails() 
    else :
        print ("Invalid Number")
    
    isValid(phno)


        
    


def display():
    print ("******HOTEL BILL***")
    print ("Customer details:")
    print (User.name)
    print ("Customer address:",User.address)
        

def record():
    print("        *** HOTEL RECORD ***\n")
    print("| CustomerID | Name   | Age  | Address | PhoneNo | Check-In |Check-Out   |")
    print("------------------------------------------------------------------------------------")
    for cus,ab,aa,b,c,ci,co in zip(cusid,aname,aage,aaddress,aphno,checkin,checkout):
        print("|",cus,"\t","|",ab,"\t","|",aa,"\t |",b,"\t |",c,"\t |",ci,"\t |",co)
   
  #  print(aname[0])
    #print('enter 1 to go to main menu')
    go=input("\nEnter 0 to go back:")
    if(go==0):
        status()
    else:
        main()

    #if aphno!=[]:
     #   print('users details are-')
      #  for n in range(-1):
       #     print("|",aname[n],"\t |",aage[n],"\t|",aphno[n],"\t|",aaddress[n],"\t|")
   # else:
    #    print('no record yet')
     #   main()

    


    

def main():
    print("1.Admin")
        
    print("2.User")

    print("3.Booking ")

    print("4.Display Record")

  

    print("0.quit")
    
    
    b=int(input("\nEnter your choice:"))
    if (b==1):
        return Admin()

    if (b==2):

        return user()
        

    if(b==3):
        return user()

    if(b==4):
        return record()       


        
    if (b==0):

        quit()

main()
