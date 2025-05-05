from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

start = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🇺🇸English",
                             callback_data="language_en"),
        InlineKeyboardButton(text="🇷🇺Русский", callback_data="language_ru"),
    ],
])

end_start = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Все верно!",
                             callback_data="lets_go"),
    ],
    [
        InlineKeyboardButton(text="Изменить язык", callback_data="change_language"),
        InlineKeyboardButton(text="Изменить часовой пояс", callback_data="change_utc")
    ]
])