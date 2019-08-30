import logging

def getlogger(mod_name:str, filepath:str):
    logger = logging.getLogger(mod_name)
    logger.setLevel(logging.INFO)
    logger.propagate = False #阻止传给父logger

    handler = logging.FileHandler(filepath)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(fmt="%(asctime)s [%(name)s %(funcName)s] %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return  logger



















