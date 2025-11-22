# HEART
HEART — Hierarchical Emotion Adaptive Response Transformer.  A persistent emotional-state controller for LLMs.

Overview

HEART is a novel architecture that adds a persistent, multi-dimensional emotional state engine to stateless language models.
Instead of simple sentiment control, HEART introduces:

an evolving emotional state vector

a dynamical update system influenced by user input, model output, and internal metrics

a conditioning pipeline that injects emotional state into the LLM per turn

This enables consistent, controllable emotional trajectories in long-form interactions, which cannot be achieved through prompt engineering or standard fine-tuning techniques.

Motivation

Transformers are stateless by design. After each interaction, the model has no internal memory or emotional inertia.
Existing solutions such as:

sentiment conditioning

LoRA-based tone training

prompt wrappers

only modify output tone for the current input.
They fail to capture long-term emotional context or dynamic affective behavior.

HEART introduces a model-agnostic emotional controller inspired by affective computing and cognitive architectures.
It maintains an independent emotional state that evolves according to interaction dynamics and influences the model’s behavior on every turn.

High-Level Architecture
User Input
     ↓
Feature Extractor (sentiment, tone, complexity)
     ↓
Emotional State Engine (ESE)
     ↓         ↑
LLM Output  ←  Conditioning Module


The Emotional State Engine maintains:

e_t = [valence, arousal, uncertainty, cognitive_load, social_orientation]


The state is updated each turn based on:

user input features

LLM output features

internal metrics such as novelty, prediction error, and confidence

The updated emotional vector is then injected into the LLM as part of the conditioning mechanism.

Emotional Vector (MVP Version)
Dimension	Description
Valence	Positive–negative affect
Arousal	Activation or energy level
Uncertainty	Confidence vs hesitation
Cognitive Load	Reasoning strain or complexity
Social Orientation	Warmth, cooperativeness, conversational tone

Values lie within a bounded range of [-1, 1].

Repository Structure (Planned)
HEART/
│
├── src/
│   ├── ese/               # emotional state engine
│   ├── llm_adapter/       # conditioning pipeline
│   ├── utils/             # feature extractors, logging
│   └── __init__.py
│
├── docs/
│   ├── architecture.md    # technical description
│   └── experiments.md     # evaluation plans
│
├── README.md
├── LICENSE
└── .gitignore

Roadmap
v0.1 — Initialization

Repository setup

Architecture documentation

Emotional state vector design

v0.2 — MVP Emotional Engine

Implement 5-dimensional emotional vector

Hand-crafted update rules

Feature extraction utilities

v0.3 — LLM Integration

Conditioning prefix or adapter injection

Multi-turn emotional behavior tests

v0.4 — Evaluation

Scripted multi-turn experiments

Emotional trajectory logging

Small user-rating study

v0.5 — Learnable Emotional Engine

Replace hand-designed rules with GRU/MLP

Compare learned vs manual dynamics

v1.0 — First Public Release

Notebook demo

Documentation

Example scripts

Optional installable package

References and Inspiration

HEART is inspired by work in:

affective computing

appraisal-based emotion models

cognitive architectures

RL agents with persistent latent states

emotion-conditioned language generation

Author

Aryavardhan Singh
Creator of the HEART architecture.

Status

This repository is under active development.
Design documents, prototypes, and initial modules will be added as the project evolves.


