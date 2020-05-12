import discord

MAX_SIZE = 1024
SPELL_EMBED_COLOR = 0x66ff66


# !incanto command
async def send_spell_details(ctx, spells, spell_name):
    if len(spells) == 1:
        embed = get_spell_embed(spells[0])
    else:
        embed = get_names_embed(spells, spell_name)
    await ctx.send(embed=embed)


# get the names of the spells in one embed
def get_names_embed(spells, spell_name):
    embed = discord.Embed(title=spell_name.capitalize(), color=SPELL_EMBED_COLOR)
    embed.description = "'" + str(spell_name) + \
                        "' ha dato molti risultati, specifica meglio tra i seguenti: "
    for spell in spells:
        embed = embed.add_field(name="Nome", value=spell["Nome"], inline=True)
    return embed


# get all the spell details splitted in embeds
def get_spell_embed(spell):
    name = spell['Nome']

    # Split description in 1024 length parts
    splits = [spell['Descrizione'][i:i + MAX_SIZE] for i in range(0, len(spell['Descrizione']), MAX_SIZE)]

    # Embed composition
    details = discord.Embed(title=name, color=SPELL_EMBED_COLOR)

    details.add_field(name='Tipo', value=spell['Tipo'], inline=True)
    details.add_field(name='Tempo di Lancio', value=spell['TempoDiLancio'], inline=True)
    details.add_field(name='Durata', value=spell['Durata'], inline=True)
    details.add_field(name='Gittata', value=spell['Gittata'], inline=True)
    details.add_field(name='Componenti', value=spell['Componenti'], inline=True)
    details.add_field(name='Descrizione', value=splits[0], inline=False)

    # If required add fields for remained description
    # name='\u200b' for empty line
    for split in splits[1:]:
        details.add_field(name='Descrizione - Continua', value=split, inline=False)

    return details


# !incantesimi command
async def send_spells_list_embed(ctx, dnd_class_lower: str, level: int, spells):
    classes = ['barbaro', 'bardo', 'chierico', 'druido', 'guerriero', 'ladro', 'mago', 'monaco', 'paladino',
               'stregone', 'ranger', 'warlock']
    if (dnd_class_lower in classes and level < 10):
        # await ctx.send("``` "+classe+" "+str(livello)+" ```")
        level = str(level)
        # embed limit is up to 25 fields, so i need a flag to create a new embed after 25 spells found
        flag = 0
        i = 0
        embed = discord.Embed(title=dnd_class_lower.capitalize(), color=SPELL_EMBED_COLOR)
        embed2 = discord.Embed(title=dnd_class_lower.capitalize(), color=SPELL_EMBED_COLOR)
        for spell in spells:
            for spell_name, spell in spell.items():
                if (i < 25):
                    embed.add_field(name="Livello: " + level, value=spell, inline=True)
                    i = i + 1
                else:
                    flag = 1
                    embed2.add_field(name="Livello: " + level, value=spell, inline=True)
                    i = i + 1
        await ctx.send(embed=embed)
        if (flag == 1):
            await ctx.send(embed=embed2)


    else:
        if (level < 10):
            await ctx.send("``` " + dnd_class_lower + " non esistente e mentre livello " + str(level) + " valido ```")
        else:
            await ctx.send("``` " + dnd_class_lower + " non esistente e livello " + str(level) + " non valido ```")
