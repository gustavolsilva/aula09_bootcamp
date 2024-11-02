# from loguru import logger
# from sys import stderr
# import getpass
# username = getpass.getuser()

from utils_log import log_decorator

# pydantic
# pandera

@log_decorator
def soma(x, y):
    return x + y

soma(2,3)
soma(2,7)