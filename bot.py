import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

# Lietotāja bilances glabāšana (vienkārši, RAM)
user_balances = {}

# Start komanda
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_balances.setdefault(user_id, 0)

    keyboard = [
        [InlineKeyboardButton("💰 Add balance", callback_data='add_balance')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome! What do you want to do?", reply_markup=reply_markup)

# Callback: Add balance
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "add_balance":
        amount = 15
        trx_amount = 63.289571  # piemērs
        trx_address = "TTBmcp3KckYDvdWYpdET8Kx5DCJF7YVbDE"

        msg = f"▶️ Insert the replenishment amount
Minimum top-up amount: {amount}€

"
        msg += f"💸 Price for payment in TRX cryptocurrency: {trx_amount}
"
        msg += f"⏳ Transfer within 15 minutes exactly this amount to the address:
`{trx_address}`"

        await query.edit_message_text(msg, parse_mode="Markdown")

def main():
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    app.run_polling()

if __name__ == "__main__":
    main()
