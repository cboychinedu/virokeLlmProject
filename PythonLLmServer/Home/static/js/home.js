// Getting the dom elements 
let imageInput = document.getElementById("imageInput"); 
let outputDiv = document.getElementById("output"); 

// Creating a function for handling the image upload 
const uploadImage = () => {
    // check if the image is present in memeory 
    if (imageInput.files.length === 0) {
        // Setting the output div message 
        outputDiv.innerHTML = "Please select an image file"; 
        return; 
    }

    // clearing the output div 
    outputDiv.innerText = ""; 

    // Setting the form data 
    let formData = new FormData(); 
    formData.append("image", imageInput.files[0]); 

    fetch("http://localhost:3001/analyze-image", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "success") {
            outputDiv.innerHTML = `Analysis: ${data.message}`;
        } else {
            outputDiv.innerHTML = `Error: ${data.message}`;
        }
    })
    .catch(error => {
        outputDiv.innerHTML = "An error occurred: " + error;
    });
}