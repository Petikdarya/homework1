"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""

import ephem
import logging
from datetime import date, datetime
 


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text('Привет! Вызови команду planet c именем планеты')



def get_constel(update, context):
    text1 = 'Вызван /planet'
    print(text1)
    current_date = datetime.strftime(datetime.now(), '%Y/%m/%d')
    print(current_date)

    planets = {"Mercury": ephem.Mercury(current_date), 
    "Venus": ephem.Venus(current_date), 
    "Mars" : ephem.Mars(current_date), 
    "Jupiter": ephem.Jupiter(current_date), 
    "Saturn": ephem.Saturn(current_date), 
    "Uranus": ephem.Uranus(current_date), 
    "Neptune": ephem.Neptune(current_date)
    }
    
    planet = str(update.message.text.split()[1]).lower().capitalize()
    print(planet)
    
    if planets.get(planet):
        print(ephem.constellation(planets[planet]))
        update.message.reply_text(ephem.constellation(planets[planet]))
    else:
        print('Неправильно введена планета')
        update.message.reply_text('Неправильно введена планета')
    



def main():
    mybot = Updater("5036829698:AAF_44TGfETog694wy65UwIQS3CzBcloZ2Q", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_constel))
    

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
