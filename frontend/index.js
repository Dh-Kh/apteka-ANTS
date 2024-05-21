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

const apiMiddleware = require('./apiMiddleware').default;

app.use(apiMiddleware);

app.use(express.static(path.join(__dirname, "public")));

const api = axios.create({
    baseURL: API_URL
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
        const token = response.data.token;
        res.cookie("token", token, COOKIE_OPTIONS);
        res.redirect("/");
    } catch (error) {
        res.render("login", {error: "Invalid credentials"});
    }
});


app.post("/logout", async(req, res) => {
    try {
        await req.apiAuth.post("logout/");
    } catch (error) {
        res.render("dashboard", {error: "An error occured during logout"});
    } finally {
        res.clearCookie("token");
        res.redirect("/login")
    }
});

{/* Need to merge sort and filter .ejs 
GET /api/filter/?full_name__icontains=Mic&position=4&joined=&joined__gte=2022-05-026&joined__lte=&email__icontains=
*/}


app.get("/sort", async(req, res) => {
    try {
        let param = req.query.sortParam || "position";
        let page = req.query.page || 1;
        const response = await api.get(`sort/${param}/?page=${page}`);
        paginationMiddleware(response)(req, res, () => {
            res.render("sort", {
                data: req.data,
                currentPage: req.page,
                totalPages: req.totalPages,
                sortParam: param
            });
        });
    } catch (error) {
        res.render("sort", {error: "An error occured during sorting"});
    }
});

app.get("/filter", async(req, res) => {
    
    try {
        const filterParams = {
            full_name: String,
            position: Number,
            joined: Date,
            email: String
        };

        const filterCondition = Object.fromEntries(
            Object.entries(filterParams)
            .filter((_, value) => value !== "")
        );

        const paramsJoin = Object.keys(filterCondition).map((key) => {
            return `${encodeURIComponent(key)}=${encodeURIComponent(filterCondition[key])}`
        })
        .join("&");

        let page = req.query.page || 1;

        const response = await api.get(`filter/?page=${page}/${paramsJoin}`);

        paginationMiddleware(response)(req, res, () => {
            res.render("filter", {
                data: req.data,
                currentPage: req.page,
                totalPages: req.totalPages
            });
        });

    } catch (error) {
        res.render("filter", {error: "An error occured during filtering"});
    }
});

{/* Modify pagination middleware to make as separete .js file */}

function paginationMiddleware(response) {
    return (req, res, next) => {
        req.data = response.data.results;
        req.page = parseInt(req.query.page) || 1;
        req.totalPages = Math.ceil(response.data.count / 10);
        next();
    }
}


app.listen(port, () => {
    console.log("Server is running")
});
