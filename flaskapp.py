from flask import Flask
from flask import send_file, request
app = Flask(__name__)

@app.route('/')
def page():
    return """
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>CPSC 4430 Lab 3</title>
    </head>
    <body>
        <img src="/rick-astley.jpg" alt="Rick Astley singing 'Never Gonna Give You Up'">
    </body>
    </html>
    """

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return (f"<p>{a} + {b} = {a + b}</p>")

@app.route('/sub/<int:a>/<int:b>')
def sub(a, b):
    return (f"<p>{a} - {b} = {a - b}</p>")

@app.route('/reverse')
def reverse():
    q = request.args.get("q", "")
    return (f"<p>{q[::-1]}</p>")

@app.route('/rick-astley.jpg')
def rick():
    return send_file('rick-astley.jpg')

if __name__ == '__main__':
    app.run(debug=True)
