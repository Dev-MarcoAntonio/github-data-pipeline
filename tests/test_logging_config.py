import logging
import pytest
from src.logging_config import setup_logging

@pytest.fixture
def logger():
    logger = logging.getLogger()
    original_handlers = logger.handlers[:]
    original_level = logger.level

    logger.handlers.clear()

    try:

        yield logger

    finally:
        for handler in logger.handlers[:]:
            handler.close()

        logger.handlers.clear()
        logger.handlers.extend(original_handlers)
        logger.setLevel(original_level)

def test_setup_logging_create_file(tmp_path,monkeypatch,logger):

    monkeypatch.chdir(tmp_path)

    logger.handlers.clear()

    setup_logging()

    assert (tmp_path / 'logs').exists()
    assert (tmp_path / 'logs' / 'pipeline.log').exists()

def test_setup_logging_level(logger):

    logger.handlers.clear()

    setup_logging()

    assert logger.level == logging.INFO

def test_setup_logging_handlers(logger):

    logger.handlers.clear()

    setup_logging()

    assert len(logger.handlers) == 2

def test_setup_logging_handler_types(logger):

    logger.handlers.clear()

    setup_logging()

    assert isinstance(logger.handlers[0], logging.FileHandler)
    assert isinstance(logger.handlers[1], logging.StreamHandler)

def test_setup_logging_handlers_level(logger):

    logger.handlers.clear()

    setup_logging()

    for handler in logger.handlers:
        assert handler.level == logging.INFO

def test_setup_logging_existing_handlers(logger):

    logger.handlers.clear()

    setup_logging()

    handlers_before = len(logger.handlers)

    setup_logging()

    assert len(logger.handlers) == handlers_before