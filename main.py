from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

from config import BOT_TOKEN
from handlers import country_keyboard, PRICES


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌍 Davlatingizni tanlang:",
        reply_markup=country_keyboard()
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    country = query.data

    if country == "uzbekistan":
        await query.message.reply_text(
            "❌ Kechirasiz!\n\nO'zbekiston uchun bilet sotilmaydi."
        )
        return

    if country == "other":
        await query.message.reply_text(
            "🌍 Boshqa davlatlar keyingi sahifada qo'shiladi."
        )
        return

    price = PRICES[country]

    await query.message.reply_text(
        f"🎟 Bilet narxi: {price}\n\nDavom etish uchun to'lov tugmasini bosing."
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Bot ishga tushdi...")
    app.run_polling()


if __name__ == "__main__":
    main()
