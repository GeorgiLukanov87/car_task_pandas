# utils/logger.py
import logging
import os


def setup_logger():
    logger = logging.getLogger('CarDataAnalyzer')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    if not os.path.exists('logs'):
        os.makedirs('logs')

    fh = logging.FileHandler('logs/car_data_analyzer.log')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger
