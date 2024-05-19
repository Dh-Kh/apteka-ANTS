const express = require("express");
const axios = require("axios");
const path = require('path');
const bodyParser = require("body-parser");
const cors = require("cors");
const app = express();
const port = 3000;

const API_URL = "http://localhost:8000/api/";

app.set('view engine', 'ejs');

app.set("views", path.join(__dirname, "pages"));

const corsOptions = {
    origin: "http://localhost:8000/",
    optionsSuccessStatus: 200,
};

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(cors(corsOptions));

app.use(express.static(path.join(__dirname, "public")));


const api = axios.create({
    baseUrl: API_URL
});

const apiAuth = axios.create({
    baseUrl: API_URL
});

apiAuth.interceptors.request.use(config => {
    const token = localStorage.getItem("token");
    if (token) {
        config.headers.Authorization = `Token ${token}`;
    }
    return config;
});

app.get("/", (res, req) => {
    res.render("dashboard")
});

app.get("/register", (req, res) => {
    res.render("register");
});

{/* CHECK WHY POST REQUESTS AREN'T SENDING*/}

app.post("/register", async(req, res) => {
    try {
        const response = await api.post('register/', req.body);
        res.redirect("/login");
    } catch (error) {
        res.render("register", {error: "Invalid credentials"});
    }
});


app.get("/login", (req, res) => {
    res.render("login");
});

app.post("/login", async(req, res) => {
    try {
        const response = await api.post('login/', req.body);
        const token = response.data;
        localStorage.setItem("token", token);
        res.redirect("/");
    } catch (error) {
        res.render("login", {error: "Invalid credentials"});
    }
});

app.post("/logout", async(req, res) => {
    try {
        await apiAuth.post("logout/");
        localStorage.removeItem("token");
        res.redirect("/login")
    } catch (error) {
        res.render("logout", {error: "An error occured"});
    }
})

app.listen(port, () => {
    console.log("Server is running")
});
