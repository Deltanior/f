from aiogram import types, Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import re
import schedule
import time
import aioschedule
import os
import asyncio


bot = Bot(token= ####)
dp = Dispatcher(bot)


rk =[0]


rozklad_for_P = {}
rozklad_for_V = {}
rozklad_for_C = {}
rozklad_for_Ch = {}
rozklad_for_Py = {}
rozklad_for_Cub = {}
rozklad_for_N = {}

list_para = []
dict_para = {}

rozklad_for_week={}
days = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', 'П\'ятниця', 'Субота', 'Неділя']

@dp.message_handler(commands=['Rozklad'])
async def rjomba(message : types.Message):
    x = 0
    b = []
    str = ''
    str_1 = ''
    k = 1
    for i in days:
        if days[x] in rozklad_for_week:
            for i in rozklad_for_week[days[x]]:
                a = (f'[{rozklad_for_week[days[x]][k][0]} \- {rozklad_for_week[days[x]][k][1]} \- {rozklad_for_week[days[x]][k][2]}]({rozklad_for_week[days[x]][k][3]})')
                str += f'{a}\n'
                k += 1
            k = 1
            str_1 +=f'{days[x]}\n{str}'
            str = ''
            x += 1
        else:
            x += 1
    await bot.send_message(message.from_user.id, f'{str_1} ', parse_mode='MarkdownV2')

@dp.message_handler(commands=['po'])
async def rjomba(message : types.Message):
    rozklad_for_P.update(dict_para)
    rozklad_for_week_1 = {days[0]:rozklad_for_P}
    rozklad_for_week.update(rozklad_for_week_1)
    await bot.send_message(message.from_user.id, rozklad_for_P)
    dict_para.clear()
    rk.clear()
    rk.append(0)

@dp.message_handler(commands=['poc'])
async def rjomba(message: types.Message):
    rozklad_for_P.clear()

@dp.message_handler(commands=['Vi'])
async def rjomba(message : types.Message):
    rozklad_for_V.update(dict_para)
    rozklad_for_week_1 = {days[1]:rozklad_for_V}
    rozklad_for_week.update(rozklad_for_week_1)
    await bot.send_message(message.from_user.id, rozklad_for_V)
    dict_para.clear()
    rk.clear()
    rk.append(0)

@dp.message_handler(commands=['vic'])
async def rjomba(message: types.Message):
    rozklad_for_V.clear()

@dp.message_handler(commands=['Ce'])
async def rjomba(message : types.Message):
    rozklad_for_C.update(dict_para)
    rozklad_for_week_1 = {days[2]:rozklad_for_C}
    rozklad_for_week.update(rozklad_for_week_1)
    await bot.send_message(message.from_user.id, rozklad_for_C)
    dict_para.clear()
    rk.clear()
    rk.append(0)

@dp.message_handler(commands=['cec'])
async def rjomba(message: types.Message):
    rozklad_for_C.clear()

@dp.message_handler(commands=['Ch'])
async def rjomba(message : types.Message):
    rozklad_for_Ch.update(dict_para)
    rozklad_for_week_1 = {days[3]:rozklad_for_Ch}
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
async def rjomba(message : types.Message):
    rozklad_for_week.clear()



@dp.message_handler(commands=['l'])
async def Yebuddy13(message: types.Message):

    asyncio.create_task(Yebuddy())

async def Yebuddy():
    x = 1
    for i in rozklad_for_week[days[0]]:
        aioschedule.every().monday.at(rozklad_for_week[days[0]][x][2]).do(Yebuddy_1,x)
        x += 1
    x = 1
    for i in rozklad_for_week[days[1]]:
        aioschedule.every().tuesday.at(rozklad_for_week[days[1]][x][2]).do(Yebuddy_2, x)
        x += 1
    x = 1
    for i in rozklad_for_week[days[2]]:
        aioschedule.every().wednesday.at(rozklad_for_week[days[2]][x][2]).do(Yebuddy_3, x)
        x += 1
    x = 1
    for i in rozklad_for_week[days[3]]:
        aioschedule.every().thursday.at(rozklad_for_week[days[3]][x][2]).do(Yebuddy_4, x)
        x += 1
    x = 1
    for i in rozklad_for_week[days[4]]:
        aioschedule.every().friday.at(rozklad_for_week[days[4]][x][2]).do(Yebuddy_5, x)
        x += 1
    x = 1
    for i in rozklad_for_week[days[5]]:
        aioschedule.every().saturday.at(rozklad_for_week[days[5]][x][2]).do(Yebuddy_6, x)
        x += 1
    x = 1
    for i in rozklad_for_week[days[6]]:
        aioschedule.every().sunday.at(rozklad_for_week[days[6]][x][2]).do(Yebuddy_7, x)
        x += 1
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def Yebuddy_1(x):
    await bot.send_message(chat_id=518018061, text=f'[{rozklad_for_week[days[0]][x][1]}]({rozklad_for_week[days[0]][x][3]})',parse_mode='MarkdownV2')

async def Yebuddy_2(x):
    await bot.send_message(chat_id=518018061, text=f'[{rozklad_for_week[days[1]][x][1]}]({rozklad_for_week[days[1]][x][3]})',parse_mode='MarkdownV2')

async def Yebuddy_3(x):
    await bot.send_message(chat_id=518018061, text=f'[{rozklad_for_week[days[2]][x][1]}]({rozklad_for_week[days[2]][x][3]})',parse_mode='MarkdownV2')

async def Yebuddy_4(x):
    await bot.send_message(chat_id=518018061, text=f'[{rozklad_for_week[days[3]][x][1]}]({rozklad_for_week[days[3]][x][3]})',parse_mode='MarkdownV2')

async def Yebuddy_5(x):
    await bot.send_message(chat_id=518018061, text=f"[{rozklad_for_week[days[4]][x][1]}]({rozklad_for_week[days[4]][x][3]})",parse_mode='MarkdownV2')

async def Yebuddy_6(x):
    await bot.send_message(chat_id=518018061, text=f'[{rozklad_for_week[days[5]][x][1]}]({rozklad_for_week[days[5]][x][3]})',parse_mode='MarkdownV2')

async def Yebuddy_7(x):
    await bot.send_message(chat_id=518018061, text=f'[{rozklad_for_week[days[6]][x][1]}]({rozklad_for_week[days[6]][x][3]})',parse_mode='MarkdownV2')



@dp.message_handler()
async def rjomba(message : types.Message):

    text_from_user = message.text
    forma_for_zchituvanya = re.compile(r'\d+\s+\w+\s+\d\d:\d\d+.*')
    new_text = forma_for_zchituvanya.search(text_from_user)
    new_text_spicok = new_text.group().split()
    list_para = [new_text_spicok[0],new_text_spicok[1],new_text_spicok[2],new_text_spicok[3]]

    rk[0] += 1
    para = {rk[0] : list_para}
    dict_para.update(para)

    await bot.send_message(message.from_user.id, dict_para)







executor.start_polling(dp, skip_updates=True)
