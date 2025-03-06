# humorous_exceptions/__init__.py
import sys

from .handler import humor_excepthook

sys.excepthook = humor_excepthook  # Activates the humor when imported
