import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_graph(self, e):
        self._model.buildgraph()

        v = self._model.numVertici()
        a = self._model.numArchi()
        pmin, pmax = self._model.getPesoMinMax()

        self._view.lista_visualizzazione_1.controls.clear()
        self._view.lista_visualizzazione_1.controls.append(
            ft.Text(f"Vertici: {v}")
        )
        self._view.lista_visualizzazione_1.controls.append(
            ft.Text(f"Archi: {a}")
        )
        self._view.lista_visualizzazione_1.controls.append(
            ft.Text(f"Peso minimo: {pmin}")
        )
        self._view.lista_visualizzazione_1.controls.append(
            ft.Text(f"Peso massimo: {pmax}")
        )

        self._view.update()

    def handle_conta_edges(self, e):
        try:
            soglia = int(self._view.txt_name.value)
        except ValueError:
            self._view.show_alert("Inserire una soglia valida")
            return

        minori, maggiori = self._model.contaArchi(soglia)

        self._view.lista_visualizzazione_2.controls.clear()
        self._view.lista_visualizzazione_2.controls.append(
            ft.Text(f"Archi con peso < {soglia}: {minori}")
        )
        self._view.lista_visualizzazione_2.controls.append(
            ft.Text(f"Archi con peso > {soglia}: {maggiori}")
        )

        self._view.update()

    def handle_ricerca(self, e):
        try:
            soglia = int(self._view.txt_name.value)
        except ValueError:
            self._view.show_alert("Inserire una soglia valida")
            return

        path, peso = self._model.camminoMassimo(soglia)

        self._view.lista_visualizzazione_3.controls.clear()

        if not path:
            self._view.lista_visualizzazione_3.controls.append(
                ft.Text("Nessun cammino trovato")
            )
        else:
            self._view.lista_visualizzazione_3.controls.append(
                ft.Text(f"Cammino: {path}")
            )
            self._view.lista_visualizzazione_3.controls.append(
                ft.Text(f"Peso totale: {peso}")
            )


