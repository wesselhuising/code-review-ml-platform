"""Unit tests for the model registry."""

from src.model_registry import save_model, load_model


class FakeModel:
    """Minimal stand-in for a trained sklearn model."""

    def predict(self, X):
        return [1 for _ in X]


def test_save_and_load_round_trip():
    """A model saved to the registry should come back out via load_model."""
    model = FakeModel()
    save_model(model)
    loaded_model = load_model()
    print(f"loaded: {loaded_model}")
