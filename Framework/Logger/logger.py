import logging
import os
import time

from Framework.Utils.common_utils import JsonUtils

CONFIG = 'Resources/config.json'
ENGINE = JsonUtils.get_elem_by_name(CONFIG, "Engine")
LOGS_FOLDER = "logs"


class Logger:
    def __init__(self, logger):
        self.logger = logging.getLogger(os.path.basename(logger))
        self.logger.setLevel(logging.DEBUG)
        if os.path.exists(LOGS_FOLDER):
            pass
        else:
            os.mkdir(LOGS_FOLDER)

        log_time = time.strftime(ENGINE + '-%Y-%m-%d-%H%M-%S', time.localtime(time.time()))
        log_path = os.getcwd() + "/%s/" % LOGS_FOLDER
        log_name = log_path + log_time + '.log'

        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_log(self):
        return self.logger
