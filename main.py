from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import BOT_TOKEN
from handlers import country_keyboard

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌍 Davlatingizni tanlang:",
        reply_markup=country_keyboard()
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
