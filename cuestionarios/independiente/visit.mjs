// Only page, random session reference and time are recorded; no form values.
let sent=false;
function recordOpening(){try{
 const url=new URL(location.href);
 if(url.searchParams.get('wtg_internal')==='1')sessionStorage.setItem('wtg-discovery-internal','1');
 if(sent||sessionStorage.getItem('wtg-discovery-internal')==='1'||document.visibilityState!=='visible')return;
 let id=sessionStorage.getItem('wtg-discovery-visit');
 if(!id){id=crypto.randomUUID();sessionStorage.setItem('wtg-discovery-visit',id);}
 const page=location.pathname.startsWith('/cuestionario')?'questionnaire':'proposal';sent=true;
 fetch('/api/service?op=open',{method:'POST',credentials:'same-origin',headers:{'Content-Type':'application/json'},body:JSON.stringify({id,page}),keepalive:true}).catch(()=>{});
}catch{/* Measurement never blocks the page or questionnaire. */}}
recordOpening();document.addEventListener('visibilitychange',recordOpening);
