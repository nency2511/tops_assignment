
      

def roll_id1():
            print("1. Add student")
            print("2. Remove student")
            print("3. View all student")
            print("4. view specific student")
      
          

def exit():
            print("**********THANK YOU!  you are exit now************")
                  
def remove_students():
       
       
              
       print(dict1.pop(id))
       print(dict1.pop(fname))
       print(dict1.pop(contact,sub1))
       print(dict1.pop(marks1,fees1))
       print(dict1.pop(sub2,marks2))
       print(dict1.pop(fees2,lname))
       print(dict1.popitem())
       


def view_students():
             print(f"serial no:{id}") 
             print(f"first name:{fname}")
             print(f"last name:{lname}")
             print(f"contact no:{contact}")
             print(f"subject:{sub1}")
             print(f"marks of {sub1}: {marks1}")
             print(f"fees of {sub1}: {fees1}")
             print(f"subject:{sub2}")
             print(f"marks of {sub2}: {marks2}")
             print(f"marks of {sub2}: {fees2}")

def view_specific_students():
        aa=input("enter first name of student you want to know the details:")
        if aa==fname:
            view_students()           
          
             

print("Press 1 for Counsellor:")
print("Press 2 for Faculaty:")
print("press 3 for Student:")

roll_id=input("enter roll_id:")

if roll_id=="1":
             roll_id1()
             choice=input("Enter a choice by counsellor:")

             if choice=="1":
                   id=(input("Enter a Serial Number:"))
                   fname=(input("Enter a First Name:"))
                   lname=(input("Enter a Last Name:"))
                   contact=(input("Enter a Contact Number:"))
                   sub1=(input("Enter a Subject:"))
                   marks1=(input("Enter a Marks:"))
                   fees1=(input("Enter a Fees:"))
                   sub2=(input("Enter a Subject:"))
                   marks2=(input("Enter a Marks:"))
                   fees2=(input("Enter a Fees:"))
                   x=id
                   y={"fname":fname, "lname":lname, "contact":contact, "subject1": {sub1: {"marks":marks1, "fees":fees1}}, 
                        "subject2": {sub2: {"marks":marks2, "fees":fees2}}}
                   dict1=dict.fromkeys(x,y)
                   print(dict1)             
            
                  
            
                   op=(input("Do you want to perform more operation Y/N:"))          
                   if op=="y":
                         roll_id1()
                        
                         choice=input("Enter a choice by counsellor:")
                         if choice=="1":
                                                
                           id=(input("Enter a Serial Number:"))
                           fname=(input("Enter a First Name:"))
                           lname=(input("Enter a Last Name:"))
                           contact=(input("Enter a Contact Number:"))
                           sub1=(input("Enter a Subject:"))
                           marks1=(input("Enter a Marks:"))
                           fees1=(input("Enter a Fees:"))
                           sub2=(input("Enter a Subject:"))
                           marks2=(input("Enter a Marks:"))
                           fees2=(input("Enter a Fees:"))
                           x=id
                           y={"fname":fname, "lname":lname, "contact":contact, "subject1": {sub1: {"marks":marks1, "fees":fees1}}, 
                              "subject2": {sub2: {"marks":marks2, "fees":fees2}}}
                           dict1=dict.fromkeys(x,y)
                           print(dict1) 
                                 
                         elif choice=="2":
                                 id1=input("enter id you want to delete the data:")
                                 if id1==id:
                                         remove_students()        
                                 else:
                                       print("*****oops! SORRY Data not Found*****")


                         elif choice=="3":
                                 view_students() 

                         elif choice=="4":
                                 view_specific_students()  

                         else:
                                 print("*****oops! EnTeR VAlid cHoicE*****")                  

             elif choice=="2":
                               id1=(input("enter id you want to delete the data:"))
                               if id1=="id":
                                       remove_students()
                                  

             elif choice=="3":
                              view_students()


             elif choice=="4":
                          view_specific_students()  

             else:
                    print("*****oops! EnTeR VAlid cHoicE*****")                   

                            
                              
elif roll_id=="2":
        roll_id1()
        choice=input("Enter a choice by faculaty:")

        if choice=="1":
                   id=(input("Enter a Serial Number:"))
                   fname=(input("Enter a First Name:"))
                   lname=(input("Enter a Last Name:"))
                   contact=(input("Enter a Contact Number:"))
                   sub1=(input("Enter a Subject:"))
                   marks1=(input("Enter a Marks:"))
                   fees1=(input("Enter a Fees:"))
                   sub2=(input("Enter a Subject:"))
                   marks2=(input("Enter a Marks:"))
                   fees2=(input("Enter a Fees:"))
                   x=id
                   y={"fname":fname, "lname":lname, "contact":contact, "subject1": {sub1: {"marks":marks1, "fees":fees1}}, 
                        "subject2": {sub2: {"marks":marks2, "fees":fees2}}}
                   dict1=dict.fromkeys(x,y)
                   print(dict1)             
            
                  
            
                   op=(input("Do you want to perform more operation Y/N:"))          
                   if op=="y":
                         roll_id1()
                        
                         choice=input("Enter a choice by faculaty:")
                         if choice=="1":
                                                
                           id=(input("Enter a Serial Number:"))
                           fname=(input("Enter a First Name:"))
                           lname=(input("Enter a Last Name:"))
                           contact=(input("Enter a Contact Number:"))
                           sub1=(input("Enter a Subject:"))
                           marks1=(input("Enter a Marks:"))
                           fees1=(input("Enter a Fees:"))
                           sub2=(input("Enter a Subject:"))
                           marks2=(input("Enter a Marks:"))
                           fees2=(input("Enter a Fees:"))
                           x=id
                           y={"fname":fname, "lname":lname, "contact":contact, "subject1": {sub1: {"marks":marks1, "fees":fees1}}, 
                              "subject2": {sub2: {"marks":marks2, "fees":fees2}}}
                           dict1=dict.fromkeys(x,y)
                           print(dict1) 
                                 
                         elif choice=="2":
                                 id1=input("enter id you want to delete the data:")
                                 if id1==id:
                                         remove_students()        
                                 else:
                                       print("*****oops! SORRY Data not Found*****")


                         elif choice=="3":
                                 view_students() 

                         elif choice=="4":
                                 view_specific_students()  

                         else:
                                 print("*****oops! EnTeR VAlid cHoicE*****")                  

        elif choice=="2":
                   id1=(input("enter id you want to delete the data:"))
                   if id1=="id":
                           remove_students()
                                  

        elif choice=="3":
                        view_students()


        elif choice=="4":
                        view_specific_students() 

        else:
                  print("*****oops! EnTeR VAlid cHoicE*****")

elif roll_id=="3":
        
        print("1.add data")
        print("2.remove data")
        choice=input("Enter a choice by student:")

        if choice=="1":
                   id=(input("Enter a Serial Number:"))
                   fname=(input("Enter a First Name:"))
                   lname=(input("Enter a Last Name:"))
                   contact=(input("Enter a Contact Number:"))
                   sub1=(input("Enter a Subject:"))
                   marks1=(input("Enter a Marks:"))
                   fees1=(input("Enter a Fees:"))
                   sub2=(input("Enter a Subject:"))
                   marks2=(input("Enter a Marks:"))
                   fees2=(input("Enter a Fees:"))
                   x=id
                   y={"fname":fname, "lname":lname, "contact":contact, "subject1": {sub1: {"marks":marks1, "fees":fees1}}, 
                        "subject2": {sub2: {"marks":marks2, "fees":fees2}}}
                   dict1=dict.fromkeys(x,y)
                   print(dict1)             
            
                  
            
                   op=(input("Do you want to perform more operation Y/N:"))          
                   if op=="y":
                         roll_id1()
                        
                         choice=input("Enter a choice by students:")
                         if choice=="1":
                                                
                           id=(input("Enter a Serial Number:"))
                           fname=(input("Enter a First Name:"))
                           lname=(input("Enter a Last Name:"))
                           contact=(input("Enter a Contact Number:"))
                           sub1=(input("Enter a Subject:"))
                           marks1=(input("Enter a Marks:"))
                           fees1=(input("Enter a Fees:"))
                           sub2=(input("Enter a Subject:"))
                           marks2=(input("Enter a Marks:"))
                           fees2=(input("Enter a Fees:"))
                           x=id
                           y={"fname":fname, "lname":lname, "contact":contact, "subject1": {sub1: {"marks":marks1, "fees":fees1}}, 
                              "subject2": {sub2: {"marks":marks2, "fees":fees2}}}
                           dict1=dict.fromkeys(x,y)
                           print(dict1) 
                                 
                         elif choice=="2":
                                 id1=input("enter id you want to delete the data:")
                                 if id1==id:
                                         remove_students()        
                                 else:
                                       print("*****oops! SORRY Data not Found*****")
 

                         else:
                                 print("*****oops! EnTeR VAlid cHoicE*****")                  

        elif choice=="2":
                   id1=(input("enter id you want to delete the data:"))
                   if id1=="id":
                           remove_students()
                                  

        else:
                  print("*****oops! EnTeR VAlid cHoicE*****")



else:
        print("*****oops! EnTeR VAlid cHoicE*****")
                          


        
           