
from flask import Flask, render_template, Response
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    files = []
    for file in os.listdir("static/bridgekmzs"):
        if file.endswith(".kmz"):
            files.append(file)
    kmz = files[len(files)-1]
    logfile = str(kmz).split(".")[0] + ".txt"
    return render_template('index.html', kmz = kmz, files = files, logfile = logfile)

@app.route('/view/<kmz>')
def view(kmz):
    files = []
    for file in os.listdir("static/bridgekmzs"):
        if file.endswith(".kmz"):
            files.append(file)
    logfile = str(kmz).split(".")[0] + ".txt"
    return render_template('index.html', kmz = str(kmz), files = files, logfile = logfile)


@app.route('/log/<logfile>')
def log(logfile):
    files = []
    for file in os.listdir("static/bridgekmzs"):
        if file.endswith(".kmz"):
            files.append(file)
    with open("static/logs/" + logfile, "r") as f:
        content = f.read()
    return render_template('log.html', content = content, files = files)
if __name__ == "__main__":
    app.run()
