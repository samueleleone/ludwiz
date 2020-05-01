import pymysql
import discord
pymysql.install_as_MySQLdb()
import MySQLdb


class obj:
    settimeout=0
    pass


class Spellbook:
    # Credenziali di accesso
    userName = None
    userPswd = None
    url = None
    dbName = None
    port = None

    cn_object = None  # Oggetto connessione al database
    cursor = None  # Cursore ottenuto da cn_object

    def __init__(self, new_userName, new_userPswd, new_url, new_dbName):
        self.url = new_url
        self.userName = new_userName
        self.userPswd = new_userPswd
        self.dbName = new_dbName
        # Mi collego al database
        self.cn_object = MySQLdb.connect(self.url,
                                         self.userName,
                                         self.userPswd,
                                         self.dbName)
        self.cursor = self.cn_object.cursor()

    #def __del__(self):
        #self.cn_object.close()
        #self.cursor.close()

    def get_spells_by_class_level(self, classe, lvl):
        query = ("CALL ottieniIncantesimiPerClasseDiLivello('" + classe + "','" + str(lvl) + "');")
        self.cursor.execute(query)
        contentList = []
        aux = {}
        for row in self.cursor:
            aux["Nome"] = row[0]
            contentList.append(aux)
            aux = {}
        return contentList


    def get_spells_by_name(self, nome):
        query = ("CALL `ottieniIncantesimiPerNome`('" + nome + "');")
        self.cursor.execute(query)
        contentList = []
        aux = {}
        for row in self.cursor:
            aux["Nome"] = row[0]
            aux["Tipo"] = row[1]
            aux["TempoDiLancio"] = row[3]
            aux["Componenti"] = row[4]
            aux["Durata"] = row[5]
            aux["Gittata"] = row[6]
            aux["Descrizione"] = row[7]
            contentList.append(aux)
            aux = {}
        return contentList

    def countSpells(self, dnd_class,level):
        query = ("CALL ottieniIncantesimiPerClasseDiLivello('" + dnd_class + "','" + str(level) + "');")
        self.cursor.execute(query)
        i=0
        for row in self.cursor:
           i=i+1
        return i

    def countWeapons(self, category):
        query = ("CALL getCategory('" + category + "');")
        self.cursor.execute(query)
        i = 0
        for row in self.cursor:
            i = i + 1 + 2
        return i

    def getWeapons(self, weaponName):
        query = ("CALL getWeaponsByName('"+weaponName+"');")
        self.cursor.execute(query)
        contentList = []
        aux = {}
        for row in self.cursor:
            aux["Nome"] = row[0]
            aux["Tipo"] = row[1]
            aux["Stile di combattimento"] = row[2]
            aux["Costo"] = row[3]
            aux["Danni"] = row[4]
            aux["Proprietà"] = row[5]
            contentList.append(aux)
            aux = {}
        return contentList

    def getWeapons_by_category(self, weaponCategory):
        query = ("CALL getCategory('" + weaponCategory + "');")
        self.cursor.execute(query)
        contentList = []
        aux = {}
        for row in self.cursor:
            aux["Categoria"] = row[0]
            aux["Nome"] = row[1]
            aux["Danni"] = row[2]
            aux["Stile di combattimento"] = row[3]

            contentList.append(aux)
            aux = {}
        return contentList

    def stampaRisultato(self, content):
        for tupla in content:
            for nomeColonna, valore in tupla.items():
                print(nomeColonna + " : " + str(valore))


'''
obj = Spellbook("standard","guruguru","localhost","dnd_5_incantesimi")
obj.stampaRisultato(obj.ottieniIncantesimiDiLivello(2))
obj.stampaRisultato(obj.ottieniIncantesimiPerNome("Ami"))
print(obj.aggiungiUtente(123456))
print(obj.aggiungiPreferiti(123456,"Amicizia"))
print(obj.rimuoviPreferiti(123456,"Amicizia"))
print(obj.aggiungiPreferiti(123456,"Amicizia"))
obj.stampaRisultato(obj.ottieniPreferiti(123456))
'''