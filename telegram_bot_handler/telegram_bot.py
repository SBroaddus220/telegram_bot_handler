#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module contains the TelegramBot class, which represents a Telegram Bot to interface with.
"""

import logging
import requests
from typing import Any

# **********
# Sets up logger
logger = logging.getLogger(__name__)


# **********
class TelegramBot:
    """Represents a Telegram bot that can send messages synchronously."""
    
    def __init__(self, bot_key: str, chat_id: str, url: str = "https://api.telegram.org") -> None:
        """Instantiates a new SynchronousTelegramBot object that can send messages synchronously to 
        the specified chat.

        Args:
            bot_key (str): Bot key for the Telegram bot.
            chat_id (str): Chat ID for the Telegram bot.
            url (str, optional): URL for Telegram bot API. Defaults to "https://api.telegram.org".
        """
        self.bot_key = bot_key
        self.chat_id = chat_id
        self.url = url
        

    def send_message(self, message: str, silent: bool = False, parse_mode: str = "HTML") -> Any:
        """Sends a message through the Telegram bot to the chat.

        Args:
            message (str): Message to send.
            silent (bool, optional): Whether to disable notifications. Defaults to False.
            parse_mode (str, optional): Mode for parsing entities in the message text. Defaults to "HTML".

        Returns:
            Any: JSON-encoded content of a response, if any.
        """
        request_object = {
            "chat_id": self.chat_id,
            "disable_notification": silent,
            "parse_mode": parse_mode,
            "text": message,
        }
        
        request_url = f"{self.url}/bot{self.bot_key}/sendMessage"
        response = requests.post(request_url, request_object)
        
        return response.json() 
        

# **********
if __name__ == "__main__":
    pass
