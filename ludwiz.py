from discord.ext import commands
from databases.spellbook import Spellbook
from spells import bot_spells
import bot_weapons
from weaponsbook import WeaponsBook
from auth import *
import helpmenu
import utilites
import pg_generator
import dice

token = token
# bot initalization!
bot = commands.Bot(command_prefix='!', description='Un taverniere che ti aiuta nella tua sessione D&D.')
dnd_manual_spells = Spellbook(db_user_spell, db_psw_spell, db_host, db_name_spell)
dnd_manual_weapons = WeaponsBook(db_user_weapons, db_psw_weapons, db_host, db_name_weapons)
bot.remove_command('help')


# get spells by class command - it gets a list with names of spells available
@bot.command()
async def incantesimi(ctx, dnd_class: str, level: int):
    # force arg to be lower
    dnd_class_lower = dnd_class.casefold()
    spells = dnd_manual_spells.get_spells_by_class_level(dnd_class_lower, level)
    await bot_spells.send_spells_list_embed(ctx, dnd_class_lower, level, spells)


# get single spell with details command
@bot.command()
async def incanto(ctx, *args):
    spell_name = utilites.PasteStringSpace(args)
    spells = dnd_manual_spells.get_spells_by_name(spell_name)
    await bot_spells.send_spell_details(ctx, spells, spell_name)


# get single weapon with details command
@bot.command()
async def arma(ctx, *args):
    weapon = utilites.PasteStringSpace(args)
    weapon = weapon.lower()
    content_onBook = dnd_manual_weapons.getWeapons(weapon)
    await bot_weapons.send_weapon_details(ctx, weapon, content_onBook)


# get weapons by category command - it gets a list with weapon available in input category
@bot.command()
async def vediarmi(ctx, *args):
    # here there is a limiter and countFieldsMax to bypass embed limit on discord.py class that's up to 25 fields (i set up to 24)
    category = utilites.PasteStringSpace(args)
    category = category.lower()
    if ('semplici' in category):
        category = 'arma semplice'
    bookContent = dnd_manual_weapons.getWeapons_by_category(category)
    await bot_weapons.send_weapons_list(ctx, category, bookContent)


# ready-bot command
@bot.event
async def on_ready():
    print('Sono pronto viandante!')


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
async def aiutodadi(ctx):
    await ctx.send(helpmenu.helpDices())


@bot.command()
async def aiutoincantesimi(ctx):
    await ctx.send(helpmenu.helpSpells())


@bot.command()
async def aiutoarmi(ctx):
    await ctx.send(helpmenu.helpWeapons())


# dice-rolling command
@bot.command()
async def lancia(ctx, *args):
    roll = dice.rolling(args)
    await ctx.send(roll)


# cleaning chat-text channel with this command - keep attention using this
@bot.command()
async def pulisci(ctx, amount: str):
    if ('tutto' in amount):
        amount = 100000
        await ctx.channel.purge(limit=amount)
        await ctx.send("```Ecco fatto! La taverna adesso è pulita```")
        print('pulito tutto')


# token is in auth.py
bot.run(token)
