import discord
import commands

from _discord import Discord

_discord = Discord()
client = _discord.get_client()

class SchedulerBot:
    commands = []
    
    async def setup(self, message):
        '''
        Command: !setup [interval] [interval-units] [member-order-list]
        '''
        print(f"I'm getting set up by {message.author}")


