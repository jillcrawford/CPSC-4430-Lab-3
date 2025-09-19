from flask import Flask
from flask import send_file, request
app = Flask(__name__)

template = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>CPSC 4430 Lab 3</title>
  </head>
  <body>
    {content}
  </body>
</html>
""".strip()