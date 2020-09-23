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

# wordList = [Word("upbringing", "opvoeding"), Word("offspring", "nakomeling"), Word("to resemble", "lijken op"),
#             Word("engaged", "verloofd"), Word("infant", "klein kind"), Word("youth", "jongere"),
#             Word("ancestor", "voorouder"), Word("nageslacht", "posterity"), Word("hereditary", "erfelijk"),
#             Word("humanity", "mensheid"), Word("cemetary", "begraafplaats"), Word("te descend", "afstammen"),
#             Word("tribe", "stam"), Word("ally", "bondgenoot"), Word("associate", "relatie"),
#             Word("parental", "ouderlijk"), Word("guardian", "voogd"), Word("to rear", "opvoeden"),
#             Word("to alienate", "vervreemden"), Word("innate", "aangeboren"), Word("to fancy", "verliefd zijn op"),
#             Word("marital", "huwelijks-"), Word("adultery", "overspel"), Word("segregation", "rassenscheiding"),
#             Word("virgin", "maagd"), Word("bachelor", "vrijgezel"), Word("single", "alleenstaand"),
#             Word("to accompany", "begeleiden"), Word("tenant", "huurder"), Word("gap", "kloof"), Word("row", "ruzie"),
#             Word("to maintain", "onderhouden"), Word("affection", "genegenheid"), Word("trouw", "faithful"),
#             Word("to age", "ouder worden"), Word("mutual", "wederzijds"), Word("guestroom", "logeerkamer"),
#             Word("coffin", "doodskist"), Word("deceased", "overleden"), Word("orphan", "wees"),
#             Word("bejaarden", "elderly"), Word("bekend", "familiar"), Word("minderjarige", "minor"),
#             Word("kennismaken met", "to make acquintance"), Word("passen op", "to look after"),
#             Word("opvoeden", "to raise"), Word("worden (leeftijd)", "to turn"), Word("jeugd", "childhood"),
#             Word("kennis", "acquaintance"), Word("delen", "to share"), Word("puber", "adolescent"),
#             Word("verkering hebben met", "to date"), Word("uitmaken", "to split up"), Word("begrafenis", "funeral"),
#             Word("weduwe", "widow")]

bot = MemriseBot(username, password, course_id)
bot.login()
