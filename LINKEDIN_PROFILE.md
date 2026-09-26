# LinkedIn Profile — Copy-Paste Ready

## **Headline** (220 chars max)
**Principal AI Engineer • Auto-Evaluation Platforms • Model Evaluation Engineer (EDI) • Zero-Meeting Delivery**

---

## **About** (2600 chars max)

Construyo **infraestructura de auto-evaluación** para que los equipos shippeen LLM features con go/no-go medibles — no vibes.

**Track B — Producto: `auto-eval-platform`**  
5 agents corren solos: Golden Set Agent (genera/curra/versiona sets, kappa≥0.8), Red Team Agent (prompt injection, jailbreak, PII nightly), Gate Synthesis Agent (bootstrap CI → 3 escenarios), Drift Agent (PSI/KL hourly), Compliance Agent (DPAs → test suites ejecutables). Deploy en 4–6 semanas, self-serve via API, handoff a 1 persona, yo me voy.

**Track A — Servicio: Fractional EDI (Model Evaluation Engineer)**  
Para equipos que necesitan evaluación *ya*: golden sets curados (kappa≥0.8, SHA-256 freeze), harness en CI/CD (pytest + Instructor + bootstrap CI), gates 3-escenarios (pesimista/base/optimista), drift monitoring (PSI/KL), compliance (Ley 25.326, GDPR, EU AI Act). Async-first, 20–30h/sem, 1 video async/semana.

**Prueba reciente:** MultiOCR (Concentrix/labIA) — Field F1 0.971, ANLS 0.984, Schema OK 100%, ZDR verificado, DPA alineado a `vnextRuntime` (14 modelos/5 proveedores). AySA MVP: 4 semanas, golden set 300+ (kappa≥0.8), self-hosted Qwen2.5, frozen test.

**Stack:** Python, Agents (LangGraph), vLLM/Ollama, FastAPI, Streamlit, Instructor/Pydantic, MLflow, Evidently, pytest, GitHub Actions, Kubernetes, Cookiecutter.

**Filosofía:** "Nadie valida lo que produce." EDI entrega modelo + evidencia + test congelado; dominio valida contra ground truth. Async-first, minimal sync: entregas via PR + dashboard + runbook. Async-first, sync only when needed. GMT-3.

**Tracks:**
- **Track A (Fractional EDI):** $12k/mo (20h/sem) — Yo hago la evaluación
- **Track B (Platform Deploy):** $50k proyecto + $8k/mo retainer — Plataforma que corre sola

**Demo:** https://david899b.github.io/auto-eval-portfolio/  
**Repo principal:** https://github.com/David899b/auto-eval-platform

---

## **Experience** (Add/Update)

### **Concentrix / labIA** — *Principal AI Engineer (EDI)* | Jan 2026 – Present
*Auto-evaluation infrastructure for MultiOCR/iX Hello*

- Architected **`auto-eval-platform`**: 5 agents (Golden Set, Red Team, Gate Synthesis, Drift, Compliance) + FastAPI + Streamlit + Cookiecutter templates
- Established **"nobody validates what they produce"** protocol: EDI delivers model+metrics+frozen test; domain experts validate
- **MultiOCR baseline**: Field F1 0.971, ANLS 0.984, Schema OK 100%, latency p95 165s — 3-scenario bootstrap
- Red-teamed iX Hello DPAs: SA §5.3 gap documented; sub-processors aligned to `vnextRuntime` (14 models/5 providers)
- ZDR verified non-default (INC000029619478); conditional offering gate
- Self-hosted Qwen2.5-7B/14B on vLLM: 40% cost reduction, latency p95 < 2s

### **Concentrix (T-Mobile Dinoboots)** — *Senior Data Analyst / Model QA Lead* | Jan 2026 – Present
- Dual-stream QA: CV outputs + CloudFactory (100+ annotators), sync AI/human datasets
- Prevented 20% accuracy degradation via adversarial scenario design
- Reduced pipeline latency 15% bridging Data Engineers ↔ Architects
- Red-teamed guardrails: 12+ adversarial scenarios (jailbreak/extraction)
- RLHF loops → 15% hallucination reduction

