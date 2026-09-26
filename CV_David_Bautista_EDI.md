# David Bautista — Model Evaluation Engineer (EDI) / AI Quality Engineer

**📍** Buenos Aires, Argentina (GMT-3) · **✉️** david899b@gmail.com · **📱** +54 9 11 3684-8807  
**🔗** [linkedin.com/in/david-bautista9](https://linkedin.com/in/david-bautista9) · [github.com/David899b](https://github.com/David899b) · [github.com/DavidLABIA](https://github.com/DavidLABIA)

---

## 🎯 Professional Summary

**Model Evaluation Engineer (EDI — Especialista en Datos e IA)** with 7+ years across the AI lifecycle, specializing in **production-grade evaluation systems**: golden sets, CI/CD harnesses, drift monitoring, adversarial testing, and compliance. 

I build the evaluation infrastructure that lets teams **ship LLM features with measurable confidence** — not vibes. My work sits at the intersection of **QA rigor, statistical methodology, and ML engineering** (the "AI Quality Engineer" convergence identified by kindatechnical, DevOpsSchool, Springer 2024).

**Core differentiator:** I don't just "test models." I design **auditable evaluation pipelines** with frozen test sets, bootstrap confidence intervals, 3-scenario reporting (pessimistic/base/optimistic), and gates that map to business risk. Rule: **"Nobody validates what they produce"** — EDI delivers model + evidence; domain experts validate against ground truth.

---

## 🛠️ Technical Stack

| Category | Tools & Technologies |
|---|---|
| **Evaluation & Quality** | Golden set design (kappa ≥ 0.8), judge/coherence 2nd-pass, bootstrap CIs, behavioral testing, adversarial sets, red-teaming |
| **MLOps & CI/CD** | GitHub Actions, GitLab CI, MLflow, Evidently, pytest, pytest-xdist, DVC, model registry, shadow/canary deployments |
| **LLM Engineering** | Instructor/Pydantic (schema enforcement), vLLM/Ollama, LangChain/LangGraph, RAG evaluation, prompt versioning |
| **Data & Stats** | Python, pandas, numpy, scikit-learn, scipy (bootstrap, power analysis), Cohen's kappa, PSI/KL drift detection |
| **Compliance & Governance** | Ley 25.326 (Argentina), GDPR, EU AI Act prep, PII minimization, DPA/SCC management, audit trails |
| **Cloud & Infra** | AWS (SageMaker, Lambda, S3), GCP (Vertex AI, BigQuery), Docker, Kubernetes basics, VPN/self-hosted LLMs |

---

## 💼 Experience

### **Concentrix / labIA** — *Model Evaluation Engineer (EDI)* | Jan 2026 – Present
*Building evaluation infrastructure for MultiOCR/iX Hello (enterprise document understanding SaaS)*

- **Designed end-to-end evaluation harness** (`ai-eval-harness`): golden set manager (versioned, frozen, SHA-256 audit trail), schema-enforced prompts (Instructor), judge with gray-zone routing, 3-scenario bootstrap reporting, CI/CD gates
- **Established "nobody validates what they produce" protocol**: EDI delivers model + metrics + frozen test; AF (domain) validates golden set/thresholds; RDB (data) validates output format/cross-reference; ESI (infra) validates connector/staging
- **MultiOCR production baseline**: Field F1 0.971, ANLS 0.984, Schema OK 100%, latency p95 165s, cost $0.0129/3 docs — measured over 3-scenario bootstrap
- **Red-teamed iX Hello DPAs**: identified SA §5.3 training-on-inputs gap; documented as contractual observation; aligned sub-processor list to `vnextRuntime` (14 models / 5 providers: OpenAI, Anthropic, Gemini, DeepSeek, Custom)
- **ZDR (Zero Data Retention) verification**: confirmed non-default via ticket INC000029619478; implemented conditional offering gate (Ops/Commercial verification required)
- **Tech**: Python, pytest, vLLM, Instructor, MLflow, Evidently, GitHub Actions, Chrome headless PDF generation, pandoc

### **Concentrix (via T-Mobile Dinoboots)** — *Senior Data Analyst / Model QA Lead* | Jan 2026 – Present
*End-to-end QA lifecycle for Computer Vision + LLM hybrid pipelines*

- **Orchestrated dual-stream QA**: CV model outputs + CloudFactory human annotation (100+ annotators), sync'ing AI/human datasets
- **Prevented 20% accuracy degradation** in beta by catching data ingestion errors via adversarial scenario design
- **Reduced pipeline latency 15%** by bridging Data Engineers ↔ Architects to refine schemas
- **Red-teamed model guardrails**: designed 12+ adversarial scenarios simulating jailbreak/extraction attempts
- **RLHF feedback loops**: engineered targeting of high-variance points → 15% hallucination reduction

### **Relo Metrics** — *Data Operations Quality Analyst* | Jul 2024 – Jan 2026
*Sports media analytics — precision engineering for global brands*

- **Achieved 99.5% "Gold Standard" accuracy** across multilingual sports media analytics, directly impacting client retention
- **Architected multi-tier QA process** reducing annotation error rates 22% in 6 months
- **RLHF optimization**: engineered feedback loops for high-variance data → 15% hallucination reduction

### **ActiveFence** — *Multilingual Data Specialist (Trust & Safety)* | Dec 2023 – Dec 2024
*AI safety / content moderation at scale (English/Spanish/Portuguese)*

- **Led adversarial red-teaming**: designed scenario models simulating AI security bypasses; identified 12+ critical vulnerabilities pre-deployment
- **Authored evaluation protocols** for "jailbreaking" resistance — became standard benchmark for Spanish/English LLM safety assessment
- **Translated linguistic nuances into data filters** → 10% false-positive reduction for high-risk content

### **Stealth Health** — *Mid-Senior Data Annotation & QA Specialist* | Mar 2022 – Jul 2024
*Medical NER (symptoms, medications, patient history) — English/Spanish*

- **Established multi-tier QA pipeline** → 22% annotation error reduction in 6 months, ensuring clinical-grade data integrity
- **High-precision annotation** for Named Entity Recognition across medical domains

### **Appen** — *Data Annotator* | Mar 2018 – Mar 2023
*Text, image, audio, video annotation for AI/NLP model training across multicultural remote teams*

---

## 🚀 Key Projects (Portfolio)

| Project | Description | Stack | Link |
|---|---|---|---|
| **ai-eval-harness** | Production-grade LLM evaluation framework: golden set manager (frozen, auditable), schema-enforced prompts, judge/coherence, 3-scenario bootstrap CI, CI/CD gates, compliance checks | Python, pytest, Instructor, MLflow, Evidently, GitHub Actions | [github.com/David899b/ai-eval-harness](https://github.com/David899b/ai-eval-harness) |
| **MultiOCR Disclaimers v1.2** | Regulatory disclaimers aligned to `vnextRuntime` (14 models/5 providers), DPA/SCC analysis, ZDR conditional gating, Legal sign-off | Markdown, HTML/CSS, Chrome headless PDF, pandoc DOCX | [github.com/DavidLABIA/multiocr-cost-analysis](https://github.com/DavidLABIA/multiocr-cost-analysis) |
| **AySA Email Classification MVP** | 4-week MVP design: golden set (300+ emails, kappa≥0.8), dual-track ESI/EDI, frozen test, 3-scenario reporting, self-hosted Qwen | Python, vLLM, Qwen2.5, Evidently, Streamlit | [github.com/DavidLABIA/aysa-piloto-labia](https://github.com/DavidLABIA/aysa-piloto-labia) |

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

## 💡 What I Bring to Your Team

| If you need… | I deliver… |
|---|---|
| **Ship LLM features without guessing** | Frozen test sets + bootstrap CI + gates → go/no-go with evidence |
| **Compliance-ready AI (Ley 25.326, GDPR, EU AI Act)** | PII-minimized pipelines, DPA/SCC management, audit trails, self-hosted options |
| **Evaluation that scales** | Harness in CI/CD, regression suites, drift alerts (PSI/KL), shadow/canary |
| **Golden sets that don't rot** | Versioned, kappa-calibrated, adversarial, refresh cadence, data cards |
| **Async-first, minimal sync** | Repos + dashboards + runbooks; sync only for kickoff/readout |

---

## 🤝 Work Preferences

- **Contract / Fractional / Project-based** (20–40h/week)
- **100% remote, async-first** (GMT-3, overlap US/EU mornings)
- **Stack-agnostic**: I adapt to your infra; I bring the evaluation methodology
- **No full-time employee roles** — I'm building a portfolio of evaluation engagements

---

> **References & portfolio:** Available on request. Start with the `ai-eval-harness` repo — it's the clearest signal of how I work.