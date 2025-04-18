from flask import Flask, render_template, request

app = Flask(__name__)

# In-memory storage for habits (replace with a database for persistent storage)
habits = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        habit = request.form['habit']
        habits.append(habit)
    return render_template('index.html', habits=habits)

if __name__ == '__main__':
    app.run(debug=True)