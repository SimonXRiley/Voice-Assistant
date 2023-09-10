import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os,sys
import random
import smtplib


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:speak("good evening")

    speak("My name is Jane, How may i assist you?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold=1
        r.energy_threshold=400
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-us")
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Would you say that again?")
        return "None"
    
    return query

def send_email(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("YOUR-EMAIL",passwo)


if __name__=="__main__":
    # wishMe()
    while True:

        query=takeCommand().lower() # type:ignore
        # print(query)

        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            # driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
            # driver.get("https://www.wikipedia.org")
            # searchbar=driver.find_element(By.NAME,"search")
            # query=query.replace("wikipedia","")
            # searchbar.send_keys(query+ Keys.RETURN)
            # path1='//*[@id="mw-content-text"]/div[1]/p[2]'
            # info=driver.find_element(By.XPATH,path1)
            # speak(info.text)
            # driver.quit()
            
            query=query.replace("wikipedia","")
            # results=wikipedia.summary(query,sentences=2)
            # speak("According to wikipedia")
            # print(results)
            # speak(results)

            wiki_wiki = wikipediaapi.Wikipedia('en')
            page_py = wiki_wiki.page(query)
            print(page_py)
            speak(page_py.summary)
                    

        
        elif 'turn off' in query:
            speak("Bye, and have a good one")
            break

        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")
            


        elif 'open google' in query:
            speak("Opening google")
            webbrowser.open_new_tab("google.com")


        elif 'open stack overflow' in query:
            speak("Opening stack overflow")
            webbrowser.open_new_tab("stackoverflow.com")


        elif 'open mail' in query:
            speak("Opening mail")
            webbrowser.open_new_tab("mail.google.com")
            webbrowser.open_new_tab("yahoo.com")
            webbrowser.open_new_tab("rediffmail.com")


        elif 'play music' in query:
            music_dir="MUSIC FOLDER"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randrange(0,len(songs))]))
            
            
        elif 'the time' in query: # what's the time 
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strtime}")
    

        elif 'open control panel' in query:
            os.system('cmd /k start control')


        elif 'shutdown computer' in query:
            os.system('cmd /k shutdown /s')


        elif 'restart computer' in query:
            os.system('cmd /k shutdown /r')


        elif 'open code' in query:
            os.startfile("C:/Microsoft VS Code/Code.exe")


        elif 'open' and '.com' in query:
            query2=query.replace("open","").strip()
            webbrowser.open_new_tab(f"{query2}")


        elif 'open' and '.in' in query:
            query2=query.replace("open","").strip()
            webbrowser.open_new_tab(f"{query2}")


        elif 'open' and '.org' in query:
            query2=query.replace("open","").strip()
            webbrowser.open_new_tab(f"{query2}")

       