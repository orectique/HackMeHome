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
    if server_id not in servers:
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
                servers[server_id]['types'][i] = []
                tag = 'Added ' + str(i)
                await message.channel.send(tag)
            return
        except:
            return await message.channel.send('There seems to be an error with your request. Please verify.')

    if message.content.startswith('-hmh rem') and message.author.guild_permissions.administrator == True:
        try:
            text = message.content[8:]
            text = list(text.split())
            for i in text:
                servers[server_id]['types'].pop(i)
                tag = 'Removed ' + str(i)
                await message.channel.send(tag)
            return
        except:
            return await message.channel.send('There seems to be an error with your request. Please verify.')

    if message.content.startswith('-hmh ls'):
        types = [i for i in servers[server_id]['types']]
        return await message.channel.send(types)
    
    if message.content.startswith('-hmh help'):
        tag = """Welcome to HackMeHome.
        **Admin** Commands:
        -hmh add/rem to add or remove categories.
        **General** Commands:
        -hmh help: Get help.
        -hmh ls: List categories.
        -hmh mentor *args: Command to add oneself as a mentor. Use category names as args, separated by a blank space.
        -hmh mentee ProjectName *args: Command to find mentors. pass relevant categories as args. 
        -hmh resolved: To be used by a mentor to clear the channel and category once the collab session is over. 
        """        
        return await message.channel.send(tag)

    if message.content.startswith('-hmh mentor'):
        text = message.content[11:]
        text = list(text.split())
        try:
            if message.author not in servers[server_id]['mentors']:
                servers[server_id]['mentors'][message.author] = {
                'count': 0
            }
                for i in text:
                    if i in servers[server_id]['types']:
                        servers[server_id]['types'][i].append(message.author)
                    else:
                        servers[server_id]['types'][i] = [message.author]
            else:
                for i in text:
                    if i in servers[server_id]['types']:
                        servers[server_id]['types'][i].append(message.author)
                    else:
                        servers[server_id]['types'][i] = [message.author]
            
            return await message.channel.send('Successfully added you as a mentor.')
        except:
            return await message.channel.send('There seems to be an error with your request. Please verify.')

    if message.content.startswith('-hmh dementor'):
        text = message.content[13:]
        text = list(text.split(' '))
        try:            
            for i in text:
                if i in servers[server_id]['types']:
                    temp = servers[server_id]['types'][i]
                    temp.remove(message.author)
                    tag = "Removed " + str(i)
                    await message.channel.send(tag)     
            servers[server_id]['types'] = temp       
            return 
        except:
            return await message.channel.send('There seems to be an error with your request. Please verify.')

    if message.content.startswith('-hmh mentee'):
        text = message.content[11:]
        text = list(text.split(' '))
        text.pop(0)
        ProjName = text.pop(0)
        team = [client.user, message.author]

        if message.author not in servers[server_id]['mentees']:
            servers[server_id]['mentees'][message.author] = 'Open'
            flag = 'Open'
        else:
            flag = servers[server_id]['mentees'][message.author]
        
        if flag == 'Open':
            for i in text:
                if i not in servers[server_id]['types']:
                    continue
                mentors = servers[server_id]['types'][i]
                temp = servers[server_id]['mentors']
                val = {}
                for mentor in temp:
                    if mentor in mentors:
                        val[mentor] = temp[mentor]
                mentor_temp = min(val, key=val.get)
                team.append(mentor_temp)
                servers[server_id]['mentors'][mentor_temp]['count'] += 1

            category = await message.guild.create_category_channel('HackMeHome Rooms')

            overwrites = {
            message.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            }
            for member in team:
                overwrites[member] = discord.PermissionOverwrite(read_messages=True)
            
            await category.create_text_channel(ProjName, overwrites=overwrites)
            servers[server_id]['mentees'][message.author] = 'Closed'

            return await message.channel.send('You have been added to a new HackMeHome room. Enjoy.')
        else:
            return await message.channel.send('You already have an open project. Please resolve that first.')

       
    if message.content.startswith('-hmh resolved') and message.author in servers[server_id]['mentors'] and message.channel.category.name == 'HackMeHome Rooms':
        try:
            await message.channel.send('Hope you had fun.')
            await message.channel.category.delete()
            return await message.channel.delete()
        except:
            return await message.channel.send('There seems to be an error with your request. Please verify.')

TOKEN = os.getenv("TOKEN")
client.run(TOKEN)
