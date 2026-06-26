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