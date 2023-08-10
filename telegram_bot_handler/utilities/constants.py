#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module holds constants used by other project modules.
"""

import logging

# **********
# Sets up logger
logger = logging.getLogger(__name__)

# **********
# Constants
#: Defines the maximum number of monospace characters that can fit on the desktop Telegram web application.
MAX_TELEGRAM_MONOSPACE_MESSAGE_CHARACTER_COUNT_DESKTOP_WEB_APP = 52

#: Defines the maximum number of monospace characters that can fit on an iPhone 8 Telegram app screen.
MAX_TELEGRAM_MONOSPACE_MESSAGE_CHARACTER_COUNT_MOBILE = 31

# **********
if __name__ == "__main__":
    pass
