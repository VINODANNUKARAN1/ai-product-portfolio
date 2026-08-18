# ML Experiment Brief Template

## Experiment Overview
- **Name:** [Experiment name]
- **Hypothesis:** If we [change], then [metric] will [improve by X%] because [reason]
- **Owner:** [PM name]
- **Duration:** [X weeks]
- **Status:** Planning / Running / Analyzing / Complete

## Business Context
- Why run this experiment?
- What decision will results inform?
- Cost of being wrong?

## Experiment Design

| Parameter | Value |
|-----------|-------|
| Control | [Current experience / no AI] |
| Treatment | [AI-powered variant] |
| Allocation | [50/50, 90/10, etc.] |
| Unit | [User / Session / Request] |
| Primary metric | [One metric that decides success] |
| Guardrail metrics | [Metrics that must NOT degrade] |
| Minimum sample size | [Calculate using power analysis] |
| Minimum duration | [2 weeks minimum for day-of-week effects] |

## Metrics

| Type | Metric | Baseline | MDE (Minimum Detectable Effect) |
|------|--------|:--------:|:-------------------------------:|
| Primary | | | |
| Secondary | | | |
| Guardrail | | | |

## AI-Specific Considerations
- Model version used: [v1.2.3]
- Known model limitations: [list]
- Confidence threshold for showing AI output: [X%]
- Fallback when AI confidence is low: [human/default]
- Cold-start handling: [what happens for new users]

## Decision Framework
| Result | Action |
|--------|--------|
| Primary metric up, guardrails safe | Ship to 100% |
| Primary metric up, guardrail degraded | Investigate, likely don't ship |
| Primary metric flat | Not worth the complexity, kill |
| Primary metric down | Kill immediately, investigate why |

## Results (Fill after experiment)
- Start date:
- End date:
- Sample size (control / treatment):
- Primary metric result:
- Statistical significance (p-value):
- Decision:
- Learnings:
