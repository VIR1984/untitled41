import openai
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

openai.api_key='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'
token ='6256506777:AAFWWMoV48KLcPa-KtXvtjk4c9DiUQHMlD8'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name}. Какой у тебя вопро?')


async def ask(update, context):
        # Get the user's message

    message = update.message.text.split(" ", 1)[1]
    print(message)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{message}",
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text

        # Reply to the user's message with the generated response
    await update.message.reply_text(response)


app = ApplicationBuilder().token(token).build()
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), ask))
app.add_handler(CommandHandler("start", start))

app.run_polling()