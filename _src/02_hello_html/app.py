from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
<html>
   <head>
      <title>Zdravo</title>
   </head>
   <body>
      <h1>Zdravo</h1>
   </body>
</html>
"""
