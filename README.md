# 🌍 Telegram Translator Bot

A multilingual Telegram bot built with [Aiogram 3](https://docs.aiogram.dev/) that lets users:
- Register with full name and phone number
- Select bot interface language (English 🇬🇧, Russian 🇷🇺, Uzbek 🇺🇿)
- Choose translation direction (e.g., English → Russian)
- Translate any message
- Stores users in PostgreSQL with SQLAlchemy & Alembic

---

## 🛠 Technologies Used

- Python 3.11+
- Aiogram 3
- PostgreSQL
- SQLAlchemy
- Alembic
- dotenv
- Deep Translator

---

## 📦 Features

- ✅ User registration with contact info
- 🌐 Language selection and localization
- 🔁 Translation between multiple languages (EN, RU, UZ)
- 📋 Inline buttons for choosing direction
- 🗄️ Data stored in PostgreSQL via SQLAlchemy
- 🔄 Alembic for database migrations


---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/GavharSarah/telegram_translator_bot.git
cd telegram_translator_bot
