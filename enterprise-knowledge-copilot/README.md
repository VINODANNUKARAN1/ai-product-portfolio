# 🤖 AI Enterprise Knowledge Assistant

## Business Problem
Support teams spend 40% of their time answering repetitive questions that are already documented. This costs enterprises $15-25 per support ticket for information that already exists in internal documents.

**Target:** Reduce support ticket volume by 60% through AI-powered self-service Q&A.

## Live Demo
🔗 [Try it here](YOUR_STREAMLIT_URL) — Upload any PDF and ask questions!

## Solution
A Retrieval Augmented Generation (RAG) chatbot that:
1. Ingests company documents (PDFs)
2. Builds a searchable knowledge base using vector embeddings
3. Answers user questions with **source citations** (transparency!)
4. Provides confidence scores (when to escalate to human)

## Architecture

```
┌──────────┐     ┌──────────────┐     ┌──────────────┐
│  Upload  │────▶│   Chunk &    │────▶│   Embed &    │
│   PDF    │     │   Split      │     │   Store      │
└──────────┘     └──────────────┘     └──────────────┘
                                            │
┌──────────┐     ┌──────────────┐     ┌─────▼────────┐
│ Response │◀────│  Generate    │◀────│  Retrieve    │
│ + Source │     │  Answer      │     │  Top-K       │
└──────────┘     └──────────────┘     └──────────────┘
```

## Tech Stack (100% Free)
| Component | Tool | Why This Choice |
|-----------|------|-----------------|
| Embeddings | sentence-transformers (all-MiniLM-L6-v2) | Free, fast, runs locally |
| Vector DB | ChromaDB | Free, no API key needed |
| LLM | HuggingFace (Mistral-7B) | Free tier available |
| Frontend | Streamlit | Free hosting on Streamlit Cloud |
| Language | Python 3.10+ | Industry standard |

## Key Product Decisions

| Decision | Options Considered | Chosen | Reasoning |
|----------|-------------------|--------|-----------|
| RAG vs Fine-tuning | Fine-tune company model vs Retrieve + Generate | RAG | $0 cost, instant updates, source citation, no training data needed |
| Embedding Model | OpenAI ada-002 vs all-MiniLM-L6-v2 | MiniLM | Free, 90% of OpenAI quality for retrieval tasks |
| Chunk Size | 200 / 500 / 1000 tokens | 500 | Tested all three. 500 balances context retention with retrieval precision. |
| Vector DB | Pinecone vs Chroma vs FAISS | ChromaDB | Free, simple, sufficient for <50K docs. Would scale to Pinecone. |

## Success Metrics (Production)
| Metric | Target | Measurement |
|--------|--------|-------------|
| Resolution Rate | >75% | Questions answered without human escalation |
| Answer Accuracy | >90% | Faithful to source documents (human eval sample) |
| User Satisfaction | >4.2/5 | Thumbs up/down + periodic survey |
| Response Time | <3 seconds | 95th percentile latency |
| Cost per Query | <$0.02 | Infrastructure + API costs / total queries |

## Ethical Considerations
- **Hallucination Risk:** Mitigated via source citations + confidence scores
- **Data Privacy:** Documents processed locally, never sent to external APIs (in free version)
- **Bias:** Model may favor recent documents; addressed by equal weighting in retrieval
- **Transparency:** Every answer shows WHICH source it came from

## How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/ai-enterprise-knowledge-assistant.git
cd ai-enterprise-knowledge-assistant

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

## How to Deploy (Free on Streamlit Cloud)
1. Push this repo to GitHub
2. Go to share.streamlit.io
3. Connect your GitHub repo
4. Select `app.py` as main file
5. Deploy — live URL in 2 minutes!

## Roadmap
- **V1 (Current):** Single document, basic Q&A, extractive answers
- **V2:** Multi-document support, conversation memory, HuggingFace LLM integration
- **V3:** Multi-tenant, user authentication, analytics dashboard, feedback loop
- **V4:** Fine-tuned model on company-specific language, auto-escalation rules

## What I'd Do Differently in Production
1. Replace free embeddings with OpenAI ada-002 (better quality, $0.0001/token)
2. Use GPT-4 for generation (better reasoning, ~$0.01/query)
3. Add caching layer (Redis) for repeated questions
4. Implement user authentication and role-based access
5. Build feedback loop: thumbs up/down trains retrieval ranking
6. Add monitoring: latency, accuracy drift, usage patterns

---

*Built by Vinod Annukaran | MSc Data Science | AI Product Manager*
*Demonstrating: GenAI product architecture + PM decision-making + responsible AI*
