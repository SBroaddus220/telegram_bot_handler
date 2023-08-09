#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script showcases how messages can be sent through a Telegram bot and how LogRecords can be handled by the message handler as defined in the logger configuration.
To use please replace the BOT_KEY and the CHAT_ID variables with your own bot key and chat id.
"""

BOT_KEY = ""
CHAT_ID = ""

import logging

from pathlib import Path

# Adds package to path
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from telegram_bot_handler.telegram_bot import TelegramBot


# **********
# Sets up logger
logger = logging.getLogger(__name__)

PROGRAM_LOG_FILE_PATH = Path(__file__).resolve().parent.parent / "program_log.txt"

LOGGER_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,  # Doesn't disable other loggers that might be active
    "formatters": {
        "default": {
            "format": "[%(levelname)s][%(funcName)s] | %(asctime)s | %(message)s",
        },
        "simple": {  # Used for console logging
            "format": "[%(levelname)s][%(funcName)s] | %(message)s",
        },
    },
    "handlers": {
        "logfile": {
            "class": "logging.FileHandler",  # Basic file handler
            "formatter": "default",
            "level": "INFO",
            "filename": PROGRAM_LOG_FILE_PATH.as_posix(),
            "mode": "a",
            "encoding": "utf-8",
        },
        "console_stdout": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": "DEBUG",
            "stream": "ext://sys.stdout",
        },
        "console_stderr": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": "ERROR",
            "stream": "ext://sys.stderr",
        },
        "telegram_bot": {   # Example telegram bot logging handler
            "class": "telegram_bot_handler.telegram_bot_handler.TelegramBotHandler",  # Custom handler
            "bot_key": BOT_KEY,
            "chat_id": CHAT_ID,
            "level": "WARNING",
        }
    },
    "root": {  # Simple program, so root logger uses all handlers
        "level": "DEBUG",
        "handlers": [
            "logfile",
            "console_stdout",
            "console_stderr",
        ]
    }
}


# **********
def example_log():
    logger.warning("This is a warning message.")
    
    
def send_message():
    telegram_bot = TelegramBot(BOT_KEY, CHAT_ID)
    telegram_bot.send_message("This is a test message.")


# **********
if __name__ == "__main__":
    import logging.config
    logging.disable(logging.DEBUG)
    logging.config.dictConfig(LOGGER_CONFIG)
    example_log()
    send_message()
    