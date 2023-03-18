from santitools.colors import colorize, colorcodes, Colorizer, create_colorizer

def test_colorize():
    assert colorize('red', 'red') == '\033[31mred\033[0m'
    assert colorcodes['red'] == '\033[31m'
def test_colorizer():
    assert isinstance(create_colorizer(), Colorizer) and isinstance(Colorizer(), Colorizer)