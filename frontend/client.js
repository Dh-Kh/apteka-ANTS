const express = require("express");
const axios = require("axios");
const path = require("path");
const app = express();
const port = 3000;

const API_URL = "";

app.use(express.static(path.join(__dirname, "public")));

app.get(

)

app.listen(port, () => {
    console.log("Server is running")
});
