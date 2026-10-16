import json,subprocess,re,os
P="/home/user/LLC/hf/oneoffer"; SFX="/home/user/LLC/hf/edit30/sfx3"
SRC="/home/user/LLC/footage2/oneoffer_source_464x832.mp4"
words=json.load(open("/home/user/LLC/plan2/words_oneoffer.json"))
END=68.4
W=[[s,e,t] for s,e,t in words if s>=0.1 and e<=END]
W=[w for w in W if not (56.1<=w[0]<58.5)]      # first take of "using a funnel that's already built for you," (he retakes it as "done for you")
iv=[];pe=None
for s,e,t in W:
    a,b=s-.06,e+.12
    if iv and s-pe<=0.40: iv[-1][1]=b
    else: iv.append([a,b])
    pe=e
iv[0][0]=0.0
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
GRADE="scale=1080:1920:flags=lanczos,unsharp=5:5:0.7:5:5:0.0,curves=master='0/0.01 0.15/0.14 0.30/0.285 0.45/0.43 0.55/0.57 0.70/0.72 0.85/0.84 0.95/0.93 1/0.975',colorbalance=bs=0.008:rm=0.006:bm=-0.006:rh=0.004:bh=-0.004,vibrance=intensity=0.06"
if os.environ.get("CUT","1")=="1":
    fc=[];ins=""
    for i,(a,b) in enumerate(iv):
        L=b-a
        fc.append(f"[0:v]trim=start={a:.3f}:end={b:.3f},setpts=PTS-STARTPTS,fps=30[v{i}]")
        fc.append(f"[0:a]atrim=start={a:.3f}:end={b:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.015,afade=t=out:st={L-0.015:.3f}:d=0.015[a{i}]")
        ins+=f"[v{i}][a{i}]"
    fc.append(f"{ins}concat=n={len(iv)}:v=1:a=1[v0][a]"); fc.append(f"[v0]{GRADE}[v]")
    os.makedirs(P+"/assets",exist_ok=True)
    subprocess.run(["ffmpeg","-v","error","-y","-i",SRC,"-filter_complex",";".join(fc),"-map","[v]","-map","[a]","-c:v","libx264","-crf","16","-preset","medium","-g","30","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","-ar","48000",P+"/assets/aroll.mp4"],check=True)
wd={"S1":(3.95,5.55),"S2":(5.58,8.95),"S3":(9.0,16.1),"S4":(16.4,22.9),"PL":(22.95,28.2),"S5":(28.5,35.9),"S6":(36.1,41.5),"S7":(41.8,48.9),"S8":(52.4,63.2),"S9":(63.3,68.4)}
win={k:[round(mp(a),3),round(mp(b),3)] for k,(a,b) in wd.items()}
kin={
 "s1":{"w":[T("trading",3.9),T("your",4.3),T("time",4.6),T("for",4.8),T("money",5.0)]},
 "s2":{"w":[T("legitimate",6.5),T("way",6.9),T("to",7.4),T("make",7.8),T("money",8.1),T("remotely",8.4)]},
 "s3":{"r":[T("without",8.9),T("without",10.5),T("without",12.9)],"i":[T("12",9.3),T("thousands",11.3),T("months",13.5)]},
 "s4":{"w":[T("why",16.8),T("the",17.2),T("one",17.6),T("offer",17.9),T("model",18.2)],"best":T("best",19.5),"six":T("six",21.5)},
 "pl":{"p":T("biggest",24.7)},
 "s5":{"a":[T("for",28.4),T("the",29.1),T("first",29.2),T("time",29.5)],"b":[T("run",30.4),T("a",30.6),T("business",30.7),T("online",30.9)],"c":[T("without",31.5),T("needing",32.1),T("an",34.4),T("expert",34.6)],"m0":T("without",31.5),"m1":T("anything",35.2)},
 "s6":{"h":[T("you",36.0),T("don't",36.1),T("need",36.4)],"t":[T("code",36.6),T("websites",38.0),T("experience",40.5)]},
 "s7":{"r":[T("funnel",41.8),T("tracking",42.6),T("ads",43.4)],"built":T("already",45.0),"h":[T("you",46.2),T("just",46.4),T("need",46.55),T("to",46.7),T("run",47.4),T("it",47.6),T("the",47.75),T("right",47.9),T("way",48.2)]},
 "s8":{"a":T("proven",53.2),"sub":T("people",54.4),"plus":T("using",60.6),"b":T("funnel",61.2),"eq":T("done",62.1),"c":T("you",62.7)},
 "s9":{"l":[[T("no",63.7),T("pages",64.2)],[T("no",65.3),T("emails",65.5)],[T("no",66.8),T("hunting",67.0)]],"s":[[T("to",64.5),T("build",64.7)],[T("to",65.8),T("write",66.0)],[T("for",67.4),T("offers",67.8)]]}}
modes=[["full",0,""],["fs",win["S1"][0],"major"],["split",win["S2"][0],"minor"],["fs",win["S4"][0],"minor"],["full",round(win["S4"][1]-.05,3),"major"],["fs",win["S5"][0],"major"],["split",win["S6"][0],"minor"],["full",round(win["S7"][1]-.05,3),"major"],["split",win["S8"][0],"major"]]
segs=[[round(c0,3),round(c0+(b-a),3)] for (a,b),c0 in zip(iv,cum)]
k=kin
cues=[]
for m,Tt,kind in modes[1:]:
    if kind=="major": cues.append(("swoosh3",Tt-.30,.6))
cues+=[("camera4",modes[1][1]-.05,1.0),("camera4",modes[5][1]-.05,.8),("riser",modes[1][1]-1.58,.7)]
cues+=[("deep",k["s1"]["w"][4],.9),("boom",k["s1"]["w"][4],.5),("deep",k["s4"]["w"][4],1.0),("impact",k["s4"]["w"][4],.8),("boom",k["s4"]["w"][4],.8),
 ("relief",k["s5"]["m1"],.4),("ding",k["s5"]["m1"]+.15,.5),("click",k["s7"]["built"],.7),("applepay",k["s8"]["c"]-.02,.55)]
ins=[];flt="";lab=""
for i,(nm,t,v) in enumerate(cues):
    ins+=["-i",f"{SFX}/{nm}.wav"];ms=int(max(0,t)*1000);flt+=f"[{i}:a]volume={v},adelay={ms}|{ms}[c{i}];";lab+=f"[c{i}]"
subprocess.run(["ffmpeg","-v","error","-y",*ins,"-filter_complex",flt+lab+f"amix=inputs={len(cues)}:normalize=0,alimiter=limit=0.9,apad,atrim=0:{D:.2f}","-ar","48000",P+"/assets/sfx.wav"],check=True)
cfg={"D":round(D,3),"win":win,"kin":kin,"modes":modes,"segs":segs}
html=open(P+"/template.tpl").read().replace("@@CFG@@",json.dumps(cfg)).replace("@@D@@",f"{D:.3f}")
for g,(a,b) in win.items(): html=html.replace(f"@@{g}a@@",str(a)).replace(f"@@{g}d@@",f"{b-a:.3f}")
open(P+"/index.html","w").write(html)
print("D",round(D,2),"segs",len(iv),"cues",len(cues));print(win);print([m[:2] for m in modes])
