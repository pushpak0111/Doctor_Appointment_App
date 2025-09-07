from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecret"  # needed for sessions

users = {
    "admin": "password",
    "pushpak": "123456"
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['user'] = username  # store user in session
            return redirect(url_for('book'))
        else:
            return render_template("login.html", error="Invalid credentials, try again.")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)  # clear session
    return redirect(url_for('home'))
