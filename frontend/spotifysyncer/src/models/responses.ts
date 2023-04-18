export abstract class APIResponse{
    status: number;
    success: boolean = false;
    errors: string[];
}

export class UploadRefreshTokenResponse extends APIResponse{
    user: number;
    saved: true;
}