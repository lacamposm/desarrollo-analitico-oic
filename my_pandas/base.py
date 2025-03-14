import csv
from typing import List, Tuple


class Tabla:
    """
    Clase para representar datos en formato tabular.

    :param datos: Lista de diccionarios que representan las filas de la tabla.
    :type datos: List[Dict[str, Any]]
    """

    def __init__(self, datos: list[dict[str, any]]):
        """
        Inicializa la clase Tabla con los datos proporcionados.

        :param datos: Lista de diccionarios con datos tabulares.
        :type datos: List[Dict[str, Any]]
        """
        self.datos = datos

    @property
    def columnas(self) -> List[str]:
        """
        Obtiene los nombres de las columnas de la tabla.

        :return: Lista con los nombres de las columnas.
        :rtype: List[str]
        """
        if not self.datos:
            return []
        return list(self.datos[0].keys())

    @property
    def forma(self) -> Tuple[int, int]:
        """
        Devuelve la dimensión de la tabla (número de filas y columnas).

        :return: Una tupla con (filas, columnas).
        :rtype: Tuple[int, int]
        """
        return len(self.datos), len(self.columnas)

    def cabeza(self, n: int = 5) -> "Tabla":
        """
        Devuelve una nueva Tabla con las primeras `n` filas.

        :param n: Número de filas a mostrar (por defecto 5).
        :type n: int, optional
        :return: Una nueva Tabla con las primeras filas.
        :rtype: Tabla
        """
        return Tabla(self.datos[:n])

    def cola(self, n: int = 5) -> "Tabla":
        """
        Devuelve una nueva Tabla con las últimas `n` filas.

        :param n: Número de filas a mostrar (por defecto 5).
        :type n: int, optional
        :return: Una nueva Tabla con las últimas filas.
        :rtype: Tabla
        """
        return Tabla(self.datos[-n:])

    def seleccionar_columnas(self, columnas: list[str]) -> "Tabla":
        """
        Devuelve una nueva Tabla solo con las columnas especificadas.

        :param columnas: Lista con los nombres de las columnas a seleccionar.
        :type columnas: List[str]
        :return: Una nueva Tabla con columnas seleccionadas.
        :rtype: Tabla
        """
        nuevos_datos = [{col: fila[col] for col in columnas if col in fila} for fila in self.datos]
        return Tabla(nuevos_datos)

    def __str__(self) -> str:
        """
        Genera una representación sencilla en texto de la tabla.

        :return: Cadena con la representación tabular.
        :rtype: str
        """
        if not self.datos:
            return "Tabla vacía."

        encabezado = " | ".join(self.columnas)
        separador = "-" * len(encabezado)
        filas = [
            " | ".join(str(fila.get(col, "")) for col in self.columnas)
            for fila in self.datos[:5]
        ]

        return "\n".join([encabezado, separador] + filas)


    @classmethod
    def desde_csv(cls, ruta_csv: str) -> "Tabla":
        """
        Crea una Tabla a partir de un archivo CSV.

        :param ruta_csv: Ruta al archivo CSV.
        :type ruta_csv: str
        :return: Nueva instancia de Tabla con los datos del CSV cargados.
        :rtype: Tabla
        """
        with open(ruta_csv, encoding="utf-8") as archivo:
            datos = list(csv.DictReader(archivo))
        return cls(datos)
