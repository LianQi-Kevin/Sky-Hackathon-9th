import axios from "axios";

function LocalAxios() {
    return axios.create({
        baseURL: process.env.NODE_ENV === "development" ? "/apiDev" : "/api",
        headers: {
            'Content-Type': 'application/json',
        },
        timeout: 3000000
    });
}

export default LocalAxios