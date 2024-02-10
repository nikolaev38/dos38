import telebot #Основная библиотека бота
import datetime # Время
import sqlite3 # База данных
import logging #Логирование

logger = logging.getLogger('logger')

bot = telebot.TeleBot('6836309396:AAH0bJ4hV2nG_fb6QTl4GeVfsR-rLI3YYDA', parse_mode='MARKDOWN') #Подключение к сети бота



bot.infinity_polling(none_stop=True, interval=0)