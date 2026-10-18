import {randomBytes,scryptSync} from 'node:crypto';
import {writeFileSync,mkdirSync} from 'node:fs';
import {resolve,dirname} from 'node:path';
const output=process.argv[2];if(!output)throw Error('Indica una ruta privada para guardar los valores');
const dest=resolve(output),root=resolve(import.meta.dirname,'..');if(dest===root||dest.startsWith(root+'/'))throw Error('Guarda los secretos fuera del repositorio');
const code='WTG-'+randomBytes(12).toString('base64url'),salt=randomBytes(16).toString('hex');
mkdirSync(dirname(dest),{recursive:true,mode:0o700});writeFileSync(dest,`ADMIN_CODE=${code}\nADMIN_CODE_HASH=${salt}:${scryptSync(code,salt,64).toString('hex')}\nADMIN_SESSION_SECRET=${randomBytes(48).toString('base64url')}\n`,{mode:0o600,flag:'wx'});console.log('Valores guardados en el archivo privado indicado.');
