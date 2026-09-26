# Toptal Application & Screening Prep — Model Evaluation Engineer (EDI)

## 🎯 Application Strategy

**Positioning:** "AI Quality Engineer" — the convergence of QA rigor, statistical methodology, and ML engineering (kindatechnical, DevOpsSchool, Springer 2024). Not a generalist ML engineer. Not a QA tester. **Specialist in production-grade LLM evaluation infrastructure.**

**Key differentiators to emphasize:**
1. **Frozen test sets + bootstrap CI** — not just "unit tests for LLMs"
2. **3-scenario reporting** — pessimistic/base/optimistic with statistical rigor
3. **"Nobody validates what they produce"** protocol — EDI delivers, domain experts validate
4. **Compliance-ready** — Ley 25.326, GDPR, EU AI Act, DPA/SCC, PII minimization
5. **Red-teaming with statistical backing** — not just "I tried some prompts"

---

## 📋 Application Form Answers

### **1. Title & Role**
**Desired Role:** AI Quality Engineer / Model Evaluation Engineer / LLM Evaluation Specialist  
**Seniority:** Senior (7+ years AI lifecycle, 2+ years specialized eval infrastructure)

### **2. Top Skills (Select 10–15)**
- LLM Evaluation & Quality Assurance
- Golden Set Design & Management
- Prompt Engineering (Schema-Enforced, Instructor/Pydantic)
- Statistical Evaluation (Bootstrap CI, Power Analysis, Kappa)
- MLOps & CI/CD for ML (GitHub Actions, MLflow, Evidently)
- Adversarial Testing & Red-Teaming (Prompt Injection, Jailbreak)
- Compliance & Governance (GDPR, EU AI Act, Ley 25.326, DPA/SCC)
- Drift Detection & Monitoring (PSI, KL Divergence, Shadow/Canary)
- Python, pytest, Instructor, vLLM/Ollama, MLflow, Evidently
- Shadow/Canary Deployment & A/B Testing

### **3. Hourly Rate Expectation**
**$150–250/hour** (Toptal typical range for Senior ML/AI Quality)
- Open to Toptal's rate guidance
- Fractional retainer preferred ($10–15k/mo for 20–30h/week)

### **4. Availability**
- **20–30 hours/week**
- **GMT-3 (Buenos Aires)** — excellent overlap with US East Coast (9am–1pm) and EU (2pm–6pm)
- **Async-first** — deliverables via repo/PR/dashboard; sync only for kickoff/readout
- **Start date:** 2 weeks from match

### **5. Portfolio Links**
- **ai-eval-harness** (core framework): https://github.com/David899b/ai-eval-harness
- **MultiOCR Disclaimers v1.2** (compliance + eval): https://github.com/DavidLABIA/multiocr-cost-analysis
- **AySA MVP** (4-week eval infra): https://github.com/DavidLABIA/aysa-piloto-labia

### **6. Why Toptal?**
> "I'm building a portfolio of fractional evaluation engagements with serious teams who need production-grade eval infra — not vibes. Toptal's client base (Series A+ startups, enterprise innovation labs) matches exactly who needs this: teams shipping LLM features who can't afford 'it works on my machine' as a release criterion. I want long-term fractional relationships, not one-off gigs."

---

## 🧪 Technical Screening Prep

### **Round 1: Conceptual / Design (30–45 min)**
**Typical questions & my answers:**

#### Q: "How would you evaluate a RAG system for a legal-tech client?"
**A:** 
1. **Golden set first**: 200+ queries × (retrieval + generation) with dual annotation (kappa≥0.8), versioned, SHA-256 frozen
2. **Decomposed metrics**: Retrieval (Recall@k, MRR) + Generation (faithfulness, answer relevance, hallucination rate) + End-to-end (accuracy vs. gold)
3. **Judge/coherence**: 2nd-pass LLM judge for faithfulness + schema enforcement (citations must exist in retrieved chunks)
4. **3-scenario bootstrap**: pessimistic/base/optimistic for each metric
5. **Gates**: Recall@5 ≥ 0.85 (pessimistic), Faithfulness ≥ 0.9 (base), Hallucination ≤ 0.05 (optimistic)
6. **Drift**: PSI on query embeddings weekly; KL on answer distributions
7. **Compliance**: PII detection in retrieved chunks + answers; audit trail per query

