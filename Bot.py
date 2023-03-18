import asyncio
import json
import re
import sqlite3

import aioschedule
from aiogram import types, Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token='5722882971:AAGY9gu6FF9HZFIUVEheS4PzR_wdl_mTi8o')
dp = Dispatcher(bot)

rk = [0]
rozklad_for_week_Zn = {}
rozklad_for_week_Ch = {}
rozklad_for_week_Zn_1 = {}
rozklad_for_week_Ch_1 = {}
rozklad_for_P = {}
rozklad_for_V = {}
rozklad_for_C = {}
rozklad_for_Ch = {}
rozklad_for_Py = {}
rozklad_for_Cub = {}
rozklad_for_N = {}

list_para = []
dict_para = {}

rozklad_for_Chiselnik = {}
rozklad_for_Znammenuk = {}

rozklad_for_week = {}
days = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', 'П\'ятниця', 'Субота', 'Неділя']




@dp.message_handler(commands=['1'])
async def rjomba(message: types.Message):
    rozklad_for_Chiselnik.update(rozklad_for_week)
    rozklad_for_week.clear()
    base = sqlite3.connect('new1.db')
    cur = base.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS {}(Nomer INTEGER PRIMARY KEY , Rozklad_Ch_1 TEXT)'.format('data'))
    base.commit()
    cur.execute("INSERT OR IGNORE INTO data VALUES(?, ?);", (message.from_user.id, json.dumps(rozklad_for_Chiselnik)))
    base.commit()
    base.close()


@dp.message_handler(commands=['2'])
async def rjomba(message: types.Message):
    rozklad_for_Znammenuk.update(rozklad_for_week)
    rozklad_for_week.clear()
    base = sqlite3.connect('new1.db')
    cur = base.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS {}(Nomer INTEGER PRIMARY KEY , Rozklad_Zn_1 TEXT)'.format('data_1'))
    base.commit()
    cur.execute("INSERT OR IGNORE INTO data_1 VALUES(?, ?);", (message.from_user.id, json.dumps(rozklad_for_Znammenuk)))
    base.commit()
    base.close()


@dp.message_handler(commands=['po'])
async def rjomba(message: types.Message):
    rozklad_for_P.update(dict_para)
    rozklad_for_week_1 = {days[0]: dict_para}
    rozklad_for_week.update(rozklad_for_week_1)
    await bot.send_message(message.from_user.id, rozklad_for_P)
    dict_para.clear()
    rk.clear()
    rk.append(0)


@dp.message_handler(commands=['poc'])
async def rjomba(message: types.Message):
    rozklad_for_P.clear()


@dp.message_handler(commands=['Vi'])
async def rjomba(message: types.Message):
    rozklad_for_V.update(dict_para)
    rozklad_for_week_1 = {days[1]: rozklad_for_V}
    rozklad_for_week.update(rozklad_for_week_1)
    await bot.send_message(message.from_user.id, rozklad_for_V)
    dict_para.clear()
    rk.clear()
    rk.append(0)


@dp.message_handler(commands=['vic'])
async def rjomba(message: types.Message):
    rozklad_for_V.clear()


@dp.message_handler(commands=['Ce'])
async def rjomba(message: types.Message):
    rozklad_for_C.update(dict_para)
    rozklad_for_week_1 = {days[2]: rozklad_for_C}
    rozklad_for_week.update(rozklad_for_week_1)
    await bot.send_message(message.from_user.id, rozklad_for_C)
    dict_para.clear()
    rk.clear()
    rk.append(0)


@dp.message_handler(commands=['cec'])
async def rjomba(message: types.Message):
    rozklad_for_C.clear()


@dp.message_handler(commands=['Ch'])
async def rjomba(message: types.Message):
    rozklad_for_Ch.update(dict_para)
    rozklad_for_week_1 = {days[3]: rozklad_for_Ch}
    rozklad_for_week.update(rozklad_for_week_1)
    await bot.send_message(message.from_user.id, rozklad_for_Ch)
    dict_para.clear()
    rk.clear()
    rk.append(0)


@dp.message_handler(commands=['chc'])
async def rjomba(message: types.Message):
    rozklad_for_Ch.clear()


@dp.message_handler(commands=['Py'])
async def rjomba(message: types.Message):
    rozklad_for_Py.update(dict_para)
    rozklad_for_week_1 = {days[4]: rozklad_for_Py}
    rozklad_for_week.update(rozklad_for_week_1)
    await bot.send_message(message.from_user.id, rozklad_for_Py)
    dict_para.clear()
    rk.clear()
    rk.append(0)


