# Operación
1. Invoca preauditoria-web con la hoja y participantes. Guarda fuentes, incertidumbres e investigación en un expediente privado. SABI/LinkedIn solo si accesibles con autorización; no se incluyen conectores ni accesos pagados.
2. Invoca propuestas-presupuestos con notas y expediente. Las decisiones de reunión prevalecen. Redacta únicamente el contenido cliente en `public`; el generador no redacta ni investiga por sí mismo.
3. Ejecuta `python3 scripts/comercial.py build expediente.json --out /ruta/cliente/site`. El generador valida, escapa HTML y crea web, presupuesto imprimible, formulario y /admin. PDF: usa Imprimir/Guardar PDF y revisa el archivo; no hay exportación binaria automática.
4. El cuestionario independiente mantiene seis pasos y estimación de 25 minutos. Para empresas adapta campos/recorrido antes de usarlo; no asumas que diez respuestas generan evaluación completa de madurez.
5. Backend: cada proyecto necesita su propio Blob privado y variables BLOB_READ_WRITE_TOKEN, ADMIN_SESSION_SECRET, ADMIN_CODE_HASH, PUBLIC_ORIGIN. Genera secretos independientes; ADMIN_CODE_HASH usa scrypt salt:hash. No copies claves de un cliente. No rotes ADMIN_SESSION_SECRET sin migrar datos cifrados. Sin configurar almacenamiento el guardado remoto/admin no funciona; el formulario conserva copia local.
6. Publicación solicitada: vincula al proyecto Vercel correcto desde la carpeta generada; configura variables y ejecuta `vercel deploy --prod`. Nunca desde la raíz del repo. Verifica dominio, guardado, recuperación, finalización y autenticación con pruebas WTG INTERNAL QA.
7. Seguimiento: `python3 scripts/comercial.py monitor --origin https://dominio --state /ruta/privada/state.json --report /ruta/privada/report.json`, con ADMIN_SESSION_SECRET en entorno. Sin baseline anterior, solo registra referencia inicial. Programa este comando en infraestructura privada. No queda programado solo por instalar la skill. Avisa solo de cambios; aperturas no confirman identidad y guardar borrador no es finalizar.

GitHub Actions valida el generador y las skills con ejemplos ficticios. No investiga de forma periódica, no publica ni envía correos automáticamente.

## Variables y código de administración
Genera los valores una sola vez por proyecto y guárdalos en un gestor de secretos. Ejemplo local (no imprime secretos):
```sh
node scripts/create-secrets.mjs /ruta/privada/cliente.env
```
Copia esos valores a las variables del proyecto Vercel. Añade PUBLIC_ORIGIN con el dominio exacto (sin barra final) y vincula un Blob privado por proyecto. El fichero generado no debe entrar en Git ni en la carpeta de publicación. El código inicial está en ADMIN_CODE y solo se comunica al administrador; configura en Vercel únicamente ADMIN_CODE_HASH y ADMIN_SESSION_SECRET, nunca ADMIN_CODE.
