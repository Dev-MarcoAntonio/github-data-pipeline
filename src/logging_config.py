import logging
from pathlib import Path

def setup_logging():

    logger = logging.getLogger()
    
    if logger.handlers:
        return

    caminho = Path('logs')
    caminho.mkdir(exist_ok= True,parents= True)

    file_handler = logging.FileHandler(
        caminho / 'pipeline.log',
        encoding= 'utf-8'
    )

    console_handler = logging.StreamHandler()

    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    file_handler.setLevel(logging.INFO)
    console_handler.setLevel(logging.INFO)
    

    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)