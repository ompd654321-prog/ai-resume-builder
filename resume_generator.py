from fpdf import FPDF
import base64
import tempfile
import os


def clean_text(text):

    if not text:
        return ""

    replacements = {

        "•": "-",
        "–": "-",
        "—": "-",
        "“": '"',
        "”": '"',
        "‘": "'",
        "’": "'",
        "\u00a0": " "

    }

    for old, new in replacements.items():

        text = text.replace(old, new)

    return text


class ResumePDF(FPDF):

    def section_title(self, title):

        self.set_font(
            "Helvetica",
            'B',
            13
        )

        self.set_text_color(
            30,
            30,
            30
        )

        self.cell(
            0,
            8,
            title,
            ln=True
        )

        self.set_draw_color(
            120,
            120,
            120
        )

        self.line(
            12,
            self.get_y(),
            198,
            self.get_y()
        )

        self.ln(3)

    def section_body(self, text):

        self.set_font(
            "Helvetica",
            '',
            11
        )

        self.multi_cell(
            0,
            6,
            clean_text(text)
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
        "Helvetica",
        'B',
        22
    )

    pdf.set_text_color(
        20,
        20,
        20
    )

    pdf.cell(
        0,
        10,
        clean_text(data.get("name", "")),
        ln=True,
        align='C'
    )

    # CONTACT LINE

    pdf.set_font(
        "Helvetica",
        '',
        10
    )

    pdf.set_text_color(
        70,
        70,
        70
    )

    pdf.set_x(25)

    # EMAIL

    pdf.cell(
        55,
        6,
        clean_text(data.get("email", ""))
    )

    # PHONE

    pdf.cell(
        5,
        6,
        "|"
    )

    pdf.cell(
        30,
        6,
        clean_text(data.get("phone", ""))
    )

    # GITHUB

    if data.get("github"):

        pdf.cell(
            5,
            6,
            "|"
        )

        pdf.set_text_color(
            0,
            0,
            255
        )

        pdf.cell(
            22,
            6,
            "GitHub",
            link=data["github"]
        )

    # LINKEDIN

    if data.get("linkedin"):

        pdf.set_text_color(
            70,
            70,
            70
        )

        pdf.cell(
            5,
            6,
            "|"
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

    if data.get("summary"):

        pdf.section_title(
            "SUMMARY"
        )

        pdf.section_body(
            data["summary"]
        )

    # SKILLS

       # SKILLS

    if data.get("skills"):

        pdf.section_title(
            "SKILLS"
        )

        skill_lines = data["skills"].split("\n")

        for line in skill_lines:

            if ":" in line:

                heading, content = line.split(":", 1)

                # BOLD HEADING

                pdf.set_font(
                    "Helvetica",
                    'B',
                    10
                )

                pdf.set_text_color(
                    20,
                    20,
                    20
                )

                pdf.write(
                    6,
                    clean_text(heading + ": ")
                )

                # NORMAL CONTENT

                pdf.set_font(
                    "Helvetica",
                    '',
                    10
                )

                pdf.set_text_color(
                    60,
                    60,
                    60
                )

                pdf.write(
                    6,
                    clean_text(content.strip())
                )

                pdf.ln(8)

            else:

                pdf.set_font(
                    "Helvetica",
                    '',
                    10
                )

                pdf.multi_cell(
                    0,
                    5,
                    clean_text(line)
                )

        pdf.ln(2)

    # EDUCATION

    education = data.get(
        "education",
        []
    )

    valid_edu = False

    for edu in education:

        if edu.get("degree"):

            valid_edu = True

    if valid_edu:

        pdf.section_title(
            "EDUCATION"
        )

        for edu in education:

            if edu.get("degree"):

                pdf.set_font(
                    "Helvetica",
                    'B',
                    11
                )

                pdf.cell(
                    0,
                    6,
                    clean_text(
                        edu["degree"]
                    ),
                    ln=True
                )

                pdf.set_font(
                    "Helvetica",
                    '',
                    10
                )

                line = (
                    f'{edu.get("college","")} '
                    f'({edu.get("year","")})'
                )

                pdf.cell(
                    0,
                    5,
                    clean_text(line),
                    ln=True
                )

                pdf.ln(2)

    # EXPERIENCE

    experience = data.get(
        "experience",
        []
    )

    valid_exp = False

    for exp in experience:

        if exp.get("job"):

            valid_exp = True

    if valid_exp:

        pdf.section_title(
            "EXPERIENCE"
        )

        for exp in experience:

            if exp.get("job"):

                pdf.set_font(
                    "Helvetica",
                    'B',
                    11
                )

                pdf.cell(
                    0,
                    6,
                    clean_text(
                        exp["job"]
                    ),
                    ln=True
                )

                pdf.set_font(
                    "Helvetica",
                    '',
                    10
                )

                pdf.cell(
                    0,
                    5,
                    clean_text(
                        exp.get("company","")
                    ),
                    ln=True
                )

                pdf.multi_cell(
                    0,
                    5,
                    clean_text(
                        exp.get("desc","")
                    )
                )

                pdf.ln(2)

    # CERTIFICATIONS

    certifications = data.get(
        "certifications",
        []
    )

    valid_cert = False

    for cert in certifications:

        if cert.get("name"):

            valid_cert = True

    if valid_cert:

        pdf.section_title(
            "CERTIFICATIONS"
        )

        for cert in certifications:

            if cert.get("name"):

                pdf.set_font(
                    "Helvetica",
                    'B',
                    11
                )

                pdf.cell(
                    0,
                    6,
                    clean_text(
                        cert["name"]
                    ),
                    ln=True
                )

                pdf.set_font(
                    "Helvetica",
                    '',
                    10
                )

                line = (
                    f'{cert.get("org","")} '
                    f'({cert.get("year","")})'
                )

                pdf.cell(
                    0,
                    5,
                    clean_text(line),
                    ln=True
                )

                pdf.ln(2)

    # PROJECTS

 
        # PROJECTS

    if data.get("projects"):

        pdf.section_title(
            "PROJECTS"
        )

        projects = data["projects"].split("\n")

        for project in projects:

            if ":" in project:

                title, desc = project.split(":", 1)

                # PROJECT TITLE

                pdf.set_font(
                    "Helvetica",
                    'B',
                    11
                )

                pdf.set_text_color(
                    20,
                    20,
                    20
                )

                pdf.multi_cell(
                    0,
                    6,
                    clean_text(title)
                )

                # DESCRIPTION

                pdf.set_x(15)

                pdf.set_font(
                    "Helvetica",
                    '',
                    10
                )

                pdf.set_text_color(
                    60,
                    60,
                    60
                )

                pdf.multi_cell(
                    180,
                    5,
                    clean_text(desc)
                )

                pdf.ln(2)

            else:

                pdf.set_x(15)

                pdf.multi_cell(
                    180,
                    5,
                    clean_text(project)
                )

    # CUSTOM SECTION

    if (
        data.get("customTitle")
        and
        data.get("customContent")
    ):

        pdf.section_title(
            clean_text(
                data["customTitle"]
            )
        )

        pdf.section_body(
            data["customContent"]
        )

    # REMOVE TEMP IMAGE

    if image_path and os.path.exists(image_path):

        os.remove(image_path)

    # PDF OUTPUT

    pdf_output = pdf.output(dest="S")

    if isinstance(pdf_output, bytearray):

        return bytes(pdf_output)

    elif isinstance(pdf_output, bytes):

        return pdf_output

    else:

        return pdf_output.encode("latin-1")