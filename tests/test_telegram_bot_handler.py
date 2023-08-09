#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" 
Test cases for the Telegram bot logging handler class.
"""

import logging

import unittest
from unittest import mock

from telegram_bot_handler.telegram_bot import TelegramBot
from telegram_bot_handler.telegram_bot_handler import TelegramBotHandler

# ****************
class TestTelegramBotHandler(unittest.TestCase):
    
    # ****************
    # Emit tests
    def test_emit(self):
        handler = TelegramBotHandler("test_key", "test_chat_id")
        record = logging.LogRecord(name="test", level=logging.INFO, pathname=None, lineno=None, msg="Test log", args=None, exc_info=None)
        record.message = "Test log"  # Guaranteed in a real LogRecord object

        # Mock the send_message method
        with mock.patch.object(TelegramBot, "send_message") as mock_send_message:
            handler.emit(record)

        # Check that send_message was called with the correctly formatted message
        formatted_record = handler._format_telegram_message(record)
        mock_send_message.assert_called_once_with(formatted_record)
    

# ****************
if __name__ == '__main__':
    unittest.main()
    