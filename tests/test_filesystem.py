import santitools.filesystem as fs

READ_PATH = './example.txt'
WRITE_PATH = './written.txt'
TUPLE = (None, b'hello world') 
def test_read_funs():
    assert fs.readfile(READ_PATH) == TUPLE

def test_write_funs(): 
    assert fs.writefile(WRITE_PATH, b'hello') == None