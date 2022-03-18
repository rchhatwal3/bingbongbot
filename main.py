#import discord library and bot serv
import discord
from botServ import botServ
from token import TOKEN
import os

bot = discord.Client()

def printLeaderboard():
    pass

def addToDatabase():
    pass

#on start
@bot.event
async def on_ready():
    print("Bot connected")

@bot.event
async def on_message(message):
    currentMessage = message.content.lower()
    print(currentMessage)

botServ()
bot.run(TOKEN)