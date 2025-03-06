# pyiwy/handler.py

import sys
import traceback as tb
from .exceptions_data import get_funny_message


def humor_excepthook(exc_type, exc_value, traceback):
    """Custom exception hook to print humorous messages instead of boring stack traces."""
    funny_message = get_funny_message(exc_type)
    for line in tb.format_tb(traceback):
        print (line)
    print(f"🔥 ERROR ALERT 🔥\n{funny_message}\n\nOriginal Error:\n {exc_type.__name__}: {exc_value}")


# Set the custom exception handler globally
sys.excepthook = humor_excepthook
