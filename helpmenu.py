def helpGeneral():
    string = "```Ciao sono Ludwiz, Un taverniere che ti aiuta giocando a D&D.\nTi elenco le possibilità dei comandi generali\n\ncommands per il lancio dei dadi:\n> Lanciare i dadi - !lancia [opzioni] (opzioni con !aiutodadi) \n\ncommands per gli incantesimi:\n> Trovare un incantesimo - !incanto [opzioni] \n> Consultare gli incantesimi - !incantesimi [opzioni]\n(Per ulteriori dettagli sulle opzioni usa !aiutoincantesimi)\n\ncommands per consultare armi:\n> Trovare arma con il nome - !arma [opzioni] \n> Consultare armi dalla categoria - !vediarmi [opzioni]\n(Per ulteriori dettagli sulle opzioni usa !aiutoarmi)\n\nAltri commands:\n> Generare 3 opzioni di classe/razza casualmente - !generapg\n```"
    return string

def helpWeapons():
    string = "``` Benvenuto nell'angolo della taverna dedicato alle armi!\nCosa vuoi vedere di preciso?\n\ncommands:\n> Cercare tutte le armi semplici o da guerra:\nesempio: !vediarmi da guerra o !vediarmi semplici\n\n>Cercare un arma con nome specifico\nesempio: !arma Alabarda - trova arma specifica\n\n```"
    return string

def helpSpells():
    string = "```Mio caro avventuriero, ricorda che è vietato incantare in taverna!\nVediamo se riesco però a consultare questo vecchio tomo per te ed aiutarti..\n\ncommands:\n> Cercare tutti gli incantesimi corrispondenti a parola chiave\nesempio: !incanto Palla - trova incanti con Palla\n\n> Cercare un incantesimo con nome specifico usando le quotes\nesempio: !incanto Palla di Fuoco - trova incantesimo specifico\n\n> Cercare tutti gli incantesimi data una Classe e il Livello\nesempio: !incantesimi Bardo 2 - trova incanti del bardo di liv.2\n\n'```"
    return string

def helpDices():
    string = "```Salve viandante, sei pronto a giocare con i tuoi dadi?\nTi do qualche suggerimento, sono esperto nel gioco dei dadi\n\ncommands:\n> Lancia 1 Dado qualsiasi - !lancia d[valore]\nesempio: !lancia d20 - tirerà un dado 20 facce\n\n> Lancia n Dadi qualsiasi - !lancia [num]d[valore]\nesempio: !lancia 2d20 - tirerà due dadi 20 facce\n\n> Lancia 1 Dado qualsiasi con modificatore - !lancia d[valore] + [modificatore]\nesempio: !lancia d20 + 3 - tirerà un dado 20 facce con modificatore 3\n\n> Lancia n Dadi qualsiasi con modificatore - !lancia [num]d[valore] + [modificatore]\nesempio: !lancia 3d8 + 4 - tirerà tre dadi 8 facce con modificatore 4\n\n```"
    return string