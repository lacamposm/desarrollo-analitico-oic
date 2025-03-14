import csv
import statistics
from typing import List, Dict, Any, Union


def convertir_tipo(valor: str) -> Union[int, float, str]:
    """
    Intenta convertir un valor string a un tipo numérico apropiado.
    
    :param str valor: El valor a convertir
    :return Union[int, float, str]: El valor convertido
    """
    try:
        return int(valor)
    except ValueError:
        try:
            return float(valor)
        except ValueError:
            return valor


def estadisticas_columna(valores: List[Union[int, float]]) -> Dict[str, float]:
    """
    Calcula estadísticas básicas para una columna numérica.
    
    :param list valores: Lista de valores numéricos
    :return dict: Diccionario con estadísticas (media, mediana, desviación estándar, min, max)
    """
    if not valores:
        return {
            "media": None,
            "mediana": None,
            "desviacion_estandar": None,
            "minimo": None,
            "maximo": None,
            "cuenta": 0
        }
    
    return {
        "media": statistics.mean(valores),
        "mediana": statistics.median(valores),
        "desviacion_estandar": statistics.stdev(valores) if len(valores) > 1 else 0,
        "minimo": min(valores),
        "maximo": max(valores),
        "cuenta": len(valores)
    }


def guardar_csv(datos: List[Dict[str, Any]], 
                ruta_archivo: str, 
                delimitador: str = ",") -> None:
    """
    Guarda una lista de diccionarios como un archivo CSV.
    
    :param list datos: Lista de diccionarios a guardar
    :param str ruta_archivo: Ruta del archivo CSV a crear
    :param str delimitador: Carácter delimitador para el CSV
    :return None: No retorna valor
    """
    if not datos:
        with open(ruta_archivo, "w", encoding="utf-8") as f:
            f.write("")
        return
    
    with open(ruta_archivo, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, 
            fieldnames=datos[0].keys(),
            delimiter=delimitador
        )
        writer.writeheader()
        writer.writerows(datos)