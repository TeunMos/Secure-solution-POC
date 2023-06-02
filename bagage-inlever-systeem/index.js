const express = require('express');
const hbs = require('hbs');
const app = express();


// Set view engine
app.set('view engine', 'hbs');

// Set static folder
app.use(express.static('public'));


app.get('/', (req, res) => {
  res.render('index');
});


// Start server
app.listen(3000, () => {
  console.log('http://localhost:3000');
});