import sys, importlib
print('Python version:', sys.version.replace('\n',' '))
print('Executable:', sys.executable)
for pkg in ('pandas','numpy'):
    try:
        m = importlib.import_module(pkg)
        print(pkg, 'version', getattr(m, '__version__', 'unknown'))
    except Exception as e:
        print(pkg, 'import error:', repr(e))
