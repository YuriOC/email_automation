import os
import io
import nltk

from flask import Flask, request, render_template
from pypdf import PdfReader
from helpers import process_text_nlp

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    
    file = request.files["email"]
    filename = file.filename

    if filename.endswith('.txt'):
        content = file.read().decode('utf-8')
        FormatedContent = process_text_nlp(content)
        print(FormatedContent["clean"])
        return f"TXT File readed successfully with {len(content)} to {len(FormatedContent['clean'])}characters", 200
    elif filename.endswith('.pdf'):
        try:
            pdf_reader = PdfReader(io.BytesIO(file.read()))
            content = ""
            for page in pdf_reader.pages:
                txt = page.extract_text()
                if txt:
                    content += txt + "\n"
            finalContent = content.strip()
            FormatedContent = process_text_nlp(finalContent)
            print(FormatedContent["clean"])
        except Exception as e:
            return f"Error reading PDF: {str(e)}", 500
        return f"PDF File readed successfully with {len(content)} to {len(FormatedContent['clean'])} characters", 200
    return "Unsupported file format", 400