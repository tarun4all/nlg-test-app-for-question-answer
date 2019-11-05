const app = require('express')();
const chalk = require('chalk');
const bodyParser = require('body-parser');
const parsePDF = require('./controller/pythonFunctionCall');
const debugMiddleware = require('./debugMiddleware');

// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }));
 
// parse application/json
app.use(bodyParser.json());

//route for add
    //if got a and b in request than added else warning will be send
app.post('/parsePDF', debugMiddleware.printReq ,parsePDF);
app.get('/getTest', debugMiddleware.printReq, (req, res) => {res.send('done')});

app.listen(3000, () => {
    console.log(chalk.blue("server starts working.") + " You can access it on url : " + chalk.yellow.bold("http://localhost:3000/parsePDF"));
});