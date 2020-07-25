import mysql.connector

from os import system,name

import time

def clear():
 _=system('cls')

import getpass

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "allunited999",
  database = "mydatabase"
)

mycursor = mydb.cursor()
#my_cursor=mydb.cursor()

#mycursor.execute("CREATE TABLE customers (name varchar(255),address varchar(255))")
#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

def authenticate():
    #mycursor.execute("DROP TABLE user1")
    #mydb.commit()
    #sql = "CREATE TABLE IF NOT EXISTS user1( username VARCHAR(255) UNIQUE,password VARCHAR(255) UNIQUE)"
    #mycursor.execute(sql)
    #mydb.commit()
    #sql = "INSERT INTO user1(username,password) VALUES (%s,%s)"
    #val = ('ShnAlmighty','getgod')
    #mycursor.execute(sql,val)
    #mydb.commit()
    clear()
    print("\t\t\t\t -----------------------------------------------")
    print("\t\t\t\t|                 Login Page:                   | ")
    print("\t\t\t\t -----------------------------------------------")
    user_name = getpass.getpass("Username: ")
    sql = "SELECT username FROM user1 WHERE username = %s"
    val = (user_name,)
    chk,chkp = 1,1
    mycursor.execute(sql,val)
    for x in mycursor:
        if user_name == x[0] : chk = 0

    if chk == 0:
        pass_word = getpass.getpass()
        sql = "SELECT password FROM user1 WHERE password = %s and username = %s"
        val = (pass_word,user_name)
        mycursor.execute(sql,val)
        for y in mycursor:
          if pass_word == y[0]: chkp = 0
          
    if chkp == 0 :
                  clear()
                  print("\n\n\n\n\n\n\n\n\n\n\n")
                  print("************************************************************************************************************************")
                  print("\t\t\t\t\t\t| WELCOME: ADMIN |")
                  print("************************************************************************************************************************")
                     #print("WELCOME ADMIN")
                  time.sleep(1.5)
                  main()
    elif chkp == 1 and chk == 0:
             print("Access Denied: Incorrect Password!")
             time.sleep(1)
             clear()
             exit()

             
    elif chk == 1:
         print("Access Denied: Incorrect Username!")
         time.sleep(1)
         clear()
         exit()





    """
    #user_na = getpass.getuser()
    user_name = getpass.getpass("Username:")
    
    sql = "SELECT username,password FROM user1"
    #val = (user_name,pass_word)
    mycursor.execute(sql)
    for x in mycursor:
     if (user_name == x[0]):
       pass_word = getpass.getpass() 
       if (pass_word == x[1]):
         clear()
         print("\n\n\n\n\n\n\n\n\n\n\n")
         print("************************************************************************************************************************")
         print("\t\t\t\t\t\t| WELCOME: ADMIN |")
         print("************************************************************************************************************************")
         #print("WELCOME ADMIN")
         time.sleep(1.5)
         main()
       else:
             print("Access Denied: Incorrect Password!")
             time.sleep(1)
             clear()
             exit()

     else:
        print("Access Denied: Incorrect Username!")
        time.sleep(1)
        clear()
        exit()
     """

"""
def store():
    sql = "CREATE TABLE IF NOT EXISTS store(details VARCHAR(255))"
    mycursor.execute(sql)
    mydb.commit()
    sto = [None]*1000
    b = 0
    mycursor.execute("SELECT * FROM bill")
    for x in mycursor:
       sto[b] = x
       b=b+1
    for x in range(0,b):
     sql = "INSERT INTO store VALUES(%s)"
     val = (str(sto[x]),)
     mycursor.execute(sql,val)
     mycursor.commit()
"""
def dat():
 count = 0
 mycursor.execute("SHOW TABLES LIKE 'customers'")
 res = mycursor.fetchone()
 if res :  
  clear()
  print("***********************************************************************************************************************")
  print("\t\t\t\t\t\tWELCOME: ADD NEW MEMBERS")
  print("***********************************************************************************************************************")
  a=input("Enter name: ")
  b=input("Enter address: ")
  c = input("Enter Mobile Number: ")
  d = input("Set your Account password: ")
  sql = "INSERT INTO customers (name,address,number) VALUES (%s,%s,%s)"
  val = (a,b,c)
  mycursor.execute(sql,val)
  mydb.commit()
  print("Updating Database...")
  time.sleep(1)
  print("Updated")
  sql = "Select * FROM customers "
  mycursor.execute(sql)
  result = mycursor
  for x in result:
    count=count+1
    #i.append(x[0])
    #n.append(x[1])
    #ad.append(x[2])
    #numb.append(x[3])  
      
  sql = "INSERT INTO user3(id,cust_name,address,num,paswd) VALUES (%s,%s,%s,%s,%s) "
  val = (count+1,a,b,c,d)
  mycursor.execute(sql,val)
  mydb.commit()
 
 else: 
  print("Table does not exists!!\nCreate Table First")


