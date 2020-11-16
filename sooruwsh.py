import discord
import asyncio
from discord.ext import commands
import logging

client = commands.Bot(command_prefix = '`')
#client.remove_command('help')
admins = [710029850991263775]
##########      admin

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="UltraViolet Family"))
    print(f'|-----------------------------------|')
    print(f'            Bot is Ready             ')
    print(f' Bot UserName: {client.user.name}    ')
    print(f' Bot User ID : {client.user.id}      ')
    print(f'|-----------------------------------|')

@client.command(aliases=['Playing'])
async def playing(ctx, *, playing):
    if ctx.message.author.id in admins:
        await client.change_presence(activity=discord.Game(name=playing))
        await ctx.send('Playing Status Changed 💫')
        print('Playing Status Changed 💫')
    else:
        await ctx.send('You Are not an Admin... 𝐒𝐡𝐞𝐲𝐤𝐡 𝐒𝐨𝐨𝐫𝐮𝐰𝐬𝐡#9999 to become an Admin')
        pass

@client.command(aliases=['Streaming'])
async def streaming(ctx, *, streaming):
    if ctx.message.author.id in admins:
        await client.change_presence(activity=discord.Streaming(name=streaming, url='https://www.twitch.tv/sooruwsh'))
        await ctx.send('Streaming Status Changed 💫')
        print('Streaming Status Changed 💫')
    else:
        await ctx.send('You Are not an Admin... Contact 𝐒𝐡𝐞𝐲𝐤𝐡 𝐒𝐨𝐨𝐫𝐮𝐰𝐬𝐡#9999 to become an Admin')
        pass

@client.command(aliases=['Listening'])
async def listening(ctx, *, listening):
    if ctx.message.author.id in admins:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=listening))
        await ctx.send('Listening Status Changed 💫')
        print('Listening Status Changed 💫')
    else:
        await ctx.send('You Are not an Admin... Contact 𝐒𝐡𝐞𝐲𝐤𝐡 𝐒𝐨𝐨𝐫𝐮𝐰𝐬𝐡#9999 to become an Admin')
        pass

@client.command(aliases=['Watching'])
async def watching(ctx, *, watching):
    if ctx.message.author.id in admins:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=watching))
        await ctx.send('Watching Status Changed 💫')
        print('Watching Status Changed 💫')
    else:
        await ctx.send('You Are not an Admin... Contact 𝐒𝐡𝐞𝐲𝐤𝐡 𝐒𝐨𝐨𝐫𝐮𝐰𝐬𝐡#9999 to become an Admin')
        pass

@client.command(aliases=['ResetStatus','rs','RS'])
async def resetstatus(ctx):
    if ctx.message.author.id in admins:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="joooon💙"))
        await ctx.send('Bot Status Reseted 💫')
        print('Bot Status Reseted 💫')
    else:
        await ctx.send('You Are not an Admin... Contact 𝐒𝐡𝐞𝐲𝐤𝐡 𝐒𝐨𝐨𝐫𝐮𝐰𝐬𝐡#9999 to become an Admin')
        pass

@client.command(pass_context=True)
async def say(ctx, *, say):
    if ctx.message.author.id in admins:
        await ctx.message.delete()
        await ctx.send(say)
        print('-------------------------------------------')
        print(f'[^say]> {ctx.message.author.name} Said {say} in {ctx.message.channel.mention}')
    else:
        await ctx.send('You Are not an Admin... Contact 𝐒𝐡𝐞𝐲𝐤𝐡 𝐒𝐨𝐨𝐫𝐮𝐰𝐬𝐡#9999 to become an Admin')
        pass


client.run('Nzc3OTk1NzM0MzQ3MDIyMzU4.X7Li_Q.-e-uAr3M5sLx14aD-Ma8kxkgipY')
