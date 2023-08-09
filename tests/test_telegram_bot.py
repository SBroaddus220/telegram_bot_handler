#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" 
Test cases for the Telegram bot implementation class.
"""

import requests

import unittest
from unittest import mock

from telegram_bot_handler.telegram_bot import TelegramBot

# ****************
class TestSynchronousTelegramBot(unittest.TestCase):
    
    # ****************
    # Send message tests
    def test_send_message(self):
        bot = TelegramBot("test_key", "test_chat_id")

        # Mock the post request
        with mock.patch.object(requests, "post") as mock_post:
            mock_post.return_value.json.return_value = {"ok": True}  # Mock the json method of the response
            response = bot.send_message("Test message")

        # Check that post was called with the correct parameters
        mock_post.assert_called_once_with(
            "https://api.telegram.org/bottest_key/sendMessage",
            {
                "chat_id": "test_chat_id",
                "disable_notification": False,
                "parse_mode": "HTML",
                "text": "Test message",
            },
        )

        # Check that the response was as expected
        assert response == {"ok": True}
    

# ****************
if __name__ == '__main__':
    unittest.main()
    