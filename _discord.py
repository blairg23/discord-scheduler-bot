import discord
import asyncio
from datetime import datetime

class Discord:
    _instance = None
    client = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

    def __init__(self):
        if self.client is None:
            self.client = discord.Client()

            if self.client is not None:
                print("Discord bot pooling created successfully")

    def get_client(self):
        return self.client

    async def send_message(self, channel, content="", embed=None):
        '''
            Just a wrapper for sending messages, so I don't have to deal with exceptions inside code
        '''
        try:
            return await self.client.send_message(channel, content=content, embed=embed)
        except Exception as e:
            pass
            #print("ERROR: cmonBruh (send_message) - "+ str(e) + " " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
      
    async def get_message(self, channel, id):
        '''
            Wrapper for getting a message to handle exceptions
        '''
        msg = None
        try:
            msg = await self.client.get_message(channel, id)
        except Exception as e:
            pass
            #print("ERROR: SwiftStrike (get_message) - "+ str(e) + " " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return msg

    async def edit_message(self, message, new_content=None, embed=None):
        '''
            Wrapper for editing a message to handle exceptions
        '''
        msg = None
        try:
            msg = await self.client.edit_message(message, new_content=new_content, embed=embed)
        except Exception as e:
            pass
            #print("ERROR: :rage: (edit_message) - "+ str(e) + " " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return msg