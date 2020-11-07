import speech_recognition as sr 
import webbrowser
import sys
r = sr.Recognizer()    

def work(result,name):
    if(result == "hello" or result == "hey" or result == "What's up"):
        print("Hello",name,", hope you are doing okay")
    elif("search" in result):
        query = result.split(" ")
        serc = ""
        for i in range(0,len(query)):
            if(i is not 0):
                serc=serc+(query[i])
        search = "http://www.google.com/search?q="+serc
        webbrowser.open(search)
    elif(result == "close" or result == "bye" or result == "bye bye" or result == "exit"):
        print("Okay","\nBye", name, "\nGoing to sleep")
        sys.exit()
    else:
        print(name,"you said: ",result)

turn = 0
while(1):         
    try:        
        with sr.Microphone() as source2:
            if(turn==0):
                print("Kindly say your name: ") 
            r.adjust_for_ambient_noise(source2, duration=0.2) 
            audio2 = r.listen(source2) 
            MyText = r.recognize_google(audio2) 
            MyText = MyText.lower()
            if(turn==0):
                name = MyText
                print("Welcome: "+MyText)
                turn=1
            else: 
                work(MyText,name) 

    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e))  

    except sr.UnknownValueError: 
        print("unknown error occured")