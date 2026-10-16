# Engine: working code from the approved edit (extracted from `hf/edit30/template.tpl`)

These are the exact, tested snippets. The full file is the reference implementation: `hf/edit30/template.tpl` (+ `hf/edit30/gen.py` for timing).
Globals used: `tl` (paused GSAP timeline), `C` (config: `C.win` scene windows, `C.kin` per-word anchor times, `C.modes` layout cuts `[mode,T,kind]`, `C.segs`, `C.D`), `W=C.win`, `Kn=C.kin`, `M`.
All times are edit-timeline seconds, mapped from speech word times.

## CSS (core classes, copy as-is)
```css
:root{--g:#a1a1a6;--w:#f5f5f7}
#sbg{position:absolute;inset:0;background:#000;opacity:0;overflow:hidden}
.orb{position:absolute;width:1300px;height:1300px;border-radius:50%;opacity:0}
.o1{background:radial-gradient(circle,rgba(10,132,255,.5),rgba(10,132,255,0) 65%);left:-350px;top:-420px}
.o2{background:radial-gradient(circle,rgba(191,90,242,.42),rgba(191,90,242,0) 65%);left:700px;top:350px}
.o3{background:radial-gradient(circle,rgba(255,159,10,.42),rgba(255,159,10,0) 65%);left:-300px;top:-380px}
.o4{background:radial-gradient(circle,rgba(255,55,95,.36),rgba(255,55,95,0) 65%);left:750px;top:300px}
.o5{background:radial-gradient(circle,rgba(48,209,88,.4),rgba(48,209,88,0) 65%);left:-350px;top:100px}
.o6{background:radial-gradient(circle,rgba(100,210,255,.36),rgba(100,210,255,0) 65%);left:650px;top:-400px}
#cring{position:absolute;left:1130px;top:90px;width:720px;height:900px;border-radius:48px;box-shadow:0 50px 140px rgba(0,0,0,.7),0 0 0 1px rgba(255,255,255,.12);opacity:0}
#vframe{position:absolute;inset:0;clip-path:inset(0px 0px 0px 0px round 0px)}
#vclip{position:absolute;inset:0}
#vz{position:absolute;inset:0;transform-origin:58% 0%}
#vp{position:absolute;inset:0;transform-origin:58% 0%}
#av{position:absolute;left:0;top:0;width:1920px;height:1080px;object-fit:cover}
#shade{position:absolute;inset:0;pointer-events:none;background:linear-gradient(180deg,rgba(0,0,0,.25) 0%,rgba(0,0,0,0) 20%,rgba(0,0,0,0) 62%,rgba(0,0,0,.6) 100%)}
.scene{position:absolute;inset:0}
.ring{position:absolute;width:600px;height:600px;border-radius:50%;border:4px solid #fff;opacity:0;pointer-events:none}
.lz{position:absolute;left:60px;top:90px;width:1010px;height:900px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.lz.fs{left:0;width:1920px}
.ln{display:block;overflow:hidden;padding:4px 12px 12px 12px;text-align:center;white-space:nowrap;line-height:1.04;letter-spacing:-.035em;font-weight:600}
.w{display:inline-block;margin:0 .11em;padding:0 .03em}
.grn{background:linear-gradient(180deg,#8dffb0 0%,#30d158 100%);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:#30d158}
.org{background:linear-gradient(180deg,#ffd60a 0%,#ff453a 100%);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:#ff9f0a}
.wht{background:linear-gradient(180deg,#ffffff 0%,#98989d 100%);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:#d1d1d6}
.dim{color:var(--g)}
.glass{background:rgba(255,255,255,.08);backdrop-filter:blur(50px) saturate(180%);-webkit-backdrop-filter:blur(50px) saturate(180%);border:1px solid rgba(255,255,255,.14);border-top-color:rgba(255,255,255,.3);box-shadow:0 40px 120px rgba(0,0,0,.5),inset 0 1px 0 rgba(255,255,255,.15)}
.hero{display:inline-block;font-weight:700;letter-spacing:-.06em;line-height:.8;font-variant-numeric:tabular-nums;padding:0 .12em 0 .02em}
.pillD{display:flex;align-items:center;gap:18px;padding:18px 34px 18px 22px;border-radius:70px;font-weight:600;font-size:42px;letter-spacing:-.02em;color:#fff;background:rgba(12,12,16,.86);border:1px solid rgba(255,255,255,.22);box-shadow:0 24px 70px rgba(0,0,0,.5)}
.pillD svg{width:56px;height:56px;flex:none}
.chip{font-size:42px}
.chip .n{font-weight:700;font-size:76px;letter-spacing:-.05em;line-height:1;background:linear-gradient(180deg,#9be7ff,#0a84ff);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:#64d2ff;min-width:54px;text-align:center}
#world{position:absolute;inset:0;transform-origin:50% 50%}
#leak{position:absolute;inset:-16%;opacity:0;overflow:hidden;pointer-events:none;mix-blend-mode:screen}
.lk{position:absolute;inset:-20%;will-change:opacity,transform}
.lk-a{background:radial-gradient(ellipse 52% 110% at 10% 58%,rgb(255 241 197/92%),transparent 45%),radial-gradient(ellipse 72% 120% at 24% 54%,rgb(255 126 57/78%),transparent 66%);filter:blur(2.8vmin)}
.lk-r{background:radial-gradient(ellipse 58% 105% at 78% 34%,rgb(255 79 61/72%),rgb(255 44 92/28%) 48%,transparent 76%);filter:blur(4vmin)}
.lk-g{background:linear-gradient(104deg,transparent 24%,rgb(255 144 62/30%) 40%,rgb(255 247 205/72%) 51%,rgb(255 124 48/22%) 62%,transparent 78%);filter:blur(2vmin)}
#lkflash{position:absolute;inset:0;background:#fff3d6;opacity:0;pointer-events:none;mix-blend-mode:screen}
#vig{position:absolute;inset:0;pointer-events:none;background:radial-gradient(ellipse at 50% 50%,transparent 62%,rgba(0,0,0,.35) 100%)}
```

