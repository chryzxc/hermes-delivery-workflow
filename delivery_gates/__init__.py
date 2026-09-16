"""Hermes Delivery Gates native plugin.

The foundation release deliberately registers no tools yet. It verifies that the
plugin can be discovered safely before delivery-gate behavior is added.
"""

__all__ = ["register"]


def register(ctx):
    """Register native Hermes plugin behavior.

    The v0.1 foundation has no tool, hook, command, network, or filesystem-write
    registration. Later releases will add documented, read-only tools here.
    """
    return None
