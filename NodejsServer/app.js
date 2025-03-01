// importing the necessary modules  
const express = require('express'); 
const chalk = require('chalk'); 
const cors = require('cors'); 

// Building the express application 
const app = express(); 

// Setting some necessary middlewares 
app.use(express.json()); 
app.use(cors({
    origin: '*', 
    methods: ['GET', 'POST'], 
    credentials: true, 
    optionsSuccessStatus: 200, 
    allowedHeaders: [
        'Content-Type', 'Authorizaton', 
        'Access-Control-Allow-Methods', 
        'access-control-allow-orign', 
        'Access-Control-Allow-Origin', 
        'Access-Control-Allow-Headers',
    ]
}));

// Setting the port and host number 
const PORT = process.env.PORT || 3000; 
const HOST = process.env.HOST || "localhost"; 

// Importing the required routes 
const home = require('./routes/homeRoutes'); 

// Setting the routes configurations 
app.use('/', home); 

// Running the nodejs server 
app.listen(PORT, HOST, () => {
    // Displaying the server message 
    let serverMessage = chalk.blue(`The server is running on ${HOST + ":" + PORT}`); 
    console.log(serverMessage); 
})