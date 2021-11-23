#!/usr/bin/env python3

from flask import Flask, request, url_for, render_template, redirect

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        xss = request.form['string']
        return render_template("index.html",xss = xss)
    else:
        return redirect(url_for('start'))


@app.route("/pathtraversal", methods=['GET','POST'])
def pathtraversal():
    if request.method == 'POST':
        filename = request.form['filename']
        if filename == "":
            filename = "text/default.txt"
        f = open(filename,'r')
        read = f.read()
        return render_template("index.html", read = read)
    else:
        return redirect(url_for('start'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

# test
if __name__ == '__main__':
    app.run(host='0.0.0.0')
