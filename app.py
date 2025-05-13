from flask import Flask, render_template, request
# A lightweight WSGI web application framework in Python,
# useful for building web applications and APIs.

import sqlite3
# A module for interacting with SQLite databases,
# allowing you to execute SQL commands and manage database files directly.

from datetime import datetime
# A module that supplies classes for manipulating dates and times.

app = Flask(__name__)
# Creates an instance of the Flask class. This instance will be our WSGI application.

# Defines the route for the homepage ('/'). When a user visits the homepage,
# the index function renders the 'index.html' template with initial values for 'selected_date' and 'no_data'.
@app.route('/')
def index():
    return render_template('index.html', selected_date='', no_data=False)

# Gets the selected date from the form submitted by the user.
@app.route('/attendance', methods=['POST'])
def attendance():
    selected_date = request.form.get('selected_date')


    # Converts the selected date string to a datetime object and formats it as 'YYYY-MM-DD'.
    selected_date_obj = datetime.strptime(selected_date, '%Y-%m-%d')
    formatted_date = selected_date_obj.strftime('%Y-%m-%d')

    # Connects to the SQLite database 'attendance.db' and creates a cursor object to interact with the database.
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()

    # Executes a SQL query to  select the 'name' and 'time' from the 'attendance' table where the date matches the formatted_date.
    # Fetches all the results and stores them in the attendance_data variable.
    cursor.execute("SELECT name, time FROM attendance WHERE date = ?", (formatted_date,))
    attendance_data = cursor.fetchall()

    # Closes the database connection.
    conn.close()

    # If no attendance data is found for the selected date, re-renders the 'index.html' template
    # with 'selected_date' and sets 'no_data' to True
    if not attendance_data:
        return render_template('index.html', selected_date=selected_date, no_data=True)

    # If attendance data is found, renders the 'index.html' template with 'selected_date' and the attendance data.
    return render_template('index.html', selected_date=selected_date, attendance_data=attendance_data)

# If this script is run directly (not imported as a module), it starts the Flask development server with debug mode enabled.
if __name__ == '__main__':
    app.run(debug=True)
