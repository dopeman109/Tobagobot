import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

user_balances = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("💰 Add balance", callback_data='add_balance')]]
    await update.message.reply_text(
        "Welcome! Click button to add balance:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "add_balance":
        msg = (
            "💳 Payment instructions:\n"
            "1. Send exactly 15 TRX\n"
            "2. To address: TTBmcp3KckYDvdWYpdET8Kx5DCJF7YVbDE\n"
            "3. Wait 15 minutes for confirmation"
        )
        await query.edit_message_text(msg)

def main():
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    if not TOKEN:
        raise ValueError("Missing bot token!")
    
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == "__main__":
    main()
