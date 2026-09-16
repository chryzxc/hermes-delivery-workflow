from delivery_gates import register


class RecordingContext:
    """Minimal context proving foundation registration has no side effects."""

    def __init__(self):
        self.calls = []


def test_foundation_registers_without_tools_or_hooks():
    context = RecordingContext()

    result = register(context)

    assert result is None
    assert context.calls == []
