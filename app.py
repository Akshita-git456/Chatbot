import re, random
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

INTENTS = [
    (re.compile(r"\bhello\b|\bhi\b", re.I), "Hello! How can I help you today?"),
    (re.compile(r"how are you", re.I), "I'm just code, but I work great!"),
    (re.compile(r"your name", re.I), "I'm a Flask-based chatbot."),
    (re.compile(r"\btime\b", re.I),  lambda: f"Time now is {datetime.now().strftime('%H:%M:%S')}"),
    (re.compile(r"\bdate\b", re.I),  lambda: f"Today is {datetime.now().strftime('%Y-%m-%d')}"),
    (re.compile(r"\b(bye|goodbye|see you|exit)\b", re.I), "Goodbye! Have a great day 😊"),
    (re.compile(r"(who (created|made) you)", re.I), "I was created by Akshita Bhatt 👩‍💻"),
    (re.compile(r"\b(thank you|thanks|thx)\b", re.I), "You're welcome!"),
    (re.compile(r"(what can you do|help|features)", re.I),
        "I can greet, tell the date/time, and answer simple questions. Ask away!"),
    (re.compile(r"\b(joke|make me laugh)\b", re.I),
        lambda: random.choice([
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "I would tell you a UDP joke, but you might not get it.",
            "A SQL query walks into a bar and sees two tables. It asks, 'May I join you?'"
        ])),
    (re.compile(r"\b(news|latest news|headlines)\b", re.I),
        "I don't fetch live news yet, but you can ask me general questions."),
    (re.compile(r"\b(weather|forecast)\b", re.I),
        "I can’t grab real‑time weather, but carrying an umbrella never hurts!"),
    (re.compile(r"\bage\b|\bold are you\b", re.I), "I'm timeless – pure code!"),
    (re.compile(r"\b(capabilities|skills|what else)\b", re.I),
        "I greet, tell time/date, crack jokes, and answer small‑talk."),
    (re.compile(r"\b(favourite|favorite) color\b", re.I),
        "I like #3498db – a nice shade of blue."),
    (re.compile(r"\bcoffee\b", re.I), "I run on electrons, but a latte sounds great for humans."),
    (re.compile(r"\btea\b", re.I), "A hot cup of chai is always comforting!"),
    (re.compile(r"\b(laugh|haha|lol)\b", re.I), "😂"),
    (re.compile(r"\b(sad|unhappy|depressed)\b", re.I),
        "I'm sorry to hear that. Talking to a friend often helps ❤️"),
    (re.compile(r"\bbored\b", re.I), "Maybe try a new hobby or learn something fun online!"),
    (re.compile(r"\b(quote|inspire me)\b", re.I),
        lambda: random.choice([
            "Stay hungry, stay foolish. – Steve Jobs",
            "Code is like humor. When you have to explain it, it’s bad. – Cory House",
            "The only way to do great work is to love what you do. – Steve Jobs"
        ])),
    (re.compile(r"\bmotivate\b|\bmotivation\b", re.I),
        "You’ve got this! One small step at a time."),
    (re.compile(r"\bemoji\b", re.I), "Here’s one: 😊"),
    (re.compile(r"\bfact\b", re.I),
        "Did you know? The first computer bug was a real moth!"),
    (re.compile(r"\b(song|music)\b", re.I), "I like anything with a good beat."),
    (re.compile(r"\b(movie|film)\b", re.I), "I enjoy sci‑fi classics… in theory."),
    (re.compile(r"\b(book|novel)\b", re.I),
        "Reading expands the mind. Have a favorite genre?"),
    (re.compile(r"\blanguages?\b", re.I), "I understand English regex‑style."),
    (re.compile(r"\b(hobby|hobbies)\b", re.I), "Chatting with you is my hobby!"),
    (re.compile(r"\b(stress|anxious)\b", re.I),
        "Take a deep breath and maybe a short walk."),
    (re.compile(r"\b(python|programming)\b", re.I),
        "Python is great for quick scripts and web APIs."),
    (re.compile(r"\b(javascript|js)\b", re.I),
        "JavaScript powers the front‑end of this chatbot."),
    (re.compile(r"\b(c\+\+|cpp)\b", re.I),
        "C++ is powerful and fast, perfect for system software."),
    (re.compile(r"\b(html|css)\b", re.I),
        "HTML and CSS build the structure and style of webpages."),
    (re.compile(r"\b(yes|yeah|yup)\b", re.I), "Glad you agree!"),
    (re.compile(r"\b(no|nope|nah)\b", re.I), "Alright, let’s consider something else."),
    (re.compile(r"\bsorry\b", re.I), "No worries at all!"),
    (re.compile(r"\blove you\b", re.I), "I appreciate the sentiment! ❤️"),
    (re.compile(r"\bbirthday\b", re.I),
        "Happy Birthday to whoever’s celebrating! 🎂"),
    (re.compile(r"\bhelp\b", re.I),
        "Just ask me a question and I’ll try my best to answer.")
]

FALLBACK = "Sorry, I didn't understand that. Could you rephrase?"

def get_reply(message:str)->str:
    for pattern, response in INTENTS:
        if pattern.search(message):
            return response() if callable(response) else response
    return FALLBACK

@app.route('/api/chat', methods=['POST'])
def chat():
    data  = request.get_json(silent=True) or {}
    reply = get_reply(data.get('message', ''))
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
