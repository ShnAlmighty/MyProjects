import mysql.connector
from os import system,name
import time
def clear():
 _=system('cls')
import getpass
from PIL import Image,ImageTk
from tkinter import Tk,Button,Label,Entry,Text,Frame,messagebox,HORIZONTAL,Toplevel,Message
global authuser

def subuser(a,b,c,d,e,f,h):
  global aduse
  global adpws
  aduse = b.get()
  adpws = a.get()
  #c.destroy()
  user_name = aduse
  #getpass.getpass("Username: ")
  sql = "SELECT username FROM user1 WHERE username = %s"
  val = (user_name,)
  chk,chkp = 1,1
  mycursor.execute(sql,val)
  for x in mycursor:
      if user_name == x[0] : chk = 0
  if chk == 0:
    pass_word = adpws
    #getpass.getpass()
    sql = "SELECT password FROM user1 WHERE password = %s and username = %s"
    val = (pass_word,user_name)
    mycursor.execute(sql,val)
    for y in mycursor:
        if pass_word == y[0]: chkp = 0
    if chkp == 0 :
      #clear()
      # print("\n\n\n\n\n\n\n\n\n\n\n")
      print("************************************************************************************************************************")
      print("\t\t\t\t\t\t| WELCOME: ADMIN |")
      print("************************************************************************************************************************")
      time.sleep(1.5)
      a.grid_remove()
      b.grid_remove()
      d.grid_remove()
      e.grid_remove()
      f.grid_remove()
      h.grid_remove()
      main()
      global authuser
      if(authuser==0):
        c.destroy()
    elif chkp == 1 and chk == 0:
      messagebox.showinfo("showerror","Access Denied: Incorrect Password!")
      print("Access Denied: Incorrect Password!")
      time.sleep(1)
      clear()
      #authuser=0
      #exit()   
  elif chk == 1:
    messagebox.showinfo("showerror","Access Denied: Incorrect Username!")
    print("Access Denied: Incorrect Username!")
    time.sleep(1)
    clear()
    #authuser=0
    #exit()

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
def setGeo():
      windowWidth = admin.winfo_reqwidth()
      windowHeight = admin.winfo_reqheight()
      positionRight = int(admin.winfo_screenwidth()/2.5 - windowWidth/2)
      positionDown = int(admin.winfo_screenheight()/2 - windowHeight/2)
      admin.geometry("")
      admin.geometry("+{}+{}".format(0, 0))

def setmain():
      admin.title("Admin Login")
      admin.config(bg='#%02x%02x%02x' % (240, 240, 237))
      setGeo()
      us = Label(admin,text="Username")
      us.config(font=("Times New Roman",13))
      us.grid(row=1,column=0,pady=(30,0),ipadx=10,ipady=1)
      usen=Entry(admin,show="*")
      usen.grid(row=1,column=1,pady=(30,0),padx=(0,30),ipadx=150,ipady=10)
      pw = Label(admin,text="Password")
      pw.grid(row=2,column=0,ipadx=10,ipady=1)
      pw.config(font=("Times New Roman",13))
      pwen = Entry(admin,show="*")
      pwen.grid(row=2,column=1,padx=(0,30),ipadx=150,ipady=10)
      adb1 = Button(admin,text='Exit',command=lambda: exit())
      adb1.grid(row=3,column=0,padx=(0,10),pady=30,ipadx=50,ipady=1)
      adb1.config(font=("Times New Roman",13))
      adb = Button(admin,text='Login',command=lambda: subuser(pwen,usen,admin,us,pw,adb,adb1))
      adb.grid(row=3,column=1,padx=(30,0),pady=30,ipadx=50,ipady=1)
      adb.config(font=("Times New Roman",13))
      admin.resizable(False,False)
      admin.mainloop()

def authenticate():
    global authuser
    authuser=1
    while(authuser==1):
      #clear()
      print("\t\t\t\t -----------------------------------------------")
      print("\t\t\t\t|                 Login Page:                   | ")
      print("\t\t\t\t -----------------------------------------------")
      global admin
      admin= Tk()
      setmain()
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
def addmem():
  clear()
  print("***********************************************************************************************************************")
  print("\t\t\t\t\t\tWELCOME: ADD NEW MEMBERS")
  print("***********************************************************************************************************************")
  a = ae1.get()
  b=ae2.get()
  c=ae3.get()
  d=ae4.get()
  #   a=input("Enter name: ")
  #   b=input("Enter address: ")
  #   c = input("Enter Mobile Number: ")
  #   d = input("Set your Account password: ")
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
  count=0
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
  al1.grid_remove()
  ae1.grid_remove()
  al2.grid_remove()
  ae2.grid_remove()
  al3.grid_remove()
  ae3.grid_remove()
  al4.grid_remove()
  ae4.grid_remove()
  asub.grid_remove()
  aframe.grid_remove()
  aframe.destroy()
  disp()

def abackf():
 aframe.grid_remove()
 aframe.destroy()
 setMenu()

