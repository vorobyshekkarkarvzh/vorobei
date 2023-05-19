from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from random import randint
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
BOT_TOKEN = '5279295188:AAG4yNjSSGU-LvkkKdJ2ZW-uGpXUvroj47A'
# Создаем экземпляр бота
bot = Bot(token=BOT_TOKEN)
# Создаем диспетчер для обработки команд
dp = Dispatcher(bot)
# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="GitHub", url="https://github.com/vorobyshekkarkarvzh")
    keyboard.add(url_button)
    await message.reply("Привет! Я бот, который может отправлять ссылки на разные ресурсы. Нажми на кнопку /help, чтобы узнать больше.", reply_markup=keyboard)
# Обработчик команды /help
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    # Создаем клавиатуру
    keyboard = types.InlineKeyboardMarkup()
    # Создаем кнопку
    url_button1 = types.InlineKeyboardButton(text="Discord 1", url="https://discord.com/channels/vorobyshekchirik#8905")
    url_button2 = types.InlineKeyboardButton(text="...", url="https://web.telegram.org/a/#1882801381")
    url_button3 = types.InlineKeyboardButton(text="Perm-ACOIN", url="https://perm-acoin.ru/")
    keyboard.add(url_button1, url_button2, url_button3)
    await message.reply("Чем я могу тебе помочь? Нажми на одну из кнопок, чтобы перейти на Discord или на сайт Perm-ACOIN.", reply_markup=keyboard)
# Запускаем бота
if __name__ == '__main__':
    executor.start_polling(dp)