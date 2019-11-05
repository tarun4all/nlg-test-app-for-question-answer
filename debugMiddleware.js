module.exports = {
    printReq: (req, res, next) => {
        console.log(req.method == 'GET' ? req.query : req.body);
        next();
    }
}