def dat():
 #count = 0
 mycursor.execute("SHOW TABLES LIKE 'customers'")
 res = mycursor.fetchone()
 global aframe
 aframe=Frame(admin)
 aframe.grid()
 if res : 
  global al1,al2,ae1,ae2,ae3,ae4,al3,al4,asub,aback
  al1 = Label(aframe,text="Enter name")
  al1.grid(row=0,column=0,sticky='nesw',padx=(4,4),pady=5,ipady=7)
  ae1 = Entry(aframe)
  ae1.grid(row=0,column=1,sticky='nesw',padx=(4,4),pady=5,ipady=7,ipadx=120)
  al2 = Label(aframe,text="Enter Address")
  al2.grid(row=1,column=0,sticky='nesw',padx=(4,4),pady=5,ipady=7)
  ae2 = Entry(aframe)
  ae2.grid(row=1,column=1,sticky='nesw',padx=(4,4),pady=5,ipady=7,ipadx=120)
  al3 = Label(aframe,text="Enter Mobile Number")
  al3.grid(row=2,column=0,sticky='nesw',padx=(4,4),pady=5,ipady=7)
  ae3 = Entry(aframe)
  ae3.grid(row=2,column=1,sticky='nesw',padx=(4,4),pady=5,ipady=7,ipadx=120)
  al4 = Label(aframe,text="Enter Password")
  al4.grid(row=3,column=0,sticky='nesw',padx=(4,4),pady=5,ipady=7)
  ae4 = Entry(aframe)
  ae4.grid(row=3,column=1,sticky='nesw',padx=(4,4),pady=5,ipady=7,ipadx=120)
  asub = Button(aframe,text="Submit",command=addmem)
  asub.grid(row=4,column=1,sticky='nesw',padx=(4,4),pady=5,ipady=10,ipadx=50)
  aback = Button(aframe,text="Back",command=abackf)
  aback.grid(row=4,column=0,sticky='nesw',padx=(4,4),pady=5,ipady=10,ipadx=50)
  setGeo()

 else: 
  print("Table does not exists!!\nCreate Table First")
 
def removeDis():
  global d1,d2,d3
  d1.grid_remove()
  for i in range(0,len(d2)):
   d2[i].grid_remove()
  d3.grid_remove()
  setMenu()

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
  global d1,d2,d3
  admin.config(bg="grey")
  setGeo()
  d1=Label(admin,text='Customers List')
  d1.grid(row=0,column=0,sticky='nesw')
  d2 = []
  fp=0
  r=1
  c=0
  for x in mycursor:
   #d2.insert(INSERT,x)
   d2.insert(fp,Label(admin))
   d2[fp].config(text=x)
   if(r%10==0):
       c=c+1
       r=1
   d2[fp].grid(row=r,column=c,sticky='nesw',padx=(4,4),pady=5,ipady=10)
   r=r+1
   fp=fp+1
   #print(x)
   #time.sleep(0.5)
  d3=Button(admin,text="back",command=lambda: removeDis())
  d3.grid(row=fp,column=0,sticky='nesw')
  admin.geometry("")
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

def rok1(id):
    print("Removing please wait...")
    time.sleep(2)
    sql = "DELETE FROM customers WHERE id = %s"
    val = (id,)
    mycursor.execute(sql,val)
    mydb.commit()
    print("DELETED")
    sql11 = "UPDATE customers SET id = id-1 WHERE id >= %s" 
    val11 = (int(id)+1,)
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
    setRemove()
    disp()

def setRemove():
    rl3.grid_remove()
    rl2.grid_remove() 
    rok.grid_remove()
    rno.grid_remove()
    # if(inv.winfo_exists()):
    #     inv.grid_remove()
    dframe.grid_remove()
    dframe.destroy()
    dele()

# def invbf():
#     inv.grid_remove()
#     invb.grid_remove()
#     dframe.pack_forget()
#     dframe.destroy()
#     dele()

def remcu():
  clear()
  print("***********************************************************************************************************************")
  print("\t\t\t\t\t\t\tREMOVAL MENU")
  print("***********************************************************************************************************************")
  f=re1.get()
  #f = input("Enter ID of the customer to be removed: ")
  go = check(int(f))
  #global inv
  if(go == 0):
   re1.grid_remove()
   rl1.grid_remove()
   rsub.grid_remove()
   rback.grid_remove()
   for x in mycursor:pass
   sql1 = "SELECT * FROM customers where id = %s "
   val1 =(f,)
   mycursor.execute(sql1,val1)
   setGeo()
   global rl2,rl3,rok,rno
   for x in mycursor:
    rl2=Label(dframe,text=x)
    rl2.grid(row=0,column=0)
    #print(x)
   rl3=Label(dframe,text="You want to remove this customer?")
   rl3.grid(row=1,column=0,sticky='nesw',padx=(4,4),pady=5,ipady=1)
   rok=Button(dframe,text="Yes",command=lambda:rok1(f))
   rok.grid(row=2,column=0,sticky='nesw',padx=(4,4),pady=5,ipady=1)
   rno=Button(dframe,text="No",command=lambda: setRemove())
   rno.grid(row=3,column=0,sticky='nesw',padx=(4,4),pady=5,ipady=1)
