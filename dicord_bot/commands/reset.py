from discord.ext import commands
from commands.lib.manage_db import manage_db
from commands.lib.EpicLib import EpicLib
from dotenv import load_dotenv
import os

load_dotenv('.env')
KEY = (os.getenv('KEY')).encode()

def setup(bot):
    bot.add_command(reset)

@commands.command(name='reset', pass_context=True)
async def reset(ctx: commands.Context):
    login_link = manage_db(key=KEY).get_login_link(str(ctx.author.id))
    if login_link == None:
        print("No login link found")
        await ctx.channel.send(f'<@{ctx.author.id}>, You don\'t have a login link registered yet')
    else:
        await EpicLib().reset_login_link(discord_id=str(ctx.author.id), loginlink=login_link, key=KEY)
        await ctx.channel.send(f'<@{ctx.author.id}> Your login link has been reset.')
