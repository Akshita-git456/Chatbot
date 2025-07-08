
🤖 Chatbot using NLP and Flask

A clean and interactive chatbot built with HTML, CSS, JavaScript, and Python (Flask).
It understands basic messages using regular expressions and replies like a friendly assistant.

---

✨ Features

* Responds to greetings, questions, and emotions
* Tells time, date, jokes, and motivational quotes
* Chat UI similar to real messaging apps
* User message on the right, bot reply on the left
* Works locally in the browser with a Flask backend

---

🛠️ Technologies Used

Frontend: HTML, CSS, JavaScript
Backend: Python + Flask
Communication: Fetch API & JSON
Logic: Regex-based intent matching

---

📁 Folder Structure

chatbot/
├── index.html - Chat UI
├── style.css - ChatGPT-style CSS
├── script.js - Sends/receives messages
├── app.py - Flask backend
├── requirements.txt - Required Python packages
└── venv/ - Virtual environment (not uploaded to GitHub)

---

🚀 How to Run the Project

1. Clone this repository
   git clone [https://github.com/Akshita-git456/Chatbot.git](https://github.com/Akshita-git456/Chatbot.git)
   cd Chatbot

2. Set up virtual environment
   python -m venv venv
   venv\Scripts\activate (For Windows)
   pip install -r requirements.txt

3. Run the backend
   python app.py

4. Open index.html using Live Server
   (Make sure the "Live Server" extension is installed in VS Code)

---

💡 How It Works

* User types a message into the input field
* Message is sent to the backend using JavaScript (Fetch API)
* Flask backend checks for regex patterns (intents)
* A suitable response is sent back
* The reply appears on the screen like a real conversation

---

🧠 Sample Intents

You Say ——— Bot Replies
hi, hello — Hello! How can I help you today?
time — Time now is 15:30:45 (for example)
joke — Sends a programming joke
quote — Sends a motivational quote
sad, bored — Encouraging messages 💚
how are you? — I'm just code, but I work great!
love you — I appreciate the sentiment! ❤️
weather, news — Replies with a basic message

You can modify and add more in the INTENTS list inside app.py

---

👩‍💻 Created By

Akshita Bhatt
B.Tech CSE (Cyber Security)
Loves building clean, functional, and creative tech projects
GitHub: Akshita-git456

---

This project is free for educational and personal use.
Feel free to fork, use, and share

⭐ Star this repo if you found it useful
Made with 💻 by Akshita – just a girl and her chatbot 💚
