const mysql = require('mysql');

// Create connection to the database
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'Anu@0718',
    database: 'nutrition_db'
});

// Connect to the database
connection.connect((err) => {
    if (err) throw err;
    console.log('Connected to the database');
});

// Query the database
connection.query('SELECT * FROM foods', (err, results) => {
    if (err) throw err;
    console.log('Data fetched from the database:');
    console.log(results);
});

// Close the connection
connection.end();