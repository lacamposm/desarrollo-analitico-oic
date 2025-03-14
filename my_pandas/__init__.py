"""
my_pandas – Una librería simplificada para la representación y manipulación de datos tabulares,
inspirada en pandas.

Proporciona clases Tabla y SuperTabla para gestionar y analizar datos tabulares fácilmente.
"""

from .base import Tabla
from .avanzada import SuperTabla

__all__ = ['Tabla', 'SuperTabla']