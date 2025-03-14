from my_pandas.base import Tabla

class SuperTabla(Tabla):
    """
    Extensión de la clase Tabla con funcionalidades adicionales para manipular datos fácilmente.
    """

    def filtrar(self, condicion) -> "SuperTabla":
        """
        Filtra las filas de la tabla según una condición especificada.

        :param condicion: Función que recibe una fila y retorna True si la fila debe mantenerse.
        :type condicion: callable
        :return: Una nueva instancia de SuperTabla con filas filtradas.
        :rtype: SuperTabla
        """
        return SuperTabla([fila for fila in self.datos if condicion(fila)])

    def ordenar_por(self, columna: str, ascendente: bool = True) -> "SuperTabla":
        """
        Ordena las filas de la tabla según los valores de una columna específica.

        :param columna: El nombre de la columna por la cual ordenar.
        :type columna: str
        :param ascendente: Indica si el orden es ascendente (True) o descendente (False).
        :type ascendente: bool, optional
        :return: Una nueva instancia de SuperTabla ordenada.
        :rtype: SuperTabla
        """
        return SuperTabla(sorted(
            self.datos,
            key=lambda x: x.get(columna),
            reverse=not ascendente
        ))

    def aplicar(self, columna: str, funcion) -> "SuperTabla":
        """
        Aplica una función a cada valor de una columna específica.

        :param columna: La columna sobre la cual aplicar la función.
        :type columna: str
        :param funcion: Función que se aplicará a cada valor de la columna.
        :type funcion: callable
        :return: Una nueva instancia de SuperTabla con los datos modificados.
        :rtype: SuperTabla
        """
        nuevos_datos = []
        for fila in self.datos:
            nueva_fila = fila.copy()
            nueva_fila[columna] = funcion(fila[columna])
            nuevos_datos.append(nueva_fila)
        return SuperTabla(nuevos_datos)

    def agregar_columna(self, nombre: str, valor_o_funcion) -> "SuperTabla":
        """
        Agrega una nueva columna con un valor constante o generado mediante una función.

        :param nombre: Nombre de la nueva columna.
        :type nombre: str
        :param valor_o_funcion: Valor constante o función que genera el valor para cada fila.
        :type valor_o_funcion: any o callable
        :return: Una nueva instancia de SuperTabla con la columna agregada.
        :rtype: SuperTabla
        """
        nuevos_datos = []
        for fila in self.datos:
            nueva_fila = fila.copy()
            if callable(valor_o_funcion):
                nueva_fila[nombre] = valor_o_funcion(fila)
            else:
                nueva_fila[nombre] = valor_o_funcion
            nuevos_datos.append(nueva_fila)
        return SuperTabla(nuevos_datos)

    def agrupar_por(self, columna: str, func_agregacion: str = "count") -> "SuperTabla":
        """
        Agrupa filas por una columna específica y aplica una función de agregación a cada grupo.

        :param columna: Nombre de la columna por la cual agrupar.
        :type columna: str
        :param func_agregacion: Función de agregación a aplicar; opciones disponibles:
            "count", "sum", "avg", "min", "max".
        :type func_agregacion: str, optional
        :return: Una nueva instancia de SuperTabla con los grupos agregados.
        :rtype: SuperTabla
        """
        grupos = {}
        for fila in self.datos:
            clave = fila[columna]
            if clave not in grupos:
                grupos[clave] = []
            grupos[clave].append(fila)

        resultado = []
        for clave, filas in grupos.items():
            nueva_fila = {columna: clave}

            if func_agregacion == "count":
                nueva_fila["conteo"] = len(filas)
            else:
                columnas_numericas = set()
                for fila in filas:
                    for col, valor in fila.items():
                        if col != columna and isinstance(valor, (int, float)):
                            columnas_numericas.add(col)

                for col in columnas_numericas:
                    valores = [fila[col] for fila in filas if col in fila]
                    if valores:
                        if func_agregacion == "sum":
                            nueva_fila[f"{col}_suma"] = sum(valores)
                        elif func_agregacion == "avg":
                            nueva_fila[f"{col}_promedio"] = sum(valores) / len(valores)
                        elif func_agregacion == "min":
                            nueva_fila[f"{col}_min"] = min(valores)
                        elif func_agregacion == "max":
                            nueva_fila[f"{col}_max"] = max(valores)

            resultado.append(nueva_fila)

        return SuperTabla(resultado)