#    v = input("You want to remove this customer?(y/n)")
#    if v == "y" or v == "Y" :	
  else:
    messagebox.showinfo("showerror","Invalid ID customer does not exists")
    #   rsub.grid_remove()
    #   rback.grid_remove() 
    #   inv=Label(dframe)
    #   inv.grid(row=2,column=0,sticky='nesw')
    #   inv.config(text="Invalid ID")
    #   global invb 
    #   invb = Button(dframe,text="back",command=invbf)
    #   invb.grid(row=3,column=0,sticky='nesw')
      #dele()
      #print("INVALID ID")

def removeRM():
    rl1.grid_remove()
    re1.grid_remove()
    rsub.grid_remove()
    rback.grid_remove()
    dframe.grid_remove()
    dframe.destroy()
    setMenu()

def dele():
 mycursor.execute("SHOW TABLES LIKE 'customers'")
 res = mycursor.fetchone()
 if res : 
  global rl1,re1,rsub,rback
  setGeo()
  global dframe
  dframe = Frame(admin)
  dframe.grid()
  rl1 = Label(dframe,text="Enter ID of the customer to be removed")
  rl1.grid(row=0,column=0,sticky='nesw',padx=(4,4),pady=5,ipady=10,ipadx=50)
  re1 = Entry(dframe)
  re1.grid(row=1,column=0,sticky='nesw',padx=(4,4),pady=5,ipady=10,ipadx=50)
  rsub = Button(dframe,text="Submit",command=remcu)
  rsub.grid(row=2,column=0,sticky='nesw',padx=(4,4),pady=5,ipady=10,ipadx=50)
  rback = Button(dframe,text="Back",command=removeRM)
  rback.grid(row=3,column=0,sticky='nesw',padx=(4,4),pady=5,ipady=10,ipadx=50)
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

# def seif():
#     sei.grid_remove()
#     sres.grid_remove()
#     sframe.grid_remove()
#     sframe.destroy()
#     search()

def serc():
  global sres
  clear()
  print("***********************************************************************************************************************")
  print("\t\t\t\t\t\tADDRESS SEARCH MENU")
  print("***********************************************************************************************************************")
  fi = se1.get()
  #fi = input("Enter customer name or id :") 
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
    #print(x)
    sres=Label(sframe)
    sres.grid(row=4,column=0)
    sres.config(text="Address is: {}".format(x))
  else: 
    messagebox.showinfo("showerror","Invalid ID!! Customer does not exists")
    # ssub.grid_remove()
    # sbac.grid_remove()
    # sres=Label(sframe)
    # sres.grid(row=2,column=0,sticky='nesw',padx=(4,4),pady=5,ipady=1)
    # sres.config(text="Invalid ID!!!!")
    # global sei 
    # sei = Button(sframe,text="back",command=seif) 
    # sei.grid(row=3,column=0)
    #print("INVALID ID")

def sback():
 sl1.grid_remove()
 se1.grid_remove()
 ssub.grid_remove()
 sbac.grid_remove()
 sframe.grid_remove()
 sframe.destroy()
 setMenu()

def search():
 mycursor.execute("SHOW TABLES LIKE 'customers'")
 res = mycursor.fetchone()
 global sl1,se1,ssub,sbac
 global sframe
 sframe=Frame(admin)
 sframe.grid()
 if res : 
  sl1=Label(sframe,text="Enter customer name or id")
  sl1.grid(row=0,column=0,sticky='nesw',padx=(4,4),pady=5,ipady=1)
  se1=Entry(sframe)
  se1.grid(row=1,column=0,sticky='nesw',padx=(4,4),pady=5,ipady=1)
  ssub = Button(sframe,text="Search",command=serc)
  ssub.grid(row=2,column=0,sticky='nesw',padx=(4,4),pady=5,ipady=1)
  sbac = Button(sframe,text="back",command=sback)
  sbac.grid(row=3,column=0,sticky='nesw',padx=(4,4),pady=5,ipady=1)
 else: 
  print("Table does not exists!!\nCreate Table First")

def createStaff():
    msg=Toplevel()
    msg.title('Checking')
    Message(msg,text="Checking...",padx=20,pady=20).grid()
    msg.after(2000,msg.destroy())
    mycursor.execute("SHOW TABLES LIKE 'staff'")
    res = mycursor.fetchone()
    if res :
        messagebox.showerror("showerror","Staff Table already exists!!")
        staffFrame.grid_remove()
        staffFrame.destroy()
        showStaff()
    else:
        sql = "CREATE TABLE IF NOT EXISTS staff(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))"
        mycursor.execute(sql)
        mydb.commit()
        sql1 = "ALTER TABLE staff AUTO_INCREMENT = 100"
        mycursor.execute(sql1)
        mydb.commit()
        messagebox.showinfo('showinfo',"Table created sucessfully")

