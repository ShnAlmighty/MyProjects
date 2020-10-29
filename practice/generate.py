import os
from tkinter import Tk,Button,Label,Entry,Text,Frame,messagebox
import webbrowser

global unooresp
unooresp=0
def contents1():
    global uno,unooresp
    unooresp=1
    uno = """ #include <SoftwareSerial.h>
#include<Arduino_JSON.h>
String payload;

SoftwareSerial ESP_Serial(0, 1); //Rx,Tx of(UNO)
int size1;
const byte numChars = 32;
char receivedChars[numChars];   // an array to store the received data

boolean newData = false;
int gpio[12]={2,3,4,5,6,7,8,9,10,11,12,13};
JSONVar obj;
void setup() {
    for(int i=0;i<10;i++)
    {
      pinMode(gpio[i],OUTPUT);
      digitalWrite(gpio[i],HIGH); 
   }
    Serial.begin(9600);
    ESP_Serial.begin(9600);//115200
    Serial.println("<Arduino is ready>");
 
}

void loop() {
    recvWithEndMarker();
    showNewData();
}

void recvWithEndMarker() {
    static byte ndx = 0;
    char endMarker = '\n';
    char rc;
   
    while (ESP_Serial.available() > 0 && newData == false) {
        rc = ESP_Serial.read();

        if (rc != endMarker) {
            receivedChars[ndx] = rc;
            ndx++;
            if (ndx >= numChars) {
                ndx = numChars - 1;
            }
        }
        else {
            receivedChars[ndx] = '\0'; // terminate the string
            size1=ndx;
            ndx = 0;
            newData = true;
        }
    }
}

void showNewData() {
    if (newData == true) {
      if(Serial){
          Serial.println(receivedChars);
          obj = JSON.parse(receivedChars);
//        int n = obj["status"].length();
//        for(int i=0;i<n;i++)
//          Serial.println(obj["status"][i]);
//        if(obj["status"])
//        ESP_Serial.println("Yes");
//        Serial.println("YES");
         int n1=obj["status"].length();
         for(int i=0;i<n1;i++)
          {
             if((int)obj["status"][i]==0)
                  {
                        digitalWrite(gpio[i],HIGH); 
                   }
             else if((int)obj["status"][i]==1)
                  {
                        digitalWrite(gpio[i],LOW); 
                  }
          }  
        }   
      else{
         // ESP_Serial.println("NOT");
      }
         newData = false;
    }
}"""
global unoesp
unoesp = """ #include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <Arduino_JSON.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <WiFiClientSecureBearSSL.h>

const uint8_t fingerprint[20] = {0xA8, 0x65, 0x52, 0x1A, 0x98, 0xF5, 0x34, 0xF2, 0x0D, 0xB1, 0x40, 0x5B, 0x54, 0xCC, 0x43, 0xCA, 0x28, 0x57, 0x78, 0x14};                  
ESP8266WiFiMulti wifiMulti;
String payload1;
    //|-------------------------------------------------|
                //ENTER DETAILS HERE
									//Username
                  //SwitchBoard
                  //SMKey
                  //Network Information
                  //Total Buttons
    //|-------------------------------------------------|
int buttons1[9];
//int gpio[7]={D1,D2,D3,D4,D5,D6,D7};
int gpio[7]={5,4,0,2,14,12,13};
int roundcheck=0;
String buttons;

JSONVar obj;
//IPAddress staticIP(192,168,0,60);
//IPAddress gateway(192,168,0,1);
//IPAddress subnet(255,255,255,0);

void setup() {
//  for(int i=0;i<total_buttons_in_switch_board;i++)
//  {
//   pinMode(gpio[i],OUTPUT);
//   digitalWrite(gpio[i],HIGH); 
//   }
  Serial.begin(9600);
  for (uint8_t t = 4; t > 0; t--) {
    Serial.printf("[SETUP] WAIT %d...\n", t);
    Serial.flush();
    delay(1000);
  }
  for(int j=0;j<total_buttons_in_switch_board;j++){
    buttons1[j]=0;
    }
    buttons=JSON.stringify(buttons1);
    wifiMulti.addAP(ssid2,pass2);
    wifiMulti.addAP(ssid3,pass3);
    if (wifiMulti.run() == WL_CONNECTED) {
//    Serial.println("");
//    Serial.println("WiFi connected");
//    Serial.println("IP address: ");
//    Serial.println(WiFi.localIP());
  //WiFi.begin("dlink_DWR-116", "aroon_6543");
  //WiFi.begin("OnePlus 6", "india999");
 // WiFi.config(staticIP,gateway,subnet);
}
}
void loop() {
  //if ((WiFi.status() == WL_CONNECTED)) {
    if (wifiMulti.run() == WL_CONNECTED) {
    std::unique_ptr<BearSSL::WiFiClientSecure>client(new BearSSL::WiFiClientSecure);
    client->setFingerprint(fingerprint);
    HTTPClient https;
    String postData;
    if(roundcheck==0){
      String bstats = JSON.stringify(buttons);
      postData="username="+username+"&smkey="+smkey+"&switchboard="+switch_board+"&bstats="+bstats;
    }else{
          String newstats=JSON.stringify(obj["status"]);
          postData="username="+username+"&smkey="+smkey+"&switchboard="+switch_board+"&bstats="+newstats;
      }
    if (https.begin(*client,"https://mysmremote.in/fetch.php/")) {  
      https.setTimeout(60000);
      https.addHeader("Content-Type", "application/x-www-form-urlencoded");
      int httpCode = https.POST(postData);
      if (httpCode > 0) {
        if (httpCode == HTTP_CODE_OK || httpCode == HTTP_CODE_MOVED_PERMANENTLY) {
          String payload = https.getString();
          payload1=payload;
          Serial.println(payload1);
          obj = JSON.parse(payload);
          //Serial.println(obj["status"]);
          buttons=obj["status"];
          int n1=obj["status"].length();
          roundcheck=1;
          //Serial.println(WiFi.localIP());
//          for(int i=0;i<n1;i++)
//          {
//              if((int)obj["status"][i]==0)
//              {
//                    digitalWrite(gpio[i],HIGH); 
//               }
//              else if((int)obj["status"][i]==1)
//              {
//                    digitalWrite(gpio[i],LOW); 
//              }
//          }
        }
      } else {
                  //Serial.println(payload1);
                  //Serial.printf("[HTTPS] GET... failed, error: %s\n", https.errorToString(httpCode).c_str());
      }
    } 
    else {
               // Serial.println(payload1);
                 //Serial.printf("[HTTPS] Unable to connect\n");
    }
   https.end();
  }
  delay(1);
}"""

