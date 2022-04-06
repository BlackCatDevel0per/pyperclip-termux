from termux.Clipboard import setclipboard
from termux.Clipboard import getclipboard

def copy(text):
    setclipboard(text)

def paste():
    return getclipboard()[1]

__all__ = ["copy", "paste", "getclipboard"]
