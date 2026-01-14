import os

from flask import Flask, request, render_template
from pypdf import PdfReader

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    file = request.files["email"]
    filename = file.filename

    if filename.endswith('.txt'):
        #content = file.read().decode('utf-8')
        return "TXT File readed successfully", 200
    elif filename.endswith('.pdf'):
        return "PDF file readed successfully", 200
    return "Unsupported file format", 400