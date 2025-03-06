import unittest
import sys
from io import StringIO
from pyiwy.exceptions_data import get_funny_message, EXCEPTION_MESSAGES
from pyiwy.handler import humor_excepthook


class TestHumorousExceptions(unittest.TestCase):

    def setUp(self):
        """Redirect stdout to capture print statements."""
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        """Reset stdout after each test."""
        sys.stdout = sys.__stdout__

    def test_get_funny_message_existing_exceptions(self):
        """Test if all defined exceptions return the expected funny message."""
        for exception_type, expected_message in EXCEPTION_MESSAGES.items():
            with self.subTest(exception=exception_type):
                self.assertEqual(get_funny_message(exception_type), expected_message)

    def test_get_funny_message_unknown_exception(self):
        """Test if an unknown exception type gets the default funny message."""

        class CustomException(Exception):
            pass

        expected_default_message = "An unexpected error occurred... but hey, at least it's not a Java exception! 😂"
        self.assertEqual(get_funny_message(CustomException), expected_default_message)

    def test_humor_excepthook(self):
        """Test if humor_excepthook prints the correct funny message when an exception occurs."""
        try:
            1 / 0  # Trigger ZeroDivisionError
        except ZeroDivisionError as e:
            humor_excepthook(type(e), e, e.__traceback__)

        output = self.held_output.getvalue().strip()
        self.assertIn("🔥 ERROR ALERT 🔥", output)
        self.assertIn(EXCEPTION_MESSAGES[ZeroDivisionError], output)

    def test_humor_excepthook_with_multiple_exceptions(self):
        """Test humor_excepthook with different built-in exceptions."""
        test_cases = [
            (KeyError("missing_key"), KeyError),
            (TypeError("wrong type"), TypeError),
            (FileNotFoundError("file.txt"), FileNotFoundError),
        ]

        for exception_instance, exception_type in test_cases:
            with self.subTest(exception=exception_type):
                humor_excepthook(
                    type(exception_instance),
                    exception_instance,
                    exception_instance.__traceback__,
                )
                output = self.held_output.getvalue().strip()
                self.assertIn("🔥 ERROR ALERT 🔥", output)
                self.assertIn(EXCEPTION_MESSAGES.get(exception_type, ""), output)
                self.held_output.truncate(0)
                self.held_output.seek(0)

    def test_backward_compatibility(self):
        """Ensure compatibility with different Python versions by checking conditionally included exceptions."""
        conditional_exceptions = {
            (3, 3): [
                BlockingIOError,
                ChildProcessError,
                ConnectionError,
                FileExistsError,
                TimeoutError,
            ],
            (3, 5): [RecursionError, StopAsyncIteration],
            (3, 6): [ModuleNotFoundError],
            (3, 10): [EncodingWarning],
        }

        for version, exceptions in conditional_exceptions.items():
            if sys.version_info >= version:
                for exc in exceptions:
                    with self.subTest(exception=exc):
                        self.assertIn(exc, EXCEPTION_MESSAGES)
                        self.assertIsInstance(EXCEPTION_MESSAGES[exc], str)


if __name__ == "__main__":
    unittest.main()