@dp.message_handler(commands=['pyc'])
async def rjomba(message: types.Message):
    rozklad_for_Py.clear()


@dp.message_handler(commands=['Cu'])
async def rjomba(message: types.Message):
    rozklad_for_Cub.update(dict_para)
    rozklad_for_week_1 = {days[5]: rozklad_for_Cub}
    rozklad_for_week.update(rozklad_for_week_1)
    await bot.send_message(message.from_user.id, rozklad_for_Cub)
    dict_para.clear()
    rk.clear()
    rk.append(0)


@dp.message_handler(commands=['cuc'])
async def rjomba(message: types.Message):
    rozklad_for_Cub.clear()


@dp.message_handler(commands=['Ne'])
async def rjomba(message: types.Message):
    rozklad_for_N.update(dict_para)
    rozklad_for_week_1 = {days[6]: rozklad_for_N}
    rozklad_for_week.update(rozklad_for_week_1)
    await bot.send_message(message.from_user.id, rozklad_for_N)
    dict_para.clear()
    rk.clear()
    rk.append(0)


@dp.message_handler(commands=['nec'])
async def rjomba(message: types.Message):
    rozklad_for_N.clear()


@dp.message_handler(commands=['Clearrozklad'])
async def rjomba(message: types.Message):
    rozklad_for_week.clear()


@dp.message_handler(commands=['l'])
async def BD_to_rozklad(message: types.Message):
    sender_id = message.from_user.id
    base_connector = sqlite3.connect("new1.db")
    cur = base_connector.cursor()
    cur.execute("SELECT Rozklad_Ch_1 FROM data WHERE Nomer == ?", (f'{sender_id}',))
    res = cur.fetchall()
    data13 = [json.loads(row[0]) for row in res]
    rozklad_for_week_Ch_1.update(data13[0])
    z = 0
    k = 0
    for i in rozklad_for_week_Ch_1:
        l = days.index(list(rozklad_for_week_Ch_1)[k])
        for i in rozklad_for_week_Ch_1[days[l]].copy():
            c = int(list(rozklad_for_week_Ch_1[days[l]].keys())[z])
            rozklad_for_week_Ch_1[days[l]][c] = rozklad_for_week_Ch_1[days[l]].pop(
                list(rozklad_for_week_Ch_1[days[l]].keys())[z])
        k += 1
    rozklad_for_week_Ch.update(rozklad_for_week_Ch_1)
    data13.clear()
    await bot.send_message(message.from_user.id, f'Чисельник\n{rozklad_for_week_Ch}')

    cur.execute("SELECT Rozklad_Zn_1 FROM data_1 WHERE Nomer == ?", (f'{sender_id}',))
    res = cur.fetchall()
    data13 = [json.loads(row[0]) for row in res]
    rozklad_for_week_Zn_1.update(data13[0])
    z = 0
    d = list(rozklad_for_week_Zn_1)
    k = 0
    for i in rozklad_for_week_Zn_1:
        l = days.index(list(rozklad_for_week_Zn_1)[k])
        for i in rozklad_for_week_Zn_1[days[l]].copy():
            c = int(list(rozklad_for_week_Zn_1[days[l]].keys())[z])
            rozklad_for_week_Zn_1[days[l]][c] = rozklad_for_week_Zn_1[days[l]].pop(
                list(rozklad_for_week_Zn_1[days[l]].keys())[z])
        k += 1
    rozklad_for_week_Zn.update(rozklad_for_week_Zn_1)
    await bot.send_message(message.from_user.id,f'Знаменник\n{rozklad_for_week_Zn}')
    data13.clear()
    asyncio.create_task(zadacha_dlya_vidpravku_chiselnika(sender_id))

