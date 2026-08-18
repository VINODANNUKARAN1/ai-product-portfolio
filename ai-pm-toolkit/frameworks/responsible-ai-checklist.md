# Responsible AI Checklist

## Pre-Ship Checklist for Any AI/ML Feature

Use this BEFORE launching any AI feature to production.

---

### 1. BIAS & FAIRNESS
- [ ] Have we tested model output across demographic groups?
- [ ] Is the training data representative of all user segments?
- [ ] Are there protected attributes that could create discrimination?
- [ ] Have we defined what "fair" means for THIS product context?
- [ ] Do disadvantaged groups receive worse outcomes?

### 2. TRANSPARENCY & EXPLAINABILITY
- [ ] Can we explain WHY the model made a specific prediction?
- [ ] Do users know when they're interacting with AI (vs human)?
- [ ] Are confidence levels communicated to users?
- [ ] Is there documentation of model limitations?
- [ ] Can users request explanation of decisions affecting them?

### 3. PRIVACY & DATA
- [ ] Is user consent obtained for data used in training?
- [ ] Can we delete individual user data from model if requested?
- [ ] Is PII (personally identifiable information) protected?
- [ ] Are we compliant with GDPR/PDPA/local data protection laws?
- [ ] Is data retention policy defined and enforced?

### 4. SAFETY & RELIABILITY
- [ ] What happens when the model is WRONG? (Failure mode defined)
- [ ] Is there a human escalation path for uncertain predictions?
- [ ] Is there a kill switch to disable the feature instantly?
- [ ] Have we tested adversarial inputs (can users trick the model)?
- [ ] Are there guardrails against harmful outputs?

### 5. USER CONTROL
- [ ] Can users override AI suggestions?
- [ ] Can users opt out of AI features entirely?
- [ ] Is the AI helping users or replacing their judgment?
- [ ] Does the product work (degraded but functional) if AI fails?
- [ ] Are users informed when AI confidence is low?

### 6. MONITORING & ACCOUNTABILITY
- [ ] Who is responsible if the AI causes harm?
- [ ] Is there ongoing monitoring for model drift/degradation?
- [ ] Are we logging predictions for audit purposes?
- [ ] Is there a process for user complaints about AI decisions?
- [ ] Do we have a plan for model retraining/updating?

---

## Severity Classification

| Risk Level | Definition | Action Required |
|-----------|-----------|-----------------|
| 🟢 Low | Cosmetic issue, no user harm | Log and fix in next sprint |
| 🟡 Medium | Incorrect output, minor user inconvenience | Fix within 1 week |
| 🟠 High | Systematic bias or frequent incorrect critical decisions | Pause feature, fix immediately |
| 🔴 Critical | Direct user harm, legal liability, safety risk | Kill switch NOW. Fix before re-enable. |

---

## When to NOT Ship

DO NOT SHIP if ANY of these are true:
1. Model discriminates against a protected group (and we can't fix it)
2. No failure mode is defined (we don't know what happens when wrong)
3. No kill switch exists (we can't turn it off instantly)
4. Users can't override the AI (removes human agency)
5. We can't explain why the model made a decision (regulatory risk)

---
*Framework by Vinod Annukaran | AI Product Manager*
