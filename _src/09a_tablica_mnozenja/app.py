from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    n = 10
    
    html = """<!DOCTYPE html>
<html>
   <head>
      <meta charset="utf-8" />
      <title>Tablica množenja</title>
   </head>
   <body>
     <table border="1">"""

    for i in range(1, n+1):
        html += "<tr>"
        for j in range(1, n+1):
            html += "<td>" + str(i*j) + "</td>"
        html += "</tr>\n"
    
    html += """
     </table>     
   </body>
</html>"""
    
    return html
