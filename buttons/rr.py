from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

menu= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ota onalar", callback_data="Ota onalar"),
            InlineKeyboardButton(text="O'quvchi", callback_data="O'quvchi"),
            InlineKeyboardButton(text="Mehmon", callback_data="Mehmon"),
        ]
    ]
)

menu2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Maktab haqida"),
            KeyboardButton(text="Farzandni ro'yhatdan o'tkazish"),
        ]
    ],
    resize_keyboard=True
)