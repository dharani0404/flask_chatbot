# flask_chatbot
Web-based Chatbot using Flask and HTML/CSS
# 💬 Web-Based Chatbot using Flask + HTML/CSS

This is a simple **web-based chatbot application** built using **Flask (Python), HTML, CSS, and JavaScript**.  
It allows users to interact with a chatbot through a clean and responsive user interface.  
The chatbot uses a **rule-based NLP logic** to understand user queries and return appropriate responses.

---

## 🚀 Features

- ✔️ Clean and simple chat UI  
- ✔️ Flask backend with API endpoint  
- ✔️ Rule-based NLP chatbot logic  
- ✔️ Handles user input without page reload (AJAX)  
- ✔️ Easily extendable with ML/NLP models  
- ✔️ Fully beginner-friendly project  

---

## 🛠️ Technologies Used

### **Frontend**
- HTML5  
- CSS3  
- JavaScript  

### **Backend**
- Python  
- Flask  

### **NLP / Chatbot Logic**
- Basic text preprocessing  
- Rule-based intent matching  

---

## 📂 Project Structure

```
chatbot-project/
│── app.py               # Flask server
│── chatbot.py           # Chatbot logic (NLP)
│── static/
│    └── style.css       # Frontend styling
│── templates/
│    └── index.html      # Chat UI
│── README.md
```

---

## 🧠 Chatbot Logic

The chatbot uses a simple rule-based approach:

```python
rules = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What can I do for you?",
    "bye": "Goodbye! Have a great day!",
    "how are you": "I'm doing great. Thanks for asking!"
}
```

The input is:
- Converted to lowercase  
- Checked against known rules  
- Returns a matching response or a default message  

---

## ▶️ How to Run the Project

### **1️⃣ Install Requirements**
Make sure you have Python installed, then run:

```bash
pip install flask
```

### **2️⃣ Start the Flask Server**

```bash
python app.py
```

### **3️⃣ Open the Web App**

Go to:

```
http://127.0.0.1:5000/
```

Start chatting with your bot!

---

## 🖼️ UI Preview (Text Description)

- A chat container on the center  
- Input box at the bottom  
- Blue bubbles for user messages  
- Grey bubbles for bot responses  

---

## 📌 Example Chat

```
User: Hello
Bot: Hi there! How can I help you today?

User: What is your name?
Bot: I'm ChatBot created using Flask!
```

---

## 🧩 Future Improvements

- Add machine learning model (NLTK, spaCy, or Transformers)
- Add speech recognition  
- Login system  
- Chat history storage using database  
- Deploy online using Render/Heroku  

