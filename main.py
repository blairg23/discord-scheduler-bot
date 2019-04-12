import discord
import bots
from discord.ext import commands

import config

client = discord.Client()
bot = commands.Bot(command_prefix='!')
scheduler_bot = bots.SchedulerBot()


@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")
    # client.loop.create_task(periodicReminders())
    # client.loop.create_task(periodicTeamUPSync())
    # cool status when bot is online
    game = discord.Game(name="DEVELOPMENT" if config.bot["version"] == "dev" else "PRODUCTION")
    await bot.change_presence(activity=game)


@bot.command()
async def ping(context):
    await context.send("pong")


@bot.command()
async def setup(context, *args):
    await scheduler_bot.setup(context, *args)


@bot.command()
async def start(context):
    await scheduler_bot.start(context)


@bot.command()
async def stop(context):
    if config.bot["version"] == "dev":
        await bot.logout()
    else:
        await context.send("Sorry, Dave, you can only shut me off in development mode.")

bot.run(config.bot["prod_token"] if config.bot["version"] == "prod" else config.bot["dev_token"])
