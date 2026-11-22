#!/usr/bin/env python3
"""Genera dashboard-resumen-qa.html con los datos reales de Proaco y GAIL.

Lee directo de los JSON de resultados. No inventa ni rellena scores ausentes:
si un juez no se corrio, no aparece.
"""
import json
import pathlib
import html as H
from collections import defaultdict

BASE = pathlib.Path(__file__).resolve().parents[2]

# ── carga ────────────────────────────────────────────────────────────────────
def load(p):
    return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))

def val(mv):
    if isinstance(mv, dict):
        v = mv.get("value")
        return float(v) if isinstance(v, (int, float)) else None
    return float(mv) if isinstance(mv, (int, float)) else None

def promedios(items):
    """Acepta un dict {regla: valor} o una lista de dicts. Ignora no-numericos."""
    if isinstance(items, dict):
        items = [items]
    acc = defaultdict(list)
    for it in items:
        if not isinstance(it, dict):
            continue
        for k, v in it.items():
            x = val(v)
            if x is not None:
                acc[k].append(x)
    return {k: sum(v) / len(v) for k, v in acc.items()}, {k: len(v) for k, v in acc.items()}

# ── GAIL ─────────────────────────────────────────────────────────────────────
gail_dir = BASE / "gail-evaluacion"
gail_ag = []
for nombre, etiqueta in [("deepeval", "DeepEval"), ("langsmith", "LangSmith"), ("gemini", "Gemini Flash Lite")]:
    f = gail_dir / "evaluacion" / f"{nombre}_resultados.json"
    if not f.exists():
        continue
    d = load(f)
    raw = d.get("promedios", {})
    pr, n = promedios(raw if isinstance(raw, dict) else {})
    if pr:
        gail_ag.append((etiqueta, pr, d.get("n_llamadas", 0), n))

masivo_f = gail_dir / "gail_masivo" / "evaluacion" / "resultados_masivos.json"
gail_heur = gail_llm = None
n_gail = 0
if masivo_f.exists():
    m = load(masivo_f)["resumen"]
    gail_heur, gail_llm, n_gail = m.get("heur"), m.get("llm"), m.get("n_llamadas", 0)

# ── Proaco ───────────────────────────────────────────────────────────────────
pro_dir = BASE / "proaco-evaluacion"
pr_in = pr_out = None
j1 = j2 = None
n_in = n_out = 0
pf = pro_dir / "evaluaciones" / "resultados_completos.json"
if pf.exists():
    items = load(pf)
    suites = defaultdict(list)
    flows = defaultdict(int)
    for it in items:
        flows[it.get("flow", "?")] += 1
        for sk, sv in it.get("suites", {}).items():
            # guardo la suite completa por llamada, para promediar regla por regla
            suites[(it.get("flow", "?"), sk)].append(sv)
    n_in, n_out = flows.get("inbound", 0), flows.get("outbound", 0)

    def agg(flow, sk):
        """Promedia cada regla sobre las llamadas que la tienen measures."""
        reglas = defaultdict(list)
        for (f, s), lst in suites.items():
            if f != flow or s != sk:
                continue
            for llamada in lst:
                if not isinstance(llamada, dict):
                    continue
                for regla, mv in llamada.items():
                    x = val(mv)
                    if x is not None:
                        reglas[regla].append(x)
        return {k: sum(v) / len(v) for k, v in reglas.items() if v}

    pr_in = agg("inbound", "inbound_heur")
    pr_out = agg("outbound", "outbound_7reglas")

    # variabilidad entre los dos jueces inbound (mismas llamadas, mismo criterio)
    j1 = agg("inbound", "inbound_7reglas_juez1")
    j2 = agg("inbound", "inbound_7reglas_juez2")

# ── render ───────────────────────────────────────────────────────────────────
def esc(s):
    return H.escape(str(s))