def staffRemove1():
        j = stre1.get()
        sql = "SELECT * FROM staff WHERE id = %s OR name = %s"
        val = (j,j)
        mycursor.execute(sql,val)
        res=""
        for x in mycursor:
            res = x 
        if res:
            g = messagebox.askquestion('askquestion',"Do you want to remove this staff member\n->{}".format(x))
            if(g == 'yes') :
                if(j.isalpha()):
                    sqlo = "SELECT id FROM staff where name = %s"
                    valo = (j,)
                    mycursor.execute(sqlo,valo)
                    for x in mycursor:
                        j = x[0]
            msg=Toplevel()
            msg.title('Checking')
            Message(msg,text="Checking...",padx=20,pady=20).grid()
            msg.after(2000,msg.destroy())
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
            messagebox.showinfo("showinfo","Staff member deleted")
        else:
            messagebox.showerror('showerror',"Invalid ID!!!")

def clrstf():
    removeframe.grid_remove()
    removeframe.destroy()
    staff()

def staffRemove():
       mycursor.execute("SHOW TABLES LIKE 'staff'")
       res = mycursor.fetchone()
       if res : 
           global removeframe,stre1
           removeframe = Frame(admin)
           removeframe.grid()   
           strl1 = Label(removeframe,text="Enter ID of the Staff member to be removed")
           strl1.grid(row=0,column=0,sticky='nesw',padx=(4,4),pady=5,ipady=10,ipadx=50)
           stre1 = Entry(removeframe)
           stre1.grid(row=1,column=0,sticky='nesw',padx=(4,4),pady=5,ipady=10,ipadx=50)
           strsub = Button(removeframe,text="Submit",command=staffRemove1)
           strsub.grid(row=2,column=0,sticky='nesw',padx=(4,4),pady=5,ipady=10,ipadx=50)
           strback = Button(removeframe,text="Back",command=clrstf)
           strback.grid(row=3,column=0,sticky='nesw',padx=(4,4),pady=5,ipady=10,ipadx=50)
       else:
          messagebox.showerror('showerror','Staff table does not exists')   

def stafffun(s):
    if(s==0):
        createStaff()
    elif(s==6):
        staffFrame.grid_remove()
        staffFrame.destroy()
        setMenu()
    elif(s==1):
        staffFrame.grid_remove()
        staffFrame.destroy()
        addStaff()
    elif(s==2):
        staffFrame.grid_remove()
        staffFrame.destroy()
        showStaff()
    elif(s==3):
        staffFrame.grid_remove()
        staffFrame.destroy()    
        staffRemove()

def addsmem():
    #f = input("Enter Name of the staff member: ")
    f=adse1.get()
    f1=adse2.get()
    #f1 = input("Enter Address: ")
    sql = "INSERT INTO staff(name,address) VAlUES (%s,%s) "
    val = (f,f1)
    mycursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo('showinfo',"Staff member added Sucessfully")

def adsbkf():
    adsframe.grid_remove()
    adsframe.destroy()
    staff()

def addStaff():
    global adsframe,adsl1,adse1,adsl2,adse2,adssub,adsback
    mycursor.execute("SHOW TABLES LIKE 'staff'")
    res = mycursor.fetchone()
    if res :
        setGeo()
        adsframe = Frame(admin)
        adsframe.grid()
        adsl1 = Label(adsframe,text="Enter Name of the staff member")
        adsl1.grid(row=0,column=0,sticky='nesw',padx=(4,4),pady=5,ipady=7)
        adse1 = Entry(adsframe)
        adse1.grid(row=0,column=1,sticky='nesw',padx=(4,4),pady=5,ipady=7,ipadx=120)
        adsl2 = Label(adsframe,text="Enter Address")
        adsl2.grid(row=1,column=0,sticky='nesw',padx=(4,4),pady=5,ipady=7)
        adse2 = Entry(adsframe)
        adse2.grid(row=1,column=1,sticky='nesw',padx=(4,4),pady=5,ipady=7,ipadx=120)
        adssub = Button(adsframe,text="Submit",command=addsmem)
        # adssub.config(bg="lightgreen")
        adssub.grid(row=2,column=1,sticky='nesw',padx=(4,4),pady=5,ipady=10,ipadx=50)
        adsback = Button(adsframe,text="Back",command=adsbkf)
        adsback.grid(row=2,column=0,sticky='nesw',padx=(4,4),pady=5,ipady=10,ipadx=50)
        # adsback.config(bg="#ff3333")
    else:
        messagebox.showerror("showerror","Customer data does not exists please create one")
        
def rmsDis():
    stdis.grid_remove()
    stdis.destroy()
    staff()