global unofile,username,unoespfile
unouser = "{u}uno.ino".format(username)
unoespuser = "{u}esp.ino".format(username)
unofile = open(unouser,"w")
unoespfile = open(unoespuser,"w")
for i in range(len(uno)):
    unofile.write(uno[i])
for i in range(len(unoesp)):
    unoespfile.write(uno[i])

def contents():
    global username
    single = "{u}.ino".format(u=username)
    global insert
    insert = """#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <Arduino_JSON.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <WiFiClientSecureBearSSL.h>

const uint8_t fingerprint[20] = {0xA8, 0x65, 0x52, 0x1A, 0x98, 0xF5, 0x34, 0xF2, 0x0D, 0xB1, 0x40, 0x5B, 0x54, 0xCC, 0x43, 0xCA, 0x28, 0x57, 0x78, 0x14};                  
ESP8266WiFiMulti wifiMulti;
String payload1;
    //|-------------------------------------------------|
                //ENTER DETAILS HERE
									//Username
                  //SwitchBoard
                  //SMKey
                  //Network Information
                  //Total Buttons
    //|-------------------------------------------------|
int buttons1[9];
//int gpio[7]={D1,D2,D3,D4,D5,D6,D7};
int gpio[7]={5,4,0,2,14,12,13};
int roundcheck=0;
String buttons;

JSONVar obj;
//IPAddress staticIP(192,168,0,60);
//IPAddress gateway(192,168,0,1);
//IPAddress subnet(255,255,255,0);

void setup() {
  for(int i=0;i<total_buttons_in_switch_board;i++)
  {
   pinMode(gpio[i],OUTPUT);
   digitalWrite(gpio[i],HIGH); 
   }

  Serial.begin(115200);
  for (uint8_t t = 4; t > 0; t--) {
    Serial.printf("[SETUP] WAIT %d...\n", t);
    Serial.flush();
    delay(1000);
  }
  for(int j=0;j<total_buttons_in_switch_board;j++){
    buttons1[j]=0;
    }
    buttons=JSON.stringify(buttons1);
    wifiMulti.addAP(ssid2,pass2);
    wifiMulti.addAP(ssid3,pass3);
    if (wifiMulti.run() == WL_CONNECTED) {
//    Serial.println("");
//    Serial.println("WiFi connected");
//    Serial.println("IP address: ");
//    Serial.println(WiFi.localIP());
  //WiFi.begin("dlink_DWR-116", "aroon_6543");
  //WiFi.begin("OnePlus 6", "india999");
 // WiFi.config(staticIP,gateway,subnet);
}
}
void loop() {
  //if ((WiFi.status() == WL_CONNECTED)) {
    if (wifiMulti.run() == WL_CONNECTED) {
    std::unique_ptr<BearSSL::WiFiClientSecure>client(new BearSSL::WiFiClientSecure);
    client->setFingerprint(fingerprint);
    HTTPClient https;
    String postData;
    if(roundcheck==0){
      String bstats = JSON.stringify(buttons);
      postData="username="+username+"&smkey="+smkey+"&switchboard="+switch_board+"&bstats="+bstats;
    }else{
          String newstats=JSON.stringify(obj["status"]);
          postData="username="+username+"&smkey="+smkey+"&switchboard="+switch_board+"&bstats="+newstats;
      }
    if (https.begin(*client,"https://mysmremote.in/fetch.php/")) {  
      https.setTimeout(60000);
      https.addHeader("Content-Type", "application/x-www-form-urlencoded");
      int httpCode = https.POST(postData);
      if (httpCode > 0) {
        if (httpCode == HTTP_CODE_OK || httpCode == HTTP_CODE_MOVED_PERMANENTLY) {
          String payload = https.getString();
          payload1=payload;
          Serial.println(payload1);
          obj = JSON.parse(payload);
          //Serial.println(obj["status"]);
          buttons=obj["status"];
          int n1=obj["status"].length();
          roundcheck=1;
          //Serial.println(WiFi.localIP());
          for(int i=0;i<n1;i++)
          {
              if((int)obj["status"][i]==0)
              {
                    digitalWrite(gpio[i],HIGH); 
               }
              else if((int)obj["status"][i]==1)
              {
                    digitalWrite(gpio[i],LOW); 
              }
          }
        }
      } else {
                 // Serial.println(payload1);
        //Serial.printf("[HTTPS] GET... failed, error: %s\n", https.errorToString(httpCode).c_str());
      }
    } 
    else {
                //Serial.println(payload1);
      //Serial.printf("[HTTPS] Unable to connect\n");
    }
   https.end();
  }
  //Serial.println("Preparing for the next round");
  delay(1);
}
"""
    global onlyEsp
    onlyEsp = open(single,"w")
    for i in range(len(insert)):
        onlyEsp.write(insert[i])

