from aiogram.types import TelegramObject
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from translations import get_i18n


user_languages = {}

class I18nMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: TelegramObject, data: dict):
        user = getattr(event, "from_user", None)
        lang_code = "en"

        if user:
            lang_code = user_languages.get(user.id, "en")

        data["i18n"] = get_i18n(lang_code)
        await handler(event, data)



