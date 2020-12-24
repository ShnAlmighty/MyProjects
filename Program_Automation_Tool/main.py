import os
from tkinter import Tk,Button,Label,Entry,Text,Frame,messagebox
import webbrowser

def contents(fileco):
    global insert
    insert = """ 
Write or paste the code here.
"""
    fch = open(fileco,"w")
    for i in range(len(insert)):
        fch.write(insert[i])

def openWeb():
  webbrowser.open("https://mysmremote.in/adminaroon123.php")

def main():
    global content,filename,location
    content = []
    filename = []
    location = os.getcwd()
    # ch = os.chdir("../../../Documents/Arduino")
    ch = location
    ser = 0
    for file in os.listdir(ch):
        if(file.endswith(".ino")):
            ser=ser+1
            filename.append(file)
    global menu
    menu = Tk()
    global mframe
    mframe = Frame(menu)
    mframe.grid()
    choice = Label(mframe,text="Select the file you want to enter")
    choice.config(font=("Times New Roman",13))
    choice.grid(row=0,column=0,sticky='nesw')
    buttons = []
    for i in range(0,len(filename)):
        buttons.append(Button(mframe,text=filename[i],command=lambda ind=i: choose(ind)))
        buttons[i].grid(row=(i+1),column=0)
        buttons[i].config(font=("Times New Roman",13))
    answ = messagebox.showinfo("showinfo","Kindly go to admin website to get customer details before going forward")
    if(answ == "ok"):
      openWeb()
    else:
      openWeb()
    menu.mainloop()

def choose(a):
    select = a
    index=select-1
    global changeFile
    changeFile = filename[index]
    contents(changeFile)
    fp = open(changeFile)
    linecount=0
    for line in fp:
        content.append(line)
        linecount=linecount+1
    for i in range(0,linecount):
        print("Line ",(i+1),":",content[i])
    global fw
    fw = open(changeFile,"w")
    global mframe
    mframe.grid_remove()
    mframe.destroy()

    global eframe
    eframe = Frame(menu)
    eframe.grid()

    global ee1,ee2,ee3,ee4
    el1 = Label(eframe,text="Enter Customers's Username")
    el1.grid(row=0,column=0)
    ee1 = Entry(eframe)
    ee1.grid(row=1,column=0)
    el2 = Label(eframe,text="Enter the Switch Board Number")
    el2.grid(row=2,column=0)
    ee2 = Entry(eframe)
    ee2.grid(row=3,column=0)
    el3 = Label(eframe,text="Enter Customers's SMKey")
    el3.grid(row=4,column=0)
    ee3 = Entry(eframe)
    ee3.grid(row=5,column=0)
    el4 = Label(eframe,text="Enter number of WiFi Netwroks the customer has:")
    el4.grid(row=6,column=0)
    ee4 = Entry(eframe)
    ee4.grid(row=7,column=0)
    esub = Button(eframe,text="Submit",command=menu1)
    esub.grid(row=8,column=0)

def clearEframe():
    for w in eframe.winfo_children():
        w.destroy()

def menu1():
    global ee1,ee2,ee3,ee4
    global username,switchboard,smkey,net  
    username = ee1.get()
    switchboard = ee2.get()
    smkey = ee3.get()
    net = ee4.get()
    net = int(net)
    clearEframe()
    global netlen
    netlen = 0
    global sen,pen
    sen = []
    pen = []
    senl = []
    penl = []
    ptemp = 0
    global eframe
    for i in range(0,net):
        netlen=netlen+1
        senl.append(Label(eframe,text="Network No {n}\nSSID:".format(n=netlen)))
        senl[i].grid(row=(0+ptemp),column=0)
        sen.append(Entry(eframe))
        sen[i].grid(row=(1+ptemp),column=0)
        penl.append(Label(eframe,text="Password:"))
        penl[i].grid(row=(2+ptemp),column=0)
        pen.append(Entry(eframe))
        pen[i].grid(row=(3+ptemp),column=0)
        ptemp=ptemp+4
    sub2 = Button(eframe,text="submit",command=menu3)
    sub2.grid(row=(4+ptemp),column=0)

def menu3():
    global ssid,passw
    ssid = []
    passw = []
    for i in range(0,len(pen)):
        ssid.append(sen[i].get())
        passw.append(pen[i].get())
    clearEframe()
    global ie1
    il1 = Label(eframe,text="Enter the number of buttons in this switchboard: ")
    il1.grid(row=0,column=0)
    ie1 = Entry(eframe)
    ie1.grid(row=1,column=0)
    isub = Button(eframe,text="Submit and Close",command=finish)
    isub.grid(row=2,column=0)

def finish():
    global username,switchboard,smkey,net,fw,content,changeFile
    buttons = ie1.get()
    content[13]=content[13]+"\t\t\t\t\t\t\t\t\tString username=\"{n}\";\n".format(n=username)
    content[14]=content[14]+"\t\t\t\t\t\t\t\t\tString switch_board=\"{n}\";\n".format(n=switchboard)
    content[15]=content[15]+"\t\t\t\t\t\t\t\t\tString smkey=\"{n}\";\n".format(n=smkey)
    netlen1=2*netlen
    p=0
    q=0
    temp=16
    while(p<netlen1):
        content[temp]=content[temp]+"\t\t\t\t\t\t\t\t\tchar ssid{m}[]=\"{n}\";\n".format(m=q+1,n=ssid[q])
        content[temp]=content[temp]+"\t\t\t\t\t\t\t\t\tchar pass{m}[]=\"{n}\";\n".format(m=q+1,n=passw[q])
        p=p+2
        q=q+1

    content[temp+1]=content[temp+1]+"\t\t\t\t\t\t\t\t\tint total_buttons_in_switch_board={n};\n".format(n=buttons)

    for i in range(len(content)):
        fw.write(content[i])

    messagebox.showinfo("showinfo","Completed")
    menu.destroy()
    os.startfile(changeFile)

if __name__ == "__main__":
    main()