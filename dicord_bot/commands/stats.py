from discord.ext import commands
from commands.lib.manage_db import manage_db
from commands.lib.EpicLib import EpicLib
from dotenv import load_dotenv
import os, asyncio

load_dotenv('.env')
KEY = (os.getenv('KEY')).encode()

def setup(bot):
    bot.add_command(stats)

async def get_stats(ctx):
    login_link = manage_db(key=KEY).get_login_link(discord_id=str(ctx.message.author.id))
    if login_link == None:
        print("No login link found")
        await ctx.channel.send(f'<@{ctx.author.id}> no login link found')
    else:
        embed = await EpicLib().get_student_infos(loginlink=login_link)
        await ctx.channel.send(embed=embed)

@commands.command(name='stats', pass_context=True)
async def stats(ctx: commands.Context):
    status = await manage_db(key=None).get_command_status(command='stats')
    if status == 1:
        asyncio.create_task(get_stats(ctx))
    else:
        await ctx.channel.send('This command is currently disabled')