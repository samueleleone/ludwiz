import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb


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
        # Database connection
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
        content_list = []
        aux = {}
        for row in self.cursor:
            aux["Nome"] = row[0]
            content_list.append(aux)
            aux = {}
        return content_list

    def get_spells_by_name(self, nome):
        query = ("CALL getSpellsByName('" + nome + "');")
        self.cursor.execute(query)
        content_list = []
        aux = {}
        for row in self.cursor:
            aux["Nome"] = row[0]
            aux["Tipo"] = row[1]
            aux["TempoDiLancio"] = row[3]
            aux["Componenti"] = row[4]
            aux["Durata"] = row[5]
            aux["Gittata"] = row[6]
            aux["Descrizione"] = row[7]
            content_list.append(aux)
            aux = {}
        return content_list