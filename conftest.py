import os

import allure
import pytest

from dotenv import load_dotenv

env = os.getenv("ENV")

if env == 'local':
    load_dotenv("env/.env.local")
elif env == 'staging':
    load_dotenv("env/.env.staging")
else:
    load_dotenv("env/.env.local")