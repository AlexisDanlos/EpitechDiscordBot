from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv('.env')
TOKEN = os.getenv('DISCORD_TOKEN')

class myBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!')

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')


bot = myBot()
bot.remove_command('help')
bot.load_extension('commands.ping')
bot.load_extension('commands.stats')
bot.load_extension('commands.subject')
bot.load_extension('commands.epilogin')
bot.load_extension('commands.del')
bot.load_extension('commands.reset')
bot.load_extension('commands.help')
bot.run(TOKEN)