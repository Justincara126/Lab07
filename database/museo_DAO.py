from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        self.lista=[]

    # TODO
    def get_museo(self):
        cnx = ConnessioneDB.get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM museo")
        for row in cursor:
            museo=Museo(row['id'],row['nome'],row['tipologia'])
            self.lista.append(museo)


        return self.lista

