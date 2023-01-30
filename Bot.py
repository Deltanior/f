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



pochatok_paru_dict_1 = {}
pochatok_paru_dict = {}
nazva_paru__pochatok_1_P = {}
nazva_paru__pochatok_1 = {}
nazva_paru_P = []
pochatok_paru_P = []
nazva_paru = []
pochatok_paru = []
dict_para = {}
rozklad= {}
Ponedilok = []
Vivtorok = []
Cereda = []
Chetver = []
Pytnycia = []
Cybota = []
Nedilya = []
time_for_para = []
nomer_paru = []
para_time = {}
para_time_day = {}
para_time_P = {}

@dp.message_handler(commands=['Rozklad'])
async def rjomba(message : types.Message):
    PONEDILOK = ''
    VIVTOROK = ''
    CEREDA = ''
    CHETVER = ''
    PYATNYCIA = ''
    CYBOTA = ''
    NEDILYA = ''
    l_1 = ''
    if 'Понеділок' in rozklad:
        PONEDILOK += rozklad['Понеділок']
        l = 'Понеділок\n' + PONEDILOK
        l_1 += l
    if 'Вівторок' in rozklad:
        VIVTOROK += rozklad['Вівторок']
        l = 'Вівторок\n' + VIVTOROK
        l_1 += l
    if 'Середа' in rozklad:
        CEREDA += rozklad['Середа']
        l = 'Середа\n' + CEREDA
        l_1 += l
    if 'Четвер' in rozklad:
        CHETVER += rozklad['Четвер']
        l = 'Четвер\n' + CHETVER
        l_1 += l
    if 'П\'ятниця' in rozklad:
        PYATNYCIA += rozklad['П\'ятниця']
        l = 'П\'ятниця\n' + PYATNYCIA
        l_1 += l
    if 'Субота' in rozklad:
        CYBOTA += rozklad['Субота']
        l = 'Субота\n' + CYBOTA
        l_1 += l
    if 'Неділя' in rozklad:
        NEDILYA += rozklad['Неділя']
        l = 'Неділя\n' + NEDILYA
        l_1 += l
    await bot.send_message(message.from_user.id,l_1)

@dp.message_handler(commands=['Pon'])
async def rjomba(message : types.Message):
    spisok = []
    x = 0
    string_for_day = ''
    for i in dict_para:
        b_1 = dict_para[f'{nomer_paru[x]}']
        spisok.append(b_1)
        string_for_day += f'{nomer_paru[x]}-{spisok[x]}\n'
        x+=1
    Ponedilok_1 = {"Понеділок":''.join(string_for_day)}
    rozklad.update(Ponedilok_1)
    Ponedilok.append(string_for_day)
    para_time_P.update(para_time_day)
    para_time_day.clear()
    nazva_paru__pochatok_1_P.update()
    nazva_paru__pochatok_1.clear()
    nazva_paru_P.append(nazva_paru)
    pochatok_paru_P.append(pochatok_paru)
    await bot.send_message(message.from_user.id, f'Понеділок\n{string_for_day}')

    dict_para.clear()
    nomer_paru.clear()
    z = 0
    for i in pochatok_paru_P[0]:
        pochatok_paru_dict = {pochatok_paru_P[0][z]: nazva_paru_P[0][z]}
        pochatok_paru_dict_1.update(pochatok_paru_dict)
        z +=1


    #await bot.send_message(message.from_user.id, pochatok_paru_P[0][1])
    #await bot.send_message(message.from_user.id, nazva_paru_P[0][0])
    #await bot.send_message(message.from_user.id, nazva_paru_P[0])
    #await bot.send_message(message.from_user.id, pochatok_paru_P[0])
    #aawait bot.send_message(message.from_user.id,pochatok_paru_dict)
    #await bot.send_message(message.from_user.id,pochatok_paru_dict_1)


@dp.message_handler(commands=['p'])
async def rjomba(message : types.Message):
    await bot.send_message(message.from_user.id, 'Понеділок\n'+''.join(Ponedilok))

@dp.message_handler(commands=['pD'])
async def rjomba(message: types.Message):
    Ponedilok.clear()

@dp.message_handler(commands=['Viv'])
async def rjomba(message : types.Message):
    spisok = []
    x = 0
    string_for_day = ''

    for i in dict_para:
        b_1 = dict_para[f'{nomer_paru[x]}']
        spisok.append(b_1)
        string_for_day += f'{nomer_paru[x]}-{spisok[x]}\n'
        x+=1
    Vivtorok_1 = {"Вівторок":''.join(string_for_day)}
    rozklad.update(Vivtorok_1)
    Vivtorok.append(string_for_day)
    await bot.send_message(message.from_user.id, f'Вівторок\n{string_for_day}')
    dict_para.clear()
    nomer_paru.clear()

