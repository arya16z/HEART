"""
Emotional State Engine (ESE) – Version 0.1
Implements a persistent, low-dimensional emotional state vector
with decay, appraisal updates, cross-interactions, and clipping.
"""

from typing import Dict, Any, List
import numpy as np


class EmotionalStateEngine:
    """
    Implements HEART's core emotional state vector and update rules.

    State dimensions (MVP):
        0: valence
        1: arousal
        2: uncertainty
        3: cognitive_load
        4: social_orientation
    """

    def __init__(self):
        # Initial emotional vector (neutral)
        self.state = np.zeros(5, dtype=np.float32)

        # Decay coefficients per dimension (tuned later)
        self.decay = np.array([0.92, 0.88, 0.90, 0.87, 0.93], dtype=np.float32)

        # Cross-interaction matrix (placeholder version)
        self.cross_matrix = np.array([
            [ 0.0,  0.02, 0.03, -0.01, 0.00],   # valence interactions
            [ 0.01, 0.00, 0.01, -0.02, 0.00],   # arousal interactions
            [-0.02, 0.02, 0.00,  0.01, 0.00],   # uncertainty interactions
            [-0.01, 0.00, 0.02,  0.00, 0.00],   # cognitive load interactions
            [ 0.00, 0.00, 0.00,  0.01, 0.00],   # social orientation interactions
        ], dtype=np.float32)

        # Bounds
        self.min_val = -1.0
        self.max_val = 1.0

    # -----------------------
    # Core methods
    # -----------------------

    def reset(self):
        """Reset to neutral emotional state."""
        self.state = np.zeros(5, dtype=np.float32)

    def get_state(self) -> List[float]:
        """Return the current emotional state."""
        return self.state.tolist()

    def update(self, features: Dict[str, Any]) -> List[float]:
        """
        Update emotional state based on extracted features.
        features: {
            "sentiment": float [-1,1]
            "novelty": float [0,1]
            "entropy": float [0,1]
            "complexity": float [0,1]
            "politeness": float [-1,1]
        }
        """

        # -------- 1. Decay existing state ----------
        decayed = self.decay * self.state

        # -------- 2. Appraisal-based deltas --------
        # These weights are placeholders; they will be tuned later.
        delta = np.zeros(5, dtype=np.float32)

        # valence boosted by sentiment & politeness
        delta[0] = 0.6 * features.get("sentiment", 0.0) \
                   + 0.2 * features.get("politeness", 0.0)

        # arousal boosted by novelty
        delta[1] = 0.7 * features.get("novelty", 0.0)

        # uncertainty boosted by entropy (low confidence)
        delta[2] = 0.8 * features.get("entropy", 0.0)

        # cognitive load boosted by complexity
        delta[3] = 0.6 * features.get("complexity", 0.0)

        # social orientation boosted by politeness
        delta[4] = 0.5 * features.get("politeness", 0.0)

        # -------- 3. Cross-interactions ------------
        cross_term = self.cross_matrix @ self.state

        # -------- 4. Combine into new state --------
        new_state = decayed + delta + cross_term

        # -------- 5. Clip for stability ------------
        new_state = np.clip(new_state, self.min_val, self.max_val)

        # update internal state
        self.state = new_state

        return self.state.tolist()


