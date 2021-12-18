import json
from flask import Flask, render_template, request, url_for, redirect, jsonify

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route('/home')
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/anime')
def anime():
  return render_template("anime.html")

@app.route('/send')
def suggestion():
  return render_template("send.html")

@app.route('/send', methods = ["POST"])
def sent():
  if request.method == "POST":
    value = request.form["animename"]

    # Append the value to the json file permanantly
    
    return render_template("sent.html", value=value)

app.run(host = "0.0.0.0", port = 8080)