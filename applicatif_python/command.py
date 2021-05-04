import os


def screenClear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        os.system('export TERM=xterm')
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