## Helpers: kinetic headline, pop, exits, easing constants
```javascript
const LEAD=.17;
/* damped spring as a GSAP ease (zeta<1 = a touch of overshoot) */
const sp=()=>"power4.out";
const SP="power4.out";

/* build a mask-line headline; words rise on their own onsets (peak lands ON the word) */
function mk(sel,lines,t0){const host=document.querySelector(sel);const els=[];
  lines.forEach(L=>{const ln=document.createElement("div");ln.className="ln";ln.style.fontSize=L.size+"px";
    L.w.forEach(([txt,t])=>{const s=document.createElement("span");s.className="w "+(L.cls||"");s.textContent=txt;ln.appendChild(s);
      const st=Math.max(t0+.02,t-LEAD);
      tl.fromTo(s,{yPercent:118,opacity:0},{yPercent:0,opacity:1,duration:.55,ease:SP},st);
      els.push(s);});
    host.appendChild(ln);});
  return els;}
const outEls=(els,t,stag=.025)=>tl.to(els,{yPercent:-120,opacity:0,duration:.3,ease:"power3.in",stagger:stag},t);
const pop=(sel,t,from={})=>tl.fromTo(sel,{scale:.95,y:26,opacity:0,...from},{scale:1,y:0,opacity:1,duration:.6,ease:SP},t);
const outBlock=(sel,t)=>tl.to(sel,{opacity:0,y:-30,scale:.97,duration:.28,ease:"power3.in"},t);
```

