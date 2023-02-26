import logging
import sys
sys.path.append('')
def setup_custom_logger(name,filename):
    logging.basicConfig(level=logging.INFO, filename=filename, filemode="a",format='%(asctime)s - %(name)s  - %(levelname)s - %(module)s - %(message)s')
    logging.FileHandler(filename)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    return logger