from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def language_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en"),
            InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru"),
            InlineKeyboardButton(text="🇺🇿 O‘zbek", callback_data="lang_uz"),
        ]
    ])

def translation_direction_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 Uzbek → 🇬🇧 English", callback_data="translate_uz_en"),
            InlineKeyboardButton(text="🇷🇺 Russian → 🇬🇧 English", callback_data="translate_ru_en"),
        ],
        [
            InlineKeyboardButton(text="🇬🇧 English → 🇺🇿 Uzbek", callback_data="translate_en_uz"),
            InlineKeyboardButton(text="🇬🇧 English → 🇷🇺 Russian", callback_data="translate_en_ru"),
        ],
        [
            InlineKeyboardButton(text="🇺🇿 Uzbek → 🇷🇺 Russian", callback_data="translate_uz_ru"),
            InlineKeyboardButton(text="🇷🇺 Russian → 🇺🇿 Uzbek", callback_data="translate_ru_uz"),
        ]
    ])









