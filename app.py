
from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="student_db"
)

@app.route('/')
def index():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    student_class = request.form['class']
    grade = request.form['grade']

    cursor = db.cursor()
    cursor.execute("INSERT INTO students (name, class, grade) VALUES (%s, %s, %s)", (name, student_class, grade))
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
