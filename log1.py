
import logging

def setup_logger():
    # Log File name
    log_file = 'C:/Python27/a.log'
    log = logging.getLogger('LINK_MONITOR')
    log.setLevel(logging.DEBUG)
    #Create file log handler and set level to debug
    #fh = logging.handlers.RotatingFileHandler(log_file, maxBytes=(MAX_LOG_BYTES/2), backupCount=1)
    fh = logging.FileHandler(log_file)
    #fh = logging.StreamHandler()
    fh.setLevel(logging.DEBUG)

    #Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    #Add formatter to log handlers
    fh.setFormatter(formatter)

    #Add log handlers to logger
    log.addHandler(fh)
    #logging.debug(log_file, 'jfkjdslkj')
    return log


log = setup_logger()
log.debug("hi")
    

