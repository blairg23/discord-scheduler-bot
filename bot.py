import discord
import _commands
import asyncio

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
        parameters = message.content.split(" ")
        interval = parameters[1]
        interval_units = parameters[2]
        member_order_list = parameters[3:]

        print(f'interval: {interval}')
        print(f'interval_units: {interval_units}')
        print(f'member_order_list: {member_order_list}')
