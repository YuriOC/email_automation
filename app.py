import os
import io

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
        content = file.read().decode('utf-8')
        return f"TXT File readed successfully with {len(content)} characters", 200
    elif filename.endswith('.pdf'):
        try:
            pdf_reader = PdfReader(io.BytesIO(file.read()))
            content = ""
            for page in pdf_reader.pages:
                content += page.extract_text()
        except Exception as e:
            return f"Error reading PDF: {str(e)}", 500
        return f"PDF File readed successfully with {len(content)} characters", 200
    return "Unsupported file format", 400