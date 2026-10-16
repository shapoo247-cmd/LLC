import json,subprocess,re,os
P="/home/user/LLC/hf/edit30"; SFX=P+"/sfx3"
words=json.load(open("/home/user/LLC/plan/words_raw.json"))
W=[[s,e,t] for s,e,t in words if 11.7<=s and e<=58.3]
W=[w for w in W if not (41.3<=w[0]<43.7)]
for w in W:
    if abs(w[0]-42.59)<.02: w[0]=43.65
iv=[];pe=None
for s,e,t in W:
    a,b=s-.06,e+.12
    if iv and s-pe<=0.40: iv[-1][1]=b
    else: iv.append([a,b])
    pe=e
iv[0][0]=11.70
cum=[];c=0
for a,b in iv: cum.append(c);c+=b-a
D=c
def mp(t):
    for (a,b),c0 in zip(iv,cum):
        if t<=b: return c0+max(0,t-a)
    return D
norm=lambda t:re.sub(r"[^\w$']","",t.lower())
def find(txt,after):
    for s,e,t in words:
        if s>=after and norm(t)==txt: return s,e
    raise Exception(txt)
T=lambda w,a:round(mp(find(w,a)[0]),3)
if os.environ.get("CUT","1")=="1":
    fc=[];ins=""
    for i,(a,b) in enumerate(iv):
        L=b-a
        fc.append(f"[0:v]trim=start={a:.3f}:end={b:.3f},setpts=PTS-STARTPTS,fps=30[v{i}]")
        fc.append(f"[0:a]atrim=start={a:.3f}:end={b:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.015,afade=t=out:st={L-0.015:.3f}:d=0.015[a{i}]")
        ins+=f"[v{i}][a{i}]"
    GRADE="curves=master='0/0.012 0.15/0.14 0.30/0.285 0.45/0.425 0.55/0.575 0.70/0.725 0.85/0.84 0.95/0.925 1/0.97',colorbalance=bs=0.01:rm=0.012:bm=-0.012:rh=0.008:bh=-0.008,vibrance=intensity=0.08,eq=saturation=1.0"
    fc.append(f"{ins}concat=n={len(iv)}:v=1:a=1[v0][a]")
    fc.append(f"[v0]{GRADE}[v]")
    os.makedirs(P+"/assets",exist_ok=True)
    subprocess.run(["ffmpeg","-v","error","-y","-i","/home/user/LLC/footage/raw_footage_1.mp4","-filter_complex",";".join(fc),"-map","[v]","-map","[a]","-c:v","libx264","-crf","17","-preset","medium","-g","30","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","-ar","48000",P+"/assets/aroll.mp4"],check=True)
wd={"L1":(13.25,14.62),"L2":(14.7,17.95),"L3":(18.05,19.95),"L4":(22.85,29.85),"CH":(44.2,47.25),
    "L6":(48.25,50.3),"L7":(50.34,53.5),"L8":(53.55,55.9),"L9":(55.9,58.45)}
win={k:[round(mp(a),3),round(mp(b),3)] for k,(a,b) in wd.items()}
mode={"s1":[round(mp(12.1),3),round(mp(29.85),3)],"s2":[round(mp(48.2),3)]}
kin={
 "l1":{"e":[T("taylor",11),T("brands",11),T("advertises",12),T("a",13)],"hero":T("$0",13),"llc":T("llc",13.6)},
 "l2":{"free":T("free",14.5),"btn":T("big",15.5),"click":T("now",17)},
 "l3":{"tech":T("technically",18),"true":T("true",19)},
 "l4":{"h1":[T("by",22.5),T("checkout",23),T("most",24.4),T("closer",25.5),T("to",26)],"h2":[T("200",26.4),T("a",27.2),T("year",27.4)],
       "rows":[T("checkout",23),T("staring",24),T("closer",25.5)],"count":T("closer",25.5),"land":T("bucks",26.8),
       "swap":T("and",27.9),"n1":[T("and",27.9),T("they",28),T("have",28.3)],"n2":[T("no",28.4),T("idea",28.6),T("how",28.8)]},
 "ch":{"a":T("two",44.3),"b":T("clicked",45.5)},
 "l6":{"w":[T("where",48.5),T("that",49),T("price",49.2),T("climbs",49.5)],"bars":T("price",49.2),"tag":round(T("climbs",49.5)+.3,3)},
 "l7":{"t":[T("the",50.1),T("one",50.3),T("setting",50.5),T("to",51.2),T("switch",51.4),T("off",51.5)],"flip":T("switch",51.4)},
 "l8":{"w":[T("is",54),T("actually",54.1),T("worth",54.4),T("it",54.6)]},
 "l9":{"a":[T("a",56.2),T("pile",56.4),T("of",56.6),T("features",56.8)],"b":[T("you'll",57),T("never",57.4),T("touch",57.6)],"tiles":T("pile",56.4),"never":T("never",57.4)}}
