import flet as ft
from UI.view import View
from database.museo_DAO import MuseoDAO
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # TODO



    def dropdown_musei(self):
        lista_musei = self._model.get_musei()
        default = [ft.dropdown.Option(key="nessun filtro", text="Nessun filtro")]
        opzioni_musei_dinamiche = [ft.dropdown.Option(key=museo.nome, text=museo.nome) for museo in lista_musei]

        opzioni_musei = default + opzioni_musei_dinamiche
        self._view.dropdown1.options = opzioni_musei

        self._view.dropdown1.value = None
        self._view.update()
    def dropdown_epoca(self):
        lista_epoche = self._model.get_epoche()
        default = [ft.dropdown.Option(key="nessun filtro", text="Nessun filtro")]
        epoche = [ft.dropdown.Option(key=epoca, text=epoca) for epoca in lista_epoche]

        totale =default+epoche
        self._view._dd_epoca.options = totale

        self._view._dd_epoca.value = None
        self._view.update()





    # CALLBACKS DROPDOWN
    # TODO
    def handler_musei(self,val):
        valore=val.control.value
        if valore is None or str(valore).lower() == "nessun filtro":
                self.museo_selezionato = None
        else:
            self.museo_selezionato = valore
    def seleziona_epoca(self, e):
        valore = e.control.valore
        if valore is None or str(valore).lower() == "nessun filtro":
            self.epoca_selezionata = None
        else:
            self.epoca_selezionata = valore






    # AZIONE: MOSTRA ARTEFATTI
    # TODO
    def mostra_artefatti(self, e):
        museo = self.museo_selezionato
        epoca = self.epoca_selezionata

        self._view._lista_finale.controls.clear()

        try:
            artefatti = self._model.get_artefatti_filtrati(museo, epoca)

            if not artefatti:
                self._view.show_alert("Non sono stati trovati artefatti che soddisfino i filtri")
            else:
                for artefatto in artefatti:
                    self._view.lista_finale.controls.append(ft.Text(str(artefatto)))
        except Exception as e:
            self._view.show_alert(e)



