import pyttsx3
import datetime
import speech_recognition as sr 
import  wikipedia
import webbrowser


engine =  pyttsx3.init('sapi5')
voices =  engine.getProperty('voices')
# print(voices[0].id)
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
        
    speak("Welcome Ma'am!! How may I help You?")
    
    
def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query






if __name__ == "__main__":
    # speak("Saloni is a Good girl")
    wishMe()
    
    
    while True:
        query = takeCommand().lower()
        
        #logic for excecuting task
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia","")
            results = wikipedia.summary(query, sentences= 4)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
            
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("www.google.com")
            
        
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Ma'am,the time is{strTime}")
            
            
            
        
            
        
            
            
    
    