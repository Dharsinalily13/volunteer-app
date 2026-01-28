# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from config import Config  # Import database & secret key

# Create Flask app
app = Flask(__name__)
app.config.from_object(Config)  # Load config

# Initialize MySQL
mysql = MySQL(app)

# ================= ROUTES =================

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# About page
@app.route('/about')
def about():
    return render_template('about.html')

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if user exists in database
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        if user:
            session['username'] = username
            flash(f"Welcome {username}!")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid username or password")
    return render_template('login.html')

# Signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Insert new user into DB
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users(username,email,password) VALUES(%s,%s,%s)", (username, email, password))
        mysql.connection.commit()
        flash("Account created successfully! You can now login.")
        return redirect(url_for('login'))
    return render_template('signup.html')

# Volunteer/Admin Dashboard
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    else:
        return redirect(url_for('login'))

# SOS alert page
@app.route('/sos', methods=['GET', 'POST'])
def sos():
    if request.method == 'POST':
        location = request.form['location']

        # Insert SOS alert into database
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO sos_alerts(username, location) VALUES(%s,%s)", 
                       (session.get('username', 'Anonymous'), location))
        mysql.connection.commit()
        flash(f"SOS alert sent for {location}!")
    return render_template('sos.html')

# Contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Save message in database
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO contact(name,email,message) VALUES(%s,%s,%s)", (name,email,message))
        mysql.connection.commit()
        flash("Your message was sent successfully!")
        return redirect(url_for('contact'))
    return render_template('contact.html')

# Resources page
@app.route('/resources')
def resources():
    return render_template('resources.html')

# Logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("You have been logged out.")
    return redirect(url_for('home'))

# ================ RUN APP =================
if __name__ == '__main__':
    app.secret_key = Config.SECRET_KEY  # Needed for session & flash
    app.run(debug=True)
