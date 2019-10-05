import discord
from datetime import datetime

day=datetime.today().weekday() #узнаем день недели в числовом виде 0-пн - 6-вс
now=datetime.strftime(datetime.now(), "%H:%M")#datetime.now().time() #узнаем текущее время (без даты)
#datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S") #Полная строка дата и время
hour=int(datetime.strftime(datetime.now(), "%H")) #текущий час в целочисленном виде

if day==0:
    kv='Сегодня понедельник, КВ в 3:00 по Мск'
elif day==1:
    kv='Cегодня вторник, КВ в 20:00 по Мск'
elif day==2:
    kv='Cегодня среда, КВ в 3:00 по Мск'
elif day==3:
    kv='Cегодня четверг, КВ в 20:00 по Мск'
elif day==4:
    kv='Cегодня пятница, КВ в 3:00 по Мск'
elif day==5:
    kv='Cегодня суббота, КВ в 14:00 и в 20:00 по Мск'
elif day==6:
    kv='Cегодня воскресенье, КВ в 14:00 по Мск'

Bot = discord.Client()
#from discord.ext import commands
#from discord.ext.commands import Bot

#Bot = ccommands.Bot(command_prefix ='!')

#@Bot.command()
#async def кв(ctx):

@Bot.event
async def on_message(message):
    if message.author == Bot.user:
        return

    if message.content.startswith('КВ'):
        await message.channel.send(kv)
        await message.channel.send('Сейчас '+str(now))

Bot.run('NjMwMDcwMzI1NzUyNzU4Mjgz.XZjPNw.EN-RaJGaAEfUZ1Rg5RSerd620Is') #токен бота

#Ссылка для добавление бота на дс сервер:
#https://discordapp.com/oauth2/authorize?client_id=630070325752758283&scope=bot&permissions=8