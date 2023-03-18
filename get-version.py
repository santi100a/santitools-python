
def open_file(f):
    try:
        f = open(f, 'r')
        data = f.read()
        f.close()
        return (None, data)
    except Exception as e:
            return (e, None)
def parse_toml(st):
    try:
        from toml import loads
        return (None, loads(st))
    except Exception as e:
         return (e, None)

err, st = open_file('pyproject.toml')
if err:
    from sys import exit, stderr
    print(f'An error ocurred: {err}', file=stderr)
    exit(1)
else:
    err, d = parse_toml(st)
    if err:
        from sys import exit, stderr
        print(f'An error ocurred: {err}', file=stderr)
        exit(1)
    else:
        print(d['project']['version'])