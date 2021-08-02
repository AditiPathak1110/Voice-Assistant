import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import matplotlib.pyplot as plt
import numpy

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I would love to help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__== "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if(query=="take rest"):
            speak("ok beautiful have a nice day and take care")
            break

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("hey Aditi According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('here we go mam...')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('anything for you mam...')
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 
       
        elif 'sum of numbers' in query:
            speak("ok mam tell me the numers")
            xx=list(map(int,input().split(","))) 
            speak("the sum is")      
            print(sum(xx))
            speak(sum(xx))

        elif 'difference of numbers' in query:
            speak("ok mam tell me the numers")
            x=list(map(int,input().split(","))) 
            speak("the difference is")      
            y=numpy.subtract(x)
            print(y)
        elif 'multiply the numbers' in query:
            speak("ok mam tell me the numers")
            xx=list(map(int,input().split(","))) 
            speak("the ans is")      
            speak(numpy.prod(xx))

        elif 'division of numbers' in query:
            speak("ok mam tell me the numers")
            xx=list(map(int,input().split(","))) 
            speak("the ans is")      
            speak(divmod(xx))

        elif 'draw a graph' in query:
            speak("tell me the co-ordinates")
            print("Input X-Axis values:")
            x=list(map(int,input().split(",")))
            x.sort()
            print("Input Y-Axis values:")
            y=list(map(int,input().split(",")))
            plt.plot(x,y,color='green',linestyle='dashed',linewidth=3,marker='o',markerfacecolor='blue',markersize=12)  #plotting in blue triangle
            plt.xlabel('x-axis')
            plt.ylabel('y-axis')
            plt.title('My Graph...')
            maxx=max(x)
            maxy=max(y)
            plt.axis([0,maxx+1,0,maxy+1])
            plt.show()      

        elif 'draw a bar chart' in query: 
            speak("tell me the co-ordinates")
            print("Input X-Axis values:")
            x=list(map(int,input().split(",")))
            print("Input height of bars:")
            y=list(map(int,input().split(",")))
            print("labels for bars:")
            z=list(map(str,input().split(",")))
            plt.bar(x,y,tick_label=z,width=0.8,color=['green','blue'])
            plt.xlabel('x-axis')
            plt.ylabel('y-axis')
            plt.title('My Bar Chart !!')
            plt.show()

        elif 'draw a pie chart' in query:
            speak("tell me the details")
            print("define labels")
            x=list(map(str,input().split(",")))   
            print("portion covered by each labels")
            y=list(map(int,input().split(","))) 
           # print("colour for each label")
            #z=list(map(str,input().split(","))) 
            plt.pie(y,explode=[0,0,0.1,0],labels=x,colors=['red', 'green', 'blue', 'gold'],startangle=90,shadow=True,radius=1.2,autopct='%1.1f%%')
            plt.legend()
            plt.show()

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "pathakajayshankar11@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Aditi. I am unable to send this email")