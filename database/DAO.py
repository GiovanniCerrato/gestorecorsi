from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente


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
    def getCorsiPD(pd):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)


        query = """SELECT * 
                    FROM corso 
                    where pd = %s """

        cursor.execute(query, (pd,))

        res = []
        for row in cursor:
            res.append(Corso(**row)) #è la stessa cosa che c'è sotto commentata ma fatta in maniera veloce, funziona solo se le colonne della tabella hanno lo stesso nome degli attributi della classe e delle chiavi del dizionario
                #codins=row["codins"],
                #crediti=row["crediti"],
                #nome=row["nome"],
                #pd=row["pd"] ))


        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCorsiPDwIscritti(pd):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        # Query corretta con tutti i campi necessari e parametri preparati
        query = """
            SELECT c.codins, c.crediti, c.nome, c.pd, COUNT(*) as numeroIscritti
            FROM iscrizione i, corso c
            where c.codins = i.codins and c.pd = %s
            GROUP BY c.codins, c.crediti, c.nome, c.pd """

        cursor.execute(query, (pd,))

        res = []
        for row in cursor:

            # Aggiungi come tupla (corso, numero_iscritti)
            res.append((Corso(
                codins=row["codins"],
                crediti=row["crediti"],
                nome=row["nome"],
                pd=row["pd"]), row["numeroIscritti"]))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getStudentiCorso(codins):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        # Query corretta con tutti i campi necessari e parametri preparati
        query = """SELECT s.*
                    FROM iscrizione i, studente s
                    WHERE i.matricola = s.matricola AND i.codins = %s  """

        cursor.execute(query, (codins,))

        res = []
        for row in cursor:
            # Aggiungi come tupla (corso, numero_iscritti)
            res.append((Studente(
                matricola=row["matricola"],
                cognome=row["cognome"],
                nome=row["nome"],
                CDS=row["CDS"])))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCDSofCorso(codins):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        # Query corretta con tutti i campi necessari e parametri preparati
        query = """ select s.CDS, count(*) as n
                    from studente s, iscrizione i
                    where s.matricola = i.matricola and i.codins = %s and s.CDS != ""
                    group by s.CDS  """

        cursor.execute(query, (codins,))

        res = []
        for row in cursor:
            res.append((row["CDS"], row["n"]))

        cursor.close()
        cnx.close()
        return res
