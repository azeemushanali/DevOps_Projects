from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__)

# Database setup
def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL
            )
        ''')
    print("Database initialized!")

# Route to display tasks
@app.route('/')
def index():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()
    return render_template('index.html', tasks=tasks)

# Route to add a new task
@app.route('/add', methods=['POST'])
def add_task():
    task_description = request.form.get('description')
    if task_description:
        with sqlite3.connect('database.db') as conn:
            conn.execute('INSERT INTO tasks (description) VALUES (?)', (task_description,))
    return redirect('/')

# Route to delete a task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    with sqlite3.connect('database.db') as conn:
        conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
