import speech_recognition as sr
import pyttsx3
import logging
import os
import datetime
import wikipedia
import webbrowser
import random
import subprocess
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"

os.makedirs(LOG_DIR, exist_ok=True)
log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

engine = pyttsx3.init("sapi5")
engine.setProperty('rate', 170)
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query
    except Exception as e:
        logging.info(e)
        print("Say that again please")
        return "None"

def greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning sir! How are you doing?")
    elif hour < 18:
        speak("Good Afternoon sir! How are you doing?")
    else:
        speak("Good Evening sir! How are you doing?")
    speak("I am Jarvis. Please tell me how may I help you today?")

def gemini_model_response(user_input):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = f"Your name is JARVIS. Answer shortly. Question: {user_input}"
    response = model.generate_content(prompt)
    return response.text

def save_note(text):
    with open("notes.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n")

def read_notes():
    if not os.path.exists("notes.txt"):
        return "You have no saved notes."
    with open("notes.txt", "r", encoding="utf-8") as f:
        return f.read()

greeting()

while True:
    query = takeCommand().lower()
    print(query)

    if "your name" in query:
        speak("My name is Jarvis")
        logging.info("User asked for assistant's name.")

    elif "time" in query:
        speak(datetime.datetime.now().strftime("Sir the time is %H:%M:%S"))
        logging.info("User asked for current time.")

    elif "how are you" in query:
        speak("I am functioning at full capacity sir!")
        logging.info("User asked about assistant's well-being.")

    elif "thank you" in query:
        speak("It's my pleasure sir. Always happy to help.")
        logging.info("User expressed gratitude.")

    elif "open google" in query:
        speak("Opening Google")
        webbrowser.open("https://google.com")
        logging.info("User requested to open Google.")

    elif "open calculator" in query or "calculator" in query:
        speak("Opening calculator")
        subprocess.Popen("calc.exe")
        logging.info("User requested Calculator.")

    elif "open notepad" in query:
        speak("Opening Notepad")
        subprocess.Popen("notepad.exe")
        logging.info("User requested Notepad.")

    elif "open terminal" in query or "open cmd" in query:
        speak("Opening Command Prompt")
        subprocess.Popen("cmd.exe")
        logging.info("User requested Command Prompt.")

    elif "open calendar" in query:
        speak("Opening Calendar")
        webbrowser.open("https://calendar.google.com")
        logging.info("User requested Calendar.")

    elif "open linkedin" in query:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com/in/md-rafi-uz-zaman-642382227")
        logging.info("User requested LinkedIn.")

    elif "youtube" in query:
        speak("Opening YouTube")
        search = query.replace("youtube", "").strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={search}")
        logging.info("User requested YouTube search.")

    elif "open facebook" in query:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")
        logging.info("User requested Facebook.")

    elif "open github" in query:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")
        logging.info("User requested GitHub.")

    elif "joke" in query:
        jokes = [
            "Why don't programmers like nature? Too many bugs.",
            "I told my computer I needed a break. It said it will go to sleep.",
            "Why do Java developers wear glasses? Because they don't C sharp."
        ]
        speak(random.choice(jokes))
        logging.info("User requested joke.")

    elif "wikipedia" in query:
        speak("Searching Wikipedia")
        topic = query.replace("wikipedia", "").strip()
        results = wikipedia.summary(topic, sentences=2)
        speak("According to Wikipedia")
        speak(results)
        logging.info("User requested Wikipedia info.")

    elif "exit" in query:
        speak("Thank you for your time sir. Have a great day ahead!")
        logging.info("User exited program.")
        exit()

    elif "take a note" in query or "make a note" in query:
        note = query.replace("take a note", "").replace("make a note", "").strip()
        if note == "":
            speak("What should I write down?")
            note = takeCommand().lower()
        save_note(note)
        speak("I have saved your note.")
        logging.info("User saved a note.")

    elif "show my notes" in query or "read my notes" in query:
        notes = read_notes()
        speak("Here are your notes.")
        speak(notes)
        print(notes)
        logging.info("User requested to read notes.")

    else:
        response = gemini_model_response(query)
        speak(response)
        logging.info("Gemini responded to custom query.")