def disp():
 mycursor.execute("SHOW TABLES LIKE 'customers'")
 res = mycursor.fetchone()
 if res : 
  clear()
  print("***********************************************************************************************************************")
  print("\t\t\t\t\t\t\tDISPLAY MENU")
  print("***********************************************************************************************************************")
  mycursor.execute("SELECT * FROM customers")
  #y,z="",""
  print("|ID| ","| Name |"," |Address|","| Mobile No|")
  for x in mycursor:
   print(x)
   time.sleep(0.5)
   """
   y = x[0]
   z = x[1]
   zz = x[2]
   print("x=",x,"y=",y,"z=",z,"zz=",zz)
   """
  
   #records = mycursor.fetchall()
   #for row in records:
   #print("Name = ",row[0])
  
 else: 
  print("Table does not exists!!\nCreate Table First")
  

def dele():
 mycursor.execute("SHOW TABLES LIKE 'customers'")
 res = mycursor.fetchone()
 if res : 
  clear()
  print("***********************************************************************************************************************")
  print("\t\t\t\t\t\t\tREMOVAL MENU")
  print("***********************************************************************************************************************")
  f = input("Enter ID of the customer to be removed: ")
  
  go = check(int(f))

  if(go == 0):
   for x in mycursor:pass
   sql1 = "SELECT * FROM customers where id = %s "
   val1 =(f,)
   mycursor.execute(sql1,val1)
   for x in mycursor:
    print(x)

   v = input("You want to remove this customer?(y/n)")
 
   if v == "y" or v == "Y" :
    print("Removing please wait...")
    time.sleep(2)
    sql = "DELETE FROM customers WHERE id = %s"
    val = (f,)
    mycursor.execute(sql,val)
    mydb.commit()
    print("DELETED")
    sql11 = "UPDATE customers SET id = id-1 WHERE id >= %s" 
    val11 = (int(f)+1,)
    mycursor.execute(sql11,val11)
    mydb.commit()
    mycursor.execute("SELECT MAX(id) FROM customers")
    u = ""
    for x in mycursor:
     u = x[0]   
    sql111 = "ALTER TABLE customers AUTO_INCREMENT = %s"
    val111 = (1,) #seting 1 instead of u also works as primary key is unique so interpretor automatically assigns the newly added entry with an unique id that is just unit bigger
    mycursor.execute(sql111,val111)
    mydb.commit()
    disp()
  	

  else: print("INVALID ID")
 
 else: 
  print("Table does not exists!!\nCreate Table First")

def create():
 mycursor.execute("SHOW TABLES LIKE 'customers'")
 res = mycursor.fetchone()
 if res :
  print("Table already exists kindly proceed with operations or Drop it:")
  time.sleep(1)
 else:
  #if chk !=1 :
   mycursor.execute("CREATE TABLE IF NOT EXISTS customers(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255),number BIGINT UNIQUE)")
   #check = 1
   print("Creating table please wait...")
   time.sleep(1)
   print("Table customers created\n Moving to Menu...")
   time.sleep(1)

def drop():
 #if uo != 1:
 mycursor.execute("SHOW TABLES LIKE 'customers'")
 res = mycursor.fetchone()
 if res : 
  mycursor.execute("DROP TABLE IF EXISTS customers")
  #chk1 = 1
  print("Removing table please wait...")
  time.sleep(1)
  print("Table customers Deleted")
  time.sleep(1)
 else:
    print("No table created kindly create table first")
    time.sleep(1)

def check(fe):
 mycursor.execute("SELECT id FROM customers")
 for x in mycursor:
  if fe in x :
   return 0
  

def search():
 mycursor.execute("SHOW TABLES LIKE 'customers'")
 res = mycursor.fetchone()
 if res : 
  clear()
  print("***********************************************************************************************************************")
  print("\t\t\t\t\t\tADDRESS SEARCH MENU")
  print("***********************************************************************************************************************")
  fi = input("Enter customer name or id :") 
  lop = check(int(fi))
  #mycursor.execute("SELECT id FROM customers")
  #for x in mycursor:
  #if int(fi) == int(x[0]):
  for i in mycursor: pass
  if lop == 0:
   sql = "SELECT address FROM customers WHERE id = %s OR name = %s"
   val = (fi,fi)
   mycursor.execute(sql,val)
   for x in mycursor:
    print(x)
  
  else: print("INVALID ID")
 
 else: 
  print("Table does not exists!!\nCreate Table First")

