import discord
from discord.ext import commands
from commands.lib.manage_db import manage_db
from dotenv import load_dotenv
import os

load_dotenv('.env')
KEY = (os.getenv('KEY')).encode()

def setup(bot):
    bot.add_command(epilogin)

@commands.command(name='epilogin', pass_context=True)
async def epilogin(ctx: commands.Context):
    if ctx.channel.type == discord.ChannelType.private:
        content = ctx.message.content.split(' ')
        if len(content) != 2:
            print("Wrong number of arguments")
            await ctx.channel.send('Usage: !epilogin <direct login link>')
        else:
            if manage_db(key=KEY).is_link_valid(content[1]) == True:
                manage_db(key=KEY).register_new_login_link(str(ctx.author.id), content[1], str(ctx.author))
                await ctx.channel.send('Your login link has been saved.')
            else:
                print("Link provided is invalid. Please check it's an autologin link and the link is still valid.")
                await ctx.channel.send('The link you provided is not valid.')
    else:
        to_del = await ctx.channel.history(limit=1).flatten()
        await to_del[0].delete()
        await ctx.channel.send('Error: This command can only be used in a DM.')