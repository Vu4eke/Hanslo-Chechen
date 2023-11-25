from logging import info
import random
import aiohttp
import discord # Подключаем библиотеку
from discord.ext import commands
from datetime import datetime
import asyncio
#========================================

intents = discord.Intents.default() # Подключаем "Разрешения"
intents.message_content = True
#ntents = discord.Intents.default(members=True)
# Задаём префикс и интенты
Client = commands.Bot(command_prefix='!', intents=intents)
Client.remove_command('help')

@Client.event
async def on_ready():
    guilds = len(Client.guilds)
    #CMD-Messages
    print("===================================================================================================================================::..")
    print("Frame: None // API: None // BD: None // Memory: No info // Status: Включён")
    while True:
       #await Client.change_presence(status = discord.Status.online, activity=discord.Activity(type=discord.ActivityType.competing, name="!help"))
       #await asyncio.sleep(15)
       #=>
       #members = 0
       #for guild in Client.guilds:
       # members += guild.member_count - 1
       #=>
       #await Client.change_presence(status = discord.Status.online, activity = discord.Activity(name = f'за {members} участниками', type = discord.ActivityType.watching))
       #await asyncio.sleep(15)
       #=>
       #!!.ЗАПУСКАТЬ В СЛУЧАЕ ТЕХНИЧЕСКИХ РАБОТ.!!
       await Client.change_presence(status = discord.Status.idle, activity = discord.Activity(name = f'за тех.работами', type = discord.ActivityType.watching))

@Client.command()
async def help(ctx):
    embed = discord.Embed(title="ㅤ▪ Chechen〡Информация о боте",
                      description="ㅤㅤㅤㅤ[``GitHub``](https://github.com/Vu4eke)〡[``Support-Discord``](https://discord.gg/STGbGYPvaW)〡[``VK``](https://vk.com/vamep)\n__ㅤ**ㅤㅤㅤ╚===============╩========╝**ㅤㅤㅤㅤㅤ__\n> Чтобы узнать статус бота: !bots\n> Версия: **__BETA-VERSION // 0.0.0__**",
                      colour=0xf5a700)

    embed.add_field(name="Администрация",
                value="▪ soon...\n▪ soon...\n▪ soon...\n▪ soon...\n▪ soon...",
                inline=True)
    embed.add_field(name="Командыᵗᵉˢᵗ⁻ᶜᵐᵈ",
                value="▪ **!clear**",
                inline=True)

    await ctx.send(embed=embed)







@Client.command(aliases=['clear', 'Clear', 'cLEAR', 'cls', 'Cls', 'cLS', 'сды', 'Сды', 'сДЫ', 'сдуфк', 'Сдуфк', 'сДУФК', 'СДУФК', 'CLEAR', 'CLS'])
@commands.has_guild_permissions(administrator=True)
async def clearning(ctx, amount: int = None):
    if amount is None:
        await ctx.send("Извините, но вы вели не правильное число.", delete_after=2.5)
        return
    await ctx.channel.purge(limit=int(amount))
    embed = discord.Embed(colour=0x00b8f5,
                          timestamp=datetime.now())
    embed.set_author(name="• Сообщении были удалены!")
    embed.add_field(name="Кол-во:",
                value=f'{amount}',
                inline=True)
    #============================
    embed.add_field(name="Статус:",
                value="Выполнено.",
                inline=True)
    embed.set_footer(text="• Chechen разработан для чего-то")
    await ctx.send(embed=embed, delete_after=7.4)
#=























Client.run('СЮДА СВОЙ ТОКЕН БОТА!!!')