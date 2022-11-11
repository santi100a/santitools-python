# Synchronous Filesystem API
def readsync(filename: str):
    """
    Reads a file and returns the contents. \r\n
    If the file does not exist, returns None.
    """
    try:
        return open(filename, 'r').read()
    except FileNotFoundError:
        return None
def writesync(filename: str, data: str):
    """
    Writes data to a file. \r\n
    If the file does not exist, it will be created. \r\n
    This erases the original file's contents, and overwrites them \r\n
    with the new data you specify. \r\n
    It returns a boolean, indicating whether or not the write was successful. \r\n
    """
    try:
        open(filename, 'w').write(data)
        return True
    except FileExistsError:
        return False
def appendsync(filename: str, data: str):
    """
    Appends data to a file.\r\n
    If the file does not exist, it will be created.\r\n
    This adds your data to the original file's contents, and appends them
    to its end.\r\n
    It returns a boolean, indicating whether or not the append was successful.
    """
    try:
        open(filename, 'a').write(data)
        return True
    except:
        return False
def deletesync(filename: str):
    """
    Deletes a file. \n
    ! Remember to avoid deleting important files. \n
    ! This will delete the file, and not just erase its contents.
    It returns a boolean, indicating whether or not the delete was successful.
    NOTE: If the file does not exist, it will return False (the delete will fail).
    """
    try:
        import os
        os.remove(filename)
        return True
    except:
        return False
# Callback-based Filesystem API

def readcall(filename: str, callback: callable):
    """
    Reads a file and returns the contents. \r\n
    If the file does not exist, it passes None to the callback.
    """
    try:
        callback(open(filename, 'r').read(), None)
    except Exception as e:
        callback(None, e)
def writecall(filename: str, data: str, callback: callable):
    """
    Writes data to a file. \r\n
    If the file does not exist, it will be created. \r\n
    This erases the original file's contents, and overwrites them with the new data \r\n
    you specify. \r\n
    It passes nothing to the callback in case everything is okay, and it passes an \r\n
    Exception to the callback in case one happened. \r\n
    """
    try:
        open(filename, 'w').write(data)
        callback(None)
    except Exception as e:
        callback(e)
def appendcall(filename: str, data: str, callback: callable):
    """
    Appends data to a file.\r\n
    If the file does not exist, it will be created.\r\n
    This adds your data to the original file's contents, and appends them
    to its end.\r\n
    It passes nothing to the callback in case everything is okay, and it passes an \r\n
    Exception to the callback in case one happened. \r\n
    """
    try:
        open(filename, 'a').write(data)
        callback(None)
    except Exception as e:
        callback(e)
def deletecall(filename: str, callback: callable):
    """
    Deletes a file. \n
    ! Remember to avoid deleting important files. \n
    ! This will delete the file, and not just erase its contents.
    It passes nothing to the callback in case everything is okay. \r\n
    NOTE: If the file does not exist, it will pass an Exception to the callback (the delete will fail).
    """
    try:
        import os
        os.remove(filename)
        callback(None)
    except Exception as e:
        callback(e)
# Asynchronous (coroutine-based) Filesystem API
async def readco(filename: str):
    """
    Reads a file and returns the contents as a co-routine. \r\n
    If the file does not exist, returns None.
    """
    try:
        return open(filename, 'r').read()
    except:
        return None
async def writeco(filename: str, data: str):
    """
    Writes data to a file. \r\n
    If the file does not exist, it will be created. \r\n
    This erases the original file's contents, and overwrites them \r\n
    with the new data you specify. \r\n
    It returns a boolean as a co-routine, indicating whether or not the write was successful. \r\n
    """
    try:
        open(filename, 'w').write(data)
        return True
    except:
        return False
async def appendco(filename: str, data: str):
    """
    Appends data to a file.\r\n
    If the file does not exist, it will be created.\r\n
    This adds your data to the original file's contents, and appends them
    to its end.\r\n
    It returns a boolean as a co-routine, indicating whether or not the append was successful.
    """
    try:
        open(filename, 'a').write(data)
        return True
    except:
        return False

async def deleteco(filename: str):
    """
    Deletes a file. \r\n
    ! Remember to avoid deleting important files. \r\n
    ! This will delete the file, and not just erase its contents. \r\n
    It returns a boolean as a co-routine, indicating whether or not the delete was successful.
    NOTE: If the file does not exist, it will return False as a co-routine (the delete will fail).
    """
    try:
        import os
        os.remove(filename)
        return True
    except:
        return False