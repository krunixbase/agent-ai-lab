class EchoTool:
    """
    Simple tool that returns the input unchanged.
    """
    def __call__(self, text: str) -> str:
        return text


class UppercaseTool:
    """
    Converts input text to uppercase.
    """
    def __call__(self, text: str) -> str:
        return text.upper()
