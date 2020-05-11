import pymysql
import discord
pymysql.install_as_MySQLdb()
import MySQLdb


class obj:
    settimeout=0
    pass


class Spellbook:
    # db credentials
    userName = None
    userPswd = None
    url = None
    dbName = None
    port = None

    cn_object = None  # db connection
    cursor = None  # db cursor

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

    def __del__(self):
        self.cn_object.close()
        

    def get_spells_by_class_level(self, classe, lvl):
        query = ("CALL getSpellsByClassLevel('" + classe + "','" + str(lvl) + "');")
        self.cursor.execute(query)
        contentList = []
        aux = {}
        for row in self.cursor:
            aux["Nome"] = row[0]
            contentList.append(aux)
            aux = {}
        return contentList


    def get_spells_by_name(self, nome):
        query = ("CALL getSpellsByName('" + nome + "');")
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
        query = ("CALL getSpellsByClassLevel('" + dnd_class + "','" + str(level) + "');")
        self.cursor.execute(query)
        i=0
        for row in self.cursor:
           i=i+1
        return i

    def stampaRisultato(self, content):
        for tupla in content:
            for nomeColonna, valore in tupla.items():
                print(nomeColonna + " : " + str(valore))





