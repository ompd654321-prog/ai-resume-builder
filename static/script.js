let uploadedImage = "";

/* IMAGE UPLOAD */

const imageInput =
document.getElementById(
"imageInput"
);

imageInput.addEventListener(
"change",
function(){

const file = this.files[0];

if(file){

const reader =
new FileReader();

reader.onload = function(e){

uploadedImage =
e.target.result;

document.getElementById(
"previewImage"
).src = uploadedImage;

document.getElementById(
"previewImage"
).style.display =
"block";

document.getElementById(
"resumeImage"
).src = uploadedImage;

document.getElementById(
"resumeImage"
).style.display =
"block";
}

reader.readAsDataURL(file);
}
});

/* EDUCATION */

function addEducation(){

const container =
document.getElementById(
"educationContainer"
);

const div =
document.createElement("div");

div.classList.add("edu-block");

div.innerHTML = `

<input type="text"
placeholder="Degree"
class="degree">

<input type="text"
placeholder="Institution"
class="college">

<input type="text"
placeholder="Year"
class="year">

<button class="delete-btn"
onclick="this.parentElement.remove();
updatePreview();">

Delete

</button>
`;

container.appendChild(div);

addListeners();
}

/* EXPERIENCE */

function addExperience(){

const container =
document.getElementById(
"experienceContainer"
);

const div =
document.createElement("div");

div.classList.add("exp-block");

div.innerHTML = `

<input type="text"
placeholder="Job Title"
class="job">

<input type="text"
placeholder="Company"
class="company">

<textarea
placeholder="Responsibilities"
class="desc"></textarea>

<button class="delete-btn"
onclick="this.parentElement.remove();
updatePreview();">

Delete

</button>
`;

container.appendChild(div);

addListeners();
}

/* CERTIFICATION */

function addCertification(){

const container =
document.getElementById(
"certificationContainer"
);

const div =
document.createElement("div");

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
onclick="this.parentElement.remove();
updatePreview();">

Delete

</button>
`;

container.appendChild(div);

addListeners();
}

/* INPUT LISTENERS */

function addListeners(){

document.querySelectorAll(
"input, textarea"
).forEach(input => {

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

/* LIVE PREVIEW */

function updatePreview(){

document.getElementById(
"previewName"
).innerText =
document.getElementById(
"name"
).value;

document.getElementById(
"previewContact"
).innerText =
document.getElementById(
"email"
).value
+
" | " +
document.getElementById(
"phone"
).value;

let linksHTML = "";

if(
document.getElementById(
"linkedin"
).value
){

linksHTML += `
<span class="link-btn">
LinkedIn
</span>
`;
}

if(
document.getElementById(
"github"
).value
){

linksHTML += `
<span class="link-btn">
GitHub
</span>
`;
}

document.getElementById(
"previewLinks"
).innerHTML = linksHTML;

document.getElementById(
"linkedin"
).value
+
"<br>" +
document.getElementById(
"github"
).value;

document.getElementById(
"previewSummary"
).innerText =
document.getElementById(
"summary"
).value;

document.getElementById(
"previewSkills"
).innerText =
document.getElementById(
"skills"
).value;

document.getElementById(
"previewProjects"
).innerText =
document.getElementById(
"projects"
).value;

document.getElementById(
"previewCustomTitle"
).innerText =
document.getElementById(
"customTitle"
).value;

document.getElementById(
"previewCustomContent"
).innerText =
document.getElementById(
"customContent"
).value;

/* EDUCATION */

let eduHTML = "";

document.querySelectorAll(
".edu-block"
).forEach(block => {

if(block.querySelector(".degree")){

const degree =
block.querySelector(
".degree"
).value;

const college =
block.querySelector(
".college"
).value;

const year =
block.querySelector(
".year"
).value;

eduHTML += `

<p>

<b>${degree}</b><br>

${college} (${year})

</p>
`;
}
});

document.getElementById(
"previewEducation"
).innerHTML =
eduHTML;

/* EXPERIENCE */

let expHTML = "";

document.querySelectorAll(
".exp-block"
).forEach(block => {

const job =
block.querySelector(
".job"
).value;

const company =
block.querySelector(
".company"
).value;

const desc =
block.querySelector(
".desc"
).value;

expHTML += `

<p>

<b>${job}</b><br>

${company}<br>

${desc}

</p>
`;
});

document.getElementById(
"previewExperience"
).innerHTML =
expHTML;

/* CERTIFICATIONS */

let certHTML = "";

document.querySelectorAll(
".cert-name"
).forEach((item,index) => {

const name =
document.querySelectorAll(
".cert-name"
)[index].value;

const org =
document.querySelectorAll(
".cert-org"
)[index].value;

const year =
document.querySelectorAll(
".cert-year"
)[index].value;

certHTML += `

<p>

<b>${name}</b><br>

${org} (${year})

</p>
`;
});

document.getElementById(
"previewCertification"
).innerHTML =
certHTML;
}

/* INITIALIZE */

addListeners();

/* TEMPLATE CHANGE */

document.getElementById(
"templateSelect"
).addEventListener(
"change",
function(){

document.getElementById(
"resumePreview"
).className =
"resume-preview " + this.value;
});

/* DOWNLOAD PDF */

document.getElementById(
"downloadBtn"
).addEventListener(
"click",
async function(){

const education = [];

document.querySelectorAll(
".edu-block"
).forEach(block => {

if(block.querySelector(".degree")){

education.push({

degree:
block.querySelector(
".degree"
).value,

college:
block.querySelector(
".college"
).value,

year:
block.querySelector(
".year"
).value

});
}
});

const experience = [];

document.querySelectorAll(
".exp-block"
).forEach(block => {

experience.push({

job:
block.querySelector(
".job"
).value,

company:
block.querySelector(
".company"
).value,

desc:
block.querySelector(
".desc"
).value

});
});

const certifications = [];

document.querySelectorAll(
".cert-name"
).forEach((item,index) => {

certifications.push({

name:
document.querySelectorAll(
".cert-name"
)[index].value,

org:
document.querySelectorAll(
".cert-org"
)[index].value,

year:
document.querySelectorAll(
".cert-year"
)[index].value

});
});

const response =
await fetch(
"/generate_pdf",
{

method:"POST",

headers:{
"Content-Type":
"application/json"
},

body:JSON.stringify({

image:
uploadedImage,

name:
document.getElementById(
"name"
).value,

email:
document.getElementById(
"email"
).value,

phone:
document.getElementById(
"phone"
).value,

linkedin:
document.getElementById(
"linkedin"
).value,

github:
document.getElementById(
"github"
).value,

summary:
document.getElementById(
"summary"
).value,

skills:
document.getElementById(
"skills"
).value,

projects:
document.getElementById(
"projects"
).value,

customTitle:
document.getElementById(
"customTitle"
).value,

customContent:
document.getElementById(
"customContent"
).value,

education:
education,

experience:
experience,

certifications:
certifications

})
});

const blob =
await response.blob();

const url =
window.URL.createObjectURL(
blob
);

const a =
document.createElement("a");

a.href = url;

a.download = "resume.pdf";

a.click();
});