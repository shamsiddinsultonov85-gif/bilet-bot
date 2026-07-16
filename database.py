import sqlite3

conn = sqlite3.connect("bot.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER UNIQUE,
    full_name TEXT,
    username TEXT,
    country TEXT,
    price TEXT,
    status TEXT
)
""")

conn.commit()


def add_user(telegram_id, full_name, username, country, price):
    cursor.execute(
        """
        INSERT OR REPLACE INTO users
        (telegram_id, full_name, username, country, price, status)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (telegram_id, full_name, username, country, price, "pending")
    )
    conn.commit()


def get_all_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()
