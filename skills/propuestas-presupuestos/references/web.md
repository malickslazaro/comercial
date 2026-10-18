# Web de propuesta — resultado principal

## Del expediente al sitio

Lee la reunión y documentos, identifica contenido autorizado para el cliente y construye la página. Reutiliza el proyecto existente si es una actualización. En una nueva propuesta, separa fuentes y materiales privados de la carpeta que se desplegará, por ejemplo:

- `work/`: material de trabajo y registro interno.
- `outputs/propuesta/`: propuesta final y presupuesto cliente.
- `work/vercel-<cliente>/`: únicamente archivos públicos del sitio y configuración del proyecto.

No despliegues la raíz del expediente. No copies conversaciones, presupuestos internos, credenciales, datos de contacto privados ni informes de seguimiento a la carpeta pública. No escondas márgenes internos en el HTML o JavaScript: siguen siendo públicos.

Usa HTML/CSS/JavaScript estáticos para una propuesta editorial sencilla y autónoma. Si existe un proyecto con otro framework, conserva su arquitectura. El objetivo es un enlace funcional y mantenible; no elegir un stack complejo por defecto.

## Diseño comercial

Adapta el diseño a la identidad real y al cliente. Para WTG, una base habitual es fondo blanco, tipografía sobria, espacio amplio y azul de marca en acciones e inversión. No fijar un azul sin consultar los activos disponibles. Máximo dos o tres tamaños principales de texto; crear jerarquía con peso, espacio y composición.

La página debe permitir entender en una lectura rápida:

- Quién propone y para quién.
- Objetivos y necesidad concreta.
- Qué se hará y qué se entregará.
- Formación u otros servicios si corresponden.
- Opciones, precio y condiciones materiales.
- Próximo paso.

Usa navegación por anclas en páginas largas, comparación de opciones en paralelo en escritorio y en vertical en móvil, FAQ desplegables accesibles y un cierre con CTA. Evita tarjetas por cada frase, exceso de etiquetas, titulares genéricos y párrafos legales diminutos. La información decisiva no debe quedar escondida en una FAQ.

Incluye logos y fotos reales autorizados cuando aporten valor. Mantén proporciones y comprueba el recorte. No reutilices contenido específico de Ujo, Audidat u otro cliente como si correspondiera al nuevo caso.

## Interactividad útil

Una web de propuesta puede incorporar guía formativa desplegable, recorrido por fases, comparación de alternativas o simulador económico. Usa HTML semántico (`details`, `summary`, botones y etiquetas) y controles por teclado. No inventes formularios de contratación con apariencia funcional si no existe un receptor real.

En simuladores, deja claros supuestos, fórmula y resultado orientativo; conserva el precio aprobado. Verifica el cálculo con casos manuales. Un simulador FUNDAE requiere consultar fuentes oficiales actuales y aplicar la metodología de `$propuestas-presupuestos` cuando esté disponible. No enviar sus entradas a analítica.

El CTA usa un enlace de agenda o contacto aportado/verificado. Diferencia clic al calendario de reserva confirmada. No añadir un píxel, seguimiento individual o servicio de pago sin autorización pertinente. Si ya hay medición autorizada, conserva exclusiones de pruebas y comprueba que una visita de QA no contamine el informe.

## Vista previa y validación

Genera la web real y ábrela con las herramientas de navegador disponibles. Usa servidor local si hace falta; no presentes una ruta `127.0.0.1` como enlace para el cliente externo.

Comprueba a tamaño escritorio y móvil:

- Sin desbordamiento horizontal, fotos rotas ni texto recortado.
- Navegación, CTA, desplegables y simuladores funcionan.
- Precios, horas y alcance coinciden con presupuesto y conversación.
- Contraste, foco y lectura por teclado suficientes.
- No hay placeholders, notas internas ni contenido heredado de otro cliente.
- Impresión limpia si se ofrece guardar PDF; no afirmar que hay PDF exportado solo por existir un botón de impresión.

Inspecciona el resultado visual, no solo el código o HTTP. Guarda una captura cuando facilite la revisión. Si falta una herramienta de inspección, declara exactamente lo comprobado y la limitación.

## Publicación y enlace compartible

Si el usuario pide publicar, o la sesión ya autoriza actualizar esa misma web, termina el trabajo y publícalo usando las herramientas disponibles. Para Vercel, identifica el proyecto, cuenta y carpeta correctos. Reutiliza el proyecto del cliente; comprueba la configuración antes de crear otro. Con dominio pedido, confirma que la URL final apunta al despliegue nuevo, no a una versión anterior.

Después, verifica la URL final, contenido actualizado, imágenes, CTA y acceso del destinatario. HTTP 200 por sí solo no demuestra que esté lista ni que sea privada. `noindex` no es control de acceso; no llamar privada a una URL pública. Si la protección exige login, verifica que el cliente puede acceder o entrega claramente una vista previa protegida. No desactivar una protección existente sin autorización.

Entrega el enlace publicado si se verificó, los archivos editables y una frase sobre lo cambiado. Si no se pidió publicación, entrega la vista previa y archivos completos sin afirmar que la web está disponible para terceros. No envíes el enlace por correo ni a contactos sin petición expresa.
