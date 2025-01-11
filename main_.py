import speech_recognition as sr
import pyttsx3
import webbrowser
import random as rand
import os
import pywhatkit
import wikipedia

def cap():
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()


    def speak(text):
        engine.say(text)
        engine.runAndWait()

    def process(c):
        if "open google" in c.lower():
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        elif "open youtube" in c.lower():
            speak("Opening Youtube")
            webbrowser.open("https://www.youtube.com")
        elif "open facebook" in c.lower():
            speak("Opening Facebook")
            webbrowser.open("https://www.facebook.com")
        elif "open whatsapp" in c.lower():
            speak("Opening Whatsapp")
            webbrowser.open("https://web.whatsapp.com")
        elif "open github" in c.lower():
            speak("Opening Github")
            webbrowser.open("https://www.github.com")
        elif "open instagram" in c.lower():
            speak("Opening Instagram")
            webbrowser.open("https://www.instagram.com")
        elif "open twitter" in c.lower():
            speak("Opening Twitter")
            webbrowser.open("https://www.twitter.com")
        elif "open linkedin" in c.lower():
            speak("Opening Linkedin")
            webbrowser.open("https://www.linkedin.com")
        elif "open stackoverflow" in c.lower():
            speak("Opening Stackoverflow")
            webbrowser.open("https://www.stackoverflow.com")
        elif "open amazon" in c.lower():
            speak("Opening Amazon")
            webbrowser.open("https://www.amazon.com")
        elif "search wikipedia" in c.lower():
            speak("what to search ?")
            try:
                with sr.Microphone(device_index=mic_index) as source:
                        print("listening....")
                        audio = r.listen(source,timeout=5)
                        print("Audio captured")
                        command = r.recognize_google(audio)
                query = command.lower().replace("search for", "").strip()
                speak(f"Searching Wikipedia for {query}")
                speak("There are multiple results for this query, please be more specific.")
            except sr.UnknownValueError:
                                speak("Sorry, I could not understand what you said")
            except sr.RequestError:
                                speak("Sorry, my speech service is down")
            except Exception as e:
                                speak(e)
                                speak("Sorry, I could not process the audio")
            except sr.WaitTimeoutError:
                                speak("Sorry, I could not process the audio")
            try:
                webbrowser.open(f"https://en.wikipedia.org/w/index.php?title=Special:Search&search={command}")
                summary = wikipedia.summary(query, sentences=5)
                speak(summary)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results for this query, please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("Sorry, I could not find any results for this query.")
            
        elif f"search" in c.lower():
            speak("Searching")
            webbrowser.open(f"https://www.bing.com/search?q={c.lower()}")
        elif "open notepad" in c:
            speak("Opening Notepad")
            os.system("notepad")
        elif "open calculator" in c:
            speak("Opening Calculator")
            os.system("calc")
        elif "open settings" in c:
            speak("Opening Settings")
            os.system("start ms-settings:")
        elif "open visual studio code" in c:
            speak("Opening Visual Studio Code")
            os.system("code")
        elif "open command prompt" in c:    
            speak("Opening Command Prompt")
            os.system("cmd")
        elif "open file explorer" in c:
            speak("Opening File Explorer")
            os.system("explorer")
        elif "open task manager" in c:
            speak("Opening Task Manager")
            os.system("taskmgr")
        elif "open control panel" in c:
            speak("Opening Control Panel")
            os.system("control")
        elif "open paint" in c:
            
            speak("Opening Paint")
            os.system("mspaint")
        elif "open word" in c:
            speak("Opening Word")
            os.system("winword")
        elif "open excel" in c:
            speak("Opening Excel")
            os.system("excel")
        elif "open powerpoint" in c:
            speak("Opening Powerpoint")
            os.system("powerpnt")
        elif "play" in c.lower():
            song = c.lower().replace("play", "").strip()
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)
        
            



    if __name__ == "__cap__":
        speak("initializing!")
        mic_list = sr.Microphone.list_microphone_names()
        
        # Specify the microphone to use by its index
        mic_index = mic_list.index('Microphone (Realtek(R) Audio)')  # Replace 'Your Microphone Name' with the actual name
        r = sr.Recognizer()
        try:
            
                with sr.Microphone(device_index=mic_index) as source:
                    audio = r.listen(source)
                    word = r.recognize_google(audio) 
                    if (word.lower()) == "cap" or "captain" or "buddy" or " hey cap" or "hey captain" or "hey buddy":
                        speak("tnnudunnudunudnuuu")
                        greetings = ["hey buddy,whats up?", "how are you my friend?", "hello,whats up?"]
                        speak(rand.choice(greetings))
                        while True:
        
                    
                            try:
                        
                                    speak("listening....")
                                
                                    with sr.Microphone(device_index=mic_index) as source:
                                        print("listening....")
                                        audio = r.listen(source,timeout=5)
                                        print("Audio captured")
                                        command = r.recognize_google(audio)
                                        if any(keyword in command.lower() for keyword in ["exit", "goodbye", "close"]):
                                            speak("Goodbye!")
                                            break
                                        else:
                                            process(command)
                            except sr.UnknownValueError:
                                speak("Sorry, I could not understand what you said")
                            except sr.RequestError:
                                speak("Sorry, my speech service is down")
                            except Exception as e:
                                speak(e)
                                speak("Sorry, I could not process the audio")
                            except sr.WaitTimeoutError:
                                speak("Sorry, I could not process the audio")
        except sr.UnknownValueError:
                            print("Sorry, I could not understand what you said")
        except sr.RequestError:
                            print("Sorry, my speech service is down")
        except Exception as e:
                            print(e)
                            print("Sorry, I could not process the audio")
        except sr.WaitTimeoutError:
                            print("Sorry, I could not process the audio")
                        