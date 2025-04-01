from telegram import ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7657366517:AAH6bzYPe8Ls0vPAAOKAhBpNZfZbNuM0AuA"

async def запуск(update, context: ContextTypes.DEFAULT_TYPE):
    клавиатура = [
        ["Уголовное право", "Конституция"],
        ["Административные права", "Контакты адвоката"]
    ]

    reply_markup = ReplyKeyboardMarkup(клавиатура, resize_keyboard=True)

    await update.message.reply_text(
        "Добро пожаловать в юридический бот!\n\nВыберите интересующую вас тему:",
        reply_markup=reply_markup
    )
