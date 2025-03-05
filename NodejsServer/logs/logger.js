// Importing the necessary modules 
const fs = require('fs'); 
const path = require('path'); 

// Create a write stream for the log ile 
const accessLogStream = fs.createWriteStream(
    path.join(__dirname, 'requests.log'), 
    { flags: 'a'}
)

// Exporting 
module.exports = accessLogStream; 