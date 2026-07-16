from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "TOKEN_BU_YERGA_YOZILMAYDI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎟 Bilet sotib olish", url="https://SIZNING-TOLOV-LINKINGIZ")],
        [InlineKeyboardButton("🎟 Купить билет", url="https://SIZNING-TOLOV-LINKINGIZ")]
    ]

    await update.message.reply_text(
        "Tilni tanlang / Выберите язык:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot ishga tushdi...")
app.run_polling()
