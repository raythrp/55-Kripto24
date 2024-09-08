function caesarEncrypt(text, shift) {
    let result = '';
    
    for (let i = 0; i < text.length; i++) {
        let char = text[i];
        
        if (char.match(/[a-z]/i)) {
            let code = text.charCodeAt(i);
            let base = (code >= 65 && code <= 90) ? 65 : 97;
            
            char = String.fromCharCode(((code - base + shift) % 26) + base);
        }
        
        result += char;
    }
    
    return result;
}

function caesarDecrypt(text, shift) {
    return caesarEncrypt(text, (26 - shift) % 26);
}

let plaintext = "Halo Diana";
let shift = 3;

const ciphertext = caesarEncrypt(plaintext, shift);
console.log(`Encrypted: ${ciphertext}`);

const decrypted = caesarDecrypt(ciphertext, shift);
console.log(`Decrypted: ${decrypted}`);
