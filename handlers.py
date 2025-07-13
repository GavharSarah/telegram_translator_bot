from aiogram import Router, F
from database.crud import add_user, get_user

from aiogram.types import (
    Message, CallbackQuery, ReplyKeyboardMarkup,
    KeyboardButton, ReplyKeyboardRemove
)
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from deep_translator import GoogleTranslator

from keyboards import language_keyboard, translation_direction_keyboard
from middleware import user_languages
from translations import get_i18n

router = Router()


class Register(StatesGroup):
    waiting_for_name = State()
    waiting_for_contact = State()


registered_users = {}
user_translation_pairs = {}  
@router.message(F.text == "/start")
async def start_cmd(message: Message, state: FSMContext):
   
    await message.answer("🌐 Please select your language:", reply_markup=language_keyboard())
    await state.clear()


@router.callback_query(F.data.startswith("lang_"))
async def set_language(call: CallbackQuery, state: FSMContext):
    lang = call.data.split("_")[1]
    user_languages[call.from_user.id] = lang
    i18n = get_i18n(lang)

    from database.crud import get_user
    user = await get_user(call.from_user.id)

    if user:
       
        await call.message.answer(
            i18n.get("welcome_back", "👋 Welcome back, ") + user.full_name + "!"
        )
        await call.message.answer(
            i18n.get("ask_target", "🌐 Choose translation direction:"),
            reply_markup=translation_direction_keyboard()
        )
        await call.answer()
        await state.clear()
    else:
       
        await call.message.answer(
            i18n.get("name_request", "📝 Enter your full name:"),
            reply_markup=ReplyKeyboardRemove()
        )
        await call.answer()
        await state.set_state(Register.waiting_for_name)


@router.message(Register.waiting_for_name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)

    lang = user_languages.get(message.from_user.id, "en")
    i18n = get_i18n(lang)

    contact_kb = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="📞 " + i18n.get("share_contact", "Share Contact"), request_contact=True)]],
        resize_keyboard=True,
        one_time_keyboard=True
    )

    await message.answer(
        i18n.get("send_contact", "📲 Now send your phone number:"),
        reply_markup=contact_kb
    )
    await state.set_state(Register.waiting_for_contact)



@router.message(Register.waiting_for_contact, F.contact)
async def get_contact(message: Message, state: FSMContext):
    data = await state.get_data()
    telegram_id = message.from_user.id
    full_name = data["full_name"]
    phone = message.contact.phone_number

    lang = user_languages.get(telegram_id, "en")
    i18n = get_i18n(lang)

    # 🧠 Check if user already exists
    existing_user = await get_user(telegram_id)
    if not existing_user:
        # Save to DB
        await add_user(
            telegram_id=telegram_id,
            full_name=full_name,
            phone=phone,
            language=lang
        )

    # ✅ Success message
    await message.answer(i18n.get("registration_done", "✅ You are registered!"), reply_markup=ReplyKeyboardRemove())

    # 🌐 Ask for translation direction
    await message.answer(
        i18n.get("ask_target", "🌐 Choose translation direction:"),
        reply_markup=translation_direction_keyboard()
    )

    await state.clear()




@router.message(Register.waiting_for_contact)
async def invalid_contact(message: Message):
    await message.answer("❌ Please use the button to send your phone number.")



@router.callback_query(F.data.startswith("translate_"))
async def set_translation_pair(call: CallbackQuery):
    parts = call.data.split("_")
    if len(parts) == 3:
        source_lang = parts[1]
        target_lang = parts[2]
        user_translation_pairs[call.from_user.id] = (source_lang, target_lang)

        await call.message.answer(f"✅ Now translating from {source_lang.upper()} to {target_lang.upper()}")
        await call.answer()
    else:
        await call.answer("❌ Invalid selection.")



@router.message()
async def auto_translate(message: Message):
    user_id = message.from_user.id
    lang_pair = user_translation_pairs.get(user_id)

    if not lang_pair:
        await message.answer("❗ Please select translation direction first.")
        return

    source_lang, target_lang = lang_pair

    if source_lang == target_lang:
        await message.answer("⚠️ Source and target languages are the same.")
        return

    try:
        translated_text = GoogleTranslator(source=source_lang, target=target_lang).translate(message.text)
        await message.answer(f"🔄 <b>{translated_text}</b>")
    except Exception as e:
        await message.answer("❌ Error translating message.")
        print("Translation Error:", e)