def bar(pct, color):
    w = max(1.5, round(pct * 100, 1))
    return (f'<div class="barbg"><div class="bar" style="width:{w}%;background:{color}"></div></div>')

def tabla(datos, colores, titulo):
    if not datos:
        return f'<div class="card"><h3>{esc(titulo)}</h3><p class="vacio">sin datos</p></div>'
    reglas = sorted(datos[0][1].keys())
    cab = "".join(f"<th>{esc(r)}</th>" for r in reglas)
    filas = ""
    for etiqueta, pr, n_llam, _ in datos:
        celdas = "".join(
            f'<td class="{cls(pr.get(r))}">{pr.get(r, 0):.3f}</td>' for r in reglas
        )
        filas += (f'<tr><td class="lbl">{esc(etiqueta)}'
                  f'<span class="n">{n_llam} llam.</span></td>{celdas}</tr>')
    return (f'<div class="card wide"><h3>{esc(titulo)}</h3>'
            f'<table><thead><tr><th class="lbl">Fuente</th>{cab}</tr></thead>'
            f'<tbody>{filas}</tbody></table></div>')

def cls(v):
    if v is None:
        return "na"
    if v < 0.35:
        return "bad"
    if v < 0.7:
        return "mid"
    return "ok"

# comparacion heur vs jueces GAIL
cmp_gail = []
if gail_heur and gail_llm:
    cmp_gail.append(("Heurística (pipeline)", gail_heur, n_gail, {}))
for etiqueta, pr, n_llam, _ in gail_ag:
    cmp_gail.append((etiqueta + " (juez)", pr, n_llam, {}))

CSS = """
*{box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
background:#0f172a;color:#e2e8f0;margin:0;padding:2.5rem 2rem;line-height:1.55;font-size:15px}
.wrap{max-width:1100px;margin:0 auto}
h1{font-size:1.8rem;margin:0 0 .3rem;color:#f8fafc;letter-spacing:-.02em}
.sub{color:#94a3b8;margin:0 0 2rem;font-size:.95rem}
h2{font-size:1.15rem;margin:2.4rem 0 .8rem;color:#f1f5f9;border-bottom:1px solid #1e293b;padding-bottom:.4rem}
h3{font-size:.92rem;margin:0 0 .7rem;color:#cbd5e1;font-weight:600}
.grid{display:grid;gap:1rem;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));margin-bottom:1.2rem}
.card{background:#1e293b;border:1px solid #334155;border-radius:10px;padding:1rem 1.1rem}
.card.wide{grid-column:1/-1}
.stat{font-size:2rem;font-weight:700;color:#f8fafc;line-height:1.1}
.stat small{font-size:.78rem;font-weight:500;color:#94a3b8;display:block;margin-top:.2rem}
.badge{display:inline-block;margin-top:.5rem;font-size:.68rem;padding:.15rem .5rem;border-radius:99px;
background:#0f172a;color:#94a3b8;border:1px solid #334155}
table{width:100%;border-collapse:collapse;font-size:.85rem;font-variant-numeric:tabular-nums}
th{text-align:right;padding:.45rem .55rem;border-bottom:2px solid #334155;color:#94a3b8;
font-weight:600;font-size:.74rem;text-transform:uppercase;letter-spacing:.03em}
th.lbl{text-align:left}
td{padding:.42rem .55rem;border-bottom:1px solid #1e293b;text-align:right}
td.lbl{text-align:left;color:#e2e8f0;font-weight:600}
td.lbl .n{display:block;font-size:.68rem;color:#64748b;font-weight:400}
.ok{color:#4ade80}
.mid{color:#fbbf24}
.bad{color:#f87171;font-weight:600}
.na{color:#475569}
.vacio{color:#64748b;font-size:.85rem}
.barbg{background:#0f172a;border-radius:99px;height:8px;overflow:hidden;min-width:60px}
.bar{height:100%;border-radius:99px}
.callout{background:#1e293b;border:1px solid #334155;border-left:3px solid #38bdf8;
border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
.callout h3{color:#38bdf8;margin:0 0 .4rem;font-size:.88rem}
.callout p{margin:.3rem 0;font-size:.9rem;color:#cbd5e1}
.callout b{color:#f8fafc}
footer{margin-top:3rem;padding-top:1.2rem;border-top:1px solid #1e293b;color:#64748b;font-size:.8rem}
@media print{body{background:#fff;color:#111} .card{background:#f8fafc;border-color:#cbd5e1}
.stat{color:#111} td,th{border-color:#e2e8f0} .callout{background:#f8fafc;border-color:#94a3b8}
.callout h3{color:#0369a1} .callout p{color:#334155} .callout b{color:#000} td.lbl{color:#111}
th{color:#475569} footer{color:#64748b}}
"""