@dp.message_handler(commands=['v'])
async def rjomba(message : types.Message):
    await bot.send_message(message.from_user.id, 'Вівторок\n'+''.join(Vivtorok))
@dp.message_handler(commands=['vD'])
async def rjomba(message: types.Message):
    Vivtorok.clear()


@dp.message_handler(commands=['Cer'])
async def rjomba(message: types.Message):
    spisok = []
    x = 0
    string_for_day = ''

    for i in dict_para:
        b_1 = dict_para[f'{nomer_paru[x]}']
        spisok.append(b_1)
        string_for_day += f'{nomer_paru[x]}-{spisok[x]}\n'
        x += 1
    Cereda_1 = {"Середа": ''.join(string_for_day)}
    rozklad.update(Cereda_1)
    Cereda.append(string_for_day)
    await bot.send_message(message.from_user.id, f'Середа\n{string_for_day}')
    dict_para.clear()
    nomer_paru.clear()

@dp.message_handler(commands=['c'])
async def rjomba(message : types.Message):
    await bot.send_message(message.from_user.id, 'Середа\n'+''.join(Vivtorok))
@dp.message_handler(commands=['cD'])
async def rjomba(message: types.Message):
    Cereda.clear()

@dp.message_handler(commands=['Che'])
async def rjomba(message: types.Message):
    spisok = []
    x = 0
    string_for_day = ''

    for i in dict_para:
        b_1 = dict_para[f'{nomer_paru[x]}']
        spisok.append(b_1)
        string_for_day += f'{nomer_paru[x]}-{spisok[x]}\n'
        x += 1
    Chetver_1 = {"Четвер": ''.join(string_for_day)}
    rozklad.update(Chetver_1)
    Chetver.append(string_for_day)
    await bot.send_message(message.from_user.id, f'Четвер\n{string_for_day}')
    dict_para.clear()
    nomer_paru.clear()

@dp.message_handler(commands=['ch'])
async def rjomba(message : types.Message):
    await bot.send_message(message.from_user.id, 'Четвер\n'+''.join(Vivtorok))
@dp.message_handler(commands=['chD'])
async def rjomba(message: types.Message):
    Chetver.clear()

@dp.message_handler(commands=['Pyt'])
async def rjomba(message: types.Message):
    spisok = []
    x = 0
    string_for_day = ''

    for i in dict_para:
        b_1 = dict_para[f'{nomer_paru[x]}']
        spisok.append(b_1)
        string_for_day += f'{nomer_paru[x]}-{spisok[x]}\n'
        x += 1
    Pytnycia_1 = {"П\'ятниця": ''.join(string_for_day)}
    rozklad.update(Pytnycia_1)
    Pytnycia.append(string_for_day)
    await bot.send_message(message.from_user.id, f'П\'ятниця\n{string_for_day}')
    dict_para.clear()
    nomer_paru.clear()


@dp.message_handler(commands=['py'])
async def rjomba(message: types.Message):
    await bot.send_message(message.from_user.id, 'П\'ятниця\n' + ''.join(Vivtorok))


@dp.message_handler(commands=['pyD'])
async def rjomba(message: types.Message):
    Pytnycia.clear()

@dp.message_handler(commands=['Cyb'])
async def rjomba(message: types.Message):
    spisok = []
    x = 0
    string_for_day = ''

    for i in dict_para:
        b_1 = dict_para[f'{nomer_paru[x]}']
        spisok.append(b_1)
        string_for_day += f'{nomer_paru[x]}-{spisok[x]}\n'
        x += 1
    Cybota_1 = {"Субота": ''.join(string_for_day)}
    rozklad.update(Cybota_1)
    Cybota.append(string_for_day)
    await bot.send_message(message.from_user.id, f'Субота\n{string_for_day}')
    dict_para.clear()
    nomer_paru.clear()

@dp.message_handler(commands=['cy'])
async def rjomba(message : types.Message):
    await bot.send_message(message.from_user.id, 'Субота\n'+''.join(Vivtorok))
@dp.message_handler(commands=['cyD'])
async def rjomba(message: types.Message):
    Cybota.clear()

