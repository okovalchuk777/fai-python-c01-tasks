from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime

log_file_location = 'log.csv'


async def logging_received_msg(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    with open(log_file_location, 'a', encoding='utf-8') as file:
        file.write(
            f"{update.message.date},{update.effective_user.first_name},{update.effective_user.last_name},{update.effective_user.id},{update.effective_chat.id}, {update.message.text}\n")


async def logging_reply_msg(update: Update, context: ContextTypes.DEFAULT_TYPE, msg) -> None:
    with open(log_file_location, 'a', encoding='utf-8') as file:
        file.write(f"{datetime.datetime.now()},{context.bot.first_name},{context.bot.last_name},{context.bot.id}, {msg}\n")


def logging_msg(msg):
    with open(log_file_location, 'a', encoding='utf-8') as file:
        file.write(f"{datetime.datetime.now()}, {msg}\n")
