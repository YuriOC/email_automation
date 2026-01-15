from flask import Flask, request, render_template
from helpers import pdfReader, email_classification_AI

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    
    if request.method == "POST":

        file = request.files["email_file"]
        filename = file.filename

        if filename.endswith('.txt'):

            content = file.read().decode('utf-8')
            finalContent = email_classification_AI(content)

        elif filename.endswith('.pdf'):

            content = pdfReader(file)
            finalContent = email_classification_AI(content)

        else:
            raise ValueError("Unsupported file format. Please upload a .txt or .pdf file.")

        return render_template("result.html", contentJSON=finalContent)
    
@app.route("/result", methods=["GET"])
def return_page():
    return render_template("result.html")