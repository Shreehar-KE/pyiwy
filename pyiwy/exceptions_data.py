# pyiwy/exceptions_data.py

import sys

# Dictionary of funny exception messages
EXCEPTION_MESSAGES = {
    ArithmeticError: "Math is hard, I get it. But Python expected better. ➗❌",
    FloatingPointError: "Floating-point numbers just did some gymnastics... and failed. 🤸‍♂️💥",
    OverflowError: "Congratulations! You just exceeded what Python can handle. 🚀🔥",
    ZeroDivisionError: "Nice try! Even Python can't divide by zero. 🤦",
    AssertionError: "Your assumption was wrong. Just like my assumption that this would work. 😅",
    AttributeError: "That attribute doesn't exist! Maybe it left the codebase to follow its dreams. 🚀",
    BufferError: "The buffer has had enough! Maybe it needs a break. 📦😵",
    EOFError: "End of file reached. Python is done talking to you. 📜💀",
    ImportError: "Import failed! Maybe the module took a vacation. 🏖️",
    LookupError: "Couldn't find what you were looking for. Maybe try Google? 🔍",
    IndexError: "Whoa! That index is out of range. Have you considered lists start at 0? 📏",
    KeyError: "That key doesn't exist! Maybe it got lost in the matrix. 🔑💻",
    MemoryError: "Out of memory! Maybe it's time to close some Chrome tabs? 💾🔥",
    NameError: "You referenced a variable that doesn't exist. Maybe it got lost in a different scope? 🌎",
    UnboundLocalError: "You tried using a local variable before defining it. Premature enthusiasm? 😆",
    OSError: "Something went wrong with the OS! Try turning it off and on again. 🔄",
    RuntimeError: "Something unexpected happened at runtime. Welcome to debugging! 🛠️",
    NotImplementedError: "This feature isn't available yet. Maybe in the next DLC? 🎮",
    SyntaxError: "Your code syntax is wrong. Python is silently judging you. 👀",
    IndentationError: "Indentation is all wrong! Python likes things neat and tidy. 📏",
    TabError: "Tabs and spaces mixed! This is why we can't have nice things. 🎭",
    SystemError: "Python encountered a system-level issue. Time to panic! 😱",
    TypeError: "You just mixed up data types. Python is not a smoothie blender! 🥤",
    ValueError: "Your value is invalid! Like my life choices. 😅",
    UnicodeError: "Unicode issue detected! Maybe your text needs therapy. 📝💭",
    UnicodeDecodeError: "Decoding failed! Your text is speaking in an unknown language. 🌍🤖",
    UnicodeEncodeError: "Encoding failed! Python refuses to speak that dialect. 💬🚫",
    UnicodeTranslateError: "Translation failed! Maybe Python isn't bilingual? 🤷",
    Warning: "This is a warning, not an error. But you should still be scared. 😨",
    BytesWarning: "Byte-related warning! 0s and 1s are rebelling. 🧮",
    DeprecationWarning: "This feature is old and might disappear. Just like my motivation. 😴",
    FutureWarning: "This will break in the future. So, future-you will suffer. 🤖",
    ImportWarning: "Something seems wrong with your imports. Did you typo the module name? 🤔",
    PendingDeprecationWarning: "It's *almost* deprecated. But not yet. Suspense! 😬",
    RuntimeWarning: "Something seems off at runtime. But Python is too polite to crash. 😇",
    SyntaxWarning: "Your syntax is sketchy, but Python is letting it slide… for now. 👀",
    UnicodeWarning: "Unicode issue ahead! Proceed with caution. 🚧",
    UserWarning: "Python is warning you. But will you listen? 🤷‍♂️",
}

# Conditionally add exceptions based on Python version
if sys.version_info >= (3, 3):
    EXCEPTION_MESSAGES.update(
        {
            BlockingIOError: "Something's blocking the operation. Maybe it's Monday? ⛔😩",
            ChildProcessError: "The child process misbehaved. Kids these days! 👶💻",
            ConnectionError: "Lost connection! Maybe the internet just took a coffee break. ☕",
            BrokenPipeError: "Pipe broken! Who dropped the wrench?! 🔧💥",
            ConnectionAbortedError: "Connection aborted. Maybe it just ghosted you? 👻",
            ConnectionRefusedError: "Connection refused. Python just said 'Nope!' 🚫",
            ConnectionResetError: "Connection reset. Did you forget to pay your internet bill? 💸",
            FileExistsError: "That file already exists! Don't try reinventing the wheel. 🛞",
            FileNotFoundError: "File not found! Maybe it's playing hide and seek? 🕵️‍♂️",
            InterruptedError: "Operation interrupted! Someone pressed Ctrl+C too hard. ⏹️",
            IsADirectoryError: "Expected a file, but got a directory. Python is confused! 📂❌",
            NotADirectoryError: "Expected a directory, but got a file. Are you messing with me? 📁❌",
            PermissionError: "You don't have permission! Python says 'Access Denied!' 🚫🔒",
            ProcessLookupError: "That process is missing! Maybe it ran away? 🏃‍♂️💨",
            TimeoutError: "Operation took too long. Python is impatient, unlike your crush. ⏳",
        }
    )

if sys.version_info >= (3, 5):
    EXCEPTION_MESSAGES.update(
        {
            RecursionError: "Recursion limit reached! Recursion limit reached! Recursion limit reached! 🔄",
            StopAsyncIteration: "Async iterator is done. Time to move on! 🏁",
        }
    )

if sys.version_info >= (3, 6):
    EXCEPTION_MESSAGES.update(
        {
            ModuleNotFoundError: "That module is nowhere to be found. Have you checked under the couch? 🛋️",
        }
    )

if sys.version_info >= (3, 10):
    EXCEPTION_MESSAGES.update(
        {
            EncodingWarning: "Something's off with your encoding. Maybe it's in Wingdings? 🔡",
        }
    )


def get_funny_message(exception_type):
    """Returns a funny message for a given exception."""
    return EXCEPTION_MESSAGES.get(
        exception_type,
        "An unexpected error occurred... but hey, at least it's not a Java exception! 😂",
    )
