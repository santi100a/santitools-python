from typing import Coroutine
from io import FileIO
from codecs import decode

def readfile(filename: str, encoding = None) -> \
tuple[None | BaseException, bytes | None]:
    __doc__ = """
    Reads a file synchronously. \n
    Returns a tuple which contains either an ``Exception`` and ``None`` (in case an 
    error occurred), or ``None`` and a ``bytes`` object.
    """
    try:
        file_stream: FileIO = open(filename, 'rb')
        result = file_stream.read()
        file_stream.close()
        data = decode(result, encoding) if encoding else result
        tup = (None, data)
        return tup
    except BaseException as e:
        return (e, None)

def writefile(filename: str, data: bytes) -> BaseException | None:
    """
    Writes ``data`` to file ``filename`` synchronously. \n
    Returns either an ``Exception`` (in case an 
    error occurred), or ``None``.
    """
    try:
        file_stream: FileIO = open(filename, 'wb')
        file_stream.write(data)
        file_stream.close()

        return None
    except BaseException as e:
        return e
def append(filename: str, data: bytes) -> BaseException | None:
    """
    Appends ``data`` to file ``filename`` synchronously. \n
    Returns either an ``Exception`` (in case an 
    error occurred), or ``None``.
    """
    try:
        file_stream: FileIO = open(filename, 'ab')
        file_stream.write(data)
        file_stream.close()

        return None
    except BaseException as e:
        return e

def delete(filename: str) -> BaseException | None:
    """
    Deletes file ``filename`` synchronously. \n
    Returns either an ``Exception`` (in case an 
    error occurred), or ``None``.
    """
    try:
        from os import remove
        remove(filename)
        return None
    except BaseException as e:
        return e

# Async 
async def readco(filename, encoding=None) -> \
Coroutine[object, object, tuple[None | BaseException, bytes | None]]:
    return readfile(filename, encoding)
async def writeco(filename, data) -> Coroutine[object, object, BaseException | None]:
    return writefile(filename, data)
async def appendco(filename, data) -> Coroutine[object, object, BaseException | None]:
    return append(filename, data)
async def deleteco(filename) -> Coroutine[object, object, BaseException | None]:
    return delete(filename)
def readcall(*args):
    from warnings import warn
    from __deprecated__ import readcall as rc
    warn('readcall is deprecated. Use readco instead.', DeprecationWarning)
    return rc(*args)
def writecall(*args):
    from warnings import warn
    from __deprecated__ import writecall as wc
    warn('writecall is deprecated. Use writeco instead.', DeprecationWarning)
    return wc(*args)
def appendcall(*args):
    from warnings import warn
    from __deprecated__ import appendcall as ac
    warn('appendcall is deprecated. Use appendco instead.', DeprecationWarning)
    return ac(*args)
def deletecall(*args):
    from warnings import warn
    from __deprecated__ import deletecall as dc
    warn('deletecall is deprecated. Use deleteco instead.', DeprecationWarning)
    return dc(*args)