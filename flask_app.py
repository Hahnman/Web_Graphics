from Flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/static/examples.html")

app.run()