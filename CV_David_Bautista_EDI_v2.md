# David Bautista — Principal AI Engineer / Model Evaluation Engineer (EDI)

**📍** Buenos Aires, Argentina (GMT-3) · **✉️** david899b@gmail.com · **📱** +54 9 11 3684-8807  
**🔗** [linkedin.com/in/david-bautista9](https://linkedin.com/in/david-bautista9) · [github.com/David899b](https://github.com/David899b) · [github.com/DavidLABIA](https://github.com/DavidLABIA) · [auto-eval-platform](https://github.com/David899b/auto-eval-platform)

---

## 🎯 Professional Summary

**Principal AI Engineer • Auto-Evaluation Platforms • Model Evaluation Engineer (EDI)**  
*Construyo infraestructura de evaluación que deja de ser un cuello de botella.*

Diseño **plataformas de auto-evaluación** (`auto-eval-platform`) donde **agentes** generan golden sets, red-teamean nightly, sintetizan gates, detectan drift y convierten regulaciones en test suites ejecutables. Los equipos despliegan via API, obtienen go/no-go medibles, y yo me voy.

También trabajo como **Fractional EDI (Model Evaluation Engineer)** para equipos que necesitan evaluación *ya*: golden sets curados (kappa ≥ 0.8), harness en CI/CD, gates 3-escenarios, drift monitoring, compliance. Async-first, 20–30h/sem.

**Cero reuniones por diseño.** Entregas via PR + dashboard + runbook. Sync = 0–1/mes. GMT-3.

---

## 🤖 Two Tracks, Same Excellence

| Track | Title | Client | Price | Deliverable | Meetings |
|-------|-------|--------|-------|-------------|----------|
| **A — Fractional EDI** | Model Evaluation Engineer | Teams shipping LLM features *now* | $200–300/h · $12k/mo | Golden sets, harness, gates, dashboard, compliance | 1 async video/week |
| **B — Platform Deploy** | Principal AI Engineer — Auto-Eval Platforms | CTOs/VP Eng who want eval solved forever | $50k project + $8k/mo | Platform deployed, 5 agents running, handoff to 1 person | 0–1/month (arch only) |

**Track A paga las cuentas. Track B escala.** Upgrade path natural: Track A → "automatizamos más" → Track B.

---

## 🛠️ Technical Stack (Agent-Native)

| Layer | Technologies |
|-------|--------------|
| **Agents** | Golden Set Agent, Red Team Agent, Gate Synthesis Agent, Drift Agent, Compliance Agent |
| **Eval Core** | Instructor/Pydantic (schema enforcement), Judge/Coherence 2nd-pass, Bootstrap CI (3 scenarios) |
| **MLOps** | MLflow, Evidently, pytest, GitHub Actions/GitLab CI, DVC, Shadow/Canary deployments |
| **LLM Infra** | vLLM/Ollama, FastAPI, LangGraph, Cookiecutter templates, Self-hosted (Qwen, Llama, etc.) |
| **Data & Stats** | Bootstrap CI, Power Analysis, Cohen's Kappa, PSI/KL Drift Detection, Cost-sensitive Gates |
| **Compliance** | Ley 25.326, GDPR, EU AI Act, DPA/SCC, PII Minimization, Audit Trails |
| **Cloud & Ops** | Kubernetes, Docker, AWS/GCP, GitOps, Self-hosted LLMs, VPN |

---

## 💼 Experience

### **Concentrix / labIA** — *Principal AI Engineer (EDI)* | Jan 2026 – Present
*Building auto-evaluation infrastructure for MultiOCR/iX Hello (enterprise document understanding SaaS)*

- **Architected `auto-eval-platform`**: 5 agents (Golden Set, Red Team, Gate Synthesis, Drift, Compliance) + FastAPI + Streamlit dashboard + Cookiecutter templates
- **Established "nobody validates what they produce" protocol**: EDI delivers model+metrics+frozen test; AF/RDB/ESI validate
- **MultiOCR production baseline**: Field F1 0.971, ANLS 0.984, Schema OK 100%, latency p95 165s, cost $0.0129 — 3-scenario bootstrap
- **Red-teamed iX Hello DPAs**: SA §5.3 training-on-inputs gap → contractual observation; sub-processors aligned to `vnextRuntime` (14 models/5 providers)
- **ZDR verification**: Confirmed non-default (INC000029619478); conditional offering gate (Ops/Commercial)
- **Self-hosted deployment**: Qwen2.5-7B/14B on vLLM, 40% cost reduction vs API, latency p95 < 2s

### **Concentrix (T-Mobile Dinoboots)** — *Senior Data Analyst / Model QA Lead* | Jan 2026 – Present
- Orchestrated dual-stream QA: CV outputs + CloudFactory human annotation (100+ annotators)
- Prevented 20% accuracy degradation via adversarial scenario design
- Reduced pipeline latency 15% bridging Data Engineers ↔ Architects
- Red-teamed guardrails: 12+ adversarial scenarios simulating jailbreak/extraction
- RLHF loops targeting high-variance points → 15% hallucination reduction

### **Relo Metrics** — *Data Operations Quality Analyst* | Jul 2024 – Jan 2026
- 99.5% "Gold Standard" accuracy across multilingual sports media analytics
- Architected multi-tier QA → 22% annotation error reduction in 6 months
- RLHF optimization: feedback loops for high-variance data → 15% hallucination reduction

### **ActiveFence** — *Multilingual Data Specialist (Trust & Safety)* | Dec 2023 – Dec 2024
- Led adversarial red-teaming: 12+ critical vulnerabilities pre-deployment
- Authored "jailbreaking" resistance eval protocols → standard benchmark for ES/EN LLM safety
- Linguistic nuance → data filters: 10% false-positive reduction

### **Stealth Health** — *Mid-Senior Data Annotation & QA Specialist* | Mar 2022 – Jul 2024
- Medical NER (symptoms, medications, patient history) EN/ES
- Multi-tier QA pipeline → 22% error reduction, clinical-grade integrity

---

## 🚀 Key Projects (Portfolio)

| Project | Type | Description | Stack | Link |
|---------|------|-------------|-------|------|
| **auto-eval-platform** | **Platform (Track B)** | 5 agents (Golden Set, Red Team, Gate Synthesis, Drift, Compliance) + FastAPI + Streamlit + Cookiecutter | Python, FastAPI, Streamlit, vLLM, Cookiecutter | [github.com/David899b/auto-eval-platform](https://github.com/David899b/auto-eval-platform) |
| **compliance-engine** | **Platform (Track B)** | Ingesta DPAs/regulaciones → test suites ejecutables + audit trails | Python, Instructor, pytest | [github.com/DavidLABIA/multiocr-cost-analysis](https://github.com/DavidLABIA/multiocr-cost-analysis) |
| **eval-template-library** | **Platform (Track B)** | Cookiecutter templates: nuevo caso de uso = `cookiecutter eval` (2h) | Cookiecutter, Jinja2, GitHub Actions | [github.com/DavidLABIA/aysa-piloto-labia](https://github.com/DavidLABIA/aysa-piloto-labia) |
| **ai-eval-harness** | **Harness (Track A)** | Golden set manager, Instructor prompts, Judge/Coherence, Bootstrap CI, GitHub Actions gates | Python, pytest, Instructor, MLflow, Evidently | [github.com/David899b/ai-eval-harness](https://github.com/David899b/ai-eval-harness) |
| **MultiOCR Disclaimers v1.2** | **Compliance + Eval** | DPA/SCC analysis, ZDR conditional gating, Legal sign-off, 14 models/5 providers | Markdown, HTML, Chrome headless PDF, pandoc | [github.com/DavidLABIA/multiocr-cost-analysis](https://github.com/DavidLABIA/multiocr-cost-analysis) |

---

## 🎓 Education & Certifications

- **MPsych** — Organizational Psychology, UNEATLANTICO-UNINI (2022)
- **BMus** — Music, UNEARTE Caracas (2017)
- **Google AI Essentials** — Google (2026, in progress)
- **Google Analytics Professional Certificate** — Google (2026, in progress)

---

## 🌐 Languages

- **Spanish** — Native
- **English** — Professional working proficiency (C1)
- **Portuguese** — Working proficiency (B2)

---

## 💡 What You Get

| If you need… | Track A (Fractional EDI) | Track B (Platform Deploy) |
|---|---|---|
| **Ship LLM features without guessing** | Golden sets + harness + gates en 2 semanas | Plataforma self-serve en 4–6 semanas |
| **Compliance-ready AI** | DPA review + PII audit + data cards | Compliance Agent: DPAs → test suites ejecutables |
| **Evaluation that scales** | Harness en CI/CD + drift alerts | Agents corren solos: nightly red-team, hourly drift |
| **Golden sets that don't rot** | Kappa ≥ 0.8, versionados, refresh manual | Golden Set Agent: auto-refresh on drift + kappa tracking |
| **Zero-meeting delivery** | 1 video async/semana | 0–1 sync/mes (solo arquitectura) |

---

## 🤝 Work Preferences

- **Contract / Fractional / Project-based** (20–40h/week)
- **100% remote, async-first** (GMT-3, overlap US/EU mornings)
- **Stack-agnostic**: Me adapto a tu infra; traigo la metodología + agentes
- **No full-time employee roles** — Construyo portfolio de engagements de evaluación

---

> **Portfolio vivo:** `auto-eval-platform` repo — es la señal más clara de cómo trabajo.  
> **Demo vivo:** https://david899b.github.io/auto-eval-portfolio/ (GitHub Pages)  
> **Referencias:** Disponibles on request.