async def zadacha_dlya_vidpravku_chiselnika(sender_id):
    if days[0] in rozklad_for_week_Ch:
        x = 1
        z = 0
        for i in rozklad_for_week_Ch[days[0]]:
            aioschedule.every().monday.at(rozklad_for_week_Ch[days[0]][x][2]).do(vidpravka_chiselnika, x, z, sender_id)
            x += 1
    if days[1] in rozklad_for_week_Ch:
        x = 1
        z = 1
        for i in rozklad_for_week_Ch[days[1]]:
            aioschedule.every().tuesday.at(rozklad_for_week_Ch[days[1]][x][2]).do(vidpravka_chiselnika, x, z, sender_id)
            x += 1
    if days[2] in rozklad_for_week_Ch:
        x = 1
        z = 2
        for i in rozklad_for_week_Ch[days[2]]:
            aioschedule.every().wednesday.at(rozklad_for_week_Ch[days[2]][x][2]).do(vidpravka_chiselnika, x, z, sender_id)
            x += 1
    if days[3] in rozklad_for_week_Ch:
        x = 1
        z = 3
        for i in rozklad_for_week_Ch[days[3]]:
            aioschedule.every().thursday.at(rozklad_for_week_Ch[days[3]][x][2]).do(vidpravka_chiselnika, x, z, sender_id)
            x += 1
    if days[4] in rozklad_for_week_Ch:
        x = 1
        z = 4
        for i in rozklad_for_week_Ch[days[4]]:
            aioschedule.every().friday.at(rozklad_for_week_Ch[days[4]][x][2]).do(vidpravka_chiselnika, x, z, sender_id)
            x += 1
    if days[5] in rozklad_for_week_Ch:
        x = 1
        z = 5
        for i in rozklad_for_week_Ch[days[5]]:
            aioschedule.every().saturday.at(rozklad_for_week_Ch[days[5]][x][2]).do(vidpravka_chiselnika, x, z, sender_id)
            x += 1
    if days[6] in rozklad_for_week_Ch:
        x = 1
        z = 6
        for i in rozklad_for_week_Ch[days[6]]:
            aioschedule.every().sunday.at(rozklad_for_week_Ch[days[6]][x][2]).do(vidpravka_chiselnika, x, z, sender_id)
            x += 1
    aioschedule.every().day.at('12:22').do(zadacha_dlya_vidpravku_znammenuka,sender_id)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def zadacha_dlya_vidpravku_znammenuka(sender_id):
    if days[0] in rozklad_for_week_Zn:
        x = 1
        z = 0
        for i in rozklad_for_week_Zn[days[0]]:
            # SendMessageToUser()
            aioschedule.every().monday.at(rozklad_for_week_Zn[days[0]][x][2]).do(vidpravka_znammenuka, x, z, sender_id)
            x += 1
    if days[1] in rozklad_for_week_Zn:
        x = 1
        z = 1
        for i in rozklad_for_week_Zn[days[1]]:
            aioschedule.every().tuesday.at(rozklad_for_week_Zn[days[1]][x][2]).do(vidpravka_znammenuka, x, z, sender_id)
            x += 1
    if days[2] in rozklad_for_week_Zn:
        x = 1
        z = 2
        for i in rozklad_for_week_Zn[days[2]]:
            aioschedule.every().wednesday.at(rozklad_for_week_Zn[days[2]][x][2]).do(vidpravka_znammenuka, x, z, sender_id)
            x += 1
    if days[3] in rozklad_for_week_Zn:
        x = 1
        z = 3
        for i in rozklad_for_week_Zn[days[3]]:
            aioschedule.every().thursday.at(rozklad_for_week_Zn[days[3]][x][2]).do(vidpravka_znammenuka, x, z, sender_id)
            x += 1
    if days[4] in rozklad_for_week_Zn_1:
        x = 1
        z = 4
        for i in rozklad_for_week_Zn[days[4]]:
            aioschedule.every().friday.at(rozklad_for_week_Zn[days[4]][x][2]).do(vidpravka_znammenuka, x, z, sender_id)
            x += 1
    if days[5] in rozklad_for_week_Zn:
        x = 1
        z = 5
        for i in rozklad_for_week_Zn[days[5]]:
            aioschedule.every().saturday.at(rozklad_for_week_Zn[days[5]][x][2]).do(vidpravka_znammenuka, x, z, sender_id)
            x += 1
    if days[6] in rozklad_for_week_Zn:
        x = 1
        z = 6
        for i in rozklad_for_week_Zn[days[6]]:
            aioschedule.every().sunday.at(rozklad_for_week_Zn[days[6]][x][2]).do(vidpravka_znammenuka, x, z, sender_id)
            x += 1
        aioschedule.every().monday.at('00:01').do(zadacha_dlya_vidpravku_chiselnika,sender_id)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def vidpravka_chiselnika(x, z, sender_id):
    await bot.send_message(chat_id=sender_id,
                           text=f'[{rozklad_for_week_Ch[days[z]][x][1]}]({rozklad_for_week_Ch[days[z]][x][3]})',
                           parse_mode='MarkdownV2')


async def vidpravka_znammenuka(x, z, sender_id):
    await bot.send_message(chat_id=sender_id,
                           text=f'[{rozklad_for_week_Zn[days[z]][x][1]}]({rozklad_for_week_Zn[days[z]][x][3]})',
                           parse_mode='MarkdownV2')


