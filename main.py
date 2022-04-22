import discord
import os
from bot import Bot
TOKEN = "OTY2ODYxMTU2NjIwODUzMjc5.YmH5nw.l4oDyaBtkNxR42Oi-WeJqmZoivQ"
PREFIX = "*"

client = discord.Client()
bot = Bot()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user or message.author.bot:
        return
    
    if message.content.startswith(f"{PREFIX}registrar"):
        await bot.register(message)


client.run(TOKEN)