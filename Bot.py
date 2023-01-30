from aiogram import types, Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import re
import schedule
import time
import aioschedule
import os
import asyncio


bot = Bot(token= '5722882971:AAGY9gu6FF9HZFIUVEheS4PzR_wdl_mTi8o')
dp = Dispatcher(bot)

rozklad_for_day = {}
rozklad_for_p = {}

nazva_paru_P = []
pochatok_paru_P = []
nazva_paru = []
pochatok_paru = []
nomer_paru = []
rozklad_for_week = []
cilka_na_paru = []
cilka_na_paru_p = []

dict_para = {}
rozklad = {}






@dp.message_handler(commands=['Rozklad'])
async def rjomba(message : types.Message):
    await bot.send_message(message.from_user.id, rozklad_for_week[0])


@dp.message_handler(commands=['Pon'])
async def rjomba(message : types.Message):
    rozklad_for_p.update(rozklad_for_day)
    nazva_paru_P.extend(nazva_paru)
    pochatok_paru_P.extend(pochatok_paru)
    rozklad_for_week.append(f'Понеділок\n{rozklad_for_p[1]}\n')
    cilka_na_paru_p.extend(cilka_na_paru)
    await bot.send_message(message.from_user.id, f'Понеділок\n{rozklad_for_p[1]}')
    #await bot.send_message(message.from_user.id, cilka_na_paru_p)
    rozklad_for_day.clear()
    nazva_paru.clear()
    pochatok_paru.clear()
    nomer_paru.clear()
    dict_para.clear()
    cilka_na_paru.clear()
    #await bot.send_message(message.from_user.id, cilka_na_paru_p)

@dp.message_handler(commands=['ClearP'])
async def rjomba(message : types.Message):
    cilka_na_paru_p.clear()
    rozklad_for_p.clear()
    rozklad_for_week.clear()



@dp.message_handler(commands=['p'])
async def rjomba(message : types.Message):
    await bot.send_message(message.from_user.id, f'Понеділок\n{rozklad_for_p[1]}')



@dp.message_handler(commands=['pD'])
async def rjomba(message: types.Message):
    rozklad_for_p.clear()
    #await bot.send_message(message.from_user.id,rozklad_for_p)


@dp.message_handler(commands=['co'])
async def rjomba(message: types.Message):
    await bot.send_message(message.from_user.id, nazva_paru_P[0])
    await bot.send_message(message.from_user.id, cilka_na_paru_p[0])
    await bot.send_message(message.from_user.id, pochatok_paru_P)




@dp.message_handler(commands=['l'])
async def Yebuddy13(message: types.Message):
    x = 0
    for i in pochatok_paru_P:
        asyncio.create_task(Yebuddy(x))
        x += 1
async def Yebuddy(x):
    aioschedule.every().monday.at(pochatok_paru_P[x]).do(Yebuddy_1,x)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def Yebuddy_1(x):
    await bot.send_message(chat_id=518018061, text=f'[{nazva_paru_P[x]}]({cilka_na_paru_p[x]})',parse_mode='MarkdownV2')







@dp.message_handler()
async def rjomba(message : types.Message):
    text_from_user = message.text
    forma_for_zchituvanya = re.compile(r'\d+\s+\w+\s+\d\d:\d\d+.*')
    new_text = forma_for_zchituvanya.search(text_from_user)
    new_text_spicok = new_text.group().split()
    para = {f"{new_text_spicok[0]}":f"{new_text_spicok[1]} {new_text_spicok[2]} {new_text_spicok[3]}"}
    dict_para.update(para)
    nomer_paru.append(new_text_spicok[0])
    nazva_paru.append(new_text_spicok[1])
    pochatok_paru.append(new_text_spicok[2])
    cilka_na_paru.append(new_text_spicok[3])
    string_for_day = ''
    x = 0
    for i in dict_para:
        b = dict_para[f'{nomer_paru[x]}']
        string_for_day += f'{nomer_paru[x]}-{nazva_paru[x]}\n'
        rozklad_for_day_1 = {1: string_for_day}
        rozklad_for_day.update(rozklad_for_day_1)
        x += 1

    await bot.send_message(message.from_user.id, dict_para)







executor.start_polling(dp, skip_updates=True)