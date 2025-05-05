from aiogram.types import ChatMemberMember, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from tgbot.middlewares.i18n.i18n_format import localization_format_new


async def check_subscription(bot, user_id: int, chat_id: str) -> ChatMemberMember:
    member = await bot.get_chat_member(chat_id, user_id)
    return member


async def send_follow_channel(bot, user_id, chat_id, user_language):
    text = localization_format_new('send_channel_follow', user_language)
    keyboard = InlineKeyboardBuilder()
    keyboard.row(
        InlineKeyboardButton(text=localization_format_new('check_follow_button', user_language),
                             callback_data="check_follow"),
        InlineKeyboardButton(text=localization_format_new('no_thanks_text', user_language),
                             callback_data="no_thanks"),
    )

    await bot.send_message(chat_id, text, reply_markup=keyboard.as_markup())
