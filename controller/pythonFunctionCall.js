const chalk = require('chalk');

const parsePDF = (req, res) => {
    if(req.body.para) {
        const spawn = require("child_process").spawn;
        const pythonProcess = spawn('python',["./script.py", req.body.para]);

        pythonProcess.stdout.on('data', (data) => {
            console.log('Python fuction returned');
            res.send(data.toString());
        });
        
        pythonProcess.stderr.on('data', (data) => {
            console.log("Error occures in python : " + data.toString());
        });
    } else {
        res.send('Please send para in params to see the Manual result.');
    }
}

module.exports = parsePDF;