# @dp.message_handler(commands=['s'])
# async def BD_to_rozklad_2(message: types.Message):
#     sender_id = message.from_user.id
#     base = sqlite3.connect("new1.db")
#     cur = base.cursor()
#     cur.execute("SELECT Rozklad_Ch_1 FROM data WHERE Nomer == ?", (f'{sender_id}',))
#     res = cur.fetchall()
#     data13 = [json.loads(row[0]) for row in res]
#     rozklad_for_week_Ch_1.update(data13[0])
#     z = 0
#     d = list(rozklad_for_week_Ch_1)
#     k = 0
#     for i in rozklad_for_week_Ch_1:
#         l = days.index(list(rozklad_for_week_Ch_1)[k])
#         for i in rozklad_for_week_Ch_1[days[l]].copy():
#             c = int(list(rozklad_for_week_Ch_1[days[l]].keys())[z])
#             rozklad_for_week_Ch_1[days[l]][c] = rozklad_for_week_Ch_1[days[l]].pop(
#                 list(rozklad_for_week_Ch_1[days[l]].keys())[z])
#         k += 1
#     rozklad_for_week_Ch.update(rozklad_for_week_Ch_1)
#     data13.clear()
#     await bot.send_message(message.from_user.id, rozklad_for_week_Ch)
#
#     cur.execute("SELECT Rozklad_Zn_1 FROM data_1 WHERE Nomer == ?", (f'{sender_id}',))
#     res = cur.fetchall()
#     data13 = [json.loads(row[0]) for row in res]
#     rozklad_for_week_Zn_1.update(data13[0])
#     z = 0
#     k = 0
#     for i in rozklad_for_week_Zn_1:
#         l = days.index(list(rozklad_for_week_Zn_1)[k])
#         for i in rozklad_for_week_Zn_1[days[l]].copy():
#             c = int(list(rozklad_for_week_Zn_1[days[l]].keys())[z])
#             rozklad_for_week_Zn_1[days[l]][c] = rozklad_for_week_Zn_1[days[l]].pop(
#                 list(rozklad_for_week_Zn_1[days[l]].keys())[z])
#         k += 1
#     rozklad_for_week_Zn.update(rozklad_for_week_Zn_1)
#     await bot.send_message(message.from_user.id, rozklad_for_week_Zn)
#     data13.clear()
#     asyncio.create_task(zadacha_dlya_vidpravku_znammenuka_2(sender_id))
#
#
# async def zadacha_dlya_vidpravku_znammenuka_2(sender_id):
#     if days[0] in rozklad_for_week_Zn:
#         x = 1
#         z = 0
#         for i in rozklad_for_week_Zn[days[0]]:
#             aioschedule.every().monday.at(rozklad_for_week_Zn[days[0]][x][2]).do(vidpravka_znammenuka_2, x, z, sender_id)
#             x += 1
#     if days[1] in rozklad_for_week_Zn:
#         x = 1
#         z = 1
#         for i in rozklad_for_week_Zn[days[1]]:
#             aioschedule.every().tuesday.at(rozklad_for_week_Zn[days[1]][x][2]).do(vidpravka_znammenuka_2, x, z, sender_id)
#             x += 1
#     if days[2] in rozklad_for_week_Zn:
#         x = 1
#         z = 2
#         for i in rozklad_for_week_Zn[days[2]]:
#             aioschedule.every().wednesday.at(rozklad_for_week_Zn[days[2]][x][2]).do(vidpravka_znammenuka_2, x, z, sender_id)
#             x += 1
#     if days[3] in rozklad_for_week_Zn:
#         x = 1
#         z = 3
#         for i in rozklad_for_week_Zn[days[3]]:
#             aioschedule.every().thursday.at(rozklad_for_week_Zn[days[3]][x][2]).do(vidpravka_znammenuka_2, x, z, sender_id)
#             x += 1
#     if days[4] in rozklad_for_week_Zn:
#         x = 1
#         z = 4
#         for i in rozklad_for_week_Zn[days[4]]:
#             aioschedule.every().friday.at(rozklad_for_week_Zn[days[4]][x][2]).do(vidpravka_znammenuka_2, x, z, sender_id)
#             x += 1
#     if days[5] in rozklad_for_week_Zn:
#         x = 1
#         z = 5
#         for i in rozklad_for_week_Zn[days[5]]:
#             aioschedule.every().saturday.at(rozklad_for_week_Zn[days[5]][x][2]).do(vidpravka_znammenuka_2, x, z, sender_id)
#             x += 1
#     if days[6] in rozklad_for_week_Zn:
#         x = 1
#         z = 6
#         for i in rozklad_for_week_Zn[days[6]]:
#             aioschedule.every().sunday.at(rozklad_for_week_Zn[days[6]][x][2]).do(vidpravka_znammenuka_2, x, z, sender_id)
#             x += 1
#
#     aioschedule.every().monday.at('00:01').do(zadacha_dlya_vidpravku_chiselnika_2, sender_id)
#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(1)
#
#
# async def zadacha_dlya_vidpravku_chiselnika_2(sender_id):
#     if days[0] in rozklad_for_week_Ch:
#         x = 1
#         z = 0
#         for i in rozklad_for_week_Ch[days[0]]:
#             aioschedule.every().monday.at(rozklad_for_week_Ch[days[0]][x][2]).do(vidpravka_chiselnika_2, x, z, sender_id)
#             x += 1
#     if days[1] in rozklad_for_week_Ch:
#         x = 1
#         z = 1
#         for i in rozklad_for_week_Ch[days[1]]:
#             aioschedule.every().tuesday.at(rozklad_for_week_Ch[days[1]][x][2]).do(vidpravka_chiselnika_2, x, z, sender_id)
#             x += 1
#     if days[2] in rozklad_for_week_Ch:
#         x = 1
#         z = 2
#         for i in rozklad_for_week_Ch[days[2]]:
#             aioschedule.every().wednesday.at(rozklad_for_week_Ch[days[2]][x][2]).do(vidpravka_chiselnika_2, x, z, sender_id)
#             x += 1
#     if days[3] in rozklad_for_week_Ch:
#         x = 1
#         z = 3
#         for i in rozklad_for_week_Ch[days[3]]:
#             aioschedule.every().thursday.at(rozklad_for_week_Ch[days[3]][x][2]).do(vidpravka_chiselnika_2, x, z,sender_id)
#             x += 1
#     if days[4] in rozklad_for_week_Ch:
#         x = 1
#         z = 4
#         for i in rozklad_for_week_Ch[days[4]]:
#             aioschedule.every().friday.at(rozklad_for_week_Ch[days[4]][x][2]).do(vidpravka_chiselnika_2, x, z, sender_id)
#             x += 1
#     if days[5] in rozklad_for_week_Ch:
#         x = 1
#         z = 5
#         for i in rozklad_for_week_Ch[days[5]]:
#             aioschedule.every().saturday.at(rozklad_for_week_Ch[days[5]][x][2]).do(vidpravka_chiselnika_2, x, z, sender_id)
#             x += 1
#     if days[6] in rozklad_for_week_Ch:
#         x = 1
#         z = 6
#         for i in rozklad_for_week_Ch[days[6]]:
#             aioschedule.every().sunday.at(rozklad_for_week_Ch[days[6]][x][2]).do(vidpravka_chiselnika_2, x, z, sender_id)
#             x += 1
#
#     aioschedule.every().monday.at('00:01').do(zadacha_dlya_vidpravku_znammenuka_2(sender_id))
#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(1)
#
#
# async def vidpravka_znammenuka_2(x, z, sender_id):
#     await bot.send_message(chat_id=sender_id,
#                            text=f'[{rozklad_for_week_Zn[days[z]][x][1]}]({rozklad_for_week_Zn[days[z]][x][3]})',
#                            parse_mode='MarkdownV2')
#
#
# async def vidpravka_chiselnika_2(x, z, sender_id):
#     await bot.send_message(chat_id=sender_id,
#                            text=f'[{rozklad_for_week_Ch[days[z]][x][1]}]({rozklad_for_week_Ch[days[z]][x][3]})',
#                            parse_mode='MarkdownV2')


@dp.message_handler()
async def rjomba(message: types.Message):
    text_from_user = message.text
    forma_for_zchituvanya = re.compile(r'\d+\s+\w+\s+\d\d:\d\d+.*')
    new_text = forma_for_zchituvanya.search(text_from_user)
    new_text_spicok = new_text.group().split()
    list_para = [new_text_spicok[0], new_text_spicok[1], new_text_spicok[2], new_text_spicok[3]]
    rk[0] += 1
    para = {rk[0]: list_para}
    dict_para.update(para)
    await bot.send_message(message.from_user.id, dict_para)


executor.start_polling(dp, skip_updates=True)