#### Q: "What's wrong with using accuracy as the main metric for LLM eval?"
**A:** Accuracy hides failure modes. For classification: need per-class precision/recall + confusion matrix. For generation: accuracy is meaningless — need faithfulness, relevance, hallucination rate, semantic similarity. For extraction: field-level F1 + schema validity. **Single-number metrics create false confidence.** That's why I use 3-scenario bootstrap across multiple metrics + slicing by subgroup (domain, length, language).

#### Q: "How do you prevent overfitting to the test set?"
**A:** **Test set is frozen (SHA-256) and touched ONCE** — at release gate. All tuning (thresholds, prompts, model selection) happens on **validation set only**. Use nested CV for hyperparameter tuning. Test set = release gate only. If test disappoints, you don't retune on test — you go back to validation, change strategy, get a NEW test set (or time-based split). This is the "test set as release gate" philosophy (TheLinuxCode, kindatechnical).

#### Q: "How do you handle evaluation for a multilingual system (EN/ES/PT)?"
**A:** 
- **Golden set per language** (minimum 50 items/lang), annotated by native speakers
- **Kappa per language** + cross-lingual consistency checks
- **Metrics sliced by language** — no aggregate hiding ES failures
- **Language-specific adversarial sets** (ES jailbreaks ≠ EN jailbreaks)
- **Prompt templates per language** with shared schema (Instructor enforces structure)
- **Drift monitoring per language** (separate PSI/KL tracks)

---

### **Round 2: Live Coding / Technical Deep-Dive (60–90 min)**

**Likely task:** "Build a minimal evaluation harness for a classification task."

**My 60-minute plan:**

```python
# 1. Schema (Instructor/Pydantic) — 5 min
class ClassificationOutput(BaseModel):
    label: Literal["spam", "ham", "promo", "transactional"]
    confidence: float = Field(ge=0, le=1)
    reasoning: str

# 2. Golden set loader (JSONL, versioned) — 10 min
class GoldenItem(BaseModel):
    id: str
    input: str
    expected: ClassificationOutput
    split: Literal["train", "val", "test"] = "test"

# 3. Model adapter (abstract, swapable) — 10 min
class ModelAdapter(ABC):
    @abstractmethod
    async def predict(self, text: str) -> ClassificationOutput: ...

# 4. Judge (schema + semantic) — 15 min
class SchemaJudge:
    def __init__(self, threshold: float = 0.85):
        self.threshold = threshold
    
    def evaluate(self, pred: ClassificationOutput, exp: ClassificationOutput) -> tuple[bool, float]:
        # Exact label match
        label_match = pred.label == exp.label
        # Confidence calibration (simplified)
        conf_score = 1 - abs(pred.confidence - exp.confidence)
        return label_match and conf_score >= self.threshold, conf_score

# 5. Bootstrap CI (3 scenarios) — 10 min
def bootstrap_ci(values: list[float], n=1000, alpha=0.05):
    boots = [np.mean(np.random.choice(values, len(values), replace=True)) for _ in range(n)]
    return {
        "pessimistic": np.percentile(boots, alpha/2*100),
        "base": np.median(boots),
        "optimistic": np.percentile(boots, (1-alpha/2)*100)
    }

# 6. Gate evaluation — 10 min
GATES = {
    "accuracy": {"pessimistic": 0.85, "base": 0.90, "optimistic": 0.95},
    "latency_p95_ms": {"pessimistic": 2000, "base": 1000, "optimistic": 500},
}

# Demo run with mock data
```

**Key talking points during coding:**
- "Schema enforcement via Instructor = 0 parsing failures in prod"
- "Bootstrap CI > single split — gives you pessimistic/base/optimistic for stakeholder conversations"
- "Gates are scenario-aware — pessimistic must pass for regulated domains"
- "Test set frozen — this harness NEVER touches test until release gate"

---

### **Round 3: English & Communication (15–20 min)**
- Fluent, technical English
- Can explain complex eval concepts to non-technical stakeholders
- Async-first communication style: "I write the doc, you read it, we sync only for decisions"
- Client-facing experience: presented eval results to CTOs, Legal, Compliance

