'''
Doesn't work with Python3.7 out of the box. If you're using Python 3.7, 
follow this: https://stackoverflow.com/a/53158394/1224827

NOTE: This is the old way of handling commands. Left in the repo for reference' sake.
Took me forever to get this shit working properly from the docs -.-;
'''
import embeds
import discord

client = discord.Client()


class Command:
    activation_string = ""
    help_string = ""
    example = ""

    async def action(self, bot, context, *args):
        raise NotImplementedError

    # default help message for every command (!command help)
    async def help(self, context):
        help_embed = embeds.info("Help for command `%s`" % self.activation_string, self.help_string)
        help_embed.add_field(name="Example", value=self.example)
        await context.send(content="", embed=help_embed)


class Setup(Command):
    activation_string = "!setup"
    help_string = "Sets up the server for bot to use:\n**Arguments**:\n`!setup [interval] [interval-units] \"[message]\" [member-order-list]`"
    example = "`!setup 6 hours \"Time to pick your loot! You have 6 hours!\" @exampleuser1 @exampleuser2 @exampleuser3`"

    async def action(self, bot, context, *args):
        await bot.setup(context, *args)


class StopCommand(Command):
    '''
        Stops the bot from within, because CTRL+C sometimes takes too long
    '''
    activation_string = "!stop"
    help_string = "DEVELOPMENT ONLY - stops the bot"

    async def action(self, bot, context, *args):
        await client.logout()