def showStaff():
    clear()
    print("***********************************************************************************************************************")
    print("\t\t\t\t\t\tDISPLAY MENU")
    print("***********************************************************************************************************************")
    mycursor.execute("SHOW TABLES LIKE 'staff'")
    res = mycursor.fetchone()
    if res :
        global stdis
        stdis = Frame(admin)
        stdis.config(bg='#ffbf80')
        stdis.grid()
        setGeo()
        std1=Label(stdis,text='Staff List')
        std1.grid(row=0,column=0,sticky='nesw',pady=(10,0))
        #std1.config(bg="skyblue")
        std2 = []
        fp=0
        r=1
        c=0
        mycursor.execute("SELECT * FROM staff")
        for x in mycursor:
           std2.insert(fp,Label(stdis))
           std2[fp].config(text=x)
           if(r%10==0):
            c=c+1
            r=1
           std2[fp].grid(row=r,column=c,sticky='nesw',padx=(4,4),pady=5,ipady=10,ipadx=30)
           r=r+1
           fp=fp+1
        std3=Button(stdis,text="back",command=lambda: rmsDis())
        std3.grid(row=fp,column=0,sticky='nesw',pady=(0,10))
        # std3.config(bg="#ff3333")
    else :
        messagebox.showerror('showerror','Staff members do not exists')

def staff():
  staffl = ["Create Staff table","Add Staff Members","Show Staff Details","Remove Staff Members","Search Staff","Update Details","Go Back To Main Menu"]
  staffm = []
  global staffFrame
  staffFrame = Frame(admin)
  staffFrame.config(bg='#ffbf80')
  admin.title("Staff Menu")
  staffFrame.grid()
  setGeo()
  for i in range(0,7):
      staffm.insert(i,Button(staffFrame,text=staffl[i],command=lambda ind=i: stafffun(ind)))
      if(i==0):
        staffm[i].grid(row=i,column=0,padx=(0,0),pady=(10,5),ipady=5,ipadx=200,sticky='nesw')
      elif(i==6):
        staffm[i].grid(row=i,column=0,padx=(0,0),pady=(5,10),ipady=5,ipadx=200,sticky='nesw')
      else: 
        staffm[i].grid(row=i,column=0,padx=(0,0),pady=5,ipady=5,ipadx=200,sticky='nesw')

#   p1 = 0
#   while p1 == 0 :
#    clear()
#    print("***********************************************************************************************************************")
#    print("\t\t\t\t\t\t\tSTAFF MENU")
#    print("***********************************************************************************************************************")
#    print("0: Create Table")
#    print("1: Add Staff Members")
#    print("2: Show Staff Details")
#    print("3: Remove Staff Members")
#    print("4: Search Staff")
#    print("5: Update Details")
#    print("6: Drop Table")
#    print("7: Go Back To Main Menu")
#    sel = int(input("ENter your choice: "))

#    if(sel == 0): 
#        mycursor.execute("SHOW TABLES LIKE 'staff'")
#        res = mycursor.fetchone()
#        if res :
#            print("Table already exists!")
#            time.sleep(1)
#        else:
#            sql = "CREATE TABLE IF NOT EXISTS staff(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))"
#            mycursor.execute(sql)
#            mydb.commit()
#            sql1 = "ALTER TABLE staff AUTO_INCREMENT = 100"
#            mycursor.execute(sql1)
#            mydb.commit()
#            print("Creating please wait...")
#            time.sleep(1)
#            print("Created")
#            time.sleep(1)

# #    elif sel == 1 :
# #     loop = 0
# #     while loop == 0 :
# #        clear()
# #        print("***********************************************************************************************************************")
# #        print("\t\t\t\t\t\tWELCOME: ADD NEW MEMBERS")
# #        print("***********************************************************************************************************************")
# #        mycursor.execute("SHOW TABLES LIKE 'staff'")
# #        res = mycursor.fetchone()
# #        if res :
# #          f = input("Enter Name of the staff member: ")
# #          f1 = input("Enter Address: ")
# #          sql = "INSERT INTO staff(name,address) VAlUES (%s,%s) "
# #          val = (f,f1)
# #          mycursor.execute(sql,val)
# #          mydb.commit()
# #          print("Updating DataBase...")
# #          time.sleep(1)
# #          print("Updated")
# #          time.sleep(1)
# #        else:
# #          print("Table does not exists\n Please create one")
# #          time.sleep(1)
# #        dot = input("Continue?(y/n) ")
# #        if(dot == "n" or dot == "N") :
# #            loop=1

#    elif sel == 2 :
#     loop = 0
#     while loop == 0 :
#        clear()
#        print("***********************************************************************************************************************")
#        print("\t\t\t\t\t\tDISPLAY MENU")
#        print("***********************************************************************************************************************")
#        mycursor.execute("SHOW TABLES LIKE 'staff'")
#        res = mycursor.fetchone()
#        if res :
#            print("Fetching details...")
#            time.sleep(1)
#            mycursor.execute("SELECT * FROM staff")
#            for x in mycursor:
#             print(x)
#             time.sleep(1)
#            #time.sleep(2)
#        else :
#             print("Table does not exists \n please create one")
#             time.sleep(1)
#        gh = input("Continue?(y/n) ")
#        if (gh == "n" or gh == "N"):
#           loop=1
      
            
#    elif sel == 3 :
#     loop = 0
#     while loop == 0 :
#        clear()
#        print("***********************************************************************************************************************")
#        print("\t\t\t\t\t\tREMOVAL MENU")
#        print("***********************************************************************************************************************")
#        
#        dot = input("Continue?(y/n) ")
#        if(dot == "n" or dot == "N"):
#         loop=1
       

