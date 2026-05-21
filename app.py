from flask import Flask
from flask import render_template
from flask import request
from flask import send_file

from resume_generator import generate_resume

from io import BytesIO

app = Flask(__name__)


# HOME PAGE

@app.route("/")
def home():

    return render_template("index.html")


# PDF GENERATION

@app.route("/generate_pdf", methods=["POST"])
def generate_pdf():

    try:

        # GET DATA FROM FRONTEND

        data = request.json

        # GENERATE PDF

        pdf_data = generate_resume(data)

        # STORE PDF IN MEMORY

        pdf_buffer = BytesIO(pdf_data)

        pdf_buffer.seek(0)

        # SEND PDF

        return send_file(

            pdf_buffer,

            as_attachment=True,

            download_name="resume.pdf",

            mimetype="application/pdf"

        )

    except Exception as e:

        print("PDF ERROR:", e)

        return {

            "error": str(e)

        }, 500


# RUN APP

if __name__ == "__main__":
    app.run()