import os
content = []
filename = []
location = os.getcwd()
# ch = os.chdir("../../../Documents/Arduino")
ch = location
ser = 0
for file in os.listdir(ch):
    if(file.endswith(".ino")):
        ser=ser+1
        print(ser,":",file)
        filename.append(file)
#print(filename)
select = int(input("Enter serial number of the file: "))
index=select-1
changeFile = filename[index]
fp = open(changeFile)
linecount=0
end=0
for line in fp:
    content.append(line)
    if(line=="int buttons1[9];"):
        end=linecount
    linecount=linecount+1
for i in range(0,linecount):
    print("Line ",(i+1),":",content[i])
# selLine = int(input("Enter the line number: "))
# selLine=selLine-1
print(end)
fw = open(changeFile,"w")
username = input("Enter Username: ")
switchboard=input("Switch Board Number: ")
smkey = input("Enter SMKey: ")
net = int(input("Enter Number of wiFi Networks: "))
ssid = []
passw = []
netlen = 0
for i in range(0,net):
    netlen=netlen+1
    inp = "Network No {n}: -> SSID:".format(n=netlen) 
    ssi = input(inp)
    password = input("\t\t -> Password:")
    ssid.append(ssi)
    passw.append(password)
buttons = input("Enter the number of buttons in this switchboard: ")
content[13]=content[13]+"\t\t\t\t\t\t\t\t\tString username=\"{n}\";\n".format(n=username)
content[14]=content[14]+"\t\t\t\t\t\t\t\t\tString switch_board=\"{n}\";\n".format(n=switchboard)
content[15]=content[15]+"\t\t\t\t\t\t\t\t\tString smkey=\"{n}\";\n".format(n=smkey)
netlen1=2*netlen
# for i in range(netlen1):
#     content[15]=content[15]+"\n"
p=0
q=0
temp=16
while(p<netlen1):
    content[temp]=content[temp]+"\t\t\t\t\t\t\t\t\tchar ssid{m}[]=\"{n}\";\n".format(m=q+1,n=ssid[q])
    #temp=temp+1
    content[temp]=content[temp]+"\t\t\t\t\t\t\t\t\tchar pass{m}[]=\"{n}\";\n".format(m=q+1,n=passw[q])
    p=p+2
    q=q+1
content[temp+1]=content[temp+1]+"\t\t\t\t\t\t\t\t\tint total_buttons_in_switch_board={n};\n".format(n=buttons)
for i in range(len(content)):
    fw.write(content[i])
ra = 0
fp = open(changeFile)
for line in fp:
    ra=ra+1
    print("Line: ",ra,line)