def staff():
  p1 = 0
  while p1 == 0 :
   clear()
   print("***********************************************************************************************************************")
   print("\t\t\t\t\t\t\tSTAFF MENU")
   print("***********************************************************************************************************************")
   print("0: Create Table")
   print("1: Add Staff Members")
   print("2: Show Staff Details")
   print("3: Remove Staff Members")
   print("4: Search Staff")
   print("5: Update Details")
   print("6: Drop Table")
   print("7: Go Back To Main Menu")
   sel = int(input("ENter your choice: "))

   if(sel == 0): 
       mycursor.execute("SHOW TABLES LIKE 'staff'")
       res = mycursor.fetchone()
       if res :
           print("Table already exists!")
           time.sleep(1)
       else:
           sql = "CREATE TABLE IF NOT EXISTS staff(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))"
           mycursor.execute(sql)
           mydb.commit()
           sql1 = "ALTER TABLE staff AUTO_INCREMENT = 100"
           mycursor.execute(sql1)
           mydb.commit()
           print("Creating please wait...")
           time.sleep(1)
           print("Created")
           time.sleep(1)

   elif sel == 1 :
    loop = 0
    while loop == 0 :
       clear()
       print("***********************************************************************************************************************")
       print("\t\t\t\t\t\tWELCOME: ADD NEW MEMBERS")
       print("***********************************************************************************************************************")
       mycursor.execute("SHOW TABLES LIKE 'staff'")
       res = mycursor.fetchone()
       if res :
         f = input("Enter Name of the staff member: ")
         f1 = input("Enter Address: ")
         sql = "INSERT INTO staff(name,address) VAlUES (%s,%s) "
         val = (f,f1)
         mycursor.execute(sql,val)
         mydb.commit()
         print("Updating DataBase...")
         time.sleep(1)
         print("Updated")
         time.sleep(1)
       else:
         print("Table does not exists\n Please create one")
         time.sleep(1)
       dot = input("Continue?(y/n) ")
       if(dot == "n" or dot == "N") :
           loop=1

   elif sel == 2 :
    loop = 0
    while loop == 0 :
       clear()
       print("***********************************************************************************************************************")
       print("\t\t\t\t\t\tDISPLAY MENU")
       print("***********************************************************************************************************************")
       mycursor.execute("SHOW TABLES LIKE 'staff'")
       res = mycursor.fetchone()
       if res :
           print("Fetching details...")
           time.sleep(1)
           mycursor.execute("SELECT * FROM staff")
           for x in mycursor:
            print(x)
            time.sleep(1)
           #time.sleep(2)
       else :
            print("Table does not exists \n please create one")
            time.sleep(1)
       gh = input("Continue?(y/n) ")
       if (gh == "n" or gh == "N"):
          loop=1
      
            
   elif sel == 3 :
    loop = 0
    while loop == 0 :
       clear()
       print("***********************************************************************************************************************")
       print("\t\t\t\t\t\tREMOVAL MENU")
       print("***********************************************************************************************************************")
       mycursor.execute("SHOW TABLES LIKE 'staff'")
       res = mycursor.fetchone()
       if res :
        j = input("Enter Name or Id of the Staff member: ")
        sql = "SELECT * FROM staff WHERE id = %s OR name = %s"
        val = (j,j)
        mycursor.execute(sql,val)
        for x in mycursor:
         print(x)
        g = input("Do you want to remove this Staff member?(y/n)")

        if(g == 'y' or g == 'Y') :

           if(j.isalpha()):
            sqlo = "SELECT id FROM staff where name = %s"
            valo = (j,)
            mycursor.execute(sqlo,valo)
            for x in mycursor:
             j = x[0]

           print("Deleting Please Wait...")
           time.sleep(1)
           sql1 = "DELETE FROM staff WHERE id = %s"
           val1 = (j,)
           mycursor.execute(sql1,val1)
           mydb.commit()
           sql111 = "UPDATE staff SET id = id-1 WHERE id >= %s"
           val111 = (int(j)+1,)
           mycursor.execute(sql111,val111)
           mydb.commit()
           sqll="SELECT MAX(id) FROM staff"
           u = ""
           mycursor.execute(sqll)
           for y in mycursor:
            u = y[0]
           sql11 = "ALTER TABLE staff AUTO_INCREMENT = %s"
           val11 = (u,)
           mycursor.execute(sql11,val11)
           mydb.commit()
           print("DELETED")
           time.sleep(1)
           
       else:
           print("Table does not exist!\nCreate Table first")
           time.sleep(1)
       dot = input("Continue?(y/n) ")
       if(dot == "n" or dot == "N"):
        loop=1
       

   elif sel == 4 :
    loop = 0
    while loop == 0 :
     clear()
     print("***********************************************************************************************************************")
     print("\t\t\t\t\t\tSEARCH MENU")
     print("***********************************************************************************************************************")
     mycursor.execute("SHOW TABLES LIKE 'staff'")
     res = mycursor.fetchone()
     if res :
         inp = input("Enter id of the staff member: ")
         sql = "SELECT * FROM staff WHERE id = %s"
         val = (inp,)
         mycursor.execute(sql,val)
         for x in mycursor:
             print(x)
         time.sleep(1)
     else:
        print("Table does not Exist!")
        time.sleep(1)
     dot = input("Continue?(y/n )")
     if(dot == "n" or dot == "N") :
         loop=1

   elif sel == 5 :
       loop = 0
       while loop == 0:
        clear()
        print("***********************************************************************************************************************")
        print("\t\t\t\t\t\tUPDATE MENU")
        print("***********************************************************************************************************************")
        mycursor.execute("SHOW TABLES LIKE 'staff'")
        res = mycursor.fetchone()
        if res : 
                take = input("Enter id of the Staff Member: ")
                sql = "SELECT * FROM staff WHERE id = %s"
                val = (take,)
                mycursor.execute(sql,val)
                for x in mycursor:
                 print(x)
                take2 = input("Modify?(y/n) ")
                if(take2 == "y" or take2 == "Y"):
                   chose = input("What do you want to change?(Name or Address): ")
                   if(chose == "name" or chose == "Name"):
                      newname = input("Enter New Name: ")
                      print("Updating...")
                      time.sleep(1)
                      sql1 = "UPDATE staff SET name = %s WHERE id = %s"
                      val1 = (newname,take)
                      mycursor.execute(sql1,val1)
                      mydb.commit()
                   elif(chose == "address" or chose == "Address"):
                      newadd = input("Enter New Address: ")
                      print("Updating...")
                      time.sleep(1)
                      sql1 = "UPDATE staff SET address = %s WHERE id = %s"
                      val1 = (newadd,take)
                      mycursor.execute(sql1,val1)
                      mydb.commit()
                      print("Updated")
                      time.sleep(1)
                   else:
                      print("Wrong Field!")
                      time.sleep(1)


        else:
         print("Table does not exists!")
         time.sleep(1)

        join = input("Continue?(y/n)")
        if (join == "n" or join =="N") :
            loop = 1
           
   elif sel == 6 :
    mycursor.execute("SHOW TABLES LIKE 'staff'")
    res = mycursor.fetchone()
    if res :
      mycursor.execute("DROP TABLE IF EXISTS staff")
      print("Removing table Please wait...")
      time.sleep(1)
      print("Removed")
      time.sleep(1)
    else:
       print("Table Does not exist!")
       
   elif sel == 7:

    #p =input("Exit portal:(y/n) ")

    #if (p == "y" or p == "Y"):
     p1 = 1
     #print("Moving to Main Menu...")
     #time.sleep(1)
    
