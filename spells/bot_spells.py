import discord

MAX_SIZE = 1024
SPELL_EMBED_COLOR = 0x66ff66
MAX_FIELDS_SIZE = 25
classes = ['barbaro', 'bardo', 'chierico', 'druido', 'guerriero', 'ladro', 'mago', 'monaco', 'paladino', 'stregone', 'ranger' , 'warlock']

# !incanto command
async def send_spell_details(ctx, spells, spell_name):
    embeds = []
    if len(spells) == 0:
        await ctx.send("```Sei sicuro? Non riesco a trovare nessun incantesimo specificato```")
    elif len(spells) == 1:
        embeds.append(get_spell_embed(spells[0]))
    else:
        embeds = get_names_embed(spells, spell_name)
    for em in embeds:
        await ctx.send(embed=em)


# get the names of the spells in one embed
def get_names_embed(spells, spell_name):
    description = "'" + str(spell_name) + \
                        "' ha dato molti risultati, specifica meglio tra i seguenti: "
    spells_filtered = [spell for spell in spells if spell["Nome"].startswith(spell_name[0].capitalize())]
    embeds = get_embeds_by_max_fields_size(spell_name.capitalize(), spells_filtered)
    return embeds


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
    check = check_class_level(dnd_class_lower, level)
    title = dnd_class_lower + " Lv " + str(level)
    if check:
        embeds = get_embeds_by_max_fields_size(title, spells)
        for em in embeds:
            await ctx.send(embed=em)
    else:
        await ctx.send("```Sei sicuro? Non riesco a trovare nulla con classe e/o livello specificati```")


def get_embeds_by_max_fields_size(title, spells):
    embed = discord.Embed(title=title.capitalize(), color=SPELL_EMBED_COLOR)
    embeds = []
    for i in range(len(spells)):
        if i % MAX_FIELDS_SIZE == MAX_FIELDS_SIZE-1:
            embeds.append(embed)
            embed = discord.Embed(title=title.capitalize(), color=SPELL_EMBED_COLOR)
        embed.add_field(name="Nome: ", value=spells[i]['Nome'], inline=True)
        # every 25 spells found, it creates a new embed and send to discord
    embeds.append(embed)
    return embeds


def check_class_level(dnd_class_lower: str, level: int):
    check = False
    if dnd_class_lower in classes and level < 10:
        check = True
    return check
