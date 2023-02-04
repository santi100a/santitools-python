# Santi's Tools

This repo contains a set of Python tools and APIs that I use for personal projects.

These utilities are:

- **Filesystem (```filesystem.py```):** A collection of tools for working with files, synchronously, callback-based or using co-routines.
- **Colors (```colors.py```):** It provides 3 ways to colorize your text with ANSI escape sequences: using an already-built dictionary, a function or a special colorizer object.
- **Math (```math.py```):** A set of math functions (for randomness mostly) and highly accurate math constants.
- **Time (```time.py```):** A time API that's very similar to JavaScript's ```Date``` object.
- **Screen Clear (```__init__.py```):** A function to easily clear the screen, by using 1 of 2 methods: the ```os``` module's ```system``` function or an ANSI escape sequence.
- **Bisect (```__init__.py```):** A binary-search algorithm as a function. It's useful for finding a value in a sorted list, with a logarithmic time complexity.
It so happens I just packaged this project, so now you can install it with the command
```pip install santitools```. Try it out!