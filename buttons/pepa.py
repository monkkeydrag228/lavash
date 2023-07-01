import logging
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = '6020379569:AAHkVgr8XqBOpwkD4C-VBgiD8upWrF5d57c'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Добро пожаловать в бот Mars! Пожалуйста, выберите опцию",)
    await message.reply("Пожалуйста укажите кем вы являетесь))",reply_markup=menu)


menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👩🏿👨🏿Я родитель",callback_data="Я родак"),
            InlineKeyboardButton(text="👦🏿Я ученик",callback_data="Я ученик"),
            InlineKeyboardButton(text="👲🏿Я нодир",callback_data="Я нодир"),
        ],
    ],
)

menu_rodak = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="🏣О школе",),
        KeyboardButton(text="👶🏻Добавить ребенка"),
        ]
    ],
    resize_keyboard=True
)
    

menu_o_shkole = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Работы учеников",callback_data="Работы учеников"),
            InlineKeyboardButton(text="Преподователи",callback_data="Преподователи"),
        ],
        [
            InlineKeyboardButton(text="Отзывы",callback_data="Отзывы"),
            InlineKeyboardButton(text="Экскурсия по школе",callback_data="Экскурсия по школе"),
        ],
        [
            InlineKeyboardButton(text="Философия школы",callback_data="Философия школы"),
        ],
    ],
)

otziv =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="14-16 лет",callback_data="14-16 лет"),
            InlineKeyboardButton(text="8-10 лет",callback_data="8-10 лет"),
        ],
        [
            InlineKeyboardButton(text="Назад",callback_data="Назад")
        ]
    ]
)


@dp.callback_query_handler(text="Я родак")
async def echo(call: types.CallbackQuery):
    await call.message.answer("Добро пожаловать в бот Mars! Пожалуйста, выберите опцию",reply_markup=menu_rodak)


# Школа /
@dp.message_handler(text="🏣О школе")
async def send_welcome(message: types.Message):
    await message.delete()
    await message.answer("Выберите кнопку",reply_markup=menu_o_shkole)


@dp.callback_query_handler(text="Работы учеников")
async def echo(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_video(video="https://t.me/Back447/474?single")

@dp.callback_query_handler(text="Преподователи")
async def echo(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_video(video="https://t.me/Back447/479")

@dp.callback_query_handler(text="Отзывы")
async def echo(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="Отзывы",reply_markup=otziv)

@dp.callback_query_handler(text="14-16 лет")
async def echo(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_video(video="https://t.me/Back447/474?single")
    await call.message.answer_video(video="https://t.me/Back447/475")
    await call.message.answer(text="Работы учеников 14-16 лет")

@dp.callback_query_handler(text="8-10 лет")
async def echo(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_video(video="https://t.me/Back447/480")

# @dp.message_handler(text="Назад")
# async def send_welcome(message: types.Message):
#     await message.delete()
#     await message.answer(reply=menu_o_shkole)

@dp.callback_query_handler(text="Экскурсия по школе")
async def echo(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_video(video="https://t.me/Back447/481",)
    await call.message.answer(text="Экскурсия по школе")

@dp.callback_query_handler(text="Философия школы")
async def echo(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="Философия школы")
    await call.message.answer_video(video="https://t.me/Back447/482")
    

# Школа \

# Ученик /
@dp.callback_query_handler(text="Я ученик")
async def echo(call: types.CallbackQuery):
    await call.message.answer("Введите Id modme")

# Ученик\

@dp.callback_query_handler(text="Я нодир")
async def echo(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("привет родак")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)