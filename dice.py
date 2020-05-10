import random
import re
import utilites

def rolling(arg):
    arg = utilites.PasteString(arg)
    arg = arg.lower()
    pattern = re.compile('^(\d{0,4}d\d{1,3})((\s*\+\s*)(\d*))*\s*$')
    regexCheck = pattern.match(arg)
    if(regexCheck != None):
        if('d' in arg):
            diceToRoll = arg.split('d')
            quantity = diceToRoll.__getitem__(0)
            valueOfDice = diceToRoll.__getitem__(1)
            print(' Devo lanciare il dado ' + valueOfDice)
            print(' Devo lanciarlo per n: ' + quantity)
            if(quantity == ''):
                quantity = 1
            i = quantity
            totResult = ''
            modifiers = ''
            modifier = 0
            if('+' in valueOfDice):
                modifiers = valueOfDice.split('+')
                valueOfDice = modifiers[0]
                print(modifiers)
                for m in modifiers:
                    if modifiers.index(m) != 0 and m != '':
                        modifier = modifier + int(m)
                print(modifier)
            if(int(valueOfDice) <= 200 and int(quantity) <= 9 and int(valueOfDice)>2):
                for i in range(int(quantity)):
                    result = utilites.rolling(int(valueOfDice))
                    modifierStamp = str(result)
                    finalResult = result + modifier
                    for m in modifiers:
                        if modifiers.index(m) != 0:
                            modifierStamp = modifierStamp +" + "+ m
                    print(modifierStamp)
                    print(finalResult)
                    totResult = str(totResult) + "```Il risultato del tuo d"+str(valueOfDice)+" è ["+str(modifierStamp)+"] = "+str(finalResult)+"```"
                else:
                    print('Modifiers not included in the expression')
                return totResult
            else:
                return '```Mi dispiace ma non puoi farlo```'
        else:
            return '```Mi dispiace ma non puoi farlo```'



    else:
        return '```Mi dispiace ma non puoi farlo```'

