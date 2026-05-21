from flask import Flask
from flask import render_template
from flask import request
from flask import Response

from resume_generator import generate_resume

app = Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/generate_pdf", methods=["POST"])
def generate_pdf():

    try:

        data = request.json

        pdf_data = generate_resume(data)

        return Response(

            pdf_data,

            mimetype="application/pdf",

            headers={

                "Content-Disposition":
                "attachment;filename=resume.pdf"

            }
        )

    except Exception as e:

        print("PDF ERROR:", e)

        return {

            "error": str(e)

        }, 500


if __name__ == "__main__":

    app.run()