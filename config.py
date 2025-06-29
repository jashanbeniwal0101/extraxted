#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_bot_token")
    API_ID = int(os.environ.get("API_ID", "your_api_id"))
    API_HASH = os.environ.get("API_HASH", "your_api_hash")
    AUTH_USERS = os.environ.get("AUTH_USERS", "1955406483")  # comma-separated IDs
