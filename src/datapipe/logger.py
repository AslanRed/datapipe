import sys

from loguru import logger

logger.add("app.log", rotation="10 MB", level="DEBUG", colorize=True)
logger.add(sys.stderr, level="ERROR", colorize=True)
