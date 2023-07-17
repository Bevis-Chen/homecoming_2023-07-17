from flask import Flask, render_template
from datetime import datetime

app= Flask(__name__)


@app.route("/")
def index():
    return "<h2>Hello Flask!</h2>"


@app.route("/nowtime")
def get_nowtime():
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    return render_template("index.html", nowtime= now)

if __name__=="__main__":
    app.run(debug=True)