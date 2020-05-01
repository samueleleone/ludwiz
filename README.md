# Ludwiz Bot

Dice roller, spellbook and weapon finder bot for Discord during D&D session written in py, with results in italian language.

Thanks to clockers and Frusco to give me their database with spells D&D 5E, i have added to his sql weapons db with two new procedures.
Here link to their original project: https://github.com/FSBots/Spellbook

## Version 0.1

Currently in beta state and probably there'll be some bugs. Tell me if you'll find someone.

### Requirements

```
If you  want help with development of the code, make sure to install requirements in requirements.txt file

in some cases you need to do:
pymysql.install_as_MySQLdb()
import MySQLdb

```

### Add LudwizBot to your Discord server

Click to add:
[Here](https://discordapp.com/api/oauth2/authorize?client_id=704422717981589624&permissions=67584&scope=bot)

### How to use

Rolling dice commands:
```

# just roll without modifier
-!lancia <dice> - example: !lancia d20 for d20 roll.

# Rolling dice with modifier
-!lancia <dice> + <modifier> - example: !lancia d20 + 4 for d20 roll with +4 modifier.
-!lancia <dice> - <modifier> - exmaple: !lancia d20 - 4 for d20 roll with -4 modifier.



# roll <x> d20 dices without modifiers

-!lancia <x>d20 - example: !lancia 2d20 for <x> d20 roll without modifier.

# roll <x> d20 dices with modifiers

-!lancia <x>d20 + <modifier> - example: !lancia 2d20 + 4 for <x> d20 roll with +4 modifier.
-!lancia <x>d20 - <modifier> - example: !lancia 2d20 - 4 for <x> d20 roll with -4 modifier.
```


Spellbook commands:
```

# just find a spell with his name
-!incanto "<spell>" - example: !incanto "Palla di Fuoco" for searching Fireball spell on spellbook

# Find a list with spells's name available by their class and level
-!incantesimi <class> <level> - example: !incantesimi Bardo 2 for searching all spells available for a level 2 bard.

```

Weapons commands:
```

# just find an weapon with his name
-!arma <weapon> - example: !arma Alabarda for searching Alabard weapon

# Find a list with weapons list available by category
-!vediarmi <category entry> - example: !vediarmi da guerra for searching all war weapons.

category entries accepted and that ludwiz can understand:
da guerra
semplice
semplici

```
Other commands:
```

# A funny random character's race and class combinations
-!generapg

```

### To Do

- More elegant and structured code in some commands
- Code Optimization
- Adding other functionalities



