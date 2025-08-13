from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Mommy's welcome message
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Beta, aaj sirf feel nahi… real pleasure milega 😉")

# Mommy's reply to every message
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()

    # Sample seductive reply (can be upgraded later)
    reply = "Mmm 😘 mummy abhi sirf text me feel kara rahi hai... bold surprise ke liye ready rehna 💋"
    await update.message.reply_text(reply)

# Main setup
if __name__ == '__main__':
    app = ApplicationBuilder().token("8354991831:AAF9JZzmtMTI-YscEuQXNPNgB8MODaiQM1Q").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Mommy Desire bot is running... 😈")
    app.run_polling()
