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


for c_emoji in client.get_all_emojis():
    if c_emoji.name == 'Coin':
        coin = c_emoji

@client.event
async def on_message(message):
    if message.author.id != "430118464754286596":

        if message.content == "clicker startup":
            await client.delete_message(message)
            await client.send_message(message.channel, "@everyone I'm holding a contest for **$25 Bitcoin** \n Whoever gets the most clicks over the next week wins \n Countdown: https://www.timeanddate.com/countdown/generic?day=08&p0=820&font=cursive \n Say \"play clicker\" to begin, and start clicking!")
            await client.send_message(message.channel, "------------------------------------------------------------------------------------------------")
                
        if message.content == "play clicker" and message.channel.name == "clickergame" or message.channel.name == "bot-devolper":
            await client.delete_message(message)
            clicks = 0
            clicker_mess = await client.send_message(message.channel, str(message.author.display_name) + " has " + str(clicks) + " coins")

            await client.add_reaction(clicker_mess, coin)
            click = "l"
            while True == True:
                click = await client.wait_for_reaction(emoji=coin, user=message.author, timeout=0.05, message=clicker_mess)
                if not click is None:
                    if len(click) > 1:
                        clicks = clicks + 1
                        await client.edit_message(clicker_mess, new_content=str(message.author.display_name) + " has " + str(clicks) + " coins")
                        await client.remove_reaction(clicker_mess, coin, message.author)
                        click = "l"
            

                    

        if message.channel.name == "clickergame":
            await client.delete_message(message)
            
    
                         
        



client.run("NDMwMTE4NDY0NzU0Mjg2NTk2.DaLinw.e4Ni_FD00Z2rHgzpyQdZ8sG1y10")


