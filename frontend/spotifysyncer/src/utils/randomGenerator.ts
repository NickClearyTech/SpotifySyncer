// dec2hex :: Integer -> String
// i.e. 0-255 -> '00'-'ff'
function dec2hex (dec: any) {
    return dec.toString(16).padStart(2, "0")
}

export function generateState(): string {
    var arr = new Uint8Array(40);
    crypto.getRandomValues(arr);
    return Array.from(arr, dec2hex).join("");
}