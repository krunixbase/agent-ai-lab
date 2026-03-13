import datetime
import math
from typing import Any, Dict


def tool_echo(input_text: str) -> str:
    """
    Returns the input text unchanged.
    Useful as a fallback or for simple transformations.
    """
    return input_text


def tool_calculator(expression: str) -> str:
    """
    Evaluates a basic math expression.
    WARNING: This is intentionally minimal and not safe for untrusted input.
    """
    try:
        result = eval(expression, {"__builtins__": {}}, math.__dict__)
        return str(result)
    except Exception:
        return "Error: invalid math expression."


def tool_datetime(_: str = "") -> str:
    """
    Returns the current date and time in ISO format.
    """
    return datetime.datetime.now().isoformat()


def register_builtin_tools(registry) -> None:
    """
    Registers built-in tools into the provided ToolRegistry instance.
    """
    registry.register("echo", tool_echo)
    registry.register("calculator", tool_calculator)
    registry.register("datetime", tool_datetime)
