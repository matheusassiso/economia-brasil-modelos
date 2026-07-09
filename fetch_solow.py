import urllib.request, json, ssl, time
ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
BASE="https://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json&dataInicial={}"
SER=[("fbcf",22102,"01/01/2010"),("ibcbr",24364,"01/01/2014")]
def fetch(code,di):
    for _ in range(4):
        try:
            req=urllib.request.Request(BASE.format(code,di),headers={"User-Agent":"Mozilla/5.0"})
            with urllib.request.urlopen(req,context=ctx,timeout=90) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            err=e; time.sleep(2)
    raise RuntimeError(f"falhou {code}: {err}")
out={}
for key,code,di in SER:
    d=fetch(code,di); labels=[];vals=[]
    for row in d:
        try: v=float(row["valor"])
        except: continue
        dd,mm,yy=row["data"].split("/"); labels.append(mm+"/"+yy); vals.append(v)
    out[key]={"labels":labels,"vals":vals,"code":code}
    print(f"{key}: {len(vals)} pts, ultimo {labels[-1]}={vals[-1]}")
open("dados_solow.json","w",encoding="utf-8").write(json.dumps(out,ensure_ascii=False,separators=(",",":")))
print("OK")
