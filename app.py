from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/form", methods=['GET','POST'])
def form():
    result = ""
    for entry in request.form.items(multi=True):
        result = result + entry[0] + " = " + entry[1] + "\n"
    return result
