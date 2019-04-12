import asyncio


class SchedulerBot:
    def __init__(self):
        self.config = {
            'interval': None,
            'message': None,
            'member_order_list': None
        }

    def get_interval_in_seconds(self, interval, interval_units):
        interval = int(interval)
        if interval_units.lower() == 'seconds':
            return interval
        elif interval_units.lower() == 'minutes':
            return interval * 60
        elif interval_units.lower() == 'hours':
            return interval * 60 * 60

    async def setup(self, context, *args):
        '''
        Command: !setup [interval] [interval-units] \"[message]\" [member-order-list]
        '''
        keep_going = True
        messages = []

        print(f"I'm getting set up by {context.author}")
        interval = args[0]
        interval_units = args[1]
        message = args[2]
        member_order_list = args[3:]

        print(f'interval: {interval}')
        print(f'interval_units: {interval_units}')
        print(f'message: {message}')
        print(f'member_order_list: {member_order_list}')

        if not isinstance(interval, int):
            try:
                interval = int(interval)
            except:
                messages.append('ERROR: Interval must be a number!')
                keep_going = False

        if not isinstance(interval_units, str) or interval_units.lower() not in ['seconds', 'minutes', 'hours']:
            messages.append("ERROR: Interval Units must be one of the following choices: ['seconds', 'minutes', 'hours']")
            keep_going = False

        if keep_going:
            interval_in_seconds = self.get_interval_in_seconds(interval=interval, interval_units=interval_units)

            self.config['interval'] = interval_in_seconds
            self.config['message'] = message
            self.config['member_order_list'] = member_order_list

            print(self.config)
        else:
            for message in messages:
                await context.send(message)

    async def start(self, context):
        interval = self.config['interval']
        usernames = self.config['member_order_list']
        message = self.config['message']

        for username in usernames:
            await context.send(f'{username}: {message}')
            await asyncio.sleep(interval)
