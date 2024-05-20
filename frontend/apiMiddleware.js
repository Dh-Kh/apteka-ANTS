const axios = require('axios');

const API_URL = "http://localhost:8000/api/";

exports.default = (req, res, next) => {
    const token = req.cookies.token;
    req.apiAuth = axios.create({
        baseURL: API_URL,
        headers: {
            "Authorization": `Token ${token}`
        },
        withCredentials: true
    });
    next();
};
