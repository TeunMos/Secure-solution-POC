const express = require('express');
const hbs = require('hbs');
const app = express();
const axios = require('axios');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');

// Set url for bagage-tracking-systeem
const bagageURL = '';

app.set('view engine', 'hbs'); // Set view engine
app.use(express.static('public')); // Set static folder
app.use(bodyParser.urlencoded({ extended: false })); // Set body parser

app.get('/', (req, res) => {
    if (req.query.desk != null && req.query.desk != undefined && req.query.desk != '')
    {
        const desk = req.query.desk; // Get desk from query (url/?desk=XXX)
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

    const bagage = {
        id : id,
        owner : req.body.name,
        CheckInDesk : req.body.desk,
        flightNumber : req.body.flight
    };
    axios.post(bagageURL, {
        bagage : bagage
    }).then((response) => {
        console.log(response);
        res.redirect('/?desk=' + req.body.desk + '&success=true');
    }).catch((error) => {
        console.log(error);
        res.status(500).send('Er is iets misgegaan');
    });
});


// Start server
app.listen(3000, () => {
  console.log('http://localhost:3000');
});