from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)  # Enable CORS

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'db'),
        database=os.getenv('DB_NAME', 'todolist'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASSWORD', 'password')
    )
    return conn

@app.route('/api/tasks')
def get_tasks():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks;')
    tasks = cursor.fetchall()
    conn.close()
    return jsonify([{'id': task[0], 'description': task[1]} for task in tasks])

if __name__ == '__main__':
    app.run(host='0.0.0.0')
