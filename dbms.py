#CREATING DATABASE AND TABLE
import mysql.connector as con
mydb=con.connect(host="localhost", user="root", passwd="shashwat1234")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists B_Tech ")
mycursor.execute("use  B_Tech")
mycursor.execute('''create table if not exists User_info
                    (
                     Username varchar(20),
                     mobile_number int(13)
                     )''')
print("**********************************") 
print("WELCOME TO THE University data management") 
print("**********************************") 
print("Please enter your Name and Phone number to begin:-")
username=input("USERNAME:")
mob=int(input("Phone number:"))
st="insert into User_info values(%s,%s)"
val=(username,mob)
mycursor.execute(st,val)
mydb.commit()
print("")
print("""++++++++++++++++++++++++++LOGIN SUCCESSFULL++++++++++++++++++++++++++""")
print("""======================================================================
++++++++++++++++++++++++++    University Data Management     +++++++++++++++++++++++++
==========================================================================""")
mycursor.execute('''create table if not exists Student_info
                   (
                    Student_Name varchar(30) ,
                    Gender varchar(20),
                    Age int(3),
                    Category varchar(20),
                    Department varchar(30),
                    Sid int(5) primary key
                    )''')
mycursor.execute('''create table if not exists Staff_info
                   (
                    Professor_Name varchar(20),
                    PhoneNumber char(10) unique key,
                    Department varchar(30),
                    Age int(100),
                    Joining_Date date,
                    Sid int(5) primary key,
                    foreign key (Sid) references Student_info (Sid)
                    )''')
mycursor.execute('''create table if not exists seats_distribution
                   (
                    Seats_In_First_Year int(3),
                    Seats_In_Second_Year int(3),
                    Seats_In_Third_Year int(3),
                    Seats_In_Final_Year int(3),
                    Department_available varchar(20)
                   )''')
#Fees for CSE
mycursor.execute('''create table if not exists Fees_Collection_CSE
                   (
                    Fees_In_First_Year int(3),
                    Fees_In_Second_Year int(3),
                    Fees_In_Third_Year int(3),
                    Fees_In_Final_Year int(3),
                    Department_CSE varchar(20)
                   )''')
#Fees for Electrical Engineering 
mycursor.execute('''create table if not exists Fees_Collection_Electrical
                   (
                    Fees_In_First_Year int(3),
                    Fees_In_Second_Year int(3),
                    Fees_In_Third_Year int(3),
                    Fees_In_Final_Year int(3),
                    Department_Electrical_Engineering varchar(20)
                   )''') 
mydb.commit()
print("")
print("""
1:Add Student info
2:Delete Student info
3:Search Student info
4:Staff Details
5:Total Seats Distribution
6:Annual fees  
7:Exit""")
print("")
a=int(input("Enter your choice:"))
print("")
#ADD STUDENT INFO
if a==1:  
    print("All information prompted are mandatory to be filled")
    name=input("Enter  Name:")
    gender=input("Gender:")
    age=int(input("Enter age:"))      
    Category=input("Enter Category GEN/OBC/SC-ST:")
    department=input("Enter department:")
    s_id=int(input("enter student id"))
    mycursor.execute("insert into Student_info (Student_Name,Gender,Age,Category,Department,Sid) values(%s,%s,%s,%s,%s,%s)",(name,gender,age,Category,department,s_id))
    print("")
    mydb.commit()
    print("""++++++++++++++++++++++
    ++DATA SUCCESSFULLY ADDED++
    ++++++++++++++++++++++""") 
#DELETE BOOKS
elif a==2:
    print("student id is compulsory") 
    print("")
    name=input("Enter  Name:")                 
    department=input("Enter department:")
    s_id=int(input("enter student id"))
    mycursor.execute("DELETE FROM Student_info WHERE Sid=%s",(s_id,))
    print("")
    print("""++++++++++++++++++++++
    ++DATA SUCCESSFULLY REMOVED++
    ++++++++++++++++++++++""") 
