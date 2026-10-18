# Comercial WTG
Sistema reutilizable para preparar reuniones y generar propuestas web, presupuestos y cuestionarios con diseño WTG.

## Dos skills
- **preauditoria-web**: hoja de números + participantes → investigación, web preliminar y expediente privado.
- **propuestas-presupuestos**: expediente + notas de reunión → propuesta, presupuesto y próximos pasos.

## Empezar
```sh
python3 scripts/comercial.py build ejemplos/expediente-demo.json --out dist/demo
python3 -m http.server 8080 --directory dist/demo
```
Abre http://localhost:8080. El presupuesto está en /presupuesto.html, el formulario en /cuestionario/ y la administración en /admin/. El backend privado requiere configuración Vercel; ver [operación](docs/operacion.md).

Instala las dos skills con `python3 scripts/install.py`. Preserva instalaciones anteriores con copia de seguridad. El repo debe mantenerse en su ruta para que los enlaces funcionen.

Referencias visuales: WTG, Ujo, Audidat y Suderow Fernández. Se conservan estilos, nunca datos de clientes. Los ejemplos y precios son ficticios.

No contiene credenciales, expedientes reales ni respuestas. El generador es determinista; la investigación y redacción las realiza el agente siguiendo las skills. La programación del seguimiento y la publicación requieren configurar servicios.
