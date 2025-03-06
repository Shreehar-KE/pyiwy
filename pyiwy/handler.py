# pyiwy/handler.py

import sys
from .exceptions_data import get_funny_message


def humor_excepthook(exc_type, exc_value, traceback):
    """Custom exception hook to print humorous messages instead of boring stack traces."""
    funny_message = get_funny_message(exc_type)
    print(f"🔥 ERROR ALERT 🔥\n{funny_message}\n\nOriginal Error: {exc_value}")


# Set the custom exception handler globally
sys.excepthook = humor_excepthook
