from discord.ext import commands

import secrets

self_bot = commands.Bot(command_prefix = "!")

@self_bot.event
async def on_ready():
    print('Logged in as')
    print(self_bot.user.name)
    print(self_bot.user.id)
    print('------')

@self_bot.command()
async def self_destruct(*args):
    return await self_bot.say("How about no.")

@self_bot.command()
async def time(*args):
    for arg in args:
        if arg.lower() == "russia":
            return await self_bot.say("I don't know the time in Russia!")
    return await self_bot.say("Derp.")

self_bot.run(secrets.SELF_BOT_TOKEN)
