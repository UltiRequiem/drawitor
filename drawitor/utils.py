def colored(red: int, green: int, blue: int, text: str) -> str:
    return f"\033[38;2;{red};{green};{blue}m{text}"


PIXEL = "\u2584"
