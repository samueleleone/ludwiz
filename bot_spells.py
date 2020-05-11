import discord

MAX_SIZE = 1024

async def send_spell_details(ctx, content_onBook, spell):
    conts = []
    embed = discord.Embed(title=spell.capitalize(), color=0x66ff66)
    if (len(content_onBook) == 1):
        tupla = content_onBook[0]
        conts = get_spell_embed(tupla,spell)
    else:
        spellToFind = spell
        for spell in content_onBook:
            if ("Nome" in spell):
                embed.description = "La parola " + str(
                    spellToFind) + ' ha dato molti risultati, specifica meglio tra i seguenti: '
                embed = embed.add_field(name="Nome", value=spell["Nome"], inline=True)
        conts.append(embed)
    if len(conts) > 0:
        for em in conts:
            await ctx.send(embed=em)




def get_spell_embed(tupla,spell):
    conts = []
    embed = discord.Embed(title=spell.capitalize(), color=0x66ff66)
    for column, value in tupla.items():
        if (column == 'Nome'):
            spellName = value
            embed.title = value
        else:
            if (column == 'Descrizione'):
                splits = [value[i:i + MAX_SIZE] for i in range(0, len(value), MAX_SIZE)]
                conts.append(embed.add_field(name=column, value=splits[0], inline=True))
                splits = splits[1:]
                for split in splits:
                    em = discord.Embed(title=spellName + " - Continua", color=0x66ff66)
                    conts.append(em.add_field(name="Descrizione", value=split, inline=True))
            else:
                embed = embed.add_field(name=column, value=value, inline=True)
                print('mucca')
    return conts


async def send_spells_list_embed(ctx,dnd_class_lower: str,level: int,spells):
    classes = ['barbaro', 'bardo', 'chierico', 'druido', 'guerriero', 'ladro', 'mago', 'monaco', 'paladino',
               'stregone', 'ranger', 'warlock']
    if (dnd_class_lower in classes and level < 10):
        # await ctx.send("``` "+classe+" "+str(livello)+" ```")
        level = str(level)
        # embed limit is up to 25 fields, so i need a flag to create a new embed after 25 spells found
        flag = 0
        i = 0
        embed = discord.Embed(title=dnd_class_lower.capitalize(), color=0x66ff66)
        embed2 = discord.Embed(title=dnd_class_lower.capitalize(), color=0x66ff66)
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