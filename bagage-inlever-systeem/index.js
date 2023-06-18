const express = require('express');
const hbs = require('hbs');
const app = express();
const axios = require('axios');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');
const FormData = require('form-data');

// Set url for bagage-tracking-systeem
const bagageURL = 'http://127.0.0.1:3000/addLuggage';

app.set('view engine', 'hbs'); // Set view engine
app.use(express.static('public')); // Set static folder
app.use(bodyParser.urlencoded({ extended: false })); // Set body parser

app.get('/', (req, res) => {
    if (req.query.desk != null && req.query.desk != undefined && req.query.desk != '')
    {
        const desk = req.query.desk; // Get desk from query (url/?desk=XXX)

        // is succesfull
        if (req.query.success != null && req.query.success != undefined && req.query.success != '')
        {
            res.render('index', {
                desk: desk,
                success: true
            });
            return;
        }
        res.render('index', {
            desk: desk
        });
    }
    else
    {
        res.status(400).send('Geen desk gevonden');
    }
});

app.post('/add-bagage', (req, res) => {
    // generate id
    const id = uuidv4();

    const data = new FormData();

    // Add data to formdata
    data.append('id', id);
    data.append('owner', req.body.owner);
    data.append('weight', req.body.weight);
    data.append('CheckInTime', new Date().toISOString().slice(0, 19).replace('T', ' '));
    data.append('CheckInDesk', req.body.CheckInDesk);

    // flightnumber : req.body.flightnumber.toLowerCase(),
    // If the passengerinformationDB was not out of scope these values would be accuired from the database with the flightnumber
    data.append('destinationGate', req.body.destinationGate);
    
    console.log(data);

    
    axios.post(bagageURL, data).then((response) => {
        res.redirect('/?desk=' + req.body.CheckInDesk + '&success=true');
    }).catch((error) => {
        // console.log(error.Data);
        console.log(error.response.data);
        res.status(500).send('Er is iets misgegaan');
    });
});


// Start server
app.listen(3005, () => {
  console.log('http://localhost:3005');
});