@dp.message_handler(commands=['Ned'])
async def rjomba(message: types.Message):
    spisok = []
    x = 0
    string_for_day = ''

    for i in dict_para:
        b_1 = dict_para[f'{nomer_paru[x]}']
        spisok.append(b_1)
        string_for_day += f'{nomer_paru[x]}-{spisok[x]}\n'
        x += 1
    Nedilya_1 = {"Неділя": ''.join(string_for_day)}
    rozklad.update(Nedilya_1)
    Nedilya.append(string_for_day)
    await bot.send_message(message.from_user.id, f'Неділя\n{string_for_day}')
    dict_para.clear()
    nomer_paru.clear()

@dp.message_handler(commands=['n'])
async def rjomba(message : types.Message):
    await bot.send_message(message.from_user.id, 'Неділя\n'+''.join(Vivtorok))
@dp.message_handler(commands=['nD'])
async def rjomba(message: types.Message):
    Nedilya.clear()



@dp.message_handler(commands=['r1'])
async def rjomba(message: types.Message):
    await bot.send_message(message.from_user.id, pochatok_paru_dict_1[pochatok_paru_P[0][0]])
    await bot.send_message(message.from_user.id, pochatok_paru_dict_1[pochatok_paru_P[0][1]])
    await bot.send_message(message.from_user.id, pochatok_paru_dict_1[pochatok_paru_P[0][2]])
    await bot.send_message(message.from_user.id, pochatok_paru_P[0][1])
    await bot.send_message(message.from_user.id, pochatok_paru_P[0][2])
    await bot.send_message(message.from_user.id, len(pochatok_paru_P[0]))





@dp.message_handler(commands=['l'])
async def Yebuddy13(message: types.Message):
    asyncio.create_task(Yebuddy())
async def Yebuddy():
    if len(pochatok_paru_P[0])<6:
        aioschedule.every().saturday.at(pochatok_paru_P[0][0]).do(Yebuddy_1)
        if len(pochatok_paru_P[0])>1:
            aioschedule.every().saturday.at(pochatok_paru_P[0][1]).do(Yebuddy_2)
            if len(pochatok_paru_P[0]) > 2:
                 aioschedule.every().saturday.at(pochatok_paru_P[0][2]).do(Yebuddy_3)
                 if len(pochatok_paru_P[0]) > 3:
                    aioschedule.every().saturday.at(pochatok_paru_P[0][3]).do(Yebuddy_4)
                    if len(pochatok_paru_P[0]) > 4:
                        aioschedule.every().saturday.at(pochatok_paru_P[0][4]).do(Yebuddy_5)
        while True:
            await aioschedule.run_pending()
            await asyncio.sleep(1)
async def Yebuddy_1():
    await bot.send_message(chat_id=518018061, text=pochatok_paru_dict_1[pochatok_paru_P[0][0]])
async def Yebuddy_2():
    await bot.send_message(chat_id=518018061, text=pochatok_paru_dict_1[pochatok_paru_P[0][1]])
async def Yebuddy_3():
    await bot.send_message(chat_id=518018061, text=pochatok_paru_dict_1[pochatok_paru_P[0][2]])
async def Yebuddy_4():
    await bot.send_message(chat_id=518018061, text=pochatok_paru_dict_1[pochatok_paru_P[0][3]])
async def Yebuddy_5():
    await bot.send_message(chat_id=518018061, text=pochatok_paru_dict_1[pochatok_paru_P[0][4]])






@dp.message_handler()
async def rjomba(message : types.Message):
    text_from_user = message.text
    forma_for_zchituvanya = re.compile(r'\d+\s+\w+\s+\d\d:\d\d+.*')
    new_text = forma_for_zchituvanya.search(text_from_user)
    new_text_spicok = new_text.group().split()
    para = {f"{new_text_spicok[0]}":f"{new_text_spicok[1]} - {new_text_spicok[2]}"}
    dict_para.update(para)
    nomer_paru.append(new_text_spicok[0])
    await bot.send_message(message.from_user.id, dict_para)


    nazva_paru.append(new_text_spicok[1])
    pochatok_paru.append(new_text_spicok[2])
    x = 0

    nazva_paru__pochatok = {}
    for i in range(len(nazva_paru)):
        nazva_paru__pochatok = {nazva_paru[x]:pochatok_paru[x]}
        nazva_paru__pochatok_1.update(nazva_paru__pochatok)
        x +=1
    #await bot.send_message(message.from_user.id, nazva_paru__pochatok_1)

    time_for_para.append(new_text_spicok[2])




executor.start_polling(dp, skip_updates=True)