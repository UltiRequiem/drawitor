import os

PIXEL = "\u2584"


def colored(red: int, green: int, blue: int, text: str) -> str:
    return f"\033[38;2;{red};{green};{blue}m{text}"


def clear_console():
    os.system("clear" if os.name == "posix" else "cls")
