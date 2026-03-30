from database.DAO import DAO


class Model:
    def __init__(self):
        pass
    def getCodins(self):
        return DAO.getCodins()

    def getAllCorsi(self):
        return DAO.getAllCorsi()
    def getCorsiPD(self,PD):
        return DAO.getCorsiPD(PD)
    def getIscrittiCorsoPD(self,PD):
        return DAO.getIscrittiCorsoPD(PD)