from flask import Flask, render_template
import webbrowser
import threading

app = Flask(__name__)

# Home page route
@app.route("/")
def home():
    return render_template("index.html", title="My Python Website", name="Arpan Singh")

# About page route 
@app.route("/about") 
def about(): 
    return "<h1>About Page</h1><p>Python just for fun haha.</p>"

# Calculator page route
@app.route("/calculator")
def calculator():
    return render_template("calculator.html"),"<h1>Calculator</h1><p>A simple calculator.</p>"

#Tictactoe page route
@app.route("/tictactoe")
def tictactoe():
    return render_template("tictactoe.html")

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
    threading.Timer(1, open_browser).start()
    app.run(debug=True, host="127.0.0.1", port=5000)
