# HEART – Hierarchical Emotion Adaptive Response Transformer
*A persistent emotional-state controller for LLMs.*

---

## Overview

HEART is a novel architecture that adds a persistent, multi-dimensional emotional state engine to stateless language models.

Instead of simple sentiment control, HEART introduces:

- an evolving emotional state vector  
- a dynamical update system influenced by user input, model output, and internal metrics  
- a conditioning pipeline that injects emotional state into the LLM per turn  

This enables consistent, controllable emotional trajectories in long-form interactions — something not possible with prompt engineering or standard fine-tuning.

---

## Motivation

Transformers are stateless by design. They lose all internal emotional context between turns.

Existing solutions such as:

- sentiment conditioning  
- LoRA-based tone tuning  
- prompt wrappers  

only affect the **current** message. They cannot sustain mood dynamics or long-term emotional context.

HEART introduces a model-agnostic emotional controller inspired by affective computing and cognitive architectures.  
It maintains its own emotional state, updates it each turn, and feeds it back into the LLM.

---

## High-Level Architecture

User Input
↓
Feature Extractor (sentiment, tone, complexity)
↓
Emotional State Engine (ESE)
↓ ↑
LLM Output ← Conditioning Module


---

## Emotional State Vector (MVP)

The Emotional State Engine maintains a vector:

e_t = [valence, arousal, uncertainty, cognitive_load, social_orientation]


### Dimension descriptions

| Dimension          | Description                                   |
|--------------------|-----------------------------------------------|
| Valence            | Positive–negative affect                      |
| Arousal            | Activation or energy level                    |
| Uncertainty        | Confidence vs hesitation                      |
| Cognitive Load     | Reasoning strain or complexity                |
| Social Orientation | Warmth, cooperativeness, conversational tone  |

Values lie in the range **[-1, 1]**.

---

## Repository Structure (Planned)

HEART/
│
├── src/
│ ├── ese/ # emotional state engine
│ ├── llm_adapter/ # conditioning pipeline
│ ├── utils/ # feature extractors, logging
│ └── init.py
│
├── docs/
│ ├── architecture.md # technical description
│ └── experiments.md # evaluation plans
│
├── README.md
├── LICENSE
└── .gitignore


---

## Roadmap

### v0.1 — Initialization
- Repository setup  
- Architecture documentation  
- Emotional vector design  

### v0.2 — MVP Emotional Engine
- Implement 5D emotional state vector  
- Hand-designed update rules  
- Feature extraction utilities  

### v0.3 — LLM Integration
- Conditioning prefix injection  
- First multi-turn emotional tests  

### v0.4 — Evaluation
- Scripted multi-turn experiments  
- Emotional trajectory logs  
- Small user study  

### v0.5 — Learnable ESE
- Replace rule-based engine with GRU/MLP  
- Compare learned vs manual dynamics  

### v1.0 — First Release
- Notebook demo  
- Documentation  
- Example scripts  

---

## References and Inspiration

HEART draws on concepts from:

- affective computing  
- appraisal-based emotion models  
- cognitive architectures  
- RL agents with persistent latent states  
- emotion-conditioned generation  

---

## Author

Aryavardhan Singh  
Creator of the HEART architecture.

---

## Status

This repository is under active development.
