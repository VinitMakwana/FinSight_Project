'''
Logger Utility
'''
import logging
from pathlib import Path

log_folder = Path('logs')
log_folder.mkdir(exist_ok=True)

log_file = log_folder/ 'project.log'

def get_logger(name:str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger