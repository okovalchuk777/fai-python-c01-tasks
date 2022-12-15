from typing import Optional
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, ConversationHandler
from bot_commands import *
from consts import *
import requests

app = ApplicationBuilder().token(TOKEN_ID).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("check", check_receiving_msg))
app.add_handler(CommandHandler("add", addition_operation))
app.add_handler(CommandHandler("calc_start", calc_start))
app.add_handler(CommandHandler("calc_help", calc_help))
app.add_handler(CommandHandler("calc_cancel", calc_cancel))


# Game Candy


async def candy_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await logging_received_msg(update, context)
    msg = f'Условие задачи: На столе лежит {initial_amount_of_sweets} конфет.\nИграют два игрока делая ходы по очереди.\nПервый ход  определяется жеребьёвкой.\nЗа один ход можно забрать не более чем 28 конфет.\nВыигрывает тот кто заберет последние конфеты.\nИспользуемые команды:\n/candy_help - справка\n/candy_start - запуск игр\n/candy_cancel - сброс/перезапуск игры (после окончания игры обязательно введите эту команду для возможности запуска новой игры)'
    await update.message.reply_text(msg)
    await logging_reply_msg(update, context, msg)


app.add_handler(CommandHandler("candy_help", candy_help))

count = 1

# вспомогательный список для умного бота с крайними точками
list_gen01 = [i for i in range(0, INITIAL_AMOUNT_OF_SWEETS + 1, MAX_NUMBER + 1)]


async def candy_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> range:
    global count
    global initial_amount_of_sweets
    global who_starts
    global first_player
    global second_player
    await logging_received_msg(update, context)
    msg = f'Меня зовут умный Бот и я бы хотел с тобой сыграть в игру "Конфеты"\nХочу пожелать тебе удачи\nПереходим к жеребьевке хода'
    await update.message.reply_text(msg)
    await logging_reply_msg(update, context, msg)
    time.sleep(2)
    first_player = 'Умный Бот'
    second_player = update.effective_user.first_name
    list_of_names = [first_player, second_player]
    who_starts = random.choice(list_of_names)
    if who_starts == first_player:
        msg02 = f'Игру начинает {who_starts}.\nПоехали!'
        await update.message.reply_text(msg02)
        await logging_reply_msg(update, context, msg02)
        n = initial_amount_of_sweets - list_gen01[-count]
        initial_amount_of_sweets -= n
        msg03 = p_print(who_starts, n, initial_amount_of_sweets)
        await update.message.reply_text(msg03)
        await logging_reply_msg(update, context, msg03)
        time.sleep(2)
        msg04 = f'Ваш ход, {second_player}.\nПомните - Вы можете брать от 1 до 28 конфет за один раз.\nСколько Вы берёте конфет?'
        await update.message.reply_text(msg04)
        await logging_reply_msg(update, context, msg04)
        count += 1
        return GAME_PROCESS
    elif who_starts == second_player:
        msg02 = f'Игру начинает {who_starts}.\nПоехали!\nВаш первый ход.\nПомните - Вы можете брать от 1 до 28 конфет за один раз.\nСколько Вы берёте конфет?'
        await update.message.reply_text(msg02)
        await logging_reply_msg(update, context, msg02)
        return GAME_PROCESS


async def candy_game_process(update: Update, context: ContextTypes.DEFAULT_TYPE) -> Optional[range]:
    global count
    global initial_amount_of_sweets
    global who_starts
    await logging_received_msg(update, context)
    input_msg = update.message.text
    while int(input_msg) < 1 or int(input_msg) > 28:
        msg = f'Возьмите корректное количество конфет (1-28)'
        await update.message.reply_text(msg)
        await logging_reply_msg(update, context, msg)
        return GAME_PROCESS
    else:
        if initial_amount_of_sweets > 0:
            initial_amount_of_sweets -= int(input_msg)
            msg01 = p_print(second_player, input_msg, initial_amount_of_sweets)
            await update.message.reply_text(msg01)
            await logging_reply_msg(update, context, msg01)
            if initial_amount_of_sweets <= 0:
                await candy_game_end_win_player()
                return
            else:
                time.sleep(2)
                n = initial_amount_of_sweets - list_gen01[-count]
                # 1-й случай, когда Smart Bot начинает первым или второй игрок (человек) берет недостаточно конфет до первой
                # критической точки (выигрыш Smart Botу обеспечен)
                if 1 <= n <= 28:
                    initial_amount_of_sweets -= n
                    msg02 = p_print(first_player, n, initial_amount_of_sweets)
                    await update.message.reply_text(msg02)
                    await logging_reply_msg(update, context, msg02)
                    if initial_amount_of_sweets <= 0:
                        await candy_game_end_win_bot()
                        return
                    else:
                        count += 1
                        msg04 = f'Ваш ход, {second_player}.\nПомните - Вы можете брать от 1 до 28 конфет за один раз.\nСколько Вы берёте конфет?'
                        await update.message.reply_text(msg04)
                        await logging_reply_msg(update, context, msg04)
                        return GAME_PROCESS
                # 2-й случай, когда первым начинал второй игрок (человек) и тоже берёт крайние точки (выигрыш человеку
                # обеспечен, если только он будет идти по критическим точкам. Если человек ошибётся - Smart Bot выиграет)
                elif n == 0:
                    n = random.randint(1, 28)
                    initial_amount_of_sweets -= n
                    msg02 = f'Ах хитрец, {second_player}!'
                    await update.message.reply_text(msg02)
                    await logging_reply_msg(update, context, msg02)
                    msg03 = p_print(first_player, n, initial_amount_of_sweets)
                    await update.message.reply_text(msg03)
                    await logging_reply_msg(update, context, msg03)
                    if initial_amount_of_sweets <= 0:
                        await candy_game_end_win_bot()
                        return
                    else:
                        count += 1
                        msg04 = f'Ваш ход, {second_player}.\nПомните - Вы можете брать от 1 до 28 конфет за один раз.\nСколько Вы берёте конфет?'
                        await update.message.reply_text(msg04)
                        await logging_reply_msg(update, context, msg04)
                        return GAME_PROCESS
                # 3-й случай, когда первым начинал второй игрок (человек) и перебрал конфет, т.е. пролетел первую критическую
                # точку (выигрыш Smart Botу обеспечен)
                elif n < 0:
                    count += 1
                    n = initial_amount_of_sweets - list_gen01[-count]
                    if 1 <= n <= 28:
                        initial_amount_of_sweets -= n
                        msg02 = p_print(first_player, n, initial_amount_of_sweets)
                        await update.message.reply_text(msg02)
                        await logging_reply_msg(update, context, msg02)
                        if initial_amount_of_sweets <= 0:
                            await candy_game_end_win_bot()
                            return
                        else:
                            count += 1
                            msg04 = f'Ваш ход, {second_player}.\nПомните - Вы можете брать от 1 до 28 конфет за один раз.\nСколько Вы берёте конфет?'
                            await update.message.reply_text(msg04)
                            await logging_reply_msg(update, context, msg04)
                            return GAME_PROCESS
    return


async def candy_game_end_win_bot():
    global initial_amount_of_sweets
    global count
    msg = f'Победил {first_player}. Не надо печалиться, {second_player}, у Вас всё впереди. Спасибо за игру!'
    url = f"https://api.telegram.org/bot{TOKEN_ID}/sendMessage?chat_id={CHAT_ID}&text={msg}"
    requests.get(url).json()
    logging_msg(msg)
    initial_amount_of_sweets = INITIAL_AMOUNT_OF_SWEETS
    count = 1
    return ConversationHandler.END


async def candy_game_end_win_player():
    global initial_amount_of_sweets
    global count
    msg = f'Победил {second_player}! Вы просто УМНИЧКА!!! Так держать!!!'
    url = f"https://api.telegram.org/bot{TOKEN_ID}/sendMessage?chat_id={CHAT_ID}&text={msg}"
    requests.get(url).json()
    logging_msg(msg)
    initial_amount_of_sweets = INITIAL_AMOUNT_OF_SWEETS
    count = 1
    return ConversationHandler.END


async def candy_cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global initial_amount_of_sweets
    global count
    await logging_received_msg(update, context)
    msg = f'Игра сброшена.'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
    await logging_reply_msg(update, context, msg)
    initial_amount_of_sweets = INITIAL_AMOUNT_OF_SWEETS
    count = 1
    return ConversationHandler.END


GAME_PROCESS = range(1)

conversation_handler = ConversationHandler(
    entry_points=[CommandHandler('candy_start', candy_start)],
    states={GAME_PROCESS: [MessageHandler(filters.TEXT & ~filters.COMMAND, candy_game_process)]},
    fallbacks=[CommandHandler('candy_cancel', candy_cancel)]
)

app.add_handler(conversation_handler)

# Некоторые сбитые с толку пользователи могут попытаться отправить созданному боту команды, которые он не понимает, поэтому можно
# использовать MessageHandler с фильтром filters.COMMAND, чтобы отвечать на все команды, которые не были распознаны предыдущими обработчиками.
# Примечание. Этот обработчик должен быть добавлен последним. Если его поставить первым, то он будет срабатывать до того,
# как обработчик CommandHandlers увидит обновление. После обработки обновления функцией unknown() все дальнейшие обработчики
# будут игнорируются.
# Чтобы обойти такое поведение, можно передать в метод dispatcher.add_handler(handler, group), помимо самой функции обработчика
# аргумент group со значением, отличным от 0. Аргумент group можно воспринимать как число, которое указывает приоритет обновления
# обработчика. Более низкая группа означает более высокий приоритет. Обновление может обрабатываться (максимум) одним
# обработчиком в каждой группе.
app.add_handler(MessageHandler(filters.COMMAND, unknown))

print('Server started')

app.run_polling()

if __name__ == '__main__':
    pass
