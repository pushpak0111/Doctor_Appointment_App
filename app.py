from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data
users = {"test": "password"}
appointments = []

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if username in users and users[username] == password:
        return redirect(url_for("book"))
    return "Invalid credentials"

@app.route("/book", methods=["GET", "POST"])
def book():
    if request.method == "POST":
        doctor = request.form["doctor"]
        date = request.form["date"]
        appointments.append({"doctor": doctor, "date": date})
        return redirect(url_for("history"))
    return render_template("book.html")

@app.route("/history")
def history():
    return render_template("history.html", appointments=appointments)

if __name__ == "__main__":
    app.run(debug=True)
