# from loguru import logger

# logger.debug("Um aviso para o desenvolvedor (ou eu mesmo) no futuro")
# logger.info("Informação importante do processo")
# logger.warning("Um aviso que algo vai parar de funcionar no futuro")
# logger.error("Aconteceu uma falha")
# logger.critical("Aconteceu uma que aborta a aplicacao")

import getpass
username = getpass.getuser()

print(username)