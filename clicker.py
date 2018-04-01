import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
import asyncio
import time


server = discord.Server
Client = discord.Client()
client = commands.Bot(command_prefix = "$")

@client.event
async def on_ready():
    print("REEEEEEEEE")

@client.event
async def on_message(message):
    if message.author.id != "430118464754286596":
        if message.content == "create clicker":
            await client.create_channel(message.author.server, "clickergame")

        if message.content == "secret clear message":
            await client.purge_from(message.channel)

        if message.content == "clicker startup":
            await client.delete_message(message)
            await client.send_message(message.channel, "@everyone I'm holding a contest for **$25 Bitcoin** \n Whoever gets the most clicks over the next week wins \n Countdown: https://www.timeanddate.com/countdown/generic?day=08&p0=820&font=cursive \n Say \"play clicker\" to begin, and start clicking!")
            await client.send_message(message.channel, "------------------------------------------------------------------------------------------------")
                
        if message.content == "play clicker" and message.channel.name == "clickergame" or message.channel.name == "bot-devolper":
            await client.delete_message(message)
            clicks = 0
            current_hour = now.hour
            auto_clickers = 3600
            clicker_mess = await client.send_message(message.channel, str(message.author.display_name) + " has " + str(clicks) + " coins")
            for c_emoji in client.get_all_emojis():
                if c_emoji.name == 'Coin':
                    coin = c_emoji
    #            for c_emoji in client.get_all_emojis():
    #                if c_emoji.name == 'Blank':
    #                    blank = c_emoji
    #            for c_emoji in client.get_all_emojis():
    #                if c_emoji.name == 'Buy':
    #                    buy = c_emoji
            await client.add_reaction(clicker_mess, coin)
    #            await client.add_reaction(clicker_mess, blank)
    #            await client.add_reaction(clicker_mess, buy)
            clicker_start = True
            click = "l"
            noc = "l"
            while True == True:
                click = await client.wait_for_reaction(emoji=coin, user=message.author, timeout=0.05, message=clicker_mess)
                if not click is None:
                    if len(click) > 1:
                        clicks = clicks + 1
                        await client.edit_message(clicker_mess, new_content=str(message.author.display_name) + " has " + str(clicks) + " coins")
                        await client.remove_reaction(clicker_mess, coin, message.author)
                        click = "l"
                        print(len(click))
            
    #                print("hello")
    #                noc = await client.wait_for_reaction(emoji=buy, user=message.author, timeout=0.05, message=clicker_mess)
    #                print("hello")
    #                if not noc is None:
    #                    if len(noc) > 1:
    #                        print("hello")
    #                        if clicks >= 100:
    #                            clicks -= 100
    #                            auto_clickers += 1
    #                        client.edit_message(clicker_mess, new_content=str(message.author.display_name) + " has " + str(clicks) + " coins and " + str(auto_clickers) + " autoclickers")
    #                        noc = "l"
    #                        await client.remove_reaction(clicker_mess, buy, message.author)

            
    #                if auto_clickers > 0:
    #                    if current_hour != now.hour:
    #                        clicks += auto_clickers * 10
    #                        current_hour = now.hour
                    

        if message.channel.name == "clickergame":
            await client.delete_message(message)
            
    
                         
        



client.run("NDMwMTE4NDY0NzU0Mjg2NTk2.DaLinw.e4Ni_FD00Z2rHgzpyQdZ8sG1y10")


