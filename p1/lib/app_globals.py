"""The application's Globals object"""

import psycopg2
from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options
from DBUtils.PooledDB import PooledDB


class Globals(object):
    """Globals acts as a container for objects available throughout the
    life of the application

    """
    def __init__(self, config):
        """One instance of Globals is created during application
        initialization and is available during requests via the
        'app_globals' variable

        """
        self.cache = CacheManager(**parse_cache_config_options(config))
        self.dbpool = PooledDB(psycopg2, 10, database='baza1', user='user1',
        password='user1', host='localhost', port=5432)
