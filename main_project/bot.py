# bot.py
import os
import discord
from html2text import html2text
from dotenv import load_dotenv
from discord.ext import commands, tasks
from CanvasCourse import CanvasCourse

load_dotenv()
token = os.getenv('DISCORD_TOKEN')


client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

course = CanvasCourse()

@client.event
async def on_message(message):
    if message.content == '!announcement':
        array = course.getAnnouncements()
        await message.channel.send(html2text(array[0]['message']))
    if message.content == '!assignment':
        await message.channel.send(course.getAssignments())
    if  message.content.startswith("!classcode"):
        classCode = message.content.split(" ")[1]
        course.setCCode(classCode)
        print(classCode)
        await message.channel.send(classCode)
    if message.content.startswith("!instcode"):
        instCode = message.content.split(" ")[1]
        course.setInst(instCode)
        await message.channel.send(instCode)
    if message.content.startswith("!authcode"):
        authCode = message.content.split(" ")[1]
        print(authCode)
        course.setAuth(authCode)
        await message.channel.send(authCode)

@tasks.loop(hours=24)
async def called_once_a_day():
    message_channel = bot.get_channel(target_channel_id)
    print(f"Got channel {message_channel}")
    await message_channel.send('!announcement')


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
