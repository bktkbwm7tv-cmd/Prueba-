import json,sys
p,key,out=sys.argv[1:4]
def find(o):
    if isinstance(o,str) and key in o: return o
    if isinstance(o,dict):
        for v in o.values():
            r=find(v)
            if r: return r
    if isinstance(o,list):
        for v in o:
            r=find(v)
            if r: return r
t=None
for line in open(p):
    try: d=json.loads(line)
    except: continue
    r=find(d)
    if r and len(r)>2000: t=r
open(out,'w').write(t); print(len(t))