#    elif sel == 4 :
#     loop = 0
#     while loop == 0 :
#      clear()
#      print("***********************************************************************************************************************")
#      print("\t\t\t\t\t\tSEARCH MENU")
#      print("***********************************************************************************************************************")
#      mycursor.execute("SHOW TABLES LIKE 'staff'")
#      res = mycursor.fetchone()
#      if res :
#          inp = input("Enter id of the staff member: ")
#          sql = "SELECT * FROM staff WHERE id = %s"
#          val = (inp,)
#          mycursor.execute(sql,val)
#          for x in mycursor:
#              print(x)
#          time.sleep(1)
#      else:
#         print("Table does not Exist!")
#         time.sleep(1)
#      dot = input("Continue?(y/n )")
#      if(dot == "n" or dot == "N") :
#          loop=1

#    elif sel == 5 :
#        loop = 0
#        while loop == 0:
#         clear()
#         print("***********************************************************************************************************************")
#         print("\t\t\t\t\t\tUPDATE MENU")
#         print("***********************************************************************************************************************")
#         mycursor.execute("SHOW TABLES LIKE 'staff'")
#         res = mycursor.fetchone()
#         if res : 
#                 take = input("Enter id of the Staff Member: ")
#                 sql = "SELECT * FROM staff WHERE id = %s"
#                 val = (take,)
#                 mycursor.execute(sql,val)
#                 for x in mycursor:
#                  print(x)
#                 take2 = input("Modify?(y/n) ")
#                 if(take2 == "y" or take2 == "Y"):
#                    chose = input("What do you want to change?(Name or Address): ")
#                    if(chose == "name" or chose == "Name"):
#                       newname = input("Enter New Name: ")
#                       print("Updating...")
#                       time.sleep(1)
#                       sql1 = "UPDATE staff SET name = %s WHERE id = %s"
#                       val1 = (newname,take)
#                       mycursor.execute(sql1,val1)
#                       mydb.commit()
#                    elif(chose == "address" or chose == "Address"):
#                       newadd = input("Enter New Address: ")
#                       print("Updating...")
#                       time.sleep(1)
#                       sql1 = "UPDATE staff SET address = %s WHERE id = %s"
#                       val1 = (newadd,take)
#                       mycursor.execute(sql1,val1)
#                       mydb.commit()
#                       print("Updated")
#                       time.sleep(1)
#                    else:
#                       print("Wrong Field!")
#                       time.sleep(1)


#         else:
#          print("Table does not exists!")
#          time.sleep(1)

#         join = input("Continue?(y/n)")
#         if (join == "n" or join =="N") :
#             loop = 1
           
#    elif sel == 6 :
#     mycursor.execute("SHOW TABLES LIKE 'staff'")
#     res = mycursor.fetchone()
#     if res :
#       mycursor.execute("DROP TABLE IF EXISTS staff")
#       print("Removing table Please wait...")
#       time.sleep(1)
#       print("Removed")
#       time.sleep(1)
#     else:
#        print("Table Does not exist!")
       
#    elif sel == 7:

#     #p =input("Exit portal:(y/n) ")

#     #if (p == "y" or p == "Y"):
#      p1 = 1
#      #print("Moving to Main Menu...")
#      #time.sleep(1)
    
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

