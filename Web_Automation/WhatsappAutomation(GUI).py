from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import datetime
from datetime import date
from tkinter import Tk,Button,Label,Entry,Text,Frame,messagebox,ttk
from PIL import ImageTk, Image

global menu
menu = Tk()
global frame1
frame1 = Frame(menu)
frame1.grid()

global driver
driver = webdriver.Chrome(r"C:\Users\L K PATNAIK\Desktop\shantanu\pyth\Web_Automation\Browsers\chromedriver.exe")
driver.get("https://web.whatsapp.com")

messagebox.showinfo('showinfo','Scan the OR code in web whatsapp')

global ans,inp1,inp2,timeE,TimerButton

timeE=None

ans = messagebox.askquestion("askquestion","QR code scanning completed?")

def send():
    global ans
    if(ans == "yes"):
        global inp1,inp2,timeE,frame1,driver
        contact =  inp1.get() 
        text = inp2.get("1.0","end-1c")
        if(timeE != None):
            alarm =  str(timeE.get())  
            if(alarm!="" or timeE == None):
                setTime = datetime.datetime.now().strftime("%H:%M:%S")
                while(setTime != alarm):
                    setTime = datetime.datetime.now().strftime("%H:%M:%S")
        else: alarm=datetime.datetime.now().strftime("%H %M %S")
        inp_xpath_search = "//*[@id='side']/div[1]/div/label/div/div[2]"
        input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
        input_box_search.click()
        time.sleep(1)
        input_box_search.send_keys(contact)
        time.sleep(1)
        selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
        time.sleep(1)
        selected_contact.click() 
        oldText = WebDriverWait(driver,50).until(lambda driver:driver.find_element_by_xpath("""//*[@id="main"]/div[3]/div/div/div[3]"""))
        messagebox.showinfo('showinfo',oldText.text)
        time.sleep(1)
        inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
        input_box = WebDriverWait(driver,50).until(lambda driver:driver.find_element_by_xpath(inp_xpath))
        time.sleep(1)
        input_box.send_keys(text + Keys.ENTER)
        messagebox.showinfo('showinfo','Message sent to {} at {}'.format(contact,alarm))
        readText = driver.find_element_by_xpath("""//*[@id="main"]/div[3]/div/div/div[3]""")

def showTimer():
    global hl,timeE,TimerButton
    TimerButton.grid_remove()
    hl = Label(frame1,text='Time at which you want to send (hh:mm:ss)')
    hl.grid(row=5,column=0,pady=(10,0))
    timeE = Entry(frame1,textvariable="")
    timeE.grid(row=6,column=0,ipadx='60',ipady='3')

img = Image.open("whatsapp.png")
img = img.resize((100,100),Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

logo = Label(frame1,image=img)
logo.grid(row=0,column=0)

l1 = Label(frame1,text='Name of person')
l1.grid(row=1,column=0,sticky='nesw',pady=(10,0))
inp1 = Entry(frame1)
inp1.grid(row=2,column=0,ipadx='60',ipady='3',pady='10',padx='20')

l2 = Label(frame1,text='Type your message')
l2.grid(row=3,column=0)
inp2 = Text(frame1,height=15,width=30)
inp2.grid(row=4,column=0)

TimerButton = Button(frame1,text='Add timer',command = lambda: showTimer())
TimerButton.grid(row=5,column=0,pady=10)

sub1 = Button(frame1,text='submit',command=lambda:send())
sub1.grid(row=7,column=0,pady=10)

menu.mainloop()
