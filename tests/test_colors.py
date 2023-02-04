from santitools.colors import colorize, colorcodes

def test_colorize():
    assert colorize('red', 'red') == '\033[31mred\033[0m'
    assert colorcodes['red'] == '\033[31m'
