import sqlite3

def connect_db():
    return sqlite3.connect("chatbot.db")

def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS chats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT,
            bot_response TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_chat(user_msg, bot_msg):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO chats (user_message, bot_response) VALUES (?, ?)",
        (user_msg, bot_msg)
    )
    conn.commit()
    conn.close()
