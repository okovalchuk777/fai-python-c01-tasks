# https://telegram.org/
# https://github.com/python-telegram-bot/python-telegram-bot
# You will find it at t.me/chuchundra_777_bot
# Use this token to access the HTTP API:
# 5608756154:AAEbgCgoCNpBOpF2Yl2sPCNGrNGvd19DFPc

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')

app = ApplicationBuilder().token("5608756154:AAEbgCgoCNpBOpF2Yl2sPCNGrNGvd19DFPc").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("check", check_receiving_msg))
app.add_handler(CommandHandler("add", addition_operation))
app.add_handler(CommandHandler("calc", calc))
app.add_handler(CommandHandler("calc_help", calc_help))
app.add_handler(CommandHandler("calc_reset", calc_reset))

print('Server started')

app.run_polling()


if __name__ == '__main__':
    pass
