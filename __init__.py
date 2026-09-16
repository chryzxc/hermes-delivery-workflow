"""Hermes native-plugin entrypoint for Delivery Gates."""

if __package__:
    from .delivery_gates import register
else:  # pytest may import a hyphenated repository root without a package name.
    from delivery_gates import register

__all__ = ["register"]
