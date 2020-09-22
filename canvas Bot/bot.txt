# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands, tasks
from CanvasCourse import CanvasCourse

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client=discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
@client.event
async def on_message(message):
    if message.content == '!announcement':
        await message.channel.send('Announcements:')
    if message.content == '!assignment':
        await message.channel.send('Assignments:')

@tasks.loop(hours=24)
async def called_once_a_day():
    message_channel = bot.get_channel(target_channel_id)
    print(f"Got channel {message_channel}")
    await message_channel.send('!anouncement')

@tasks.loop(hours=24)
async def called_once_a_day():
    message_channel = bot.get_channel(target_channel_id)
    print(f"Got channel {message_channel}")
    await message_channel.send('!assignment')

@called_once_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")



client.run(token)