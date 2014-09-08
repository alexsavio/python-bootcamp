import logging
import time
logging.basicConfig(filename='myapp.log', filemode='w',
                    level=logging.INFO,
                    format='%(asctime)s %(message)s')

def do_something():
    logger = logging.getLogger('do_something')
    logger.info('Doing something')
    time.sleep(3)

logger = logging.getLogger('main')

logger.info('Started')

do_something()

logger.info('Finished')