def setcont(a,b):
  global contact_customer
  contact_customer=a
  b.destroy()
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
            if(items==""):
              items = item_namee
            else:
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
            if(qty==""):
              qty=str(choose_quantity)
            else:
              qty = qty + "\n" + str(choose_quantity)
            #b2=b2+1
            sql = "SELECT price FROM item WHERE id = %s"
            val = (choose_item,)
            mycursor.execute(sql,val)
            price_item = 0
            for x in mycursor:
                price_item = x[0]
            if(prices==""):
              prices = str(price_item)
            else:
              prices = prices + "\n" + str(price_item)
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
            if(inm == "Y" or inm == "y"):
              clear()
            else:
              loop = 1
              inv1 = "***********************************************************************************************************************\n \t\t\t\t\t\t CUSTOMER BILL:\n***********************************************************************************************************************"
              inv1 = inv1+"\nNAME:"+str(customer)+"\nITEMS:"+str(items)+"\nQUANTITY:"+str(qty)+"\nPRICES:"+str(prices)+"\nTOTAL:"+str(total_bill)+"\n"
              print(inv1)
              hj=1
              while(hj==1):
                qrcode = input("Show QR Code for UPI payment(y/Y)?")
                if(qrcode == "Y" or qrcode == "y"):
                  payment = Tk()
                  im = ImageTk.PhotoImage(Image.open("code.jpeg"))
                  paymentCode = Label(payment,image=im)
                  paymentCode.grid(row=0,column=0)
                  payment.mainloop()
                authentica = input("Transaction Complete(y/n)?")
                if(authentica is not "y" or authentica is not "Y" ):
                  top = input("Do you want to cancel transaction?")
                  if(top == "y" or top == "Y"):
                    hj=0 
                elif(authentica == "y" or authentica == "Y"): 
                  sqlo = "INSERT INTO bill(cust_name,item_name,quantity,price,tot,turn) VALUES (%s,%s,%s,%s,%s,%s)"
                  valo = (customer,items,qty,prices,total_bill,int(appear)+1)
                  mycursor.execute(sqlo,valo)
                  mydb.commit()
                  invoice = open("bill.txt","wt")
                  invoice_log = open("billlog.txt","at")
                  inv = "***********************************************************************************************************************\n \t\t\t\t\t\t CUSTOMER BILL:\n***********************************************************************************************************************"
                  inv = inv+"\nNAME:"+str(customer)+"\nITEMS:"+str(items)+"\nQUANTITY:"+str(qty)+"\nPRICES:"+str(prices)+"\nTOTAL:"+str(total_bill)+"\n"
                  invoice.write(inv)
                  invoice_log.write(inv)

                  clear()
                  print("***********************************************************************************************************************")
                  print("\t\t\t\t\t\t CUSTOMER BILL:")
                  print("***********************************************************************************************************************")
                  sqln = "SELECT * FROM bill WHERE cust_name = %s AND turn = %s"
                  valn = (customer,int(appear)+1)
                  mycursor.execute(sqln,valn)
                  
                  for x in mycursor:
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
                        print("\n-Customer Name: ",x[0],"\n-Item:",x[1],"\n-Quantity:",x[2],"\n-Price: ",x[3],"\n\tTOTAL BILL : ",x[4])
                        print("***********************************************************************************************************************")

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
# def select_menu1(h,menu1,a,b,c,d,e,f,g,hh,i,j,k):
#   global meroot
#   meroot=h
#   a.grid_remove()
#   b.grid_remove()
#   c.grid_remove()
#   d.grid_remove()
#   e.grid_remove()
#   f.grid_remove()
#   g.grid_remove()
#   hh.grid_remove()
#   i.grid_remove()
#   j.grid_remove()
#   k.grid_remove()
#   if(h==2):
#     disp() 
global l 

def removeMenu():
  global m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11
  m1.grid_remove()
  m2.grid_remove()
  m3.grid_remove()
  m4.grid_remove()
  m5.grid_remove()
  m6.grid_remove()
  m7.grid_remove()
  m8.grid_remove()
  m9.grid_remove()
  m10.grid_remove()
  m11.grid_remove()

def select_menu(h,menu1):
  global meroot
  meroot=h
  if(h==1):
    removeMenu()
    dat()
  elif(h==2):
    removeMenu()
    disp()
  elif(h==3):
    removeMenu()
    dele()
  elif(h==4):
    removeMenu()
    search()
  elif(h==7):
    removeMenu()
    staff()
  elif(h==11):
    sure = messagebox.askquestion('askquestion',"Do you want to logout?")
    if(sure == "yes"):
     removeMenu()
     global l
     l=1
    #  admin.config(bg='white')
     msg=Toplevel()
     msg.title('Logged out')
     Message(msg,text="You have sucessfully logged out",padx=20,pady=20).grid()
     msg.after(2000,msg.destroy())
     setmain()

def setMenu():
  admin.config(bg='skyblue')
  setGeo()
  global m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11
  m1 = Button(admin,text='Add Members',command=lambda: select_menu(1,admin))
  m1.grid(row=0,column=0,pady=(10,5),sticky='nesw')
  m1.config(font=("Times New Roman",13))
  m2 = Button(admin,text='Show DataBase',command=lambda: select_menu(2,admin))
  m2.grid(row=1,column=0,pady=5,sticky='nesw')
  m2.config(font=("Times New Roman",13))
  m3 = Button(admin,text='Remove Members',command=lambda: select_menu(3,admin))
  m3.grid(row=2,column=0,pady=5,sticky='nesw')
  m3.config(font=("Times New Roman",13))
  m4 = Button(admin,text='Search Customer Address',command=lambda: select_menu(4,admin))
  m4.grid(row=3,column=0,pady=5,sticky='nesw')
  m4.config(font=("Times New Roman",13))
  m5 = Button(admin,text='\tDrop Table\t',command=lambda: select_menu(5,admin))
  m5.grid(row=4,column=0,pady=5,sticky='nesw')
  m5.config(font=("Times New Roman",13))
  m6 = Button(admin,text='Update Customer Details',command=lambda: select_menu(6,admin))
  m6.grid(row=5,column=0,pady=5,sticky='nesw')
  m6.config(font=("Times New Roman",13))
  m7 = Button(admin,text='Staff Management',command=lambda: select_menu(7,admin))
  m7.grid(row=6,column=0,pady=5,sticky='nesw')
  m7.config(font=("Times New Roman",13))
  m8 = Button(admin,text='Item Management',command=lambda: select_menu(8,admin))
  m8.grid(row=7,column=0,pady=5,sticky='nesw')
  m8.config(font=("Times New Roman",13))
  m9 = Button(admin,text='Generate Bill',command=lambda: select_menu(9,admin))
  m9.grid(row=8,column=0,pady=5,sticky='nesw')
  m9.config(font=("Times New Roman",13))
  m10 = Button(admin,text='Delete Bill Log',command=lambda: select_menu(10,admin))
  m10.grid(row=9,column=0,pady=5,sticky='nesw')
  m10.config(font=("Times New Roman",13))
  m11 = Button(admin,text='Logout',command=lambda: select_menu(11,admin))
  m11.grid(row=10,column=0,padx=(0,0),pady=(5,10),ipady=1,ipadx= admin.winfo_reqwidth())
  m11.config(font=("Times New Roman",13)) 

