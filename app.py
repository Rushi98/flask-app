from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/form", methods=['GET','POST'])
def form():
    return render_template('form.html', form=request.form)
