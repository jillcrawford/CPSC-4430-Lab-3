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

@app.route('/rick-astley.jpg')
def rick():
    return send_file('rick-astley.jpg')

if __name__ == '__main__':
    app.run(debug=True)
