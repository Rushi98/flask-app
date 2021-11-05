from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/form", methods=['GET','POST'])
def form():
    result = ""
    form = request.form
    result = result + "<p>" + "name is " + form["name"] + "</p>"
    result = result + "<p>" + "school is " + form["school"] + "</p>" 
    return result