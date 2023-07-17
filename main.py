from flask import Flask, render_template, request
from datetime import datetime
from crawler.pm25 import get_pm25

app= Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")

@app.route("/pm25")
def pm25values():
    # 檢查是否有勾選
    sort= request.args.get("sort")
    print(sort)
    columns, values= get_pm25(sort)
    return render_template("pm25.html", sort= sort, columns= columns, values= values)

@app.route("/nowtime")
def get_nowtime():
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    return render_template("index.html", nowtime= now)

if __name__=="__main__":
    app.run(debug=True)