---

## 🎭 Behavioral / Culture Fit Prep

| Question | My Story (STAR) |
|---|---|
| "Tell me about a time you disagreed with a stakeholder on a release decision." | **Situation:** MultiOCR latency p95 165s vs. 15s gate. **Task:** Release pressure from Sales. **Action:** Presented 3-scenario data — pessimistic 165s, base 120s, optimistic 80s. Proposed: ship with guardrails (async fallback + shadow) + 2-week latency sprint. **Result:** Released with guardrails; latency fixed in sprint; zero incidents. |
| "Describe a project where you had to learn a new technology quickly." | **Situation:** Needed self-hosted LLM for AySA (Ley 25.326). **Task:** Deploy Qwen2.5-7B/14B on vLLM in 1 week. **Action:** Studied vLLM docs, built Docker compose, tuned KV cache, benchmarked vs. API. **Result:** Deployed in 3 days; 40% cost reduction vs. API; latency p95 < 2s. |
| "How do you handle ambiguous requirements?" | **Situation:** Client wanted "high accuracy" for extraction. **Task:** Define measurable gates. **Action:** Ran workshop: "What does failure cost?" → mapped to field-level F1 thresholds per field criticality. Built score composite weighted by business impact. **Result:** Gates approved by Legal + Product; first release passed. |

---

## 📚 Reference Materials to Review (Night Before)

- `ai-eval-harness` repo — know every class/method
- `kindatechnical.com` — "The Convergence of QA, Statistics, and AI Engineering"
- `DevOpsSchool` — "Model Evaluation Engineer Role Blueprint"
- `TheLinuxCode` — "Training vs Testing vs Validation Sets"
- `Springer 2024` — "QA for ML ≠ QA for Software" (key quotes)
- Your own CV + portfolio projects — cold recall

---

## ✅ Day-of Checklist

- [ ] GitHub repos public & readable (`ai-eval-harness`, `multiocr-cost-analysis`, `aysa-piloto-labia`)
- [ ] Local env ready: Python 3.11, pytest, numpy, instructor, vLLM (mock ok)
- [ ] Quiet space, good mic, stable internet
- [ ] Water, notebook, pen
- [ ] Toptal calendar link confirmed
- [ ] Timezone confirmed (GMT-3 vs. interviewer)
- [ ] 3 questions ready for them:
  1. "What's the typical engagement model for AI Quality Engineers on Toptal — fractional retainer or project-based?"
  2. "How does Toptal handle IP ownership for evaluation frameworks built during engagements?"
  3. "What's the biggest eval gap you see in Toptal clients today?"

---

## 🚨 Red Flags to Avoid

| Don't Say | Do Say |
|---|---|
| "I test LLMs" | "I build evaluation infrastructure with frozen test sets, bootstrap CI, and measurable gates" |
| "I write prompts" | "I engineer schema-enforced prompts with judge/coherence 2nd-pass and versioning" |
| "I do QA for AI" | "I'm an AI Quality Engineer — the convergence of QA rigor, stats, and ML eng" |
| "Accuracy is 95%" | "Base scenario accuracy 0.95 (CI 0.92–0.97); pessimistic 0.92 fails gate → guardrails required" |
| "I can start Monday" | "I can start in 2 weeks; need 1 week for client offboarding, 1 week for onboarding setup" |

---

## 📞 Post-Screening Follow-Up

**Within 2 hours:** Email recruiter with:
- Link to `ai-eval-harness` (if not shared)
- One-pager: "How I'd evaluate [their tech stack / typical client use case]"
- Availability confirmation

**Within 24 hours:** LinkedIn connect with interviewer (if appropriate) + thank you note referencing specific technical discussion point.

---

## 📈 Success Metrics

| Stage | Target |
|---|---|
| Application submitted | Day 1 |
| Screening call scheduled | Week 1 |
| Technical screen passed | Week 2 |
| English/communication passed | Week 2 |
| **Toptal accepted** | **Week 3** |
| First client match | Week 4–6 |
| **First engagement signed** | **Week 6–8** |

---

**Ready. The portfolio (`ai-eval-harness`) does the heavy lifting. Walk in knowing your methodology is bulletproof.**