from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecret"  # required for session management

# Hardcoded users for demo
users = {
    "admin": "password",
    "pushpak": "123456"
}

# Home → Login page
@app.route('/')
def home():
    return render_template('login.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['user'] = username  # save user in session
            return redirect(url_for('book'))
        else:
            return render_template("login.html", error="Invalid credentials, try again.")

    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

# Book Appointment page
@app.route('/book', methods=['GET', 'POST'])
def book():
    if 'user' not in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        doctor = request.form['doctor']
        date = request.form['date']
        # Save the appointment (for now just print or store in session)
        if 'appointments' not in session:
            session['appointments'] = []
        session['appointments'].append({"doctor": doctor, "date": date})

        return redirect(url_for('history'))

    return render_template('book.html')

# History page
@app.route('/history')
def history():
    if 'user' not in session:
        return redirect(url_for('home'))

    appointments = session.get('appointments', [])
    return render_template('history.html', appointments=appointments)


# Run the app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