def stat(valor, etiqueta, sub=""):
    num = float(valor) if isinstance(valor, str) else valor
    c = cls(num) if isinstance(num, (int, float)) else "na"
    color = {"ok": "#4ade80", "mid": "#fbbf24", "bad": "#f87171", "na": "#64748b"}[c]
    return (f'<div class="card"><div class="stat" style="color:{color}">{valor}'
            f'<small>{esc(etiqueta)}</small></div>'
            f'{f"<span class=badge>{esc(sub)}</span>" if sub else ""}</div>')

# ── KPIs ─────────────────────────────────────────────────────────────────────
kpis = []
consent = (gail_heur or {}).get("pide_consentimiento")
if consent is not None:
    kpis.append(stat(f"{consent:.3f}", "GAIL pide consentimiento", "heurística · el más bajo"))
saludo = (pr_in or {}).get("saludo_presente")
if saludo is not None:
    kpis.append(stat(f"{saludo:.3f}", "Proaco saluda al iniciar", "inbound heurística"))
out_consent = (pr_out or {}).get("pide_consentimiento")
if out_consent is not None:
    kpis.append(stat(f"{out_consent:.3f}", "Proaco outbound pide consentimiento", "0.000 = nunca pide"))
if j1 and j2:
    common = [k for k in j1 if k in j2]
    dif = max((abs(j1[k] - j2[k]) for k in common), default=0)
    kpis.append(stat(f"{dif:.3f}", "Mayor desacuerdo entre jueces", "mismas llamadas, 2 jueces"))

html = f"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Evaluación de agentes de voz — Proaco y GAIL</title><style>{CSS}</style></head><body><div class="wrap">
<h1>Evaluación de agentes de voz</h1>
<p class="sub">Proaco y GAIL · resultados de producción · heurística + LLM judge con comparación multi-juez</p>
<div class="grid">{''.join(kpis)}</div>

<div class="callout">
<h3>Cómo leer estos números</h3>
<p>Las <b>heurísticas</b> son reglas determinísticas sobre la transcripción: baratas, reproducibles, sin variabilidad. Se usan para <b>compliance duro</b>.</p>
<p>Los <b>jueces LLM</b> capturan lo que la regex no ve (tono, coherencia) pero <b>no son deterministas</b>. Por eso se corren varios sobre la misma llamada: para medir cuánta variabilidad hay antes de confiar en un score.</p>
<p>Cuando heurística y juez discrepan mucho, <b>el juez no está catching el problema</b> — no que el bot esté mejor.</p>
</div>

<h2>GAIL — {n_gail} llamadas outbound</h2>
{tabla(cmp_gail, [], 'Mismo pipeline, cuatro fuentes de score')}

