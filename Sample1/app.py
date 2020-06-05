from flask import Flask
from flask import render_template,request
import corona_date

app = Flask(__name__)
app.debug= True
@app.route("/")
def hello():
    return render_template("search.html")
@app.route("/h")
def us():
    return "I LOVE YOU"

@app.route("/head")
def head():
    return render_template("home.html")

@app.route("/f")
def form():
    return render_template("form.html")
@app.route("/login", methods=["POST"])
def get_form_values():
    fn = request.form['fname']
    ln = request.form['lname']

    return f"Hello {fn} {ln}"


@app.route("/d")
def corona():
    return render_template("corona.html")

@app.route("/getdate", methods=["POST"])
def get_corona_date():
    dt = request.form['date1']
    return f"Corona Virus Update on {dt}"


# Original
@app.route('/corona_search', methods=["POST"])
def get_covid_data():
    filter_date=request.form['kdate']
    fdata=corona_date.covid_data_filter(filter_date)
    return render_template('search_results.html',kdate=filter_date,data=fdata)


app.run()