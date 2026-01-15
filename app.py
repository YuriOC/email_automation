from flask import Flask, request, render_template
from helpers import EmptyFileError, FileReadError, email_classification_AI, read_file

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        
        return render_template("index.html")
    
    if request.method == "POST":

        file = request.files["email_file"]
        filename = file.filename

        try:
            full_text = read_file(file, filename)
            final_content = email_classification_AI(full_text)
        except EmptyFileError as e:
            return {
                "error": "EmptyFileError",
                "message": str(e)
            }
        except FileReadError as e:
            return {
                "error": "FileReadError",
                "message": str(e)
            }
        
        return render_template("result.html", contentJSON=final_content)

@app.route("/result", methods=["GET"])
def return_page():
    return render_template("result.html")