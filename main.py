from flask import Flask, render_template, request
from datetime import datetime
from crawler.pm25 import get_pm25
import json

app = Flask(__name__)


def get_today():
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    return now


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/othercharts")
def get_othercharts():
    return render_template("othercharts.html")


@app.route("/pm25-charts")
def pm25_charts():
    return render_template("pm25-charts.html")


@app.route("/pm25-json")
def get_pm25_json():
    columns, values = get_pm25()
    sites = [value[0] for value in values]
    pm25 = [value[2] for value in values]
    # count= len(sites)

    json_data = {"updatetime": get_today(), "counts": len(sites),
                 "sites": sites, "pm25": pm25}
    # json.dumps >> 輸出字串
    return json.dumps(json_data, ensure_ascii=False)


@app.route("/pm25", methods=["GET", "POST"])
def pm25values():
    # 檢查是否有勾選 (request.GET=>args)
    sort = False
    # (request.POST=> form)
    if request.method == "POST":
        sort = request.form.get("sort")  # 為了GET存在
        print(sort)
    columns, values = get_pm25(sort)
    return render_template("pm25.html", datetime=get_today(),
                           sort=sort, columns=columns, values=values)


@app.route("/nowtime")
def get_nowtime():
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    return render_template("index.html", nowtime=now)


if __name__ == "__main__":
    # print(get_pm25_json())
    app.run(debug=True)
