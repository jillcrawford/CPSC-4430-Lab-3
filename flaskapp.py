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
        <h1>Welcome to my page for my 3rd Software Engineering Lab!</h1>
        <p>Please pick which option seems most appealing:</p>
        <ul>
            <li><a href='/add'>Addition</a></li>
            <li><a href='/sub'>Subtraction</a></li>
            <li><a href='/reverse'>Reverse Text</a></li>
        </ul>
        <img src="/rick-astley.jpg" alt="Rick Astley singing 'Never Gonna Give You Up'">
    </body>
    </html>
    """

@app.route('/add')
def add():
    a = request.args.get('a')
    b = request.args.get('b')
    result =""
    if a and b and a.isdigit() and b.isdigit():
        result = f"<p>{a} + {b} = {int(a) + int(b)}</p>"

    return f"""
    <!doctype html>
    <html>
    <head>
        <title>Addition</title>
    </head>
    <body>
        <h2>Addition</h2>
        <form action='/add'>
            <input type='number' name='a' required> +
            <input type='number' name='b' required>
            <button type='submit'>Add</button>
        </form>
        {result}
        <p><a href='/'>Go back</a></p>
    </body>
    </html>
    """

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
