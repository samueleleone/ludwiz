import discord
import random

def generateClassAndRace():
    classes = ['Barbaro', 'Dardo', 'Chierico', 'Druido', 'Guerriero', 'Ladro', 'Mago', 'Monaco', 'Paladino',
               'Stregone', 'Ranger', 'Warlock']
    races = ['Elfo', 'Halfling', 'Nano', 'Umano', 'Dragonide', 'Gnomo', 'Mezzoelfo', 'Mezzorco', 'Tiefling']
    embed = discord.Embed(title="Generatore di personaggi", color=0x66ff66,
                          description="Salve avventuriero! Siete nuovo da queste parti.. chi siete?")
    for i in range(3):
        dnd_class = random.choice(classes)
        race = random.choice(races)
        embed.add_field(name="Opzione " + str(i + 1), value=dnd_class + " " + race, inline=False)
    return embed
