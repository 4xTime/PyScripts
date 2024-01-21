from SHevents import *
from Util import *
#from Util import update_embed
import discord
from discord.ext import commands , tasks
import os

class webSHbot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(**kwarg)
        self.title
        self.tekst
        self.time:float
        self.dir_events_folder

    async def update_embed(counter,embed_mess,message):
        #counter = counter * 3600
        counter = counter*1
        while True:
            counter = counter -1
            embed_mess.set_field_at(0, name='Time to expire', value=str(datetime.timedelta(seconds=counter)))
            #message = await channel.fetch_message(embed_mess.message_id)
            await message.edit(embed=embed_mess)
            #await message.add_reaction("👍")
            await asyncio.sleep(1)
            if counter == 0:
                #TODO if time expire message will show that time is expired and no one can be added to dataset
                embed_mess.set_field_at(0, name='Time to expire', value=str("TIME EXPIRED"))
                await message.edit(embed=embed_mess)

                await webSHbot.create_web_event("T","a",5,'SHbotWebControl/SiteSHbot/events')
                break

    async def create_web_event(title,tekst,time:float,dir_events_folder):
        while True:
            if os.path.exists(dir_events_folder):
                if get_format_from_file(dir_events_folder+'//'):
                    title,tekst,time = extract_data(dir_events_folder+'//')
                    delete_file_after_event_create(dir_events_folder+'//')

                    embed = discord.Embed(title=title,description=tekst)
                    embed.add_field(name='Value', value=time)

                    msg = await SetBotChannel(bot.get_guild(server_id),channel_id).send(embed=embed,delete_after=time*3600)

                    await msg.add_reaction("👍")
                    await msg.add_reaction("👎")
                                    
                    print(f"{log_time()}{color_text(' SUCCES:',GREEN)} event created")
                    event_log(f"{log_time()} SUCCES: event created")

                    await webSHbot.update_embed(time,embed,msg);

                    break;
            else:
                print(f"{log_time()}{color_text(' ERROR: ',RED)}{color_text(' events ',YELLOW)} Can't be found")
                event_log(f"{log_time()} ERROR: events Can't be found")
                break

    async def setup_hook(self):
         await self.create_web_event() 
         await self.update_embed()


@bot.event
async def on_ready():
    create_file_for_dataset_and_serverlog('SHbotWebControl/dataset.txt','SHbotWebControl/ServerLog')
    print(f"{log_time()} bot->{color_text('READY',GREEN)}")
    event_log(f"{log_time()} bot->READY")
    activity = discord.Activity(type=discord.ActivityType.listening, name="MUSIC")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    await webSHbot.create_web_event("T","a",5,'SHbotWebControl/SiteSHbot/events')

bot.run(TOken)