# HEART Architecture

## Introduction

HEART (Hierarchical Emotion Adaptive Response Transformer) is a hybrid architecture that augments stateless Large Language Models with a persistent emotional controller.

The core idea:
- LLMs are excellent at conditional generation
- but have no *internal* state that persists across turns
- HEART adds a compact emotional state that evolves dynamically
- the LLM conditions on this state every turn

This document outlines the architecture, emotional vector, update rules, and system design.

---

## System Overview

HEART consists of three major components:

1. **Feature Extractor**  
   Converts user input and model output into numerical features (sentiment, complexity, entropy, tone, etc.)

2. **Emotional State Engine (ESE)**  
   Maintains a low-dimensional emotional vector  
   Updates it every turn using dynamical equations

3. **LLM Conditioning Module**  
   Injects the emotional state into the LLM  
   (via prefix tokens or learned adapters)

The high-level pipeline:

User Input
↓
Feature Extraction
↓
Emotional State Engine → Emotional Vector e_t
↓ ↑
Conditioning Module ←─────────┘
↓
LLM Output


---

## Emotional State Vector

For the MVP, HEART uses a 5-dimensional emotional vector:

e_t = [valence, arousal, uncertainty, cognitive_load, social_orientation]


### Dimensions

| Dimension          | Description                                   |
|--------------------|-----------------------------------------------|
| Valence            | Positive–negative affect                      |
| Arousal            | Activation / energy level                     |
| Uncertainty        | Confidence vs hesitation                      |
| Cognitive Load     | Reasoning strain or complexity                |
| Social Orientation | Warmth and cooperativeness                    |

Each dimension lies within a bounded range **[-1, 1]**.

---

## Update Dynamics

The emotional state updates once per interaction turn:

e_(t+1) = decay(e_t) + appraisal(user_features, model_features) + cross_interactions + noise

### 1. Decay

Emotions naturally drift toward neutrality:

decay(e_t) = α * e_t
where α ∈ [0.8, 0.99] depending on dimension


### 2. Appraisal

Appraisal is computed from extracted features:

- sentiment score → valence  
- novelty → arousal  
- entropy → uncertainty  
- output length / depth → cognitive load  
- politeness markers → social orientation  

General form:

delta[i] = W_i · features

Where **W_i** is a hand-tuned weight vector for dimension *i*.

### 3. Cross-Interactions

Affect dimensions influence each other. Example:

if cognitive_load high → arousal decreases
if valence low → uncertainty increases

This can be modeled as:

cross = M × e_t

Where **M** is a 5×5 interaction matrix.

### 4. Clipping and Stability

After each update:
e_(t+1) = clip(e_(t+1), -1, 1)

This prevents emotional drift into unstable regions.

---

## Feature Extraction

Features come from:

### User Input
- sentiment polarity  
- toxicity / politeness  
- length and complexity  
- topic / intent  

### Model Output
- entropy of token distribution (confidence)  
- length and reasoning complexity  
- tone features (politeness, assertiveness)  

### System Metrics
- prediction error (for tool-using agents)  
- novelty / surprise  
- latency or model failure events  

All features form a vector **f_t** used by the update rule.

---

## Conditioning the LLM

HEART conditions the LLM using one of two approaches.

### Option A — Prefix Injection (MVP)
Convert emotional vector into human-readable structured text:

[EMOTION_STATE]
valence: 0.4
arousal: -0.2
uncertainty: 0.1
load: 0.7
orientation: 0.3
Injected before the user message each turn.

Simple, model-agnostic, works with any LLM.

### Option B — Embedding Projection (Advanced)
Project emotional vector into LLM embedding space:

E = P(e_t)

Then prepend E to the token embeddings.

This requires small finetuning or adapter blocks.

---

## Safety Mechanisms

- clip emotional ranges  
- detect degenerate loops  
- automatic reset after extreme states  
- cap arousal during unsafe contexts  
- enforce minimum valence during sensitive tasks  

These rules prevent emotional runaway or manipulation.

---

## Future Extensions

- learned ESE (GRU) instead of rule-based  
- higher-dimensional emotional manifold  
- reward-driven emotional policies (RL)  
- episodic memory tied to emotional arcs  

---

## Summary

HEART transforms a stateless LLM into a stateful emotional agent by:

- introducing a persistent emotional vector  
- updating it dynamically using appraisal and decay  
- feeding it back into the LLM at each step  

This results in more consistent, human-like emotional trajectories during long-form interaction.