def modify():
     mycursor.execute("SHOW TABLES LIKE 'customers'")
     res = mycursor.fetchone()
     if res :
       clear()
       print("***********************************************************************************************************************")
       print("\t\t\t\t\t\tUPDATE MENU")
       print("***********************************************************************************************************************")
       take = input("Enter id of the Customer: ")
       sql = "SELECT * FROM customers WHERE id = %s"
       val = (take,)
       mycursor.execute(sql,val)
       for x in mycursor:
           print(x)
       take2 = input("Modify?(y/n) ")
       if(take2 == "y" or take2 == "Y"):
        chose = input("What do you want to change?(Name or Address): ")
        if(chose == "name" or chose == "Name"):
         newname = input("Enter New Name: ")
         print("Updating...")
         time.sleep(1)
         sql1 = "UPDATE customers SET name = %s WHERE id = %s"
         val1 = (newname,take)
         mycursor.execute(sql1,val1)
         mydb.commit()
        elif(chose == "address" or chose == "Address"):
         newadd = input("Enter New Address: ")
         print("Updating...")
         time.sleep(1)
         sql1 = "UPDATE customers SET address = %s WHERE id = %s"
         val1 = (newadd,take)
         mycursor.execute(sql1,val1)
         mydb.commit()
         print("Updated")
         time.sleep(1)
        else:
            print("Wrong Field!")
            time.sleep(1)

     else:
         print("Table does not exists!")
         time.sleep(1)


