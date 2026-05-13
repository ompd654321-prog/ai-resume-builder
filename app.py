from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
from flask import after_this_request

from resume_generator import generate_resume

import os

app = Flask(__name__)

@app.route("/")
def home():

    return render_template("index.html")

@app.route("/generate_pdf", methods=["POST"])
def generate_pdf():

    data = request.json

    pdf_path = generate_resume(data)

    @after_this_request
    def remove_file(response):

        try:

            if os.path.exists(pdf_path):

                os.remove(pdf_path)

        except Exception as e:

            print(e)

        return response

    return send_file(
        pdf_path,
        as_attachment=True,
        download_name="resume.pdf"
    )

if __name__ == "__main__":

    app.run(debug=True)