def main():
# check,chk1 = 0,0
 #create(check)
 global l
 l = 0
 setMenu()
#  while(l == 0):
#   check,chk1 =0,0
#   dd = 0
#   clear()
#   print("***********************************************************************************************************************")
#   print("\t\t\t\t\t\t\tMENU")
#   print("***********************************************************************************************************************")
#   print("0: Create Table")
#   print("1: Add Members")
#   print("2: Show Database")
#   print("3: Remove Members")
#   print("4: Search Customer Address")
#   print("5: Drop Table")
#   print("6: Update Customer Details")
#   print("7: Staff Management")
#   print("8: Item Management")
#   print("9: Generate Bill")
#   print("10: Delete Bill Log")
#   print("11: Exit Program")
#   #choice = int(input("\nEnter your choice: "))
#   # menu = Tk()
#   # menu.title("Menu")
#   # m = []*11
#   # l = ["Add Members","Show Database","Remove Members","Search Customer Address","Drop Table","Update Customer Details","Staff Management","Item Management","Generate Bill","Delete Bill Log","Exit Program"]
#   # for i in range(0,11):
#   #   m[i].append(Button(admin,text=l[i],command=lambda: select_menu((i+1),admin)))
#   #   m[i].grid(row=i,column=0,pady=5,sticky='nesw')
#   #   m[i].config(font=("Times New Roman",13))
#   global meroot
#   choice=meroot
#   if choice == 0 :
#    create()
#   elif choice == 9 :
#           bill()
#           print("Moving to Main Menu..")
#           time.sleep(1)
#   elif choice == 10:
#       you = input("Do you want to delete the Bill Log?(y/n)")
#       if(you == "Y" or you == "y"):
#            mycursor.execute("DROP TABLE bill") 
#            mydb.commit()
#            print("Deleting Bill Log...")
#            time.sleep(1)
#            print("Deleted")
#            time.sleep(1)
#       print("Moving to Main Menu...")
#       time.sleep(1)
#   elif choice == 8 :
#       loop = 0
#       while loop == 0:
#           item()
#           ans = input("Want to continue?(y/n)" )
#           if(ans != "Y" or ans != "y"):
#              print("Moving to Main Menu...")
#              time.sleep(1)
#              loop = 1
#   elif choice == 6 :
#      loop = 0
#      while loop ==0:
#          modify()
#          ho = input("Want to continue: (y/n)")
#          if(ho == "n" or ho == "N"):
#           loop = 1
#      time.sleep(1)
#   elif choice == 7:
#    lo = 'y'
#    while(lo == 'y' or lo == 'Y'):
#     staff()
#     lo = input("Want to continue:(y/n) ")
#    if(lo != 'y' or lo != 'Y'):
#     print("Moving to Main Menu...")
#     time.sleep(1)   
#   elif choice == 5 :
#    drop()
#   elif choice == 1 :
#    o = input("Want to add?(y/n)")
#    while(o == "y" or o == "Y"):
#      dat()
#      o=input("Want to continue?(y/n):")
#      if o == "N" or o == "n":
#       print("Thank you")
#       time.sleep(1)
#       """print("Your database is:")
#       disp()"""
#   elif choice == 2 :
#    cho = input("Do you want to see database?(y/n)")
#    while(cho == 'y' or cho == 'Y'):
#     disp()
#     cho = input("do you want to continue?(y/n)")
#     if(cho != 'y' or cho !='Y'):
#      time.sleep(1)
#   elif choice == 3 :
#    ch1 = input("Do you want to delete from database?(y/n)")
#    while(ch1 == 'y' or ch1 == 'Y'):
#     dele()
#     ch1 = input("Want to continue?(y/n)")
#   elif choice == 11 :
#    print("Thank you for visiting")
#    l = 1
#    global authuser
#    authuser=0
#    exit()
#    time.sleep(1)
#   elif choice == 4:
#    c2 = "y"
#    while(c2 == "y" or c2 == "Y"):
#     search()
#     c2 = input("Want to continue?(y/n)")
#   else:
#    print("Wrong choice!!!")
#    dd = 1

authenticate()
#store()
#mycursor.execute("DROP TABLE bill")
#mydb.commit()
#create()
#mycursor.execute("ALTER TABLE customers ADD COLUMN ID INT AUTO_INCREMENT PRIMARY KEY")
