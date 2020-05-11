import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from spellbook import Spellbook
import botSpells
from weaponsbook import WeaponsBook
import pymysql
from auth import *
import helpmenu
import utilites
import random
import os
import pg_generator
import dice

token = token
# bot initalization!
bot = commands.Bot(command_prefix='!', description='Un taverniere che ti aiuta nella tua sessione D&D.')
dnd_manual = Spellbook("db_user", "db_psw", "db_host", "db_name")
bot.remove_command('help')

# get spells by class command - it gets a list with names of spells available

@bot.command()
async  def incantesimi(ctx,dnd_class: str,level: int):
    # force arg to be lower
    dnd_class_lower = dnd_class.casefold()
    spells = dnd_manual.get_spells_by_class_level(dnd_class_lower, level)
    await botSpells.send_spells_list_embed(ctx,dnd_class_lower,level,spells)



# get single weapon with details command
@bot.command()
async def arma(ctx, *args):
            dnd_manual = WeaponsBook("db_user", "db_password", "db_host", "db_name")
            weapon = utilites.PasteStringSpace(args)
            weapon = weapon.lower()
            content_onBook = dnd_manual.getWeapons(weapon)
            if(content_onBook):
                for tupla in content_onBook:
                    embed = discord.Embed(title=weapon.capitalize(), color=0x66ff66)
                    for column, value in tupla.items():
                        if(column=="Nome"):
                            embed.title=value
                        embed = embed.add_field(name=column, value=value, inline=True)
                    await ctx.send(embed=embed)

            else:
                await ctx.send("```Non trovo l'arma [" + weapon.capitalize() + "]```")


# get weapons by category command - it gets a list with weapon available in input category
@bot.command()
async def vediarmi(ctx,*args):
        #here there is a limiter and countFieldsMax to bypass embed limit on discord.py class that's up to 25 fields (i set up to 24)
        dnd_manual = WeaponsBook("db_user", "db_password", "db_host", "db_name")
        category = utilites.PasteStringSpace(args)
        category = category.lower()
        if('semplici' in category):
            category='arma semplice'
        bookContent = dnd_manual.getWeapons_by_category(category)
        if(bookContent):
            embed = discord.Embed(title=category.capitalize(), color=0x66ff66)
            embed_second = discord.Embed(title=category.capitalize(), color=0x66ff66)
            embed_third = discord.Embed(title=category.capitalize(), color=0x66ff66)
            i=0
            flag=0
            for tupla in bookContent:
                for column,value in tupla.items():
                    if(column != "Categoria"):
                        if(i<24):
                            embed.add_field(name=column,value=value)
                            i=i+1
                        elif(i<48):
                                flag=1
                                embed_second.add_field(name=column, value=value)
                                i = i + 1
                        elif(i<96):
                                flag=2
                                embed_third.add_field(name=column,value=value)
                                i=i+1
                    else:
                        embed.title=value
                        embed_second.title=value
                        embed_third.title=value
            await ctx.send(embed=embed)
            if(flag==1):
                await ctx.send(embed=embed_second)
            if(flag==2):
                await ctx.send(embed=embed_second)
                await ctx.send(embed=embed_third)

        else:
            await ctx.send("```Non trovo le armi di categoria [" + category.capitalize() + "]```")

# ready-bot command
@bot.event
async def on_ready():
    print('Sono pronto viandante!')

# get single spell with details command
@bot.command()
async def incanto(ctx,*args):
    spell = utilites.PasteStringSpace(args)
    content_onBook = dnd_manual.get_spells_by_name(spell)
    await botSpells.send_spell_details(ctx, content_onBook, spell)


# random-character generator command - just to have fun with your friends on generate strange characters :)
@bot.command()
async def generapg(ctx):
        embed = pg_generator.generateClassAndRace()
        await ctx.send(embed=embed)


# Help commands
@bot.command()
async def aiuto(ctx, *args):
        await ctx.send(helpmenu.helpGeneral())
@bot.command()
async  def aiutodadi(ctx):
    await ctx.send(helpmenu.helpDices())
@bot.command()
async  def aiutoincantesimi(ctx):
    await ctx.send(helpmenu.helpSpells())
@bot.command()
async  def aiutoarmi(ctx):
    await ctx.send(helpmenu.helpWeapons())

# dice-rolling command
@bot.command()
async  def lancia(ctx,*args):
    roll = dice.rolling(args)
    await ctx.send(roll)

#cleaning chat-text channel with this command - keep attention using this
@bot.command()
async def pulisci(ctx, amount: str):
    if('tutto' in amount):
        amount=100000
        await ctx.channel.purge(limit=amount)
        await ctx.send("```Ecco fatto! La taverna adesso è pulita```")
        print('pulito tutto')

#token is in auth.py
bot.run(token)
