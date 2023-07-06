import logging
from translate import Translator
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'token'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

ru_letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
en_letters = "abcdefghijklmnopqrstuvwxyz"


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    text = message.text
    if text[0].lower() in ru_letters:
        translator = Translator(from_lang="russian", to_lang="english")
    elif text[0].lower() in en_letters:
        translator = Translator(from_lang="english", to_lang="russian")
    else:
        await message.answer('Я тебя не понимаю')
        return
    translation = translator.translate(text)
    await message.answer(translation)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)