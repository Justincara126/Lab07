from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    # TODO
    def get_artefatti(self):
        cnx=ConnessioneDB.get_connection()
        cursor=cnx.cursor(dictionary=True)
        cursor.execute('select * from artefatto')
        lista=[]
        for row in cursor:
            artefatto=Artefatto(row['id'],row['nome'],row['tipologia'],row['epoca'],row['id_museo'])
            lista.append(artefatto)
            return lista

    def get_artefatti_con_filtro(self,museo, epoca):
        cnx=ConnessioneDB.get_connection()
        cursor=cnx.cursor
        result=[]
        if museo is None and epoca is None:
            query = f"""SELECT * FROM artefatto"""
        elif museo is None:
            query = f"""SELECT * FROM artefatto WHERE epoca = \"{epoca}\""""
        elif epoca is None:
            query = f"""SELECT * FROM artefatto WHERE id_museo = \'{museo}\'"""
        else:
            query = f"""SELECT * FROM artefatto WHERE epoca = \"{epoca}\" AND id_museo = \'{museo}\'"""
        cursor.execute(query)
        for row in cursor:
            result.append(Artefatto(row["id"], row["nome"], row["tipologia"], row["epoca"], row["id_museo"]))
        cursor.close()
        cnx.close()
        return result
