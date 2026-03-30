import flet as ft

from model.model import Model


class Controller:
    def __init__(self, view):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = Model()

    def handlePrintCorsiPD(self,e):
        self._view.txt_result.controls.clear()
        self._PD = self._view.ddPD.value
        print(self._PD)
        if self._PD != None:
            for c in self._model.getCorsiPD(self._PD):
                self._view.txt_result.controls.append(ft.Text(f"{c}"
                ))
            self._view.update_page()
        else:
            self._view.txt_result.controls.append(ft.Text("Inserisci prima un periodo didattico!!"))
            self._view.update_page()


    def handlePrintIscrittiCorsiPD(self,e):
        self._view.txt_result.controls.clear()
        self._PD = self._view.ddPD.value
        if self._PD != None:
            for c,numeroIscritti in self._model.getIscrittiCorsoPD(self._PD):
                self._view.txt_result.controls.append(ft.Text(f"{c.nome}({c.codins}): {numeroIscritti} iscritti"
                ))
            self._view.update_page()
        else:
            self._view.txt_result.controls.append(ft.Text("Inserisci prima un periodo didattico!!"))
            self._view.update_page()

    def handlePrintIscrittiCodins(self,e):
        pass
    def handlePrintCDSCodins(self,e):
        pass
    def fillddCodIns(self):
        '''for cod in self._model.getCodins():
            self._view.ddCodins.options.append(
            ft.dropdown.Option(cod)
            )'''

        for c in self._model.getAllCorsi():
            self._view.ddCodIns.options.append(ft.dropdown.Option(
                key = c.codins,
                data = c,
                on_click = self._choiceDDCodIns
            ))

    def _choiceDDCodIns(self,e):
        self._ddCodInsValue = e.control.data
        print(self._ddCodInsValue)
