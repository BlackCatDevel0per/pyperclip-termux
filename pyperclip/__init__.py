from termux.Clipboard import setclipboard as copy
from termux.Clipboard import getclipboard

def paste():
    return getclipboard()[1]

__all__ = ["copy", "paste", "getclipboard"]