## Layout engine + light-leak transitions + presenter push-in + shockwave ring
```javascript
/* three layouts: full-frame presenter ("full"), full-screen animation ("fs"), both at once ("split").
   Layout changes are hard cuts hidden under a light leak (layered amber/red/gold glow, after the registry block organic-light-leak-overlay). */
const CARD="inset(90px 70px 90px 1130px round 48px)",FULL="inset(0px 0px 0px 0px round 0px)";
const ST={full:{clip:FULL,x:0,y:0,vo:1,bg:0,ring:0,sh:1},split:{clip:CARD,x:330,y:90,vo:1,bg:1,ring:1,sh:0},fs:{clip:CARD,x:330,y:90,vo:0,bg:1,ring:0,sh:0}};
const SPM="power3.inOut";
const modeAt=t=>{let m="full";C.modes.forEach(([mm,tt])=>{if(t>=tt-1e-6)m=mm;});return m;};
const segBase=t=>{let i=0;C.segs.forEach(([a],k)=>{if(t>=a-1e-3)i=k;});return i%2?1.12:1;};
const vzS=(m,t)=>m==="full"?segBase(t):1;
C.modes.forEach(([m,T,kind],i)=>{if(!i)return;const b=ST[m],big=kind==="major",d=i%2?1:-1;
  tl.set("#vframe",{clipPath:b.clip,opacity:b.vo},T);
  tl.set("#vclip",{x:b.x,y:b.y},T);
  tl.set("#vz",{scale:vzS(m,T)},T);
  tl.set("#vp",{scale:1},T);
  tl.set("#sbg",{opacity:b.bg},T);tl.set("#cring",{opacity:b.ring},T);tl.set("#shade",{opacity:b.sh},T);
  /* push-zoom through the cut */
  tl.fromTo("#world",{scale:1},{scale:big?1.07:1.035,duration:big?.3:.2,ease:"power2.in",immediateRender:false},T-(big?.3:.2));
  tl.fromTo("#world",{scale:big?1.07:1.035},{scale:1,duration:.55,ease:"power3.out",immediateRender:false},T);
  /* the leak: builds into the cut, peaks on it, burns off */
  const up=big?.28:.2,peak=big?.82:.55;
  tl.fromTo("#leak",{opacity:0},{opacity:peak,duration:up,ease:"power2.in",immediateRender:false},T-up);
  tl.to("#leak",{opacity:0,duration:big?.62:.45,ease:"power2.out"},T+.03);
  tl.fromTo(".lk-a",{xPercent:-35*d,scale:.9,rotation:-4*d},{xPercent:25*d,scale:1.12,rotation:2*d,duration:.95,ease:"power1.inOut",immediateRender:false},T-.34);
  tl.fromTo(".lk-r",{xPercent:30*d,yPercent:-8,scale:1.08},{xPercent:-22*d,yPercent:8,scale:.94,duration:.95,ease:"power1.inOut",immediateRender:false},T-.34);
  tl.fromTo(".lk-g",{xPercent:-45*d,rotation:-6*d},{xPercent:35*d,rotation:4*d,duration:.95,ease:"power1.inOut",immediateRender:false},T-.34);
  if(big){tl.fromTo("#lkflash",{opacity:0},{opacity:.32,duration:.07,ease:"power2.in",immediateRender:false},T-.06);tl.to("#lkflash",{opacity:0,duration:.3,ease:"power2.out"},T+.01);}
});
/* slow push-in while the presenter is full frame (eases to 1 at the next cut) */
const PUSH=.05;
C.modes.forEach(([m,t0],i)=>{if(m!=="full")return;const e=C.modes[i+1]?C.modes[i+1][0]:C.D;
  tl.fromTo("#vp",{scale:1},{scale:1+PUSH,duration:Math.max(.1,e-t0),ease:"none",immediateRender:false},t0);});
/* alternate punch-in on each jump cut while the presenter is full frame */
C.segs.forEach(([a],i)=>{if(!i)return;
  if(modeAt(a)==="full")tl.set("#vz",{scale:segBase(a)},a);});
/* shockwave ring on the big hits */
const ring=(x,y,col,t,s=2.2)=>{const r=document.createElement("div");r.className="ring";r.style.left=(x-300)+"px";r.style.top=(y-300)+"px";r.style.borderColor=col;document.getElementById("root").appendChild(r);
  tl.fromTo(r,{scale:.25,opacity:.9},{scale:s,opacity:0,duration:1.0,ease:"power3.out",immediateRender:false},t);};
```

## Ambient glow crossfade (static orbs, one pair per scene)
```javascript
/* ambient glow per beat (left zone only; behind the card) */
const orbSets={L1:[1,1,0,0,0,0],L2:[0,0,0,0,1,1],L3:[0,0,0,0,1,1],L4:[0,0,1,1,0,0],L6:[0,0,1,1,0,0],L7:[0,0,0,0,1,1],L8:[1,1,0,0,0,0],L9:[1,1,0,0,0,0]};
Object.keys(orbSets).forEach(id=>{const a=W[id][0];orbSets[id].forEach((v,i)=>tl.to(`.o${i+1}`,{opacity:v,duration:.5,ease:"power2.inOut"},a-.1));});
```

## Example: hero reveal with logo + ring (opening)
```javascript
/* ---------- L1: $0 ---------- */
{const[a,b]=W.L1,k=Kn.l1;
 const e=[];ring(960,540,"#30d158",k.hero);pop("#logo1",a+.03,{y:20});
 const hs=document.querySelectorAll("#l1h .hc");
 tl.fromTo(hs[0],{scale:1.18,y:30,opacity:0,filter:"blur(10px)"},{scale:1,y:0,opacity:1,filter:"blur(0px)",duration:.5,ease:SP},k.hero-LEAD);
 tl.fromTo(hs[1],{scale:1.18,y:30,opacity:0,filter:"blur(10px)"},{scale:1,y:0,opacity:1,filter:"blur(0px)",duration:.5,ease:SP},k.hero-LEAD+.07);
 const l=mk("#l1l",[{size:80,cls:"",w:[["LLC",k.llc],["formation.",k.llc+.08]]}],a);
 outEls([...e,...l],b-.3);outBlock("#logo1",b-.3);tl.to("#l1h",{opacity:0,scale:.94,y:-20,duration:.28,ease:"power3.in"},b-.3);}
```

## Example: cursor click on a button (UI demo)
```javascript
/* ---------- L2: free formation / sign up ---------- */
{const[a,b]=W.L2,k=Kn.l2;
 pop("#win2",a+.02,{y:50,scale:.94});
 const h=mk("#h2",[{size:96,cls:"wht",w:[["Free",k.free],["formation.",k.free+.18]]}],a);
 pop("#btn",k.btn-LEAD,{y:40,scale:.9});
 const tx=(x,y,t,d,e)=>tl.to("#cur",{x,y,duration:d,ease:e||"power3.inOut"},t);
 tl.fromTo("#cur",{x:900,y:800,opacity:0},{x:900,y:800,opacity:1,duration:.2},k.btn-.1);
 tx(544,577,Math.max(a+.3,k.click-.62),.55);
 tl.to("#btn",{scale:.95,duration:.08,ease:"power2.out"},k.click).to("#btn",{scale:1,duration:.3,ease:SP},k.click+.08);
 tl.to("#cur",{scale:.86,duration:.08,transformOrigin:"20% 10%"},k.click).to("#cur",{scale:1,duration:.25,ease:SP},k.click+.08);
 tl.fromTo("#ripple",{scale:1,opacity:.9},{scale:1.28,opacity:0,duration:.55,ease:"power2.out",immediateRender:false},k.click);
 outEls(h,b-.3);outBlock("#win2",b-.3);tl.to("#cur",{opacity:0,duration:.2},b-.3);}
```

## Example: receipt card with live count-up and headline swap
```javascript
/* ---------- L4: checkout ---------- */
{const[a,b]=W.L4,k=Kn.l4;
 const h1=mk("#h4a",[{size:58,cls:"dim",w:[["By",k.h1[0]],["checkout,",k.h1[1]],["it’s",k.h1[2]],["closer",k.h1[3]],["to",k.h1[4]]]},{size:118,cls:"org",w:[["$200",k.h2[0]],["a",k.h2[1]],["year.",k.h2[2]]]}],a);
 pop("#card",a+.1,{y:90,scale:.95});
 [["#r1",k.rows[0]],["#r2",k.rows[1]],["#r3",k.rows[2]]].forEach(([r,t])=>tl.fromTo(r,{opacity:0,y:18},{opacity:1,y:0,duration:.45,ease:SP},t-LEAD));
 const o={v:0};tl.fromTo(o,{v:0},{v:216,duration:k.land-k.count,ease:"power3.out",onUpdate(){document.getElementById("totn").textContent="$"+Math.round(o.v);}},k.count);
 ring(960,730,"#ff9f0a",k.land);
 tl.fromTo("#totn",{scale:1},{scale:1.07,duration:.16,yoyo:true,repeat:1,ease:"power2.out",transformOrigin:"right center",immediateRender:false},k.land-.04);
 tl.fromTo("#lz4",{x:0},{x:-395,duration:.8,ease:SPM},k.swap-.2);
 outEls(h1,k.swap-.45);
 const h2=mk("#h4b",[{size:58,cls:"dim",w:[["and",k.n1[0]],["they",k.n1[1]],["have",k.n1[2]]]},{size:118,cls:"wht",w:[["no",k.n2[0]],["idea",k.n2[1]],["how.",k.n2[2]]]}],a);
 outEls(h2,b-.3);outBlock("#card",b-.3);}
```

