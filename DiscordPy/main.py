import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready')

servers = {}

@client.event
async def on_message(message):
    global servers

    if message.author == client.user:
        return

    server_id = message.guild.id
    if server_id not in severs:
        servers[server_id] = {
            "mentors":{

            },
            "mentees":{

            },
            "types":{

            }
        }
    
    if message.content.startswith('-hmh add') and message.author.guild_permissions.administrator == True:
        try:
            text = message.content[8:]
            text = list(text.split())
            for i in text:
                servers[server_id][types][i] = []
            return
        except:
            return await message.channel.send('There seems to be an error with your request. Please verify.')

    if message.content.startswith('-hmh rem') and message.author.guild_permissions.administrator == True:
        try:
            text = message.content[8:]
            text = list(text.split())
            for i in text:
                servers[server_id][types].pop(i)
            return
        except:
            return await message.channel.send('There seems to be an error with your request. Please verify.')

    if message.content.startswith('-hmh mentor'):
        text = message.content[11:]
        text = list(text.split())
        return

    if message.content.startswith('-hmh mentee'):
        return
    


TOKEN = os.getenv("TOKEN")
client.run(TOKEN)
