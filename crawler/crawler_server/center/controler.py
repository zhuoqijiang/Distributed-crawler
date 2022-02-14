import concurrent.futures.thread
import logging
from concurrent.futures import ThreadPoolExecutor


class Controler:
    _pool = concurrent.futures.thread.ThreadPoolExecutor
    _pool_status = 0
    pool_size = 0

    @staticmethod
    def init():
        Controler._pool = ThreadPoolExecutor(max_workers=2)
        Controler._pool_status = 1
        Controler._pool_size = 2

    @staticmethod
    def add(task):
        Controler._pool.submit(task)

    @staticmethod
    def change_thread_pool_size(size):
        Controler._pool.shutdown()
        Controler._pool = ThreadPoolExecutor(max_workers=size)
        logging.info("change thread as {}".format(size))



