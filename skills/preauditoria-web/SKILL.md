---
name: preauditoria-web
description: Prepara reuniones comerciales investigando empresa e interlocutores a partir de una hoja de números y las personas del correo. Analiza datos financieros, LinkedIn, SABI si hay acceso y benchmark sectorial, y genera una presentación web preliminar y un expediente reutilizable.
---

# Preauditoría y web para preparar la reunión

## Entrada mínima

El usuario aporta una hoja de números o documento de empresa y copia las personas o el correo de la reunión. Con eso, investiga y produce los entregables; no exijas un brief adicional. La identidad de la empresa o persona solo requiere una pregunta si no puede resolverse con suficiente confianza. No presupongas el contenido de la «hoja de números»: inspecciona sus columnas, unidades, periodos y fórmulas.

La salida principal es una presentación web de preauditoría para orientar la reunión, más un expediente interno que después consume `$propuestas-presupuestos`. No es una oferta definitiva ni un diagnóstico confirmado por el cliente.

## Investigación autónoma

Lee [investigacion.md](references/investigacion.md). Resuelve la empresa jurídica, marca, web y personas antes de atribuir cuentas o cifras. Investiga la web corporativa, perfiles profesionales de LinkedIn y fuentes financieras y sectoriales pertinentes. Usa SABI cuando exista acceso autorizado por conector, navegador o exportación. No afirmes haber consultado un servicio que no es accesible; sigue con fuentes disponibles y registra la carencia. No compres informes ni suscripciones por defecto.

Analiza la hoja aportada antes de reemplazarla por cifras externas. Documenta fechas, unidades, entidad, fuente y diferencias. El benchmark compara empresas o estadísticas sectoriales razonablemente equivalentes; no convierte promedios sectoriales en cifras del cliente. Conserva la diferencia entre hechos, cálculos, estimaciones e hipótesis.

Relaciona la investigación con oportunidades concretas de procesos, IA, digitalización o colaboración que encajen con WTG y el caso. Describe beneficio potencial, fundamento, dato a validar y pregunta de reunión. No prometas porcentajes de ahorro o ROI sin base suficiente. No hagas afirmaciones sobre herramientas internas, equipo o problemas que no se hayan observado.

## Dos salidas distintas

- **Interna:** contexto financiero detallado, investigación de interlocutores, fuentes, benchmark, oportunidades y guion de preguntas. Incluye el estado de certeza y pendientes.
- **Cliente:** web breve, profesional y personalizada: contexto, objetivos preliminares, oportunidades a explorar, ejemplos relevantes y temas de conversación. No expongas fichas personales, correos privados, notas de negociación, estados financieros privados ni hipótesis sensibles como hechos.

Lee [web.md](references/web.md) para construir y validar la página. Usa el estilo de propuestas anteriores como referencia visual, sin heredar precios ni datos de otros clientes. Las cifras privadas pueden apoyar el análisis interno; no se publican por estar en el documento aportado. Sin permiso para mostrarlas, usa explicaciones cualitativas o datos públicos pertinentes.

## Expediente para la segunda skill

Guarda en la carpeta del cliente:

- `work/expediente_cliente.json`: identidad del cliente, proveedor, interlocutores, archivos de origen, fuentes con URL/fecha, hechos, cálculos, hipótesis, benchmark, oportunidades, preguntas, decisiones conocidas y datos pendientes.
- `work/preauditoria_interna.md`: informe legible para preparar la reunión; los datos privados permanecen aquí.
- `outputs/preauditoria/index.html`: web cliente y sus activos públicos.

Estos nombres son convenciones, no motivo para sobrescribir archivos existentes. Reutiliza el expediente del cliente y actualiza de forma trazable. Registra la ruta del informe y la web para que la siguiente skill los localice sin pedir volver a subirlos. Si hay varias empresas con nombres similares, enlaza por identidad jurídica o dominio verificados.

Entrega el enlace de vista previa o publicado si se solicitó y verificó, más la ruta del expediente interno. Verifica la web en móvil y escritorio. Preparar la reunión no autoriza contactar personas, enviar mensajes, comprar acceso ni publicar sin autorización existente.

## Motor de este repositorio

Lee `../../docs/operacion.md` y `../../docs/diseno.md`. El motor y las plantillas están en la raíz de este repositorio. Genera con `python3 scripts/comercial.py build <expediente.json> --out <carpeta-publica>`. El expediente separa `public` de información interna: el motor solo renderiza `public`. Usa el perfil de cuestionario apropiado; el incluido es para un profesional independiente y no representa una auditoría corporativa completa. No publiques las respuestas ni el expediente.
