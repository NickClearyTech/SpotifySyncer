import {codeToToken, spotifyTokenToSyncerToken} from "../../service/BackendService";

// Handles checking of getting a token from spotify using a code
export async function GetSpotifyTokenFromCode(code: string): Promise<[boolean, string, string]> {
    let result = await codeToToken(code);
    if (result.length != 2 || result[1].access_token == null || result[1].access_token !instanceof String){
        return [false, "", ""];
    }
    return [true, result[1].access_token, result[1].refresh_token];
}

export async function GetSyncerTokenFromSpotifyToken(code: string, client_id: string): Promise<[boolean, string, string]> {
    let result = await spotifyTokenToSyncerToken(code, client_id);
    if (result.length != 2 || result[1].access_token == null || result[1].access_token !instanceof String){
        return [false, "", ""];
    }
    return [true, result[1].access_token, result[1].refresh_token];
}