def bill():
           clear()
           bot = ""
           appear = 0
           print("***********************************************************************************************************************")
           print("\t\t\t\t\t\tBILLING COUNTER")
           print("***********************************************************************************************************************")
           m = input("Enter Mobile Number of the Customer: ")
           s = "SELECT number FROM customers"
           #v = (m,)
           mycursor.execute(s)
           check_numb = ""
           for t in mycursor:
             if int(m) == t[0]:  
               check_numb = t[0]
               #print(check_numb)
             #else : check_numb = ""
           customer,item_namee = "",""
           if not check_numb:
               new_user = 1
               take_ans = input("New Customer: Do You want to Sign Up?(y/n) ")
               if(take_ans == "y" or take_ans == "Y"):
                   dat()
                   sq = "SELECT name FROM customers WHERE number = %s"
                   vq = (m,)
                   mycursor.execute(sq,vq)
                   for t in mycursor:
                       customer = t[0]
               else:
                   customer_name = input("Enter your Name: ")
                   customer = customer_name
               time.sleep(1)
           else:
            sql = "SELECT name FROM customers WHERE number = %s"
            val = (m,)
            mycursor.execute(sql,val)            
            for x in mycursor:  
              print("\t\t\t\t WELCOME:",x[0])
              time.sleep(1)
              customer = x[0]
           loop = 0
           total_bill = 0
           items,qty,prices="","",""  
           while loop == 0 :
            clear() 
            print("***********************************************************************************************************************")
            print("\t\t\t\t\t\tITEM SELECTION:")
            print("***********************************************************************************************************************")
            mycursor.execute("SELECT * FROM item")

            for x in mycursor: 
                #print("***********************************************************************************************************************")
                print("\n-ID : ",x[0],"\n-Item Name :",x[1],"\n-Price :",x[2],"\n-Stock: ",x[3])
                print("***********************************************************************************************************************")

            print("***********************************************************************************************************************")
            choose_item = input("Choose item: ")
           # mys = "SELECT "
            if choose_item.isalpha():
                item_namee = choose_item
                sqll = "SELECT id FROM item WHERE name = %s"
                vall = (choose_item,)
                mycursor.execute(sqll,vall)
                for x in mycursor:
                    #choose_item = x[0]
                    bot = x[0]
                if not bot:
                    print("Invalid Item Selection!!")
                    exit()
                else:
                    choose_item = bot
            elif choose_item.isnumeric():
                sqlll = "SELECT name FROM item WHERE id = %s"
                valll = (choose_item,)
                mycursor.execute(sqlll,valll)
                for x in mycursor:
                    item_namee = x[0]
                if not item_namee :
                    print("Invalid Item Id")
                    exit()
            items = items + "\n" + item_namee
            #b=b+1
            mycursor.execute("SHOW TABLES LIKE 'bill'")
            res = mycursor.fetchone()
            if res :
             sqld = "SELECT MAX(turn) FROM bill WHERE cust_name = %s "
             vald = (customer,)
             mycursor.execute(sqld,vald)
             for y in mycursor:
               if y[0] is not None:
                appear = y[0]
               else: appear = 0
            else:
              mycursor.execute("CREATE TABLE IF NOT EXISTS bill(cust_name VARCHAR(255),item_name VARCHAR(255),quantity VARCHAR(255),price VARCHAR(255),tot FLOAT, turn INT) ")
              mydb.commit()

            choose_quantity = int(input("Enter quantity: "))
            qty = qty + "\n" + str(choose_quantity)
            #b2=b2+1
            sql = "SELECT price FROM item WHERE id = %s"
            val = (choose_item,)
            mycursor.execute(sql,val)
            price_item = 0
            for x in mycursor:
                price_item = x[0]
            prices = prices + "\n " + str(price_item)
            #b1=b1+1
            bil = int(price_item)*choose_quantity
            #b = b+1
            total_bill = total_bill+bil
            #bil1=str(bil)
            #sql11 = "INSERT INTO bill (cust_name,item_name,quantity,price) VALUES (%s,%s,%s,%s)"
            #val11 = (customer,item_namee,choose_quantity,price_item,)
            #mycursor.execute(sql11,val11)
            #mydb.commit()
            inm = input("Do you want to add more?(y/n) ")
            if(inm == "n" or inm == "N"):
             loop = 1
            else: clear()

           sqlo = "INSERT INTO bill(cust_name,item_name,quantity,price,tot,turn) VALUES (%s,%s,%s,%s,%s,%s)"
           valo = (customer,items,qty,prices,total_bill,int(appear)+1)
           mycursor.execute(sqlo,valo)
           mydb.commit()
           invoice = open("bill.txt","wt")
           invoice_log = open("billlog.txt","at")
           inv = "***********************************************************************************************************************\n \t\t\t\t\t\t CUSTOMER BILL:\n***********************************************************************************************************************"
           #inv = inv+"\nNAME:"+str(customer)+"\nITEMS:\n"+str(items)+"\tQUANTITY:\n"+str(qty)+"\tPRICES:\n"+str(prices)+"\tTOTAL:\n"+str(total_bill)+"\n"
           inv = inv+"\nNAME:"+str(customer)+"\tITEMS:"+"\tQUANTITY:"+"\tPRICES:"+"\n\t"+str(items)+"\t"+str(qty)+"\t"+str(prices)+"TOTAL:\n"+str(total_bill)+"\n"
           invoice.write(inv)
           invoice_log.write(inv)
           
           """
           sqlo = "INSERT INTO bill(cust_name,item_name,quantity,price,tot,turn) VALUES (%s,%s,%s,%s,%s,%s)"
           valo = (customer,items,qty,prices,total_bill,int(appear)+1)
           """
           clear()
           print("***********************************************************************************************************************")
           print("\t\t\t\t\t\t CUSTOMER BILL:")
           print("***********************************************************************************************************************")
           sqln = "SELECT * FROM bill WHERE cust_name = %s AND turn = %s"
           valn = (customer,int(appear)+1)
           mycursor.execute(sqln,valn)
           for x in mycursor:
                #print("***********************************************************************************************************************")
                print("\n-Customer Name: ",x[0],"\n-Item: ",x[1],"\n-Quantity: ",x[2],"\n-Price: ",x[3],"\n\tTOTAL BILL : ",x[4])
           print("***********************************************************************************************************************")

           wantto = input("\nDo you want to see Bill Log?(y/n)")
           if(wantto == "y" or wantto == "Y"):
            clear()
            print("***********************************************************************************************************************")
            print("\t\t\t\t\t\tBILL LOG:")
            print("***********************************************************************************************************************")
            
            mycursor.execute("SELECT * FROM bill")
            for x in mycursor:
                 #print("***********************************************************************************************************************")
                 print("\n-Customer Name: ",x[0],"\n-Item:",x[1],"\n-Quantity:",x[2],"\n-Price: ",x[3],"\n\tTOTAL BILL : ",x[4])
                 print("***********************************************************************************************************************")

             #print("***********************************************************************************************************************")

            
            

