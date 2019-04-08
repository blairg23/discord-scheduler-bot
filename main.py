import discord
import bot
import _commands

from _discord import Discord

import config as cfg

_discord = Discord()
client = _discord.get_client()

bot = bot.SchedulerBot()

bot.commands.append(_commands.Setup())

if cfg.bot["version"] == "dev":
    bot.commands.append(_commands.StopCommand())


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")
    # client.loop.create_task(periodicReminders())
    # client.loop.create_task(periodicTeamUPSync())
    # cool status when bot is online
    game = discord.Game(name="DEVELOPMENT" if cfg.bot["version"] == "dev" else "PRODUCTION")
    await client.change_presence(game=game)


# on message go through registered commands
@client.event
async def on_message(message):
    for command in bot.commands:
        if message.content.startswith(command.activation_string):
            vals = message.content.split(" ")
            if len(vals) > 1:
                if vals[1] == "help":
                    await command.help(message)
                    return

            await command.action(bot, message)
            return


print(cfg)
client.run(cfg.bot["prod_token"] if cfg.bot["version"] == "prod" else cfg.bot["dev_token"])
