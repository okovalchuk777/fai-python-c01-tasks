from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from spy import *
import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,  # use operator.div for Python 2
    '%': operator.mod,
    '^': operator.xor,
}


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await logging_received_msg(update, context)
    msg = f'Hello {update.effective_user.first_name}'
    # print(msg)
    await update.message.reply_text(f'{msg}')
    await logging_reply_msg(update, context, msg)


async def check_receiving_msg(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    await logging_received_msg(update, context)
    await update.message.reply_text(f'{msg}')
    await logging_reply_msg(update, context, msg)


async def addition_operation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await logging_received_msg(update, context)
    msg = update.message.text
    msg = msg.split()
    x = int(msg[1])
    y = int(msg[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')
    await logging_reply_msg(update, context, msg)


async def calc_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await logging_received_msg(update, context)
    msg = f'This is calc bot\n Enter command /calc in order start\n first enter the operation with two numbers (use a space to divide between digits and signs)\n Press Enter and the first operation will be performed\n then enter the sign and number through the space and press Enter and the calculator will work with the previous result\n If you want to start new calculations, enter the command "/calc_reset" and start again'
    await update.message.reply_text(msg)
    await logging_reply_msg(update, context, msg)


calc_result = 0


async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global calc_result
    await logging_received_msg(update, context)
    input_msg = update.message.text
    input_msg = input_msg.split()
    if len(input_msg) == 3:
        reply_msg = f'{calc_result} {input_msg[1]} {int(input_msg[2])} = {ops[input_msg[1]](calc_result, int(input_msg[2]))}'
        await update.message.reply_text(reply_msg)
        calc_result = ops[input_msg[1]](calc_result, int(input_msg[2]))
        await logging_reply_msg(update, context, reply_msg)
    elif len(input_msg) == 4:
        reply_msg = f'{int(input_msg[1])} {input_msg[2]} {int(input_msg[3])} = {ops[input_msg[2]](int(input_msg[1]), int(input_msg[3]))}'
        await update.message.reply_text(reply_msg)
        calc_result = ops[input_msg[2]](int(input_msg[1]), int(input_msg[3]))
        await logging_reply_msg(update, context, reply_msg)


async def calc_reset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global calc_result
    await logging_received_msg(update, context)
    reply_msg = f'Calculator reset'
    await update.message.reply_text(reply_msg)
    calc_result = 0
    await logging_reply_msg(update, context, reply_msg)