def item():
    fnloop = 0
    while fnloop == 0 :
          clear()
          print("***********************************************************************************************************************")
          print("\t\t\t\t\t\t\tITEM MENU")
          print("***********************************************************************************************************************")
          print("0: Create Table")
          print("1: Add Item")
          print("2: Show Item List")
          print("3: Remove an Item")
          print("4: Search Item")
          print("5: Update Item")
          print("6: Drop Table")
          print("7: Go Back to Main Menu")
          choice = int(input("\nEnter your choice: "))

          if choice == 0:   
           mycursor.execute("SHOW TABLES LIKE 'item'")
           res = mycursor.fetchone()
           if res :
              print("Table already exists!")
              time.sleep(1)
           else:
            sql = "CREATE TABLE IF NOT EXISTS item(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price FLOAT, quantity INT)"
            mycursor.execute(sql)
            mydb.commit()
            #sql1 = "ALTER TABLE staff AUTO_INCREMENT = 100"
            #mycursor.execute(sql1)
            #mydb.commit()
            print("Creating please wait...")
            time.sleep(1)
            print("Created")
            time.sleep(1)

          elif choice == 1:
                 loop = 0
                 while loop == 0 :
                    clear()
                    print("***********************************************************************************************************************")
                    print("\t\t\t\t\t\tWELCOME: ADD NEW ITEMS")
                    print("***********************************************************************************************************************")
                    mycursor.execute("SHOW TABLES LIKE 'item'")
                    res = mycursor.fetchone()
                    if res :
                             f = input("Enter Name of the Item :")
                             f1 = input("Enter Price : ")
                             f2 = input("Enter quantity: ")
                             sql = "INSERT INTO item (name,price,quantity) VAlUES (%s,%s,%s) "
                             val = (f,f1,f2)
                             mycursor.execute(sql,val)
                             mydb.commit()
                             print("Updating DataBase...")
                             time.sleep(1)
                             print("Updated")
                             time.sleep(1)
                    else:
                             print("Table does not exists\n Please create one")
                             time.sleep(1)
                    dot = input("Continue?(y/n) ")
                    if(dot == "n" or dot == "N") :
                                   loop=1


          elif choice == 2:

                loop = 0
                while loop == 0 :
                 clear()
                 print("***********************************************************************************************************************")
                 print("\t\t\t\t\t\tDISPLAY MENU")
                 print("***********************************************************************************************************************")
                 mycursor.execute("SHOW TABLES LIKE 'item'")
                 res = mycursor.fetchone()
                 if res :
                       print("Fetching details...")
                       time.sleep(1)
                       mycursor.execute("SELECT * FROM item")
                       for x in mycursor:
                        print(x)
                        time.sleep(1)
                       #time.sleep(2)
                 else :
                    print("Table does not exists \n please create one")
                    time.sleep(1)
                 gh = input("Continue?(y/n) ")
                 if (gh == "n" or gh == "N"):
                     loop=1


          elif choice == 3:
            loop = 0
            while loop == 0 :
                   clear()
                   print("***********************************************************************************************************************")
                   print("\t\t\t\t\t\tREMOVAL MENU")
                   print("***********************************************************************************************************************")
                   mycursor.execute("SHOW TABLES LIKE 'item'")
                   res = mycursor.fetchone()
                   if res :
                    j = input("Enter Name or Id of the Item: ")
                    sql = "SELECT * FROM item WHERE id = %s OR name = %s"
                    val = (j,j)
                    mycursor.execute(sql,val)
                    for x in mycursor:
                     print(x)
                    g = input("Do you want to remove this Staff member?(y/n)")

                    if(g == 'y' or g == 'Y') :

                        if(j.isalpha()):
                         sqlo = "SELECT id FROM item where name = %s"
                         valo = (j,)
                         mycursor.execute(sqlo,valo)
                         for x in mycursor:
                          j = x[0]

                        print("Deleting Please Wait...")
                        time.sleep(1)
                        sql1 = "DELETE FROM item WHERE id = %s"
                        val1 = (j,)
                        mycursor.execute(sql1,val1)
                        mydb.commit()
                        sql111 = "UPDATE item SET id = id-1 WHERE id >= %s"
                        val111 = (int(j)+1,)
                        mycursor.execute(sql111,val111)
                        mydb.commit()
                        sqll="SELECT MAX(id) FROM item"
                        u = ""
                        mycursor.execute(sqll)
                        for y in mycursor:
                            u = y[0]
                        sql11 = "ALTER TABLE item AUTO_INCREMENT = %s"
                        val11 = (u,)
                        mycursor.execute(sql11,val11)
                        mydb.commit()
                        print("DELETED")
                        time.sleep(1)
           
                   else:
                       print("Table does not exist!\nCreate Table first")
                       time.sleep(1)
                   dot = input("Continue?(y/n) ")
                   if(dot == "n" or dot == "N"):
                    loop=1
              
          elif choice == 4 :
                  loop = 0
                  while loop == 0 :
                     clear()
                     print("***********************************************************************************************************************")
                     print("\t\t\t\t\t\tSEARCH MENU")
                     print("***********************************************************************************************************************")
                     mycursor.execute("SHOW TABLES LIKE 'item'")
                     res = mycursor.fetchone()
                     if res :
                         inp = input("Enter id or Name of the Item: ")
                         if (inp.isalpha()):
                             sql = "SELECT id FROM item WHERE name = %s"
                             val = (inp,)
                             mycursor.execute(sql,val)
                             for x in mycursor:
                                 inp = x[0]
                         sql = "SELECT * FROM item WHERE id = %s"
                         val = (inp,)
                         mycursor.execute(sql,val)
                         for x in mycursor:
                             print(x)
                             time.sleep(1)
                     else:
                        print("Table does not Exist!")
                        time.sleep(1)
                     dot = input("Continue?(y/n)")
                     if(dot == "n" or dot == "N") :
                         loop=1

          elif choice == 6 :
                mycursor.execute("SHOW TABLES LIKE 'item'")
                res = mycursor.fetchone()
                if res :
                  mycursor.execute("DROP TABLE IF EXISTS item")
                  print("Removing table Please wait...")
                  time.sleep(1)
                  print("Removed")
                  time.sleep(1)
                  mydb.commit()
                else:
                   print("Table Does not exist!")

          elif choice == 5 :
                  loop = 0
                  while loop == 0:
                    clear()
                    print("***********************************************************************************************************************")
                    print("\t\t\t\t\t\tUPDATE MENU")
                    print("***********************************************************************************************************************")
                    mycursor.execute("SHOW TABLES LIKE 'item'")
                    res = mycursor.fetchone()
                    if res : 
                        take = input("Enter id of the Item ID : ")
                        sql = "SELECT * FROM item WHERE id = %s"
                        val = (take,)
                        mycursor.execute(sql,val)
                        for x in mycursor:
                         print(x)
                        take2 = input("Modify?(y/n) ")
                        if(take2 == "y" or take2 == "Y"):
                           chose = input("What do you want to change?(Name or price or quantity): ")
                           if(chose == "name" or chose == "Name"):
                            newname = input("Enter New Name: ")
                            print("Updating...")
                            time.sleep(1)
                            sql1 = "UPDATE item SET name = %s WHERE id = %s"
                            val1 = (newname,take)
                            mycursor.execute(sql1,val1)
                            mydb.commit()
                           elif(chose == "price" or chose == "Price"):
                            newadd = input("Enter New Address: ")
                            print("Updating...")
                            time.sleep(1)
                            sql1 = "UPDATE item SET price = %s WHERE id = %s"
                            val1 = (newadd,take)
                            mycursor.execute(sql1,val1)
                            mydb.commit()
                            print("Updated")
                            time.sleep(1)
                           elif(chose == "quantity" or chose == "Quantity"):
                            newadd = input("Enter New Quantity: ")
                            print("Updating...")
                            time.sleep(1)
                            sql1 = "UPDATE item SET quantity = %s WHERE id = %s"
                            val1 = (newadd,take)
                            mycursor.execute(sql1,val1)
                            mydb.commit()
                            print("Updated")
                            time.sleep(1)
                        else:
                         print("Wrong Field!")
                         time.sleep(1)


                    else:
                     print("Table does not exists!")
                     time.sleep(1)

                    join = input("Continue?(y/n)")
                    if (join == "n" or join =="N") :
                        loop = 1

          elif choice == 7:
             fnloop = 1
            

