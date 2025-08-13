from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = "8354991831:AAF9JZzmtMTI-YscEuQXNPNgB8MODaiQM1Q"  # Replace this

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello baby, Mommy Desire is ready for your naughty chats 😘")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "kiss" in text:
        await update.message.reply_text("Mmmuah 😚 Mommy's lips are all yours baby...")
    else:
        await update.message.reply_text("Mommy is listening, tell me more... 😉")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()
