import unittest
import logging
from car_data_analyzer.utils.logger import setup_logger


class TestLogger(unittest.TestCase):

    def test_logger(self):
        logger = setup_logger()
        self.assertIsInstance(logger, logging.Logger, "Logger should be an instance of logging.Logger")


if __name__ == '__main__':
    unittest.main()