## Example: line chart that draws on, accelerating, with a live counter
```javascript
/* ---------- L6: price climbs (line draws on, accelerating; live counter rides the dot) ---------- */
{const[a,b]=W.L6,k=Kn.l6;
 const h=mk("#h6",[{size:62,cls:"dim",w:[["Where",k.w[0]],["the",k.w[1]],["price",k.w[2]]]},{size:128,cls:"org",w:[["climbs.",k.w[3]]]}],a);
 pop("#panel",a+.12,{y:70,scale:.95});
 const ln=document.getElementById("ln"),len=ln.getTotalLength(),dot=document.getElementById("dot"),cpr=document.getElementById("cpr"),lb=document.getElementById("lbl6");
 ln.style.strokeDasharray=len;ln.style.strokeDashoffset=len;
 const mix=(c1,c2,u)=>c1.map((v,i)=>Math.round(v+(c2[i]-v)*u));
 const G=[48,209,88],A=[255,179,64],R=[255,69,58];
 const o={p:0};
 const upd=()=>{const p=o.p,pt=ln.getPointAtLength(len*p);
   ln.style.strokeDashoffset=len*(1-p);dot.setAttribute("cx",pt.x);dot.setAttribute("cy",pt.y);dot.style.opacity=p>0?1:0;cpr.setAttribute("width",pt.x);
   lb.style.opacity=p>0?1:0;lb.style.left="0px";lb.style.top=Math.max(8,pt.y-96)+"px";
   lb.textContent="$"+Math.round(200*p)+(p>.985?" / yr":"");lb.style.left=Math.min(Math.max(120,pt.x-250),1000-lb.offsetWidth)+"px";
   const col=p<.5?mix(G,A,p/.5):mix(A,R,(p-.5)/.5);lb.style.color="rgb("+col.join(",")+")";};
 tl.fromTo(o,{p:0},{p:1,duration:k.tag-(k.bars-.6),ease:"power2.in",onUpdate:upd,immediateRender:false},k.bars-.6);
 tl.fromTo("#dot",{scale:1},{scale:1.9,duration:.22,yoyo:true,repeat:1,ease:"power2.out",transformOrigin:"center",immediateRender:false},k.tag-.05);
 ring(1430,520,"#ff453a",k.tag,1.15);
 tl.fromTo("#lbl6",{scale:1},{scale:1.12,duration:.2,yoyo:true,repeat:1,ease:"power2.out",transformOrigin:"left center",immediateRender:false},k.tag);
 outEls(h,b-.3);outBlock("#panel",b-.3);}
```

## Example: toggle switch flip
```javascript
/* ---------- L7: toggle ---------- */
{const[a,b]=W.L7,k=Kn.l7;
 const h=mk("#h7",[{size:62,cls:"dim",w:[["The",k.t[0]],["one",k.t[1]],["setting",k.t[2]]]},{size:128,cls:"wht",w:[["to",k.t[3]],["switch",k.t[4]],["off.",k.t[5]]]}],a);
 pop("#sw",a+.15,{y:60,scale:.88});pop("#lab",a+.3,{y:20});
 ring(565,560,"#30d158",k.flip+.25);
 tl.to("#kn",{x:-184,duration:.5,ease:"power4.out"},k.flip);
 tl.to("#sw",{backgroundColor:"#39393d",boxShadow:"0 0 0 1px rgba(255,255,255,.1) inset,0 36px 100px rgba(0,0,0,.5)",duration:.35,ease:"power2.out"},k.flip);
 outEls(h,b-.3);outBlock("#sw",b-.3);outBlock("#lab",b-.3);}
```

## Example: list/menu cascade that dims to one highlighted item
```javascript
/* ---------- L9: the whole menu of features nobody uses (full-screen; content from the real site) ---------- */
{const[a,b]=W.L9,k=Kn.l9;
 pop("#logo9",a+.04,{y:16});
 const h=mk("#h9",[{size:60,cls:"dim",w:[["A",k.a[0]],["pile",k.a[1]],["of",k.a[2]],["features",k.a[3]]]},{size:108,cls:"wht",w:[["you’ll",k.b[0]],["never",k.b[1]],["touch.",k.b[2]]]}],a);
 const cols=[...document.querySelectorAll("#cols9 .col")];
 cols.forEach((c,ci)=>{
   tl.fromTo(c,{opacity:0,y:56,scale:.97},{opacity:1,y:0,scale:1,duration:.6,ease:"power4.out"},k.tiles-LEAD+ci*.09);
   c.querySelectorAll(".fr").forEach((r,ri)=>tl.fromTo(r,{opacity:0,x:-16},{opacity:1,x:0,duration:.42,ease:"power3.out"},k.tiles-LEAD+.14+ci*.06+ri*.042));
 });
 /* on "never": everything dims except the one thing she actually came for */
 [...document.querySelectorAll("#cols9 .fr")].forEach((r,i)=>{
   if(r.dataset.keep){tl.to(r,{backgroundColor:"rgba(48,209,88,.20)",color:"#8dffb0",duration:.45,ease:"power2.out"},k.never-LEAD);
     tl.to(r.querySelector(".fi svg"),{color:"#30d158",duration:.45,ease:"power2.out"},k.never-LEAD);return;}
   tl.to(r,{opacity:.26,duration:.5,ease:"power2.out"},k.never-LEAD+(i%10)*.022);});
 tl.fromTo("#cols9",{scale:1},{scale:1.035,duration:b-a,ease:"none",immediateRender:false},a);}
```
