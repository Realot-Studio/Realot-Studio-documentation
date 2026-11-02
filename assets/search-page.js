(function(){
  const input=document.getElementById('doc-search-input'),form=document.getElementById('doc-search-form'),meta=document.getElementById('search-meta'),results=document.getElementById('search-results');
  if(!input||!form||!meta||!results)return;
  const aliases={
    apk:['android','application package','build service','mobile app'],android:['apk','mobile export','build service'],
    project:['realot','save file','load file','archive'],realot:['project','project file','.realot'],
    autosave:['save now','backup','persist','save project'],
    online:['browser','web','hosted','website'],update:['publish','reload','cache','refresh'],
    install:['pwa','progressive web app','add to home screen'],
    movement:['physics','rigidbody','character controller','velocity'],
    follow:['navigation','nav agent','pathfinding','steering'],
    collision:['collider','rigidbody','physics','trigger'],
    enemy:['npc','non-player character','ai','navigation'],
    icon:['favicon','launcher icon'],
    script:['javascript','gameplay code','api','lifecycle']
  };
  const tokenize=s=>(String(s||'').toLowerCase().match(/[a-z0-9_.$+-]{2,}/g)||[]).filter(w=>!['the','and','for','with','from','that','this','what','when','where','your','you','are','can','how','into','use','using','does','not','all','has','have','will','then','than','their','they','them','its','our','was','were','but','or','as','is','a','an','of','to','in','on','by','be'].includes(w));
  function expand(tokens){const out=new Set(tokens);tokens.forEach(t=>(aliases[t]||[]).forEach(a=>tokenize(a).forEach(x=>out.add(x))));return [...out]}
  function editSimilarity(a,b){if(a===b)return 1;if(!a||!b)return 0;if(Math.abs(a.length-b.length)>3)return 0;let prev=Array.from({length:b.length+1},(_,i)=>i);for(let i=1;i<=a.length;i++){let cur=[i];for(let j=1;j<=b.length;j++)cur[j]=Math.min(cur[j-1]+1,prev[j]+1,prev[j-1]+(a[i-1]===b[j-1]?0:1));prev=cur;}return 1-prev[b.length]/Math.max(a.length,b.length)}
  function score(doc,terms,phrase){const title=String(doc.title||doc.t||'').toLowerCase(),desc=String(doc.description||doc.d||'').toLowerCase(),section=String(doc.section||doc.s||'').toLowerCase(),keywords=(doc.keywords||[]).join(' ').toLowerCase(),heads=(doc.headings||[]).join(' ').toLowerCase(),content=String(doc.content||doc.x||'').toLowerCase();let s=0,matched=0;
    if(phrase&&title.includes(phrase))s+=18;if(phrase&&desc.includes(phrase))s+=8;
    terms.forEach(term=>{let weight=0;if(title.split(/[^a-z0-9_.$+-]+/).includes(term))weight=9;else if(title.includes(term))weight=6;else if(keywords.includes(term))weight=5;else if(heads.includes(term))weight=4;else if(desc.includes(term))weight=3;else if(section.includes(term))weight=2;else if(content.includes(term))weight=1;else {const near=(doc.keywords||[]).reduce((m,w)=>Math.max(m,editSimilarity(term,w)),0);if(near>.82)weight=1.5;}if(weight){s+=weight;matched++;}});
    const coverage=terms.length?matched/terms.length:0;s+=coverage*4;if(doc.f)s+=1.5;return s;
  }
  function esc(s){return String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
  function render(items,terms){if(!items.length){results.innerHTML='<div class="search-empty">No close matches yet. Try a broader phrase, a component name, or a related term. You can also browse the <a href="docs/index.html">documentation index</a>.</div>';return;}
    results.innerHTML=items.map(({doc,rank})=>{const title=doc.title||doc.t,description=doc.description||doc.d,url=doc.url||doc.u,content=doc.content||doc.x||'';let snippet=description||content.slice(0,220);let pos=-1;for(const t of terms){const i=content.toLowerCase().indexOf(t);if(i>=0&&(pos<0||i<pos))pos=i;}if(pos>=0)snippet='…'+content.slice(Math.max(0,pos-95),Math.min(content.length,pos+210))+'…';return '<article class="search-result"><div class="result-section">'+esc(doc.section||doc.s||'Documentation')+'</div><h2><a href="'+esc(url)+'">'+esc(title)+'</a></h2><p>'+esc(snippet)+'</p><div class="result-match">Related match · '+Math.round(rank)+' relevance points</div></article>';}).join('');}
  let records=[];fetch('search-index.json').then(r=>{if(!r.ok)throw Error('index unavailable');return r.json()}).then(j=>{records=j;run();}).catch(()=>{meta.textContent='The search index could not be loaded. Open the documentation index or the AI retrieval guide instead.';});
  let requestNumber=0;
  function run(){
    const q=input.value.trim(),raw=tokenize(q),terms=expand(raw),phrase=q.toLowerCase();
    if(!q){meta.textContent=records.length+' pages are ready to search. Enter a topic, API name or description of the task.';results.innerHTML='';return;}
    const current=++requestNumber;
    const endpoint=new URL('api/search',new URL(document.documentElement.dataset.root||'./',location.href));
    endpoint.searchParams.set('q',q); endpoint.searchParams.set('limit','12');
    fetch(endpoint.toString(),{headers:{Accept:'application/json'}}).then(r=>{if(!r.ok)throw Error('search endpoint unavailable');return r.json();}).then(data=>{
      if(current!==requestNumber)return;
      const ranked=(data.results||[]).map(item=>({doc:{title:item.title,description:item.description,section:item.section,url:item.url,content:item.snippet},rank:item.score||0}));
      meta.textContent=ranked.length+' closest matches for “'+q+'”';render(ranked,terms);
    }).catch(()=>{
      if(current!==requestNumber)return;
      const ranked=records.map(doc=>({doc,rank:score(doc,terms,phrase)})).filter(x=>x.rank>0).sort((a,b)=>b.rank-a.rank).slice(0,20);
      meta.textContent=ranked.length+' relevant results for “'+q+'” (local index)';render(ranked,terms);
    });
  }
  const q=new URLSearchParams(location.search).get('q')||'';input.value=q;form.addEventListener('submit',e=>{e.preventDefault();history.replaceState(null,'','search.html'+(input.value.trim()?'?q='+encodeURIComponent(input.value.trim()):''));run();});input.addEventListener('input',()=>{if(input.value.trim().length>=2)run();});if(q)setTimeout(run,0);
})();