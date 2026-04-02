import flet as ft

from model.model import Model


class Controller:
    def __init__(self, view):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = Model()

        self._ddCodInsValue = None

    def handlePrintCorsiPD(self,e):
        self._view.txt_result.controls.clear()
        pd = self._view.ddPD.value
        print(pd)
        if pd is None:
            self._view.create_alert("Attenzione, selezionare un periodo didattico!!")
            self._view.update_page()
            return
        if pd == "I":
            pdInt = 1
        else:
            pdInt = 2
        corsiPD = self._model.getCorsiPD(pdInt)
        if not len(corsiPD):
            self._view.txt_result.controls.append(ft.Text(f"Nessun corso trovato per il {pd} periodo didattico."))
            self._view.update_page()
            return
        self._view.txt_result.controls.append(ft.Text(f"Di seguito i corsi del {pd} periodo didattico:"))
        for c in corsiPD:
            self._view.txt_result.controls.append(ft.Text(f"{c}"))
        self._view.update_page()

    def handlePrintIscrittiCorsiPD(self,e):
        self._view.txt_result.controls.clear()
        pd = self._view.ddPD.value
        print(pd)
        if pd is None:
            self._view.create_alert("Attenzione, selezionare un periodo didattico!!")
            self._view.update_page()
            return
        if pd == "I":
            pdInt = 1
        else:
            pdInt = 2

        corsi = self._model.getCorsiPDwIscritti(pdInt)

        if not len(corsi):
            self._view.txt_result.controls.append(ft.Text(f"Nessun corso trovato per il {pd} periodo didattico."))
            self._view.update_page()
            return
        self._view.txt_result.controls.append(ft.Text(f"Di seguito i corsi del {pd} periodo didattico con dettaglio iscritti:"))
        for c, n in corsi:
            self._view.txt_result.controls.append(ft.Text(f"{c} -- N iscritti: {n}"))
        self._view.update_page()

    def handlePrintIscrittiCodins(self,e):
        self._view.txt_result.controls.clear()
        if self._ddCodInsValue is None:
            self._view.create_alert("Per favore selezionare un insegnamento.")
            self._view.update_page()
            return
        #se arrivo qua posso recuperare gli studenti
        studenti = self._model.getStudentiCorso(self._ddCodInsValue.codins)

        if not len(studenti):
            self._view.txt_result.controls.append(ft.Text(f"Nessuno studente iscritto a questo corso."))
            self._view.update_page()
        self._view.txt_result.controls.append(ft.Text(f"Di seguito gli studenti iscritti al corso {self._ddCodInsValue}:"))

        for s in studenti:
            self._view.txt_result.controls.append(ft.Text(f"{s}"))
            self._view.update_page()


    def handlePrintCDSCodins(self,e):
        self._view.txt_result.controls.clear()
        if self._ddCodInsValue is None:
            self._view.create_alert("Per favore selezionare un insegnamento.")
            self._view.update_page()
            return
        cds = self._model.getCDSofCorso(self._ddCodInsValue.codins)

        if not len(cds):
            self._view.txt_result.controls.append(ft.Text(f"Nessuno CDS afferente al corso {self._ddCodInsValue}:."))
            self._view.update_page()

        self._view.txt_result.controls.append(
            ft.Text(f"Di seguito i CDS che includono il corso {self._ddCodInsValue}:"))

        for cds,n in cds:
            self._view.txt_result.controls.append(ft.Text(f"{cds} - N iscritti: {n}"))
        self._view.update_page()

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