def main():
# check,chk1 = 0,0
 #create(check)
 l = 0
 while(l == 0):
  check,chk1 =0,0
  dd = 0
  clear()
  print("***********************************************************************************************************************")
  print("\t\t\t\t\t\t\tMENU")
  print("***********************************************************************************************************************")
  print("0: Create Table")
  print("1: Add Members")
  print("2: Show Database")
  print("3: Remove Members")
  print("4: Search Customer Address")
  print("5: Drop Table")
  print("6: Update Customer Details")
  print("7: Staff Management")
  print("8: Item Management")
  print("9: Generate Bill")
  print("10: Delete Bill Log")
  print("11: Exit Program")
  choice = int(input("\nEnter your choice: "))
  
  if choice == 0 :
   create()

  elif choice == 9 :
      loop = 0
      while loop == 0:
          bill()
          ans = input("Want to continue?(y/n)")
          if(ans == "N" or ans == "n"):
            print("Moving to Main Menu..")
            time.sleep(1)
            loop = 1

  elif choice == 10:
      you = input("Do you want to delete the Bill Log?(y/n)")
      if(you == "Y" or you == "y"):
           mycursor.execute("DROP TABLE bill") 
           mydb.commit()
           print("Deleting Bill Log...")
           time.sleep(1)
           print("Deleted")
           time.sleep(1)
      print("Moving to Main Menu...")
      time.sleep(1)

  elif choice == 8 :
      loop = 0
      while loop == 0:
          item()
          ans = input("Want to continue?(y/n)" )
          if(ans != "Y" or ans != "y"):
             print("Moving to Main Menu...")
             time.sleep(1)
             loop = 1
             #time.sleep(1)

  elif choice == 6 :
     loop = 0
     while loop ==0:
         modify()
         ho = input("Want to continue: (y/n)")
         if(ho == "n" or ho == "N"):
          loop = 1
     time.sleep(1)

  elif choice == 7:
   lo = 'y'
   while(lo == 'y' or lo == 'Y'):
    staff()
    lo = input("Want to continue:(y/n) ")
   if(lo != 'y' or lo != 'Y'):
    print("Moving to Main Menu...")
    time.sleep(1)
     
  elif choice == 5 :
   drop()

  elif choice == 1 :
   o = input("Want to add?(y/n)")
   while(o == "y" or o == "Y"):
     dat()
     o=input("Want to continue?(y/n):")
     if o == "N" or o == "n":
      print("Thank you")
      time.sleep(1)
      """print("Your database is:")
      disp()"""
  
  elif choice == 2 :
   cho = input("Do you want to see database?(y/n)")
   while(cho == 'y' or cho == 'Y'):
    disp()
    cho = input("do you want to continue?(y/n)")
    if(cho != 'y' or cho !='Y'):
     time.sleep(1)
   """if cho == "n" or cho == "N"
    print("")"""
  
  elif choice == 3 :
   ch1 = input("Do you want to delete from database?(y/n)")
   while(ch1 == 'y' or ch1 == 'Y'):
    dele()
    ch1 = input("Want to continue?(y/n)")
  
  elif choice == 11 :
   print("Thank you for visiting")
   l = 1
   time.sleep(1)

  elif choice == 4:
   c2 = "y"
   while(c2 == "y" or c2 == "Y"):
    search()
    c2 = input("Want to continue?(y/n)")

  else:
   print("Wrong choice!!!")
   dd = 1
  
  """if dd != 1 :
   g = input("Exit(y/n)?")
   if g == 'y' or g == 'Y':
    l = 1"""
  
#main()
authenticate()
#store()
#mycursor.execute("DROP TABLE bill")
#mydb.commit()
#create()
#mycursor.execute("ALTER TABLE customers ADD COLUMN ID INT AUTO_INCREMENT PRIMARY KEY")
