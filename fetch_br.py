import urllib.request, json, ssl, time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
BASE = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json&dataInicial={}"

# (chave, codigo, dataInicial, monthly_decimate)
SERIES = [
    ("ipca12",     13522, "01/01/2014", False),
    ("ipcaMes",    433,   "01/01/2014", False),
    ("selic",      432,   "01/01/2018", True),   # diaria (limite 10 anos) -> mensal
    ("dolar",      3698,  "01/01/2014", False),
    ("dividaPib",  13762, "01/01/2014", False),
    ("desemprego", 24369, "01/01/2014", False),
    ("ibcbr",      24364, "01/01/2014", False),
    ("baseMon",    1785,  "01/01/2014", False),
    ("infHist",    190,   "01/01/1989", False),  # IGP-DI: hiperinflacao + Plano Real
]

def fetch(code, di):
    url = BASE.format(code, di)
    err = None
    for _ in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, context=ctx, timeout=90) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            err = e; time.sleep(2)
    raise RuntimeError(f"falhou {code}: {err}")

out = {}
for key, code, di, dec in SERIES:
    data = fetch(code, di)
    labels, vals = [], []
    seen = {}
    for row in data:
        d = row["data"]            # DD/MM/YYYY
        try:
            v = float(row["valor"])
        except (ValueError, TypeError):
            continue
        dd, mm, yy = d.split("/")
        ml = f"{mm}/{yy}"
        if dec:
            seen[ml] = v           # ultimo valor do mes vence
        else:
            labels.append(ml); vals.append(v)
    if dec:
        for ml, v in seen.items():
            labels.append(ml); vals.append(v)
    out[key] = {"labels": labels, "vals": vals, "code": code}
    print(f"{key}: {len(vals)} pontos, ultimo {labels[-1] if labels else '?'}={vals[-1] if vals else '?'}")

with open("dados_br.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
print("OK -> dados_br.json")
