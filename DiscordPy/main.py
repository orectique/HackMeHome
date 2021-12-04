import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_message(message):
    if message.author == client.user:
        return


TOKEN = os.getenv("TOKEN")
client.run(TOKEN)
