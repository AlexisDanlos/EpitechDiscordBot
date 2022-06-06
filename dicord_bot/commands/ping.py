from discord.ext import commands

def setup(bot):
    bot.add_command(ping)

@commands.command(name='ping', pass_context=True)
async def ping(ctx: commands.Context):
    await ctx.send('Pong!')