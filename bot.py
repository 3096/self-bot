from discord.ext import commands

import config
import usertime
import secrets

self_bot = commands.Bot(command_prefix = "!")

@self_bot.event
async def on_ready():
    config.setup()
    print('Logged in as')
    print(self_bot.user.name)
    print(self_bot.user.id)
    print('------')

@self_bot.command()
async def self_destruct(*args):
    return await self_bot.say("How about no.")

@self_bot.command(pass_context=True)
async def settime(ctx, *args):
    return await self_bot.say( usertime.set_time(ctx, *args) )

@self_bot.command()
async def timezones():
    return await self_bot.say( usertime.get_all_timezones() )

@self_bot.command(pass_context=True)
async def time(ctx, *args):
    return await self_bot.say( usertime.get_time(ctx, *args) )

self_bot.run(secrets.SELF_BOT_TOKEN)
