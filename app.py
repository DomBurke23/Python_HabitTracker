from flask import Flask, render_template, request, redirect, url_for, jsonify
from Database.userRepository import UserRepository 

import datetime 
import sqlite3
import os  # Import the os module for path manipulation

app = Flask(__name__)

# In-memory storage for habits and their completion status
# (replace with a database for persistent storage)
# Structure: {'habit_name': {'2025-04-18': True, '2025-04-19': False, ...}}
habit_tracking = {}
habits = []

#region SQL Database variables 
DATABASE_FOLDER = 'Database'
DATABASE_FILE = 'pythonHabitsUsers.db'
DATABASE_PATH = os.path.join(DATABASE_FOLDER, DATABASE_FILE)
SCHEMA_FILE = 'schema.sql'
SCHEMA_PATH = os.path.join(DATABASE_FOLDER, SCHEMA_FILE)
DEBUG_MODE = True
#endregion 

#region Add Habit 
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        habit = request.form['habit']
        if habit not in habits:
            habits.append(habit)
            # Initialize tracking for the new habit for the current month
            today = datetime.date.today()
            start_of_month = today.replace(day=1)
            end_of_month = (start_of_month.replace(month=start_of_month.month + 1, day=1) - datetime.timedelta(days=1))
            habit_tracking[habit] = habit_tracking.get(habit, {})
            for day in [start_of_month + datetime.timedelta(days=d) for d in range((end_of_month - start_of_month).days + 1)]:
                date_str = day.strftime('%Y-%m-%d')
                if date_str not in habit_tracking[habit]:
                    habit_tracking[habit][date_str] = False # Default to not done
    return render_template('index.html', habits=habits)
#endregion 

#region Remove Habit 
@app.route('/remove_habit', methods=['POST'])
def removeHabit():
    if request.method == 'POST':
            habit_to_remove = request.form['remove_habit']
            if habit_to_remove in habits:
                habits.remove(habit_to_remove)
                if habit_to_remove in habit_tracking:
                    del habit_tracking[habit_to_remove]  # Remove tracking data
    return redirect(url_for('index'))
#endregion 

#region calendar table 
@app.route('/calendar', methods=['GET', 'POST'])
def calendar():
    today = datetime.date.today()
    year = today.year
    month = today.month
    month_name = today.strftime('%B')
    first_day = datetime.date(year, month, 1)
    last_day = (first_day.replace(month=month + 1, day=1) - datetime.timedelta(days=1))
    days_in_month = [first_day + datetime.timedelta(days=d) for d in range((last_day - first_day).days + 1)]

    if request.method == 'POST':
        habit_name = request.form['habit_name']
        date_str = request.form['date']
        status = request.form['status'] == 'done'
        if habit_name in habit_tracking:
            habit_tracking[habit_name][date_str] = status

    return render_template('calendar.html',
                           habits=habits,
                           month_name=month_name,
                           days_in_month=days_in_month,
                           habit_tracking=habit_tracking,
                           today=today)
#endregion 

#region Login Sql Database
# on mac test in terminal sqlite3 --version 
def get_db():
    # Return rows as dictionaries, using .Row over .fetchall() allows you to index per column as well as row 
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def close_db(conn):
    if conn:
        conn.close()

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    try:
        with open(SCHEMA_PATH, 'r') as f:
            cursor.executescript(f.read())
        conn.commit()
        print(f"Database initialized from {SCHEMA_PATH}")
    except sqlite3.OperationalError as e:
        print(f"Error initializing database: {e}")
    finally:
        close_db(conn)

# Initialize the database when the application starts (you might do this once separately)
with app.app_context():
    init_db()

# Instantiate the UserRepository
user_repository = UserRepository(DATABASE_PATH)

@app.route('/login')
def show_login():
    users = user_repository.fetch_users() if DEBUG_MODE else None
    return render_template('login.html', users=users)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = user_repository.fetch_user_by_username(username)
    # In a real application, you'd hash passwords!
    if user and user['password'] == password:
        return redirect(url_for('index'))
    else:
        return jsonify({'error': 'Invalid username or password'}), 401
#endregion 

#region Register 
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # ... logic to save user to database ...
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html')
#endregion

if __name__ == '__main__':
    app.run(debug=True)