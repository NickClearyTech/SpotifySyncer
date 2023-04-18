import axios, {AxiosResponse} from "axios";
import {UploadRefreshTokenResponse} from "../models/responses";

const axiosClient = axios.create({
    baseURL: `${import.meta.env.VITE_API_FULL_URL}`
})

export async function getCallback(){
    try {
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
    try {
        let result = await axiosClient.post("/codetotoken/", data);
        return [null, result.data]
    } catch (error){
        return [error]
    }
}

export async function spotifyTokenToSyncerToken(token: string, client_id: string){
    try {
        let result = await axiosClient.post(`/auth/convert-token?grant_type=convert_token&client_id=${client_id}&backend=spotify&token=${token}`)
        return [null, result.data]
    } catch (error) {
        return [error]
    }
}

export async function uploadRefreshToken(token: string, expiry: string): Promise<UploadRefreshTokenResponse> {
    try {
        const {data, status } = await axiosClient.post<UploadRefreshTokenResponse>(`/refreshtoken/`, {
            "refresh_token": token,
            "expiry": expiry
        });
        if (status == 200) {
            data.success = true;
            data.status = status;
            return data
        }
        data.success = false;
        data.status = status;
        return data;
    } catch (error) {
        let response: UploadRefreshTokenResponse = new UploadRefreshTokenResponse;
        response.success = false;
        if (axios.isAxiosError(error)) {
            response.errors = [error.message];
        } else {
            // @ts-ignore
            response.errors = [error.toString()];
        }
        return response;
    }
}