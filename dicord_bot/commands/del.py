from discord.ext import commands
from commands.lib.manage_db import manage_db

def setup(bot):
    bot.add_command(delete)

@commands.command(name='del', pass_context=True)
async def delete(ctx: commands.Context):
    content = ctx.message.content.split()
    if len(content) == 2:
        number = int(content[1])
        messages = await ctx.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()
    else:
        await ctx.send('```Usage:\n\t!del <number>```')