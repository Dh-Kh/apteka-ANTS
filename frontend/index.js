const express = require("express");
const axios = require("axios");
const path = require('path');
const bodyParser = require("body-parser");
const cors = require("cors");
const cookieParser = require("cookie-parser");
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
app.use(cookieParser());

app.use(express.static(path.join(__dirname, "public")));


const api = axios.create({
    baseURL: API_URL
});

const apiAuth = axios.create({
    baseURL: API_URL
});

apiAuth.interceptors.request.use(config => {
    const token = document.cookie
        .split('; ')
        .find(row => row.startsWith('token='))
        ?.split('=')[1];
    if (token) {
        config.headers.Authorization = `Token ${token}`;
    }
    return config;
});

const COOKIE_OPTIONS = {
    maxAge: 14 * 24 * 60 * 60 * 1000,
    httpOnly: true,
}

app.get("/", (req, res) => {
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
        res.cookie("token", token);
        res.redirect("/");
    } catch (error) {
        res.render("login", {error: "Invalid credentials"});
    }
});

app.post("/logout", async(req, res) => {
    try {
        await apiAuth.post("logout/");
        res.clearCookie("token");
        res.redirect("/login")
    } catch (error) {
        res.render("logout", {error: "An error occured"});
    }
})

app.listen(port, () => {
    console.log("Server is running")
});
