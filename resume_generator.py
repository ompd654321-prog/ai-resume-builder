from fpdf import FPDF
import base64
import tempfile
import uuid
import os

class ResumePDF(FPDF):

    def section_title(self, title):

        self.set_font("Arial", 'B', 13)

        self.set_text_color(30, 30, 30)

        self.cell(
            0,
            8,
            title,
            ln=True
        )

        self.set_draw_color(120, 120, 120)

        self.line(
            12,
            self.get_y(),
            198,
            self.get_y()
        )

        self.ln(3)

    def section_body(self, text):

        self.set_font("Arial", '', 11)

        self.multi_cell(
            0,
            6,
            text
        )

        self.ln(2)


def generate_resume(data):

    pdf = ResumePDF()

    pdf.add_page()

    pdf.set_auto_page_break(
        auto=True,
        margin=15
    )

    image_path = None

    # IMAGE HANDLING

    if data.get("image"):

        try:

            image_data = data["image"]

            header, encoded = image_data.split(",", 1)

            image_bytes = base64.b64decode(encoded)

            temp_image = tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".jpg"
            )

            temp_image.write(image_bytes)

            temp_image.close()

            image_path = temp_image.name

        except Exception as e:

            print("Image Error:", e)

    # PROFILE IMAGE

    if image_path and os.path.exists(image_path):

        try:

            pdf.image(
                image_path,
                x=85,
                y=10,
                w=35,
                h=35
            )

            pdf.ln(40)

        except Exception as e:

            print("PDF Image Error:", e)

            pdf.ln(10)

    else:

        pdf.ln(10)

    # NAME

    pdf.set_font(
        "Arial",
        'B',
        22
    )

    pdf.set_text_color(20,20,20)

    pdf.cell(
        0,
        10,
        data["name"],
        ln=True,
        align='C'
    )

    # CONTACT LINE

    pdf.set_font(
        "Arial",
        '',
        10
    )

    pdf.set_text_color(
        70,
        70,
        70
    )

    pdf.cell(
        55,
        6,
        data["email"],
        align='R'
    )

    pdf.cell(
        10,
        6,
        "|",
        align='C'
    )

    pdf.cell(
        35,
        6,
        data["phone"],
        align='C'
    )

    # GITHUB LINK

    if data["github"]:

        pdf.cell(
            10,
            6,
            "|",
            align='C'
        )

        pdf.set_text_color(
            0,
            0,
            255
        )

        pdf.cell(
            25,
            6,
            "GitHub",
            link=data["github"]
        )

    # LINKEDIN LINK

    if data["linkedin"]:

        pdf.set_text_color(
            70,
            70,
            70
        )

        pdf.cell(
            10,
            6,
            "|",
            align='C'
        )

        pdf.set_text_color(
            0,
            0,
            255
        )

        pdf.cell(
            30,
            6,
            "LinkedIn",
            link=data["linkedin"]
        )

    pdf.ln(12)

    # SUMMARY

    if data["summary"]:

        pdf.section_title(
            "SUMMARY"
        )

        pdf.section_body(
            data["summary"]
        )

    # SKILLS

    if data["skills"]:

        pdf.section_title(
            "SKILLS"
        )

        pdf.section_body(
            data["skills"]
        )

    # EDUCATION

    if data["education"]:

        valid_edu = False

        for edu in data["education"]:

            if edu["degree"]:

                valid_edu = True

        if valid_edu:

            pdf.section_title(
                "EDUCATION"
            )

            for edu in data["education"]:

                if edu["degree"]:

                    pdf.set_font(
                        "Arial",
                        'B',
                        11
                    )

                    pdf.cell(
                        0,
                        6,
                        edu["degree"],
                        ln=True
                    )

                    pdf.set_font(
                        "Arial",
                        '',
                        10
                    )

                    pdf.cell(
                        0,
                        5,
                        f'{edu["college"]} ({edu["year"]})',
                        ln=True
                    )

                    pdf.ln(2)

    # EXPERIENCE

    if data["experience"]:

        valid_exp = False

        for exp in data["experience"]:

            if exp["job"]:

                valid_exp = True

        if valid_exp:

            pdf.section_title(
                "EXPERIENCE"
            )

            for exp in data["experience"]:

                if exp["job"]:

                    pdf.set_font(
                        "Arial",
                        'B',
                        11
                    )

                    pdf.cell(
                        0,
                        6,
                        exp["job"],
                        ln=True
                    )

                    pdf.set_font(
                        "Arial",
                        '',
                        10
                    )

                    pdf.cell(
                        0,
                        5,
                        exp["company"],
                        ln=True
                    )

                    pdf.multi_cell(
                        0,
                        5,
                        exp["desc"]
                    )

                    pdf.ln(2)

    # CERTIFICATIONS

    if data["certifications"]:

        valid_cert = False

        for cert in data["certifications"]:

            if cert["name"]:

                valid_cert = True

        if valid_cert:

            pdf.section_title(
                "CERTIFICATIONS"
            )

            for cert in data["certifications"]:

                if cert["name"]:

                    pdf.set_font(
                        "Arial",
                        'B',
                        11
                    )

                    pdf.cell(
                        0,
                        6,
                        cert["name"],
                        ln=True
                    )

                    pdf.set_font(
                        "Arial",
                        '',
                        10
                    )

                    pdf.cell(
                        0,
                        5,
                        f'{cert["org"]} ({cert["year"]})',
                        ln=True
                    )

                    pdf.ln(2)

    # PROJECTS

    if data["projects"]:

        pdf.section_title(
            "PROJECTS"
        )

        pdf.section_body(
            data["projects"]
        )

    # CUSTOM SECTION

    if (
        data["customTitle"]
        and
        data["customContent"]
    ):

        pdf.section_title(
            data["customTitle"]
        )

        pdf.section_body(
            data["customContent"]
        )

    # OUTPUT

    output = f"resume_{uuid.uuid4()}.pdf"

    pdf.output(output)

    # DELETE TEMP IMAGE

    if image_path and os.path.exists(image_path):

        os.remove(image_path)

    return output