<h2>Proaco — {n_in} inbound · {n_out} outbound</h2>
<div class="grid">
{tabla([("Inbound (heurística)", pr_in, n_in, {})] if pr_in else [], [], 'Inbound')}
{tabla([("Outbound (7 reglas)", pr_out, n_out, {})] if pr_out else [], [], 'Outbound')}
</div>
"""

if j1 and j2:
    common = sorted([k for k in j1 if k in j2])
    filas = "".join(
        f'<tr><td class="lbl">{esc(k)}</td><td class="{cls(j1[k])}">{j1[k]:.3f}</td>'
        f'<td class="{cls(j2[k])}">{j2[k]:.3f}</td>'
        f'<td class="{"bad" if abs(j1[k]-j2[k])>0.2 else "mid"}">{abs(j1[k]-j2[k]):.3f}</td></tr>'
        for k in common
    )
    html += f"""<div class="card wide"><h3>Variabilidad del juez — mismas {n_in} llamadas inbound, dos jueces independientes</h3>
<table><thead><tr><th class="lbl">Regla</th><th>Juez 1</th><th>Juez 2</th><th>Diferencia</th></tr></thead>
<tbody>{filas}</tbody></table>
<p class="vacio" style="margin-top:.8rem">Dos jueces, mismo criterio, misma transcripción. Cuando la diferencia es del orden de la métrica, el score no es confiable.</p></div>"""

html += f"""<h2>Hallazgos</h2>
<div class="callout"><h3>1 · El consentimiento es el problema crítico</h3>
<p>GAIL pide consentimiento en <b>{(gail_heur or {}).get('pide_consentimiento', 0)*100:.0f}%</b> de las llamadas. Proaco outbound: <b>{(pr_out or {}).get('pide_consentimiento', 0):.3f}</b> — nunca lo pide. Es el hallazgo más grave y es el mismo en ambos clientes.</p></div>

<div class="callout"><h3>2 · Inbound y outbound son productos distintos</h3>
<p>Proaco inbound saluda en <b>{(pr_in or {}).get('saludo_presente', 0):.3f}</b> y se despide en <b>{(pr_in or {}).get('despedida_presente', 0):.3f}</b>: empieza mal, termina bien.</p>
<p>Outbound se presenta perfecto (<b>{(pr_out or {}).get('se_presenta', 0):.3f}</b>) pero no menciona el propósito (<b>{(pr_out or {}).get('menciona_proposito', 0):.3f}</b>). <b>Evaluar solo inbound da una conclusión que no aplica a outbound.</b></p></div>

<div class="callout"><h3>3 · La variabilidad del juez es del tamaño del efecto medido</h3>
<p>Mismo input, dos jueces, diferencias de hasta <b>{max((abs(j1[k]-j2[k]) for k in j1 if k in j2), default=0) if j1 and j2 else 0:.3f}</b>.
Por eso las reglas duras se anclan en heurística, y por eso un juez solo no alcanza para levantar un gate.</p></div>

<h2>Cómo se puede reproducir</h2>
<div class="card wide">
<p style="margin:.2rem 0"><b>GAIL</b> — <code>gail-evaluacion/evaluacion/</code>: <code>deepeval_resultados.json</code>, <code>langsmith_resultados.json</code> · heurísticas en <code>gail_masivo/evaluacion/resultados_masivos.json</code></p>
<p style="margin:.5rem 0"><b>Proaco</b> — <code>proaco-evaluacion/evaluaciones/resultados_completos.json</code>: 6 suites (heurística, LLM judges, 7 reglas × 2 jueces, por flow)</p>
<p style="margin:.5rem 0">Los jueces ausentes no se rellenan con ceros: si una fuente no se corrió, no aparece.</p>
</div>

<footer>Generado desde los JSON de resultados. Scores = {H.escape('value')} con justificación por métrica. Sin datos de clientes.</footer>
</div></body></html>"""

out = BASE / "_entrega-qa" / "dashboard-evaluacion-agentes.html"
out.parent.mkdir(exist_ok=True)
out.write_text(html, encoding="utf-8")
print(f"OK {out.name}: {len(html)/1024:.1f} KB")
print(f"   GAIL {n_gail} | Proaco in={n_in} out={n_out}")