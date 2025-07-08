const chatLog = document.getElementById('chat-log');
const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');

chatForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  const text = userInput.value.trim();
  if (!text) return;
  appendMsg(text, 'user');
  userInput.value = '';

  // typing effect
  appendMsg('…', 'bot');

  try {
    const res = await fetch('http://127.0.0.1:5000/api/chat', {  // new

      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: text })
    });
    const data = await res.json();
    chatLog.lastChild.remove(); // remove typing
    appendMsg(data.reply, 'bot');
  } catch {
    chatLog.lastChild.remove();
    appendMsg('Server error. Try again later.', 'bot');
  }
});

function appendMsg(text, sender) {
  const li = document.createElement('li');
  li.textContent = text;
  li.className = sender;
  chatLog.appendChild(li);
  chatLog.scrollTop = chatLog.scrollHeight;
}
