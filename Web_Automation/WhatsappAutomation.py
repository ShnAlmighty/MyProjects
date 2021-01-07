from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import datetime
from datetime import date

contact = input("Enter the contact name you want to message")
text = input("Enter the message:\n")
alarm = input("Enter the time at which you want to send this message(hh:mm:ss)")
setTime = datetime.datetime.now().strftime("%H:%M:%S")

while(setTime != alarm):
    setTime = datetime.datetime.now().strftime("%H:%M:%S")

driver = webdriver.Chrome(r"C:\Users\L K PATNAIK\Desktop\shantanu\pyth\Web_Automation\Browsers\chromedriver.exe")
driver.get("https://web.whatsapp.com")
input("Scan QR Code, And then press Enter")
print("Logged In")
inp_xpath_search = "//*[@id='side']/div[1]/div/label/div/div[2]"
input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
input_box_search.click()
time.sleep(7)
input_box_search.send_keys(contact)
time.sleep(7)
selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
time.sleep(7)
selected_contact.click()
inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
input_box = driver.find_element_by_xpath(inp_xpath)
time.sleep(7)
input_box.send_keys(text + Keys.ENTER)
time.sleep(7)
driver.quit()
print("Message Sent")