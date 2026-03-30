from database.DB_connect import DBConnect
from model.corso import Corso


class DAO():

    @staticmethod
    def getCodins():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select codins from corso """

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["codins"])

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllCorsi():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select * from corso """

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Corso(
                codins = row["codins"],
                crediti =  row["crediti"] ,
                nome = row["nome"],
                pd = row["pd"]
            ))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCorsiPD(PD):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        if PD == 'I':
            PDint = 1
        elif PD == 'II': PDint = 2

        query = f"select * from corso where pd = {PDint} "

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Corso(
                codins=row["codins"],
                crediti=row["crediti"],
                nome=row["nome"],
                pd=row["pd"]
            ))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getIscrittiCorsoPD(PD):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        if PD == 'I':
            PDint = 1
        elif PD == 'II':
            PDint = 2
        else:
            return []  # Gestisci caso invalido

        # Query corretta con tutti i campi necessari e parametri preparati
        query = """
            SELECT i.codins, c.crediti, c.nome, c.pd, COUNT(*) as numeroIscritti
            FROM iscrizione i
            INNER JOIN corso c ON i.codins = c.codins
            WHERE c.pd = %s
            GROUP BY i.codins, c.crediti, c.nome, c.pd
        """

        cursor.execute(query, (PDint,))

        res = []
        for row in cursor:
            corso = Corso(
                codins=row["codins"],
                crediti=row["crediti"],
                nome=row["nome"],
                pd=row["pd"]
            )
            # Aggiungi come tupla (corso, numero_iscritti)
            res.append((corso, row["numeroIscritti"]))

        cursor.close()
        cnx.close()
        return res