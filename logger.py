import logging

logger = logging.getLogger(
    name='logger',

)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler('app.log')
msg_format = "%(asctime)s %(name) %(levename) %(message)"
datefmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter(fmt=msg_format, datefmt=datefmt)
handler.setFormatter(formatter)
logger.addHandler(handler)
