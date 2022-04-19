
import discord

from discord.ext import commands

intents = discord.Intents.default()

bot = commands.Bot('!', intents=intents)

@bot.command()
async def gethist(ctx: commands.Context):
    print('init')
    chan = ctx.channel
    messages = await chan.history(limit = 100, oldest_first=True, before=ctx.message).flatten()
    f = open("log.txt", "a")
    for msg in messages:
        if msg.author == bot.user:
            return
        else:
            print(msg.content)
            await chan.send(msg.content)
            f.write(str(msg.content + "\n" + "\n" ))
    else:
        f.close()

@bot.event
async def on_ready():
    print("connected")


with open('token.txt') as t:
    token = t.readline().rstrip()


bot.run(token)

