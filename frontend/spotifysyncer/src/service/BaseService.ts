import axios from "axios";

const axiosClient = axios.create({
    baseURL: `${import.meta.env.VITE_API_FULL_URL}`
})

export async function getCallback(){
    try{
        const {data } = await axiosClient.get("/callback")
        return [null, data]
    } catch (error) {
        return [error];
    }
}

export async function codeToToken(code: string){
    let data: object = {
        code: code
    }
    try{
        let result = await axiosClient.post("/codetotoken/", data);
        return [null, result.data]
    } catch (error){
        return [error]
    }
}