function registerUser(){

    let username = document.getElementById("username").value.trim();
    let email = document.getElementById("email").value.trim();
    let occupation = document.getElementById("occupation").value;
    let password = document.getElementById("password").value;

    if(username === "" || email === "" || occupation === "" || password === ""){
        alert("Please fill all fields");
        return;
    }

    fetch("/api/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username: username,
            email: email,
            occupation: occupation,
            password: password
        })
    })
    .then(response => response.json())
    .then(data => {
        if(data.success){
            alert("Registration successful");
            window.location.href = "/";
        }
        else{
            alert(data.error);
        }
    })
    .catch(error => {
        alert("Registration error: " + error);
    });
}

function loginUser(){

    let username = document.getElementById("username").value.trim();
    let occupation = document.getElementById("occupation").value;
    let password = document.getElementById("password").value;

    if(username === "" || occupation === "" || password === ""){
        alert("Please fill all fields");
        return;
    }

    fetch("/api/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username: username,
            occupation: occupation,
            password: password
        })
    })
    .then(response => response.json())
    .then(data => {
        if(data.success){

            localStorage.setItem("user_id", data.user_id);
            localStorage.setItem("username", data.username);
            localStorage.setItem("email", data.email);

            if(data.occupation){
                localStorage.setItem("occupation", data.occupation);
            }
            else{
                localStorage.setItem("occupation", occupation);
            }

            localStorage.removeItem("assessmentStarted");
            localStorage.removeItem("faceScanDone");
            localStorage.removeItem("questionnaireDone");

            window.location.href = "/dashboard";
        }
        else{
            alert(data.error);
        }
    })
    .catch(error => {
        alert("Login error: " + error);
    });
}

function goToFaceScan(){
    window.location.href = "/facescan";
}

function goToQuestionnaire(){

    if(
        localStorage.getItem("assessmentStarted") === "true" &&
        localStorage.getItem("faceScanDone") === "true"
    ){
        window.location.href = "/questionnaire";
    }
    else{
        alert("Please complete Face Scan first.");
        window.location.href = "/facescan";
    }
}

function goToReports(){

    if(
        localStorage.getItem("assessmentStarted") === "true" &&
        localStorage.getItem("faceScanDone") === "true" &&
        localStorage.getItem("questionnaireDone") === "true"
    ){
        window.location.href = "/reports";
    }
    else{
        alert("Please complete Face Scan and Questionnaire first.");
        window.location.href = "/dashboard";
    }
}

function goToRecommendations(){

    if(
        localStorage.getItem("assessmentStarted") === "true" &&
        localStorage.getItem("faceScanDone") === "true" &&
        localStorage.getItem("questionnaireDone") === "true"
    ){
        window.location.href = "/recommendations";
    }
    else{
        alert("Please complete assessment first.");
        window.location.href = "/dashboard";
    }
}

function goToHistory(){
    window.location.href = "/history";
}