### **Relo Metrics** — *Data Operations Quality Analyst* | Jul 2024 – Jan 2026
- 99.5% "Gold Standard" accuracy across multilingual sports media analytics
- Multi-tier QA → 22% annotation error reduction in 6 months
- RLHF optimization → 15% hallucination reduction

### **ActiveFence** — *Multilingual Data Specialist (Trust & Safety)* | Dec 2023 – Dec 2024
- Adversarial red-teaming: 12+ critical vulnerabilities pre-deployment
- Authored "jailbreaking" eval protocols → standard benchmark for ES/EN LLM safety
- Linguistic nuance → data filters: 10% false-positive reduction

---

## **Skills** (Top 20 — Pin these)

`AI Platform Engineering` `LLM Evaluation Infrastructure` `Agentic Workflows` `Golden Set Automation` `Red Teaming Automation` `GitOps` `Kubernetes` `vLLM` `LangGraph` `Zero-Meeting Delivery` `Model Evaluation` `Prompt Engineering` `MLOps` `MLflow` `Evidently` `Compliance` `Ley 25.326` `GDPR` `EU AI Act` `Python`

---

## **Featured** (Pin these 6)

1. **auto-eval-platform** — https://github.com/David899b/auto-eval-platform
2. **compliance-engine** — https://github.com/DavidLABIA/multiocr-cost-analysis
3. **eval-template-library** — https://github.com/DavidLABIA/aysa-piloto-labia
4. **ai-eval-harness** — https://github.com/David899b/ai-eval-harness
4. **MultiOCR Disclaimers v1.2** — https://github.com/DavidLABIA/multiocr-cost-analysis
5. **AySA Email Classification MVP** — https://github.com/DavidLABIA/aysa-piloto-labia

---

## **Open to Work** Settings

- **Job titles:** Principal AI Engineer, Model Evaluation Engineer, AI Quality Engineer, Fractional AI Lead
- **Job types:** Contract, Freelance, Part-time
- **Location:** Remote (Argentina, GMT-3)
- **Start date:** Immediately
- **Visibility:** Recruiters only (or All LinkedIn if comfortable)

---

## **Headline Variations** (Test which performs better)

1. `Principal AI Engineer • Auto-Evaluation Platforms • Model Evaluation Engineer (EDI) • Zero-Meeting`
2. `Principal AI Engineer • Auto-Eval Platforms • Golden-Set-as-a-Service • Fractional EDI • Async-First`
3. `Model Evaluation Engineer (EDI) • Auto-Evaluation Platforms • Zero-Meeting • Fractional/Contract`

---

## **Post Ideas** (1/week for 8 weeks)

| Week | Topic | Format |
|------|-------|--------|
| 1 | "Why Your LLM Feature Needs a Frozen Test Set (Not Just Unit Tests)" | Article + GitHub gist |
| 2 | "The 3-Scenario Reporting Framework I Use for Every LLM Eval" | Article + bootstrap code |
| 3 | "How I Built a Red Team Agent That Runs Nightly (And Finds Real Holes)" | Article + agent code |
| 4 | "Golden Sets That Don't Rot: Versioning, Kappa, Drift-Triggered Refresh" | Article + agent stub |
| 5 | "Compliance as Code: Turning DPAs into Executable Test Suites" | Article + compliance agent |
| 6 | "The Gate Synthesis Agent: From Bootstrap CI to Cost-Sensitive Thresholds" | Article + gate synthesis |
| 7 | "Drift Detection That Actually Works: PSI/KL + Auto-Retrain Triggers" | Article + drift agent |
| 8 | "Zero-Meeting Delivery: How I Ship Eval Infra Without Calls" | Article + workflow diagram |

---

## **Quick Wins This Week**

- [ ] Update Headline + About (copy from above)
- [ ] Update Experience (copy from above)
- [ ] Pin 6 Featured repos
- [ ] Reorder Skills (top 10 from list above)
- [ ] Set Open to Work → Contract/Freelance/Part-time, Remote, GMT-3
- [ ] Post Week 1 article (Thursday/Friday optimal)
- [ ] Connect with 20 CTOs/VP Eng at Series A AI startups (personalized note)