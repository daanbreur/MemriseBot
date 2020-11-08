#  Copyright (c) 2020.
#  Created By: Daan Breur

from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from MemriseBot import MemriseBot
from configparser import ConfigParser
from utils import Word


Config = ConfigParser()
Config.read('config.ini')
username = Config.get('account', 'username')
password = Config.get('account', 'password')
course_id = Config.get('course', 'course_id')

bot = MemriseBot(username, password, course_id)
bot.login()
