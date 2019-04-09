import discord
import asyncio


class SchedulerBot:
    commands = []
    
    async def setup(self, context, *args):
        '''
        Command: !setup [interval] [interval-units] \"[message]\" [member-order-list]
        '''
        print(f"I'm getting set up by {context.author}")
        interval = args[0]
        interval_units = args[1]
        message = args[2]
        member_order_list = args[3:]

        print(f'interval: {interval}')
        print(f'interval_units: {interval_units}')
        print(f'message: {message}')
        print(f'member_order_list: {member_order_list}')
