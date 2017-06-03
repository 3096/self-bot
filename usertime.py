import pytz
from pytz import timezone
from datetime import datetime
import discord
import json


def find_tz(str):
    for tz in pytz.all_timezones:
        if str.lower() in tz.lower():
            return tz
    return None

def get_all_timezones():
    response = "Here is a list of time zones I know:\n"
    response += "https://github.com/3096/self-bot/blob/master/documents/timezones.md"
    return response

def set_time(ctx, *args):
    if len(args) == 0:
        return "Usage: !settime {your time zone}"

    if len(ctx.message.mentions) > 0:
        if ctx.message.mentions[0] != ctx.message.author and not ctx.message.author.server_permissions.administrator:
            return "Only administrator can set other's time zone!"
        else:
            member = ctx.message.mentions[0]
    else:
        member = ctx.message.author

    for kw in args:
        tz = find_tz(kw)
        if tz is not None:
            break
    if tz is None:
        return "No time zone match found! Try !timezones to check available time zones."

    with open('config/usertime.json', 'r') as f:
        usertimes = json.load(f)
    usertimes[member.id] = tz
    with open('config/usertime.json', 'w') as f:
        json.dump(usertimes, f)

    return "{}'s time zone has been set to \"{}\"".format(member.mention, tz)

def get_timestr(member, usertimes):
    return datetime.now(timezone(usertimes[member.id])).strftime("%I:%M %p, %a %b. %d (%Z%z)")

def get_time_msg(member, usertimes):
    if member.id in usertimes:
        return "{}'s time is {}.".format(member.mention, get_timestr(member, usertimes))
    else:
        return "I don't know {}'s time zone, use !settime to tell me!".format(member.mention)

def get_time_of(members, usertimes, response):
    for member in members:
        response += get_time_msg(member, usertimes) + "\n"
    return response

def get_time(ctx, *args):
    with open('config/usertime.json', 'r') as f:
        usertimes = json.load(f)

    for kw in args:
        if kw.lower() == "online":
            members = []
            for member in ctx.message.server.members:
                if member.status == discord.Status.online and not member.bot:
                    members.append(member)

            return get_time_of(members, usertimes, "Here is all online members' local time:\n")

    if len(ctx.message.mentions) > 0:
        return get_time_of(ctx.message.mentions, usertimes, "")
    else:
        author = ctx.message.author
        if author.id in usertimes:
            return "{}, your time is {}.".format(author.mention, get_timestr(author, usertimes))
        else:
            return "I don't know your time zone, {}. use !settime to tell me!".format(author.mention)
