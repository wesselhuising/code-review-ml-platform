"""Tiny local "model registry".

Handles saving and loading the trained fraud-risk model to/from disk.
"""

import os
import pickle

MODEL_PATH = "models/model.pkl"

_model = None
if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, "rb") as f:
        _model = pickle.load(f)


def save_model(model):
    """Persist the trained model."""
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)


def load_model():
    return _model