kw={"$0":"#30d158","200":"#ff9f0a","two":"#64d2ff"}
caps=[];cur=[]
for s,e,t in W:
    o=mp(s)
    if cur and (o-cur[-1][1]>0.45 or len(cur)>=6): caps.append(cur);cur=[]
    cur.append([t,round(o,3),round(mp(e),3)])
    if re.search(r"[.,?!]$",t): caps.append(cur);cur=[]
if cur: caps.append(cur)
CAPS=[{"t0":c[0][1],"t1":c[-1][2],"w":[[x[0],x[1],kw.get(re.sub(r"[^\w$]","",x[0].lower()),"")] for x in c]} for c in caps]
segs=[[round(c0,3),round(c0+(b-a),3)] for (a,b),c0 in zip(iv,cum)]
k=kin
modes=[["full",0,""],["fs",win["L1"][0],"major"],["split",win["L2"][0],"minor"],["full",round(win["L2"][1]-.05,3),"major"],["fs",win["L4"][0],"major"],["split",round(kin["l4"]["swap"]-.2,3),"minor"],["full",round(win["L4"][1]-.05,3),"major"],["fs",win["L6"][0],"major"],["split",win["L7"][0],"minor"],["fs",win["L9"][0],"minor"]]
# professional, not SFX-heavy: swoosh on the five major cuts only, camera click on just two of them, ONE riser (into the opening $0 reveal)
cues=[]
for m,T,kind in modes[1:]:
    if kind=="major": cues.append(("swoosh3",T-.30,.6))
cues+=[("camera4",modes[1][1]-.05,1.0),("camera4",modes[4][1]-.05,.8)]
cues+=[("riser",kin["l1"]["hero"]-.24-1.58,.7)]
# impacts and resolution
cues+=[("deep",k["l1"]["hero"],1.0),("boom",k["l1"]["hero"],.6),("impact",k["l4"]["land"],.95),("boom",k["l4"]["land"],.9),("relief",k["l7"]["flip"]+.3,.4)]
# one Apple UI sound per key gesture
cues+=[("click",k["l2"]["click"],.85),("applepay",k["l3"]["true"]-.02,.55),("click",k["l7"]["flip"]+.15,.8),("ding",k["l7"]["flip"]+.5,.55)]
ins=[];flt="";lab=""
for i,(nm,t,v) in enumerate(cues):
    ins+=["-i",f"{SFX}/{nm}.wav"];ms=int(max(0,t)*1000);flt+=f"[{i}:a]volume={v},adelay={ms}|{ms}[c{i}];";lab+=f"[c{i}]"
subprocess.run(["ffmpeg","-v","error","-y",*ins,"-filter_complex",flt+lab+f"amix=inputs={len(cues)}:normalize=0,alimiter=limit=0.9,atrim=0:{D:.2f}","-ar","48000",P+"/assets/sfx.wav"],check=True)
cfg={"D":round(D,3),"win":win,"kin":kin,"modes":modes,"segs":segs}
html=open(P+"/template.tpl").read().replace("@@CFG@@",json.dumps(cfg)).replace("@@D@@",f"{D:.3f}")
for g,(a,b) in win.items():
    html=html.replace(f"@@{g}a@@",str(a)).replace(f"@@{g}d@@",f"{b-a:.3f}")
open(P+"/index.html","w").write(html)
print("D",round(D,2),"segs",len(iv),"cues",len(cues));print(win);print(mode)
