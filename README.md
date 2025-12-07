# 🧠 JARVIS – Voice Assistant System (Python)

JARVIS is a Python-based desktop voice assistant that listens to voice commands, performs system tasks, retrieves information, manages notes, opens applications, and communicates through speech—providing a hands-free assistant experience inspired by Iron Man’s JARVIS.

It uses Speech Recognition and Text-to-Speech (TTS) to interact naturally with users while running locally on your system.

---

## ✨ Features

- **Time-based greeting** (morning, afternoon, evening)
- **Voice command recognition** powered by Google Speech Recognition  
- **Text-to-speech responses** using `pyttsx3`
- **Time announcements**
- **Wikipedia search** with spoken summaries
- **Open websites:** Google, Facebook, YouTube, GitHub, LinkedIn
- **YouTube voice search**
- **Open system apps:** Calculator, Notepad, CMD
- **Open Google Calendar**
- **Jokes and small talk**
- **Local Notes System**
  - “Take a note…” → saves to `notes.txt`
  - “Show my notes” → reads notes aloud
- **Graceful exit** via voice command

---


## 💻 Requirements 

- Python 3.11 or higher 


## How to run? 

1. Create a virtual environment:

   ```bash
   conda create -n jarvis python=3.11 -y
   ```

2. Activate virtual environment:

   ```bash
   conda activate jarvis
   ```

3. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the JARVIS script:

   ```bash
   python jarvis.py
   ```


### 📜 License

This project is open-source and free to use for learning purposes.