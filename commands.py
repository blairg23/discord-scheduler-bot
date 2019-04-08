'''
Doesn't work with Python3.7 out of the box. If you're using Python 3.7, 
follow this: https://stackoverflow.com/a/53158394/1224827
'''
import embeds
from _discord import Discord

_discord = Discord()
client = _discord.get_client()


class Command:
    activation_string = ""
    help_string = ""
    example = ""

    async def action(self, bot, message):
        raise NotImplementedError

    # default help message for every command (!command help)
    async def help(self, message):
        help_embed = embeds.Info("Help for command `%s`" % self.activation_string, self.help_string)
        help_embed.add_field(name="Example", value=self.example)
        await _discord.send_message(message.channel, embed=help_embed)


class Setup(Command):
    activation_string = "!setup"
    help_string = "Sets up the server for bot to use:\n**Arguments**:\n`!setup [interval] [interval-units] [member-order-list] \"[command]\"`" # TODO
    example = "`!setup 6 hours @exampleuser1 @exampleuser2 @exampleuser3 \"Time to pick your loot! You have 6 hours!\"`"

    async def action(self, bot, message):
        await bot.setup(message)


class StopCommand(Command):
    '''
        Stops the bot from within, because CTRL+C sometimes takes too long
    '''
    activation_string = "!stop"
    help_string = "DEVELOPMENT ONLY - stops the bot"

    async def action(self, bot, message):
        await client.logout()
