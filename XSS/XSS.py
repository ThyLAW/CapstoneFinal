#!/usr/bin/env python3

from flask import Flask, request, url_for, render_template, redirect

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/test")
def start2():
    return render_template("index2.html")

@app.route("/home", methods=['POST'])
def home():
    xss = request.form['string']
    return render_template("index.html",xss = xss)

@app.route("/test2", methods=['POST'])
def test():
    filename = request.form['filename']
    if filename == "":
        filename = "text/default.txt"
    f = open(filename,'r')
    read = f.read()
    return render_template("index2.html", read = read)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

