from flask import Flask, request, render_template
from helpers import pdfReader, email_classification_AI

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    
    if request.method == "POST":

        file = request.files["email"]
        filename = file.filename

        if filename.endswith('.txt'):

            content = file.read().decode('utf-8')
            finalContent = email_classification_AI(content)
            return finalContent, 200
        
        elif filename.endswith('.pdf'):

            content = pdfReader(file)
            finalContent = email_classification_AI(content)
            return finalContent, 200
        
        return "Unsupported file format", 4004