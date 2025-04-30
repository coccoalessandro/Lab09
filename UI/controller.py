import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self, e):
        distanza = self._view.txt_name.value
        self._model.buildGraph(distanza)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {self._model.numNodi()}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {self._model.numArchi()}"))
        self._view.txt_result.controls.append(ft.Text(f"Elenco archi: "))
        o = ""
        d = ""
        risultato = DAO.getAllAeroporti()
        for edge in self._model._grafo.edges:
            for r in risultato:
                if edge[0] == r[0]:
                    o = r[1]
                if edge[1] == r[0]:
                    d = r[1]
            self._view.txt_result.controls.append(ft.Text(f"{o} - {d}: {self._model._grafo[edge[0]][edge[1]]['peso']} miglia"))
        self._view.update_page()
