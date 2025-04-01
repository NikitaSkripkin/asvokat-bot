from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7657366517:AAH6bzYPe8Ls0vPAAOKAhBpNZfZbNuM0AuA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Уголовное право", "Конституция"],
        ["Процессуальные права", "Контакты адвоката"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Добро пожаловать в юридического бота!\n\nВыберите интересующую вас тему:",
        reply_markup=reply_markup
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
