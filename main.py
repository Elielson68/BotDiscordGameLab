import discord
from discord.ext import commands, tasks
from discord import TextChannel
import time, datetime
from keep_alive import keep_alive
import os
import random
dias_semana = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print("bot online")
    hour=time.localtime().tm_hour
    minute=time.localtime().tm_min
    
    horario.start()


@tasks.loop(minutes=1.0)
async def horario():
    aviso = "{} A reunião iniciará em 10 minutos, estejam preparados.\nLink no meet: {}"
    dia = time.localtime().tm_wday
    hour=time.localtime().tm_hour
    minute=time.localtime().tm_min
    # Aviso para todos
    if dias_semana[dia] == 'seg':
      if hour == 13 and minute == 50:
        print("Aviso enviado!")
        channel_geral = bot.get_channel(816763031048552469)
        await channel_geral.send(aviso.format("@everyone", "https://meet.google.com/gdj-nucj-agy"))

    #Aviso para os sound design
    if dias_semana[dia] == 'ter':
      if hour == 13 and minute == 50:
        print("Aviso enviado!")
        channel_geral = bot.get_channel(816763031048552469)
        await channel_geral.send(aviso.format("<@&816741389919977532>", "https://meet.google.com/gdj-nucj-agy"))

    #Aviso para os programadores
    if dias_semana[dia] == 'qua':
      if hour == 13 and minute == 50:
        print("Design: Aviso enviado!")
        channel_programmers = bot.get_channel(808457915731935249)
        await channel_programmers.send("<@&819324733962584075> A reunião iniciará em 10 minutos, estejam preparados.\nLink no meet: https://meet.google.com/ops-ienr-qaw")

        print("Programadores: Aviso enviado!")
        channel_geral = bot.get_channel(816763031048552469)
        await channel_geral.send("<@&816741256130068522> A reunião iniciará em 10 minutos, estejam preparados.\nLink no meet: https://meet.google.com/ops-ienr-qaw")

    #Aviso para os artistas
    if dias_semana[dia] == 'qui':
      if hour == 14 and minute == 20:
        print("Aviso enviado!")
        channel_geral = bot.get_channel(816763031048552469)
        await channel_geral.send(aviso.format("<@&816741779801768006>", "https://meet.google.com/gdj-nucj-agy"))
    
    #Aviso para os roteiristas
    if dias_semana[dia] == 'sex':
      if hour == 13 and minute == 50:
        print("Aviso enviado!")
        channel_geral = bot.get_channel(816763031048552469)
        await channel_geral.send(aviso.format("<@&816741170734432258>", "https://meet.google.com/gdj-nucj-agy"))

    #Aviso para os level design
    if dias_semana[dia] == 'dom':
      if hour == 14 and minute == 50:
        print("Aviso enviado!")
        channel_lvldesign = bot.get_channel(829453458385010728)
        await channel_lvldesign.send(aviso.format("<@&816743285933998120>", "https://meet.google.com/gdj-nucj-agy"))
    

    
@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))

@bot.command()
async def pato(ctx):
    await ctx.send("quack!")

@bot.command()
async def quote(ctx):
  messages = await bot.get_channel(837777944780472320).history(limit=200).flatten()
  messages = [msg.content for msg in messages]
  index = random.randint(0, (len(messages)-1))
  await ctx.send(messages[index])

@bot.command()
async def teste(ctx):
  channel_programmers = bot.get_channel(808457915731935249)
  await channel_programmers.send("<@&808459802917339206> testando novamente")

keep_alive()
bot.run(os.getenv("TOKEN"))
