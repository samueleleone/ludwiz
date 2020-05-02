import pymysql
import discord
pymysql.install_as_MySQLdb()
import MySQLdb
class obj:
    settimeout=0
    pass


class WeaponsBook:
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
        

    def countWeapons(self, category):
        query = ("CALL getWeaponsByCategory('" + category + "');")
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
        query = ("CALL getWeaponsByCategory('" + weaponCategory + "');")
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

