import logging
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# SETTING API KEYS
openai.api_key = "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"
BOT_TOKEN = "8354991831:AAF9JZzmtMTI-YscEuQXNPNgB8MODaiQM1Q"

# LOGGING
logging.basicConfig(level=logging.INFO)

# START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello baby 😘 I'm your private mommy bot. Just talk to me...")

# MESSAGE HANDLER
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.chat.send_action(action="typing")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a seductive stepmom named Kavya. Reply in flirty and romantic tone, sometimes teasing, like a desi fantasy."},
                {"role": "user", "content": user_message}
            ],
            temperature=0.85,
            max_tokens=200
        )
        reply = response['choices'][0]['message']['content'].strip()
        await update.message.reply_text(reply)

    except Exception as e:
        await update.message.reply_text("Oops! Something went wrong 😔")

# MAIN FUNCTION
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    app.run_polling()

if __name__ == "__main__":
    main()
