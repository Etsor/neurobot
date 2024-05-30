
from aiogram import Bot, Dispatcher, executor, types
from neiro.neuro_gen import generate_image
from neiro.neiro_assistant import get_response
from neiro.neiro_consult import get_advice
from config import TELEGRAM_TOKEN

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Нажми /help чтобы узнать что я умею')



@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer('Напишите команду /generate_image и ваш запрос чтобы сгенерировать картинку. Напишите команду /advice и ваш запрос чтобы получить совет')


@dp.message_handler(commands='advice')
async def advice(message: types.Message):
    user = message.get_args()
    response_text = await get_advice(user)
    await message.answer(response_text)

@dp.message_handler(commands='generate_image')
async def handle_message(message: types.Message):
    user = message.get_args()
    response_text = await get_response(user)
    user_text = response_text
    await message.reply(f'Вот твой улучшенный промпт: {user_text}')
    print(user_text)
    await message.reply('Идет генерация изображения')

    try:
        image_data = generate_image(user_text)
        await message.reply_photo(photo=image_data)
    except Exception as e:
        await message.reply(f"Произошла ошибка: {e}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)