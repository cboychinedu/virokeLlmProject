// Importing the necessary modules 
const express = require('express'); 

// Creating the router object 
const router = express.Router(); 

// Setting the router for the home page 
router.post('/generate', async(req, res) => {
    // Getting the user's input message 
    try {
        // Getting the user's input message 
        userMessage = req.body.message; 

        // Setting the user's message as a json object 
        data = JSON.stringify({
            "message": userMessage, 
        })
        
        // Set the url 
        const url = "http://localhost:3001/llm-request"; 

        // Making a request to the llm server 
        const response = await fetch(url, {
            method: 'POST', 
            headers: { 'Content-Type': 'application/json'}, 
            body: data, 
        }); 

        // Getting the response data from the llm server 
        const dataResponse = await response.json();
        const successMessage = JSON.stringify(dataResponse);  

        // Sending it back to the client 
        return res.send(successMessage)
    }

    // Catch the error 
    catch (error) {
        // Generate the error message 
        let errorMessage = JSON.stringify({
            "message": error.toString().trim(), 
            "status": "error", 
            "statusCode": 500, 
        })

        // Sending back the error message 
        return res.send(errorMessage); 
    }
})


// Exporting the router object 
module.exports = router; 