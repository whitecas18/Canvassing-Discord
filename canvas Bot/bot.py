# bot.py
import os
import discord
from html2text import html2text
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
    if  message.content.startswith("!id1"):
        global classCode
        classCode = message.content[4:]
    if message.content.startswith("!id2"):
        global instCode
        instCode = message.content[4:]
        await message.channel.send(instCode)
    if message.content.startswith("!id3"):
        global authCode
        authCode = message.content[4:]


@client.event
async def on_message(message):
    if message.content == '!announcement':
        course = CanvasCourse(instCode,authCode,classCode)
        array = course.getAnnouncements()
        await message.channel.send(html2text(array[0]['message']))
    if message.content == '!assignment':
        await message.channel.send(course.getAssignments())
    if message.content == '!test':
        await message.channel.send(classCode+' '+instCode+' '+authCode)
        

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


client.run(token)