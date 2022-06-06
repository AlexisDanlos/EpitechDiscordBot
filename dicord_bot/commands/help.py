from discord.ext import commands

def setup(bot):
    bot.add_command(help)

@commands.command(name='help', pass_context=True)
async def help(ctx: commands.Context):
    content = ctx.message.content.split()
    if len(content) == 1:
        await ctx.send('```!epilogin\n!del\n!ping\n!reset\n!stats\n!subject\n!help\n\n\nUse !help <command> for more information```')
    elif len(content) == 2:
        if content[1] == 'epilogin':
            await ctx.send('```!epilogin <direct login link>\n\nSaves a direct login link to your account```')
        elif content[1] == 'del':
            await ctx.send('```!del <number>\n\nDeletes the last <number> messages```')
        elif content[1] == 'ping':
            await ctx.send('```!ping\n\nChecks if the bot is online```')
        elif content[1] == 'reset':
            await ctx.send('```!reset\n\nResets your login link```')
        elif content[1] == 'stats':
            await ctx.send('```!stats\n\nShows your credits number and GPA```')
        elif content[1] == 'subject':
            await ctx.send('```!subject <subject>\n\nSends a webhook with the list of the documents for the given subject```')
        elif content[1] == 'help':
            await ctx.send('```!help\n\nShows this message```')
        else:
            await ctx.send('```Command not found. Use !help for a list of commands```')
    else:
        await ctx.send('```Usage:\n\t!help\n\t!help <command>```')