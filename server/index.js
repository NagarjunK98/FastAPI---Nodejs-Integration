let request = require("request")
let express = require("express");
const PORT = 3000;
const PYSERVER = "http://127.0.0.1:8000"

app = express()

app.get("/fetch_params", (req, res) => {
    let name = req.query.name;
    let dob = req.query.dob;
    url = `${PYSERVER}/v1/api/query-params/query_param?name=${name}&dob=${dob}`
    request(url, (err, response, body) => {
        if(err) {
            console.log(err)
        }
        res.send(JSON.parse(body))
    })

})

app.listen(PORT, console.log(`Express server running on PORT:${PORT}`))