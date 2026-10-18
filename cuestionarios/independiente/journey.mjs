// A bounded client interview. The full schema remains the storage/admin contract.
export function buildJourney(full){
 const all=new Map(full.sections.flatMap(s=>s.fields).map(f=>[f.id,f]));
 const field=(id,extra={})=>({...all.get(id),...extra});
 const process=field('procesos');
 process.fields=['nombre','entradas','pasos','salida','responsables','herramientas','tiempo','dolor'].map(id=>({...process.fields.find(f=>f.id===id)}));
 process.label='Un encargo que conozcas bien';
 process.fields.find(f=>f.id==='pasos').placeholder='1. Recibo la solicitud y los datos\n2. Preparo memoria y planos\n3. Reviso y entrego';
 process.fields.find(f=>f.id==='tiempo').label='¿Cuánto tiempo te lleva, aproximadamente?';
 const tools=field('tools');tools.rows=[tools.rows[0],tools.rows[1],tools.rows[3],tools.rows[6],tools.rows[7],tools.rows[9],tools.rows[10],tools.rows[11]];tools.label='¿Qué programas utilizas? Solo los que uses habitualmente.';
 const maturity=['mad_estrategia_estrategia','mad_estrategia_indicadores','mad_operaciones_digitalizacion','mad_operaciones_documentacion','mad_datos_organizacion','mad_datos_calidad','mad_tecnologia_sistemas','mad_tecnologia_seguridad','mad_equipo_competencias','mad_equipo_colaboracion'];
 const sections=[
 {id:'actividad',title:'Tu actividad',minutes:3,lead:'Unas referencias para situar tu trabajo. Revisa los datos precargados y corrige lo que haga falta.',fields:[field('contacto_nombre',{label:'Tu nombre'}),field('contacto_email'),field('que_hacen',{help:'Basta con indicar tus servicios principales.'}),field('empleados',{options:['Solo yo','Yo, con colaboradores externos según el encargo','Tengo una pequeña estructura de apoyo']}),field('alcance')]},
 {id:'objetivo',title:'Qué quieres mejorar',minutes:3,lead:'Buscamos una primera mejora práctica: una tarea que podamos simplificar o un bloqueo que merezca resolver primero.',fields:[field('problemas_top',{label:'¿Qué dos o tres tareas te quitan más tiempo?',placeholder:'Por ejemplo: adaptar memorias, buscar antecedentes, preparar ofertas…'}),field('resultado_esperado'),field('exito',{label:'Si empezamos por una sola tarea, ¿cuál te gustaría desbloquear primero?',placeholder:'Elige una tarea concreta y cuéntanos qué resultado te ayudaría en tu día a día.'})]},
 {id:'caso',title:'Un encargo real',minutes:6,lead:'Elige un solo encargo habitual: una legalización, un proyecto o una dirección de obra. Explícalo brevemente; completaremos los detalles contigo.',fields:[process]},
 {id:'archivo',title:'Herramientas y archivos',minutes:4,lead:'Queremos saber con qué trabajas y cómo encuentras o reutilizas la documentación. Deja en blanco los programas que no utilices.',fields:[tools,field('donde_info'),field('fuente_unica',{label:'Cuando necesitas recuperar un proyecto anterior, ¿cómo lo encuentras y qué te cuesta más?'}),field('integraciones',{label:'¿Qué información copias a mano de un programa o documento a otro?'})]},
 {id:'ia_limites',title:'IA y confidencialidad',minutes:3,lead:'Tu experiencia actual y los límites que debemos respetar al trabajar con tus documentos.',fields:[field('uso_ia'),field('herramientas_ia'),field('para_que_ia',{label:'Si has probado IA, ¿para qué y qué resultado te ha dado?',help:'Si todavía no la usas, puedes dejar esta pregunta en blanco.'}),field('nube'),field('datos_prohibidos',{label:'¿Qué información no debemos utilizar en herramientas externas?',help:'Describe el tipo de información; no incluyas documentos ni datos de clientes.'})]},
 {id:'punto_partida',title:'Tu punto de partida',minutes:6,lead:'Diez elecciones rápidas sobre tu forma de trabajar. No es un examen: escoge lo que más se parece a tu práctica actual.',fields:[...maturity.map(id=>field(id,{other:false})),field('preguntas_sesion',{label:'¿Qué duda te gustaría resolver en la sesión?'}),field('disponibilidad',{label:'¿Qué disponibilidad tienes para la primera sesión de trabajo?'})]}
 ];return {...full,sections,journeyVersion:1,estimatedMinutes:25};
}
