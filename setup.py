"""Install packages as defined in this file into the Python environment."""
from setuptools import setup, find_packages

setup(
    name="vemestael_esport_bot",
    author="Vemestael",
    author_email="volodimir.grigoryev@gmail.com",
    url="https://github.com/Vemestael/vemestael_esport_bot",
    description="Telegram bot to display the list of matches for the games Dota 2 and cs:go",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "python-telegram-bot==13.5",
        "requests==2.25.1",
        "easysettings==4.0.0",
        "python-dotenv==0.17.1",
    ],
    entry_points={
        "console_scripts": [
            "vemestael_esport_bot=src.vemestael_esport_bot:main",
        ]
    },
)