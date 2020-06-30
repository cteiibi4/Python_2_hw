import logging
import logging.handlers

logger = logging.getLogger('app.'+ __name__)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - app.%(__name__)s %(message)')

fh = logging.handlers.TimedRotatingFileHandler('app.'+__name__+'.log', when='midnight', interval=1, encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    pass