def clear():
    """
    Clears the terminal screen with 2 methods: \n
    1. Using the os module, or
    2. Using an ANSI (ASCII) escape sequence.
    """
    try:
        from os import system, name
        if system('cls' if name == 'nt' else 'clear') == 1:
            print('\033[2J\033[1;1H', end='')
        return
    except:
        return
def bisect(list: list | tuple | set, query):
    from iter import bisect
    return bisect(list, query)