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
    """
    Searches through a list or other iterable using an iterative binary-search algorithm. \n
    Returns the index of the query if found, otherwise returns -1. \n
    """
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == query:
            return mid
        elif list[mid] < query:
            low = mid + 1
        else:
            high = mid - 1
    return -1