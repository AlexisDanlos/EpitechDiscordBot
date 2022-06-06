from discord.ext import commands
from commands.lib.manage_db import manage_db
from commands.lib.EpicLib import EpicLib
from dotenv import load_dotenv
import os

load_dotenv('.env')
KEY = (os.getenv('KEY')).encode()

def setup(bot):
    bot.add_command(subject)

@commands.command(name='subject', pass_context=True)
async def subject(ctx: commands.Context):
    content = ctx.message.content.split(' ')
    if len(content) != 2:
        print("Wrong number of arguments")
        await ctx.channel.send('Usage: !subject <subject name>')
    else:
        subject = content[1]
        login_link = manage_db(key=KEY).get_login_link(str(ctx.author.id))
        if login_link == None:
            print("No login link found")
            await ctx.channel.send(f'<@{ctx.author.id}> no login link found')
        else:
            embed = await EpicLib().get_project_subject(subject, loginlink=login_link)
            if embed == False:
                print("No subject found")
                await ctx.channel.send('Subject not found')
            else:
                print("Subject found")
                await ctx.channel.send(embed=embed)