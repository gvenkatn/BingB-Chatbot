from flask import Flask, request, jsonify
import openai
import sqlite3

app = Flask(__name__)
openai.api_key = "your_openai_api_key"

def initialize_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS faq (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Database setup (SQLite for simplicity)
def get_db_connection():
    conn = sqlite3.connect('university.db')
    conn.row_factory = sqlite3.Row
    return conn

# Fetching FAQ responses
def get_faq_response(question):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT answer FROM faq WHERE question LIKE ?", ('%' + question + '%',))
    row = cur.fetchone()
    conn.close()
    return row["answer"] if row else None

# Chatbot route
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    
    # Check FAQ database first
    faq_response = get_faq_response(user_input)
    if faq_response:
        return jsonify({"response": faq_response})
    
    # If not in FAQ, use GPT
    gpt_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful university assistant."},
                  {"role": "user", "content": user_input}]
    )
    
    return jsonify({"response": gpt_response["choices"][0]["message"]["content"]})

def insert_sample_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.executemany('''
        INSERT INTO faq (question, answer) VALUES (?, ?)
    ''', [
        ("How do I register for courses?", "You can register via the university portal at https://portal.university.edu."),
        ("Where is the Computer Science department?", "The Computer Science department is in the Engineering Building, Room 123."),
        ("How do I contact the IT helpdesk?", "You can reach the IT helpdesk at support@university.edu or call (123) 456-7890.")
    ])
    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_db()
    insert_sample_data()
    app.run(debug=True)
