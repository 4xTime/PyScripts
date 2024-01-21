import discord
from discord.ext import commands
from Util import *

intents = discord.Intents().all()

client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix="!",intents=intents)
bot.remove_command("help")
channel_id,server_id,TOken= read_credentials_from_file("SHbotWebControl/config.ini")

@bot.event
async def on_reaction_add(reaction, user):
    mess = reaction.message
    if user != bot.user:
        if str(reaction.emoji) == "👍":
            #channel where message is
            if reaction.message.channel.id == channel_id:
                    Bol,_,__ = search_for_user(str(user))
                    if Bol == False:
                        if os.path.isfile('SHbotWebControl/dataset.txt') == True:
                            with open('SHbotWebControl/dataset.txt','a') as File:
                                print(f"{log_time()}{color_text(' SUCCES: ',GREEN)}{color_text(user,CYAN)} has been added to database")
                                event_log(f"{log_time()} SUCCES: {user} has been added to database")
                                File.write(str(user)+"\n")
                            File.close()

        if str(reaction.emoji) == "👎":
            #channel where message is
            if reaction.message.channel.id == channel_id:
                Bol,line_num,line = search_for_user(str(user))
                if Bol == True:
                    with open("SHbotWebControl/dataset.txt", "r") as input:
                        with open("SHbotWebControl/temp.txt", "w") as output:
                            for line in input:
                                if line.strip("\n") != str(user):
                                    output.write(line)
                                print(f"{log_time()}{color_text(' SUCCES: ',GREEN)}{color_text(user,CYAN)} has been deleted from database")
                                event_log(f"{log_time()} SUCCES: {user} has been deleted from database")

                    os.replace('SHbotWebControl/temp.txt', 'SHbotWebControl/dataset.txt')

@bot.event 
async def add_react(msg,reactup):
    for howm in reactup:
        await msg.add_reaction("{}".format(howm))
