""" logger """
import logging
from flask import current_app as app


from utils.config import LOG_LEVEL

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    level=LOG_LEVEL,
                    datefmt='%Y-%m-%d %H:%M:%S')


# this is so that we can have log.debug(XXX) calls in the app
# without XXX being evaluated when not at debug level
# this allows args to log.debug & co. to be lambdas that will
# get called when the loglevel is right
# cf. datascience/occasions, in which the data printed in
# debug calls is costly to compute.
def wrapper_logging(level, *args):
    global logging
    if logging.getLogger().isEnabledFor(level):
        evaled_args = map(lambda a: a() if callable(a) else a,
                          args)
        logging.log(level, *evaled_args)

class Log(dict):
    def __init__(self, *args, **kwargs):
        super(Log, self).__init__(*args, **kwargs)
        self.__dict__ = self

app.log = Log()
app.log.critical = lambda *args: wrapper_logging(logging.CRITICAL, *args)
app.log.debug = lambda *args: wrapper_logging(logging.DEBUG, *args)
app.log.error = lambda *args: wrapper_logging(logging.ERROR, *args)
app.log.info = lambda *args: wrapper_logging(logging.INFO, *args)
app.log.warning = lambda *args: wrapper_logging(logging.WARNING, *args)
