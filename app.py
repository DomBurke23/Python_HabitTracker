from flask import Flask, render_template, request
import datetime 

app = Flask(__name__)

# In-memory storage for habits (replace with a database for persistent storage)
# Structure: {'habit_name': {'2025-04-18': True, '2025-04-19': False, ...}}
habit_tracking = {}
habits = []

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

    print('habits:', habits)
    print('habits tracking:', habit_tracking)
    
    return render_template('calendar.html',
                           habits=habits,
                           month_name=month_name,
                           days_in_month=days_in_month,
                           habit_tracking=habit_tracking,
                           today=today)
#endregion 

if __name__ == '__main__':
    app.run(debug=True)