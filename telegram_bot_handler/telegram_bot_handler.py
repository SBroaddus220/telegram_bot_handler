#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module contains the TelegramBotHandler class, which represents a logging handler for messages sent with the Telegram Bot.
"""

import time
import logging

from telegram_bot_handler.utilities import constants
from telegram_bot_handler.telegram_bot import TelegramBot

# **********
# Sets up logger
logger = logging.getLogger(__name__)


# **********
class TelegramBotHandler(logging.Handler):
    """Custom logging handler for the TelegramBot class."""
    
    def __init__(self, bot_key: str, chat_id: str, url: str = "https://api.telegram.org"):
        """Instantiates a new TelegramBotHandler object.

        Args:
            bot_key (str): Bot key for the Telegram bot.
            chat_id (str): Chat ID for the Telegram bot.
            url (str, optional): URL for Telegram bot API. Defaults to "https://api.telegram.org".
        """
        super().__init__()
        
        #: Telegram bot to receive messages
        self.bot = TelegramBot(bot_key, chat_id, url)
    
    
    def _format_telegram_message(self, record: logging.LogRecord) -> str:
        """Formats a log record into a message to send to the Telegram bot.
        This format is designed to look good as a Telegram message.

        Args:
            record (logging.LogRecord): Record to format.

        Returns:
            str: Formatted log record.
        """
        
        def format_category(category: str, value: str) -> str:
            """Formats a category and its value to be displayed in a log entry.

            Args:
                category (str): Category to format.
                value (str): Value to format.

            Returns:
                str: Formatted category and value.
            """
            return f"{category.ljust(max_category_length)} - {value}"
        
        # Manually add the asctime attribute to the record.
        # This is necessary because the asctime attribute is not innate to the LogRecord class.
        record.asctime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(record.created))
        
        # Records log record attributes
        categories = {}
        
        if hasattr(record, "funcName") and record.funcName:
            categories["Function"] = f"{record.funcName}"
        
        if hasattr(record, "asctime") and record.asctime:
            categories["Time"] = f"{record.asctime}"
        
        if hasattr(record, "process") and record.process:
            categories["PID"] = f"{record.process}"
            
        assert hasattr(record, "message"), "Log record does not have a message attribute. Please contact the developer."
        
        # Determines the maximum length of the categories in the log entry
        max_category_length = max(len(category) for category in categories.keys())
        
        # Formats lines
        formatted_category_lines = [format_category(category, value) for category, value in categories.items()]
        
        # Determines the maximum length of the lines in the log entry
        max_line_length = max(len(formatted_line) for formatted_line in formatted_category_lines + [record.message])
    
        # Assembles the log entry
        log_entry = ""
        
        log_entry += "<pre>"
        log_entry += f"{record.levelname.upper().center(min(max_line_length, constants.MAX_TELEGRAM_MONOSPACE_MESSAGE_CHARACTER_COUNT_MOBILE), '-')} \n"
        log_entry += "\n".join(formatted_category_lines)
        log_entry += f"\n\n{record.message}"
        log_entry += "</pre>"
        
        return log_entry


    def emit(self, record: logging.LogRecord) -> None:
        """Configures and sends logging records to the Telegram bot.

        Args:
            record (logging.LogRecord): Record to send to the Telegram bot.
        """
        # Assembles the log message
        log_entry = self._format_telegram_message(record)
        self.bot.send_message(log_entry)
        

# **********
if __name__ == "__main__":
    pass
