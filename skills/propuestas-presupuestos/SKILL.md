---
name: propuestas-presupuestos
description: Crea la propuesta comercial web y su presupuesto después de una reunión, reutilizando el expediente de preauditoria-web y las notas o transcripción como nuevo input. Define objetivos, servicios, entregables, fases, formación, inversión y CTA, y publica cuando se solicita.
---

# Propuesta web y presupuesto después de la reunión

Entrega una propuesta web profesional y su presupuesto coherente. El nuevo input habitual son las notas o transcripción de la reunión: reutiliza el expediente de `$preauditoria-web` sin pedir otra vez documentos, cifras o investigación ya disponibles. Lee [propuesta.md](references/propuesta.md) para la narrativa y [web.md](references/web.md) para construir la web. Lee [presupuesto.md](references/presupuesto.md) para el desglose, las fórmulas, el coste interno y los escenarios de bonificación cuando correspondan. Trabaja con el proveedor y cliente indicados; no asumas que todos los encargos pertenecen a WTG.

## Reutilizar la preauditoría y confirmar la reunión

Localiza `work/expediente_cliente.json` y `work/preauditoria_interna.md` en el expediente del cliente, o los equivalentes enlazados por la primera skill. Si el trabajo se invoca en otra conversación, busca por empresa/dominio y las rutas aportadas. Si no se localiza, pide solo la ubicación que falta y avanza con las notas; no inventes que has leído el expediente.

Cruza las notas nuevas con la investigación: qué hipótesis se confirmaron, cuáles se descartaron, objetivos expresados, servicios de interés, interlocutores, compromisos, restricciones y próximos pasos. Las notas de la reunión prevalecen sobre hipótesis previas. Reinvestiga solo datos ausentes, contradictorios o que puedan haber cambiado; no repitas todo el benchmark por rutina.

La información obtenida sirve para redactar una oferta concreta. Presenta qué hacemos, cómo, qué recibe el cliente, opciones, inversión y CTA. En consultoría distingue actividades y entregables; en formación explica audiencia, sesiones, horas y temario preliminar sujeto al análisis, sin prometer cursos adicionales. No añadas licencias o acceso anual a plataformas sin acuerdo.

## Alcance e inversión

Lee los archivos y decisiones del expediente: reunión, propuesta existente, servicios, entregables, cantidades, horas, exclusiones y precios aprobados. La última corrección expresa del usuario prevalece. Busca los datos disponibles antes de preguntar. No inventes tarifas, fiscalidad, participantes, NIF, plazos, descuentos ni condiciones de pago.

Distingue dos encargos:

- **Formalizar un precio aprobado:** conserva el importe; no exijas un modelo de coste interno para poder emitir el borrador de presupuesto.
- **Calcular un precio:** modela esfuerzo, costes, terceros y margen con fuentes o parámetros explícitos. Presenta escenarios como estimaciones, no como tarifas oficiales.

Si falta un dato material, deja el presupuesto condicionado y avanza con las partidas conocidas. Pide solo lo necesario para cerrar el cálculo. No amplíes el servicio para justificar un ticket mayor.

## Producción

Define opciones mutuamente excluyentes y servicios opcionales; indica qué incluye cada paquete. Mantén una sola línea de precio si el total está aprobado y no existe un reparto por partidas; no inventes el desglose económico.

Separa base, impuestos, total y pagos. El coste interno y el margen nunca se incluyen por defecto en la versión cliente. Si hay consultoría y formación, reconcilia horas del formador, horas por participante y grupos. Las bonificaciones son escenarios condicionados; no son descuentos garantizados en factura.

Para un modelo recalculable, genera una hoja con parámetros y fórmulas editables, más un resumen cliente. Para un presupuesto fijo sencillo, entrega un documento o HTML imprimible según el formato solicitado. Si se pide PDF, expórtalo y revisa el resultado. La web comercial es la salida por defecto de un encargo completo tras la reunión; si el usuario solicita solo un presupuesto o un cambio puntual, respeta ese alcance.

## Coherencia y entrega

Comprueba aritmética decimal, redondeos, subtotales, impuestos, descuentos y suma de pagos. Revisa que el presupuesto y la propuesta existente tengan los mismos precios, alcance, sesiones y entregables. Una revisión de presupuesto no autoriza modificar o publicar una web existente: actualiza también la web si el encargo lo incluye.

Conserva fuentes, hipótesis y costes en un archivo interno separado. Entrega el presupuesto cliente y, cuando se haya solicitado, el modelo económico editable. Enlaza archivos reales con rutas absolutas. Identifica de forma breve los datos pendientes que impidan considerarlo definitivo.

Construye y revisa la web siguiendo las referencias de esta skill; no dependas de la primera skill para volver a generar la presentación previa. Preparar el presupuesto no autoriza enviarlo por correo, contratar servicios ni publicarlo; respeta cualquier autorización ya dada en la sesión sin solicitarla de nuevo.

## Salidas del expediente

Guarda la web y activos cliente en `outputs/propuesta/`, el presupuesto cliente en el formato apropiado y el modelo de costes o notas internas en `work/`. Actualiza el expediente con necesidades confirmadas y decisiones, sin borrar las fuentes originales. La carpeta de publicación contiene solo material cliente autorizado.

Abre y verifica la web en móvil y escritorio, cálculos, interacciones y CTA. Si el usuario pide publicación, despliega y comprueba el dominio final siguiendo `references/web.md`. No hagas pasar un localhost por un enlace compartible ni llames privada a una página pública. La web preliminar y la oferta posterior son fases distintas: no reemplaces la primera URL salvo que el usuario lo pida o el encargo autorice actualizar ese mismo sitio.

## Motor de este repositorio

Lee `../../docs/operacion.md` y `../../docs/diseno.md`. El motor y las plantillas están en la raíz de este repositorio. Genera con `python3 scripts/comercial.py build <expediente.json> --out <carpeta-publica>`. El expediente separa `public` de información interna: el motor solo renderiza `public`. Usa el perfil de cuestionario apropiado; el incluido es para un profesional independiente y no representa una auditoría corporativa completa. No publiques las respuestas ni el expediente.
