import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import random
import requests
import wikipedia
import pywhatkit as kit
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
import pyjokes
import pyautogui
import time



# Initialize pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function to speak
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# Function to take voice command
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  # Adjust for background noise
        r.pause_threshold = 1  # Seconds of non-speaking audio before a phrase is considered complete
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query.lower()
        except sr.WaitTimeoutError:
            speak("Sorry, I didn't hear anything. Please try again.")
            return "none"
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return "none"
        except sr.RequestError:
            speak("Sorry, I'm having trouble with my speech recognition service.")
            return "none"
        except Exception as e:
            print(f"Error: {e}")
            speak("Sorry, there was an error. Please try again.")
            return "none"

# Function to greet based on time of day
def wishing():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 16:
        speak("Good Afternoon")
    elif 16 <= hour < 20:
        speak("Good Evening")
    else:
        speak("Good Night")
    speak("I am Cherry")


def send_email(to, content):
    try:
        from_email = "your_email@gmail.com"  # Replace with your email
        from_password = "your_password"  # Replace with your password

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to
        msg['Subject'] = "Test Email from AI Assistant"

        msg.attach(MIMEText(content, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        text = msg.as_string()
        server.sendmail(from_email, to, text)
        server.quit()
        speak("Email has been sent successfully")
    except Exception as e:
        print(e)
        speak("There was an issue while sending the email, please check it out yourself")


def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=83263a48a797182dbc3926e513'
    response = requests.get(main_url)

    # Check if the request was successful
    if response.status_code != 200:
        speak("Sorry, I couldn't fetch the news.")
        return

    main_page = response.json()
    articles = main_page.get('articles', [])
    if not articles:
        speak("Sorry, there are no news articles available at the moment.")
        return

    head = [ar["title"] for ar in articles]
    days = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]

    for i, day in enumerate(days):
        if i < len(head):
            speak(f"Today's {day} news is {head[i]}")



if __name__ == '__main__':
    speak("Hi")
    wishing()
    speak("Hello Devika! How are you doing? I am activated.")

    while True:
    # if 1:
        query = takecommand()

        # if query == "none":
        #     continue  # Skip processing if no valid query is obtained

        # Commands based on user queries
        query = query.lower()

        if "open notepad" in query:
            try:
                npath = "C:\\Windows\\System32\\notepad.exe"
                speak("Opening Notepad.")
                os.startfile(npath)
            except Exception as e:
                speak("I am unable to open Notepad.")
                print(e)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "close notepad " in query:
            speak("closing notepad")
            os.system("taskkill/f/im notepad.exe")

        elif any(keyword in query for keyword in ["open youtube", "open Instagram", "open cuims", "open chatgpt",
                                                 "open Google", "open G-Mail", "open Linkedin"]):

                if "youtube" in query:
                            try:
                                ypath = "https://www.youtube.com"
                                speak("Opening YouTube soon")
                                webbrowser.open(ypath)
                            except Exception as e:
                                speak("I am unable to open YouTube")
                                print(e)


                elif "open Instagram" in query:
                            try:
                                ipath = "https://www.instagram.com"
                                speak("Opening Instagram soon")
                                webbrowser.open(ipath)
                            except Exception as e:
                                speak("I am unable to open Instagram")
                                print(e)


                elif "cuims" in query:

                                try:
                                    cpath = "https://uims.cuchd.in/"
                                    speak("Opening cuims soon")
                                    webbrowser.open(cpath)
                                except Exception as e:
                                    speak("I am unable to open cuims")
                                    print(e)


                elif "chatgpt" in query:
                    try:
                        hpath = "https://www.chatgpt.com"
                        speak("Opening chatgpt soon")
                        webbrowser.open(hpath)
                    except Exception as e:
                        speak("I am unable to open chatgpt")
                        print(e)


                elif "google" in query:
                    try:
                        lpath = "https://www.google.com"
                        speak("Opening Google soon")
                        webbrowser.open(lpath)
                    except Exception as e:
                        speak("I am unable to open Google")
                        print(e)


                elif "g-mail" in query:
                    try:
                        opath = "https://mail.google.com/mail/u/0/#inbox"
                        speak("Opening Gmail soon")
                        webbrowser.open(opath)
                    except Exception as e:
                        speak("I am unable to open Gmail")
                        print(e)


                elif "linkedin" in query:
                    try:
                        npath = "https://www.linkedin.com/in/devika-dhir-b3571321a/"
                        speak("Opening Linkedin soon")
                        webbrowser.open(npath)
                    except Exception as e:
                        speak("I am unable to open Linkedin")
                        print(e)


        elif "open calculator" in query:

            try:

                calpath = "C:\\Windows\\System32\\calc.exe"

                os.startfile(calpath)

            except Exception as e:

                speak("I am unable to open Calculator.")

                print(e)

        elif "play music" in query:
            music_dir = "C:\\Users\\Devika\\Music\\music_in_this_device"
            music_files = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]
            if not music_files:
                speak("No music files found in the directory.")
            else:
                music_file = random.choice(music_files)
                music_path = os.path.join(music_dir, music_file)
                os.startfile(music_path)
                speak(f"Now playing: {music_file}")

        elif "stop music" in query:
            speak("Stopping music playback.")
            # Add functionality to stop music playback if required

        elif "ip address" in query:
            try:
                ip = requests.get('https://api.ipify.org').text
                speak(f"Your IP Address is {ip}")
            except requests.exceptions.RequestException as e:
                speak("Sorry, I couldn't retrieve your IP address. Please check your internet connection.")
                print(e)

        elif "wikipedia" in query:
            try:
                query = query.replace("wikipedia", "").strip()
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
                print(results)
            except wikipedia.exceptions.WikipediaException as e:
                speak("Sorry, I couldn't find any relevant information on Wikipedia.")
                print(e)

        elif "search" in query:
            speak("What should I search for?")
            search_query = takecommand()

            if search_query != "none":
                speak(f"Searching for {search_query}")
                webbrowser.open(f"https://www.google.com/search?q={search_query}")

        elif "send whatsapp message" in query:
            try:
                speak("Please tell me the phone number including the country code.")
                phone_number = takecommand()
                # if phone_number == "none":
                #     continue

                speak("What message would you like to send?")
                message = takecommand()
                # if message == "none":
                #     continue

                # Get the current time and add 2 minutes
                now = datetime.datetime.now()
                send_time_hour = now.hour
                send_time_minute = now.minute + 2
                if send_time_minute >= 60:
                    send_time_hour += 1
                    send_time_minute -= 60
                if send_time_hour >= 24:
                    send_time_hour -= 24

                speak("Sending your message now.")
                kit.sendwhatmsg(phone_number, message, send_time_hour, send_time_minute)

                speak("Message has been scheduled successfully.")
            except Exception as e:
                speak("Sorry, I couldn't send the message.")
                print(e)

        elif "time" in query:

            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Devika, The time is {strTime}")
            print(f"The time is {strTime}")

        elif "set alarm " in query:
            nn=int(datetime.datetime.now().hour)
            if nn==22:
                music_dir='E:\\music'
                songs=os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))

        elif "send email" in query:
            try:
                speak("what should i write in mail ?")
                content =takecommand().lower()
                to="devikadhir1710@gmail.com"
                sendemail=(to,content)
                speak("email  has been sent succssfully")

            except Exception as e:
                print (e)
                speak("there is an issue while sending mail, kindly checkit out yourself")

        elif "quit" in query:
            speak("chlo enjoy koi baat hui toh btana")
            speak("devika anything else in mind?")
            sys.exit()

        elif "tell me a joke " in query:
            joke=pyjokes.get_joke()
            speak(joke)

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "tell me news" in query:
            speak("okay , wait a while")
            news()