def openWeb():
  webbrowser.open("https://mysmremote.in/adminaroon123.php")

def main():
    global content,filename,location
    content = []
    filename = []
    location = os.getcwd()
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
    choice = Label(mframe,text="Type of File")
    # choice = Label(mframe,text="Select the file you want to enter")
    choice.config(font=("Times New Roman",13))
    choice.grid(row=0,column=0,sticky='nesw')
    buttons = []
    choicef = ["ESP","Arduino+ESP"]
    #for i in range(0,len(filename)):
    for i in range(0,2):
        buttons.append(Button(mframe,text=choicef[i],command=lambda ind=i: choose(ind)))
        # buttons.append(Button(mframe,text=filename[i],command=lambda ind=i: choose(ind)))
        buttons[i].grid(row=(i+1),column=0)
        buttons[i].config(font=("Times New Roman",13))
    answ = messagebox.showinfo("showinfo","Kindly go to admin website to get customer details before going forward")
    if(answ == "ok"):
      openWeb()
    else:
      openWeb()
    menu.mainloop()

def choose(a):
    global username
    if(a==0):
        contents()
        global onlyEsp
        fp = open(onlyEsp)
    elif(a==1):
        contents1()
        global unofile,unoespfile
        fp = open(unoespfile)
    linecount=0
    for line in fp:
        content.append(line)
        linecount=linecount+1
    for i in range(0,linecount):
        print("Line ",(i+1),":",content[i])
    global fw
    #fw = open(changeFile,"w")
    fw = fp
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
    global username,switchboard,smkey,net,fw,content
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
    global unoespfile,unofile
    if(unooresp==1):
        os.startfile(unofile)
        os.startfile(unoespfile)
    else:
        os.startfile(fw)

if __name__ == "__main__":
    main()