#Searching Student Info
elif a==3:
    print("search by :-")
    print("")
    print("""1:Search by name
2:Search by Student id """)
    print("")
    l=int(input("Search by?:"))
    #BY Student NAME
    print("")
    if l==1:
        o=input("Enter Name to search:")
        mycursor.execute("select * from Student_info where Student_Name='%s'",(o,))
        tree=mycursor.fetchall()
        print("")
        if tree!=None:
            
            print("""++++++++++++++++++++
                    ++Student Info Is Avilable++
                    ++++++++++++++++++++""")
        else:
            print("Student Info Is Not Avilable!!!!!!!")
    elif l==2:
        o=int(input("Enter student id to search:"))
        mycursor.execute("select * from Student_info where Sid='%s'",(o,))
        tree=mycursor.fetchone()
        print("")
        if tree!=None:
            print("""++++++++++++++++++++
                ++Student Info Is Avilable++
                     ++++++++++++++++++++""")
        else:
            print("Student Info Is Not Avilable!!!!!!!")
    else:
        print("Invalid Choice")                 
#staff details
elif a==4:
    print("")
    print("1:Print all Staff detail")
    print("2:Print staff department vise ")
    print("3:New staff entry")
    print("4:Remove staff")
    print("")
    ch=int(input("Enter your choice:"))
    print("")
    if ch==1:
        mycursor.execute("select * from Staff_info")
        run=mycursor.fetchall()
        print("")
        for i in run:
            print(i)
    if ch==2:          
        mycursor.execute("select * from Staff_info GROUP BY Department ")
        run=mycursor.fetchall()
        print("")
        for i in run:
            print(i)
    if ch==3:
        ProfessorName=str(input("Enter Fullname:"))
        phno=int(input("Staff phone no.:"))
        Department =str(input("CSE/Electrical:"))
        age=int(input("Age:"))
        Joining_Date=input("yyyy-mm-dd")               
        Sid= int(input("enter student id") )             
        mycursor.execute("insert into Staff_info(Professor_Name,PhoneNumber,Department,Age,Joining_Date,Sid) values('"+ProfessorName+"','"+Department+"','"+str(age)+"','"+str(Joining_Date)+"', "'+str(sid)+'");")
        print("")
        print("""+++++++++++++++++++++++++++++
        +STAFF IS SUCCESSFULLY ADDED+
        +++++++++++++++++++++++++++++""")
        mydb.commit()            
    if ch==4:
        nm=str(input("Enter staff name to remove:"))
        mycursor.execute("select name from staff_info where name='"+nm+"'")
        toy=mycursor.fetchone()
        if toy is not None:
            mycursor.execute("delete from staff_info where name='"+nm+"'")
            print("")
            print("""+++++++++++++++++++++++++++++++++
                    ++STAFF IS SUCCESSFULLY REMOVED++
                    +++++++++++++++++++++++++++++++++""")
            mydb.commit()
        else:
            print("")
            print("STAFF DOESNOT EXIST!!!!!!")
#Total Seats Distribution
elif a==5:
    print("1:Seats for CSE")
    print("2:Seats for Electrical Engineering")
    print("")
    ch=int(input("Enter your choice:"))
    print("")
    if ch==1:
        print("Seats available is CSE departments:")
        print("")
        mycursor.execute("select * from seats_distribution  ")
        run=mycursor.fetchall()
        print("")
        for i in run:
            print(i) 
    if ch==2:                 
        mycursor.execute("select * from seats_distribution where Department_available=Electrical engineering")
        run=mycursor.fetchall()
        print("")
        for i in run:
            print(i)            
#total fees for each year
elif a==6:
    print("1:fees for CSE")
    print("2:fees for electrical engineering")
    print("")
    ch=int(input("enter your choice:"))
    print("")
    if ch==1:
        print("Fees FOR CSE DEpartment Annualy")
        print("")
        mycursor.execute("select * from Fees_Collection_CSE")
        run=mycursor.fetchall()
        print("")
        for i in run:
            print(i)               
    if ch==2:
        mycursor.execute("select * FROM Fees_Collection_Electrical")
        run=mycursor.fetchall()
        print("")
        for i in run:
            print(i) 
#EXIT                         
elif a==7:
        print("""++++++++++++++++++++++++++THANKS FOR VISITING++++++++++++++++++++++++++""")
        print("""======================================================================
        ++++++++++++++++++++++++++    University Data Management     +++++++++++++++++++++++++
        ==========================================================================""")
else:
        print ("%%%%%%%%%%%%%%%%%% The service you have selected is not available%%%%%%%%%%%%%%%%%%")                 
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

