def object1(): #Declaring a section

    obj1=input("Are you carrying any firearms? (y/n) ") #Asking question

    if obj1 == 'n': #Proceeding if no
        print("") #Making it neat by adding a free line
        object2()
    elif obj1 == 'y': #Asking to inform someone if yes
        print("")
        print("Please inform a security officer to proceed.")
        exit() #End program
    else:
        print("")
        print("Invalid input, try again. ")
        print("")
        object1() #Starts this section again if invalid input
        
def object2():
    
    obj2=input("Are you carrying any explosives? (y/n) ")

    if obj2 == 'n':
        print("")
        object3()
    elif obj2 == 'y':
        print("")
        print("Please inform a security officer to proceed.")
        exit()
    else:
        print("")
        print("Invalid input, try again. ")
        print("")
        object2()
        
def object3():

    obj3=input("Are you carrying any batteries? (y/n) ")

    if obj3 == 'n':
        print("")
        object4()
    elif obj3 == 'y':
        print("")
        print("Please inform a security officer to proceed.")
        exit()
    else:
        print("")
        print("Invalid input, try again. ")
        print("")
        object3()
        
def object4():
    
    obj4=input("Are you carrying any electric vechiles such as segways, scooters, etc? (y/n) ")

    if obj4 == 'n':
        print("")
        object5()
    elif obj4 == 'y':
        print("")
        print("Please inform a security officer to proceed.")
        exit()
    else:
        print("")
        print("Invalid input, try again. ")
        print("")
        object4()
        
def object5():
    
    obj5=int(input("How much water/drink are you carrying in liters? (Enter 0 if none) "))
    
    if obj5 < 1:
        print("")
        object6()
    else:
        print("")
        print("Please inform a security officer to proceed.")
        exit()
        
def object6():
    
    obj6=int(input("How much shampoo/cleaning products are you carrying in liters? (Enter 0 if none) "))
    
    if obj6 < 1:
        print("")
        declare()
    else:
        print("")
        print("Please inform a security officer to proceed.")
        exit()
        
def declare():
    
    decl=input("Do you need to declare any other items? (y/n) ")

    if decl == 'n':
        print("")
        finish()
    elif decl == 'y':
        print("")
        print("Please inform a security officer to state and declare items.")
        exit()
    else:
        print("")
        print("Invalid input, try again. ")
        print("")
        declare()
        
def finish():
    
    print("Thank you for completing TSA! Enjoy your flight.")

    exit()
    
print("Welcome to Dubai Airport Security's Online TSA.")

object1()