let uploadedImage = "";

/* IMAGE UPLOAD */

document.getElementById("imageInput")
.addEventListener("change", function () {

    const file = this.files[0];

    if (file) {

        const reader = new FileReader();

        reader.onload = function (e) {

            uploadedImage = e.target.result;

            document.getElementById("previewImage").src = uploadedImage;
            document.getElementById("previewImage").style.display = "block";

            document.getElementById("resumeImage").src = uploadedImage;
            document.getElementById("resumeImage").style.display = "block";
        };

        reader.readAsDataURL(file);
    }
});


/* EDUCATION */

function addEducation() {

    const container =
        document.getElementById("educationContainer");

    const div = document.createElement("div");

    div.classList.add("edu-block");

    div.innerHTML = `
    
    <input type="text" placeholder="Degree" class="degree">

    <input type="text" placeholder="Institution" class="college">

    <input type="text" placeholder="Year" class="year">

    <button class="delete-btn"
    onclick="this.parentElement.remove(); updatePreview();">

    Delete

    </button>
    `;

    container.appendChild(div);

    addListeners();
}


/* EXPERIENCE */

function addExperience() {

    const container =
        document.getElementById("experienceContainer");

    const div = document.createElement("div");

    div.classList.add("exp-block");

    div.innerHTML = `

    <input type="text" placeholder="Job Title" class="job">

    <input type="text" placeholder="Company" class="company">

    <textarea placeholder="Responsibilities"
    class="desc"></textarea>

    <button class="delete-btn"
    onclick="this.parentElement.remove(); updatePreview();">

    Delete

    </button>
    `;

    container.appendChild(div);

    addListeners();
}


/* CERTIFICATIONS */

function addCertification() {

    const container =
        document.getElementById("certificationContainer");

    const div = document.createElement("div");

    div.classList.add("edu-block");

    div.innerHTML = `

    <input type="text"
    placeholder="Certification Name"
    class="cert-name">

    <input type="text"
    placeholder="Organization"
    class="cert-org">

    <input type="text"
    placeholder="Year"
    class="cert-year">

    <button class="delete-btn"
    onclick="this.parentElement.remove(); updatePreview();">

    Delete

    </button>
    `;

    container.appendChild(div);

    addListeners();
}


/* LISTENERS */

function addListeners() {

    document.querySelectorAll("input, textarea")
        .forEach(input => {

            input.removeEventListener(
                "input",
                updatePreview
            );

            input.addEventListener(
                "input",
                updatePreview
            );
        });
}


/* PREVIEW */

function updatePreview() {

    document.getElementById("previewName")
        .innerText =
        document.getElementById("name").value;

    /* CONTACT */

    document.getElementById("previewContact")
        .innerText =
        document.getElementById("email").value +
        " | " +
        document.getElementById("phone").value;

    /* LINKS */

    let linksHTML = "";

    const github =
        document.getElementById("github").value;

    const linkedin =
        document.getElementById("linkedin").value;

    if (github) {

        linksHTML += `
        <a href="${github}"
        target="_blank"
        class="link-btn">

        GitHub

        </a>
        `;
    }

    if (linkedin) {

        linksHTML += `
        <a href="${linkedin}"
        target="_blank"
        class="link-btn">

        LinkedIn

        </a>
        `;
    }

    document.getElementById("previewLinks")
        .innerHTML = linksHTML;

    /* SUMMARY */

    document.getElementById("previewSummary")
        .innerText =
        document.getElementById("summary").value;

    /* SKILLS */

    let skillsHTML = "";

    document.getElementById("skills")
        .value
        .split("\n")
        .forEach(line => {

            if (line.includes(":")) {

                let parts = line.split(":");

                skillsHTML += `
                <p>

                <b>${parts[0]}:</b>

                ${parts[1]}

                </p>
                `;
            }

            else {

                skillsHTML += `
                <p>${line}</p>
                `;
            }
        });

    document.getElementById("previewSkills")
        .innerHTML = skillsHTML;

    /* PROJECTS */

    let projectHTML = "";

    document.getElementById("projects")
        .value
        .split("\n")
        .forEach(line => {

            if (line.includes(":")) {

                let parts = line.split(":");

                projectHTML += `
                <p>

                <b>${parts[0]}</b><br>

                ${parts[1]}

                </p>
                `;
            }

            else {

                projectHTML += `
                <p>${line}</p>
                `;
            }
        });

    document.getElementById("previewProjects")
        .innerHTML = projectHTML;

    /* CUSTOM */

    document.getElementById("previewCustomTitle")
        .innerText =
        document.getElementById("customTitle").value;

    document.getElementById("previewCustomContent")
        .innerText =
        document.getElementById("customContent").value;

    /* EDUCATION */

    let eduHTML = "";

    document.querySelectorAll(".edu-block")
        .forEach(block => {

            const degree =
                block.querySelector(".degree");

            if (degree) {

                eduHTML += `
                <p>

                <b>${degree.value}</b><br>

                ${block.querySelector(".college").value}

                (${block.querySelector(".year").value})

                </p>
                `;
            }
        });

    document.getElementById("previewEducation")
        .innerHTML = eduHTML;

    /* EXPERIENCE */

    let expHTML = "";

    document.querySelectorAll(".exp-block")
        .forEach(block => {

            expHTML += `
            <p>

            <b>${block.querySelector(".job").value}</b><br>

            ${block.querySelector(".company").value}<br>

            ${block.querySelector(".desc").value}

            </p>
            `;
        });

    document.getElementById("previewExperience")
        .innerHTML = expHTML;

    /* CERTIFICATIONS */

    let certHTML = "";

    document.querySelectorAll(".cert-name")
        .forEach((item, index) => {

            certHTML += `
            <p>

            <b>${document.querySelectorAll(".cert-name")[index].value}</b><br>

            ${document.querySelectorAll(".cert-org")[index].value}

            (${document.querySelectorAll(".cert-year")[index].value})

            </p>
            `;
        });

    document.getElementById("previewCertification")
        .innerHTML = certHTML;
}


/* TEMPLATE */

document.getElementById("templateSelect")
.addEventListener("change", function () {

    document.getElementById("resumePreview")
        .className =
        "resume-preview " + this.value;
});


/* DOWNLOAD PDF */

document.getElementById("downloadBtn")
.addEventListener("click", async function () {

    const education = [];

    document.querySelectorAll(".edu-block")
        .forEach(block => {

            const degree =
                block.querySelector(".degree");

            if (degree) {

                education.push({

                    degree: degree.value,

                    college:
                        block.querySelector(".college").value,

                    year:
                        block.querySelector(".year").value
                });
            }
        });

    const experience = [];

    document.querySelectorAll(".exp-block")
        .forEach(block => {

            experience.push({

                job:
                    block.querySelector(".job").value,

                company:
                    block.querySelector(".company").value,

                desc:
                    block.querySelector(".desc").value
            });
        });

    const certifications = [];

    document.querySelectorAll(".cert-name")
        .forEach((item, index) => {

            certifications.push({

                name:
                    document.querySelectorAll(".cert-name")[index].value,

                org:
                    document.querySelectorAll(".cert-org")[index].value,

                year:
                    document.querySelectorAll(".cert-year")[index].value
            });
        });

    const response = await fetch(
        "/generate_pdf",
        {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                image: uploadedImage,

                name:
                    document.getElementById("name").value,

                email:
                    document.getElementById("email").value,

                phone:
                    document.getElementById("phone").value,

                github:
                    document.getElementById("github").value,

                linkedin:
                    document.getElementById("linkedin").value,

                summary:
                    document.getElementById("summary").value,

                skills:
                    document.getElementById("skills").value,

                projects:
                    document.getElementById("projects").value,

                customTitle:
                    document.getElementById("customTitle").value,

                customContent:
                    document.getElementById("customContent").value,

                education: education,

                experience: experience,

                certifications: certifications
            })
        }
    );

    const blob = await response.blob();

    const url =
        window.URL.createObjectURL(blob);

    const a =
        document.createElement("a");

    a.href = url;

    a.download = "resume.pdf";

    a.click();

    window.URL.revokeObjectURL(url);
});


/* INITIALIZE */

addListeners();