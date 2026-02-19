import sqlite3

class Database:
    def __init__(self, db_name='bithocker.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY,
                type TEXT,
                content TEXT,
                user_id INTEGER,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS consents (
                user_id INTEGER PRIMARY KEY,
                status BOOLEAN,
                source TEXT
            )
        ''')
        self.conn.commit()

    def log_event(self, log_type, content, user_id):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO logs (type, content, user_id) VALUES (?, ?, ?)', (log_type, content, user_id))
        self.conn.commit()

    def set_consent(self, user_id, status, source='manual'):
        cursor = self.conn.cursor()
        cursor.execute('REPLACE INTO consents (user_id, status, source) VALUES (?, ?, ?)', (user_id, status, source))
        self.conn.commit()

    def get_consent(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT status FROM consents WHERE user_id = ?', (user_id,))
        result = cursor.fetchone()
        return result[0] if result else False