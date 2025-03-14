# Clase 3: Programación Orientada a Objetos y Documentación Profesional

## 🎯 Objetivos de la sesión

- Dominar la documentación de código con docstrings
- Comprender los principios fundamentales de la Programación Orientada a Objetos (POO) en Python
- Aprender a estructurar proyectos mediante modularización
- Generar documentación profesional utilizando Sphinx

## 📘 Programación Orientada a Objetos en Python

### Documentación de funciones en Python

```python
def funcion(parametro1: int, parametro2: str) -> float:
    """Breve descripción de la función.
    
    :param int parametro1: Descripción del parámetro 1
    :param str parametro2: Descripción del parámetro 2
    :return float: Descripción del valor retornado
    
    :example:
    >>> funcion(1, 2)
    3
    """
    # Código de la función
```

### OOP - Conceptos fundamentales

La Programación Orientada a Objetos es un paradigma que nos permite modelar el mundo real mediante objetos que tienen:

- **Atributos**: características o propiedades de un objeto
  - *Ejemplo*: Un objeto Coche puede tener atributos como `marca`, `modelo`, `color`, `año`

- **Métodos**: acciones o comportamientos que puede realizar un objeto
  - *Ejemplo*: El Coche puede tener métodos como `arrancar()`, `frenar()`, `acelerar()`

- **Encapsulamiento**: ocultación de datos internos y exposición controlada mediante interfaces
  - Protege la integridad de los datos de un objeto
  - En Python usamos convenciones como `_atributo` (protegido) y `__atributo` (privado)

- **Herencia**: mecanismo para crear nuevas clases a partir de clases existentes
  - Permite reutilizar código y establecer jerarquías
  - *Ejemplo*: `SUV` hereda de `Coche` y añade características específicas

- **Polimorfismo**: capacidad de objetos de distintas clases para responder al mismo método
  - *Ejemplo*: Diferentes vehículos pueden responder al método `arrancar()` de manera distinta

### Definiendo clases en Python

```python
class Coche:
    """Clase para representar un coche."""
    
    # Constructor
    def __init__(self, marca: str, modelo: str, año: int) -> None:
        """Inicializa un nuevo objeto Coche.
        
        :param marca: La marca del coche
        :param modelo: El modelo del coche
        :param año: El año de fabricación del coche
        """
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False
        self.velocidad = 0
        
    def arrancar(self) -> bool:
        """Arranca el motor del coche.
        
        :return: True si el coche arrancó correctamente, False si ya estaba encendido
        """
        if not self.encendido:
            self.encendido = True
            print(f"{self.marca} {self.modelo} arrancado.")
            return True
        else:
            print(f"{self.marca} {self.modelo} ya estaba encendido.")
            return False
            
    def acelerar(self, incremento: int) -> int:
        """Aumenta la velocidad del coche.
        
        :param incremento: Cantidad en km/h a incrementar
        :return: La nueva velocidad del coche
        """
        if self.encendido:
            self.velocidad += incremento
            print(f"{self.marca} {self.modelo} acelerando a {self.velocidad} km/h.")
            return self.velocidad
        else:
            print("No se puede acelerar un coche apagado.")
            return 0
    
    def __str__(self) -> str:
        """Representación en texto del coche.
        
        :return: Cadena descriptiva del coche
        """
        estado = "encendido" if self.encendido else "apagado"
        return f"{self.marca} {self.modelo} ({self.año}) - {estado}, {self.velocidad} km/h"
```

#### Ejemplo de uso de la clase


```python
# Crear una instancia de la clase Coche
mi_coche = Coche("Toyota", "Corolla", 2023)
print(mi_coche)  # Toyota Corolla (2023) - apagado, 0 km/h

# Usar los métodos
mi_coche.arrancar()
mi_coche.acelerar(20)
print(mi_coche)  # Toyota Corolla (2023) - encendido, 20 km/h

# Crear otra instancia
otro_coche = Coche("Honda", "Civic", 2022)
print(otro_coche)  
```

#### Herencia - Ejemplo

```python
class SUV(Coche):
    """Clase para representar un SUV, que hereda de Coche."""
    
    def __init__(self, marca: str, modelo: str, año: int, traccion: str) -> None:
        """Inicializa un nuevo SUV.
        
        :param marca: La marca del SUV
        :param modelo: El modelo del SUV
        :param año: El año de fabricación
        :param traccion: Tipo de tracción (4x4, 4x2, AWD)
        """
        # Llamada al constructor de la clase padre
        super().__init__(marca, modelo, año)
        self.traccion = traccion
        self.modo_off_road = False
    
    def activar_modo_off_road(self) -> bool:
        """Activa el modo todoterreno.
        
        :return: True si se activó correctamente, False en caso contrario
        """
        if self.encendido and self.traccion in ["4x4", "AWD"]:
            self.modo_off_road = True
            print(f"{self.marca} {self.modelo}: Modo off-road activado.")
            return True
        else:
            print(f"No se puede activar el modo off-road.")
            return False
    
    def __str__(self) -> str:
        """Representación en texto del SUV.
        
        :return: Cadena descriptiva del SUV
        """
        # Reutilizamos el método de la clase padre y añadimos información
        texto_base = super().__str__()
        modo = "Modo off-road activado" if self.modo_off_road else "Modo normal"
        return f"{texto_base}, Tracción: {self.traccion}, {modo}"
```

#### Atributos y métodos de clase

```python
class Vehiculo:
    """Clase para representar un vehículo genérico."""
    
    # Atributo de clase (compartido por todas las instancias)
    num_vehiculos = 0
    
    def __init__(self, tipo: str) -> None:
        """Inicializa un nuevo vehículo.
        
        :param tipo: Tipo de vehículo
        """
        self.tipo = tipo
        # Incrementamos el contador de clase
        Vehiculo.num_vehiculos += 1
    
    @classmethod
    def obtener_total_vehiculos(cls) -> int:
        """Método de clase para obtener el número total de vehículos.
        
        :return: Número total de vehículos creados
        """
        return cls.num_vehiculos
    
    @staticmethod
    def validar_patente(patente: str) -> bool:
        """Método estático para validar un formato de patente.
        
        :param patente: Patente a validar
        :return: True si la patente tiene formato válido, False en caso contrario
        """
        # Ejemplo básico: 3 letras seguidas de 3 números
        import re
        return bool(re.match(r'^[A-Z]{3}\d{3}$', patente))
```

### Estructurando proyectos mediante modularización

```markdown
mi_paquete/
  ├── __init__.py         # Convierte la carpeta en un paquete importable
  ├── modulo1.py          # Módulo con funciones y clases relacionadas
  ├── modulo2.py          # Otro módulo con funcionalidad específica
  └── subpaquete/         # Subpaquete para organizar código relacionado
      ├── __init__.py
      └── modulo3.py
```

## 📖 Documentación profesional con Sphinx

### Configuración básica de Sphinx

```bash
# Instalar Sphinx
pip install sphinx sphinx_rtd_theme

# Iniciar un proyecto de documentación
mkdir docs
cd docs
sphinx-quickstart
```

El archivo `conf.py` generado contiene la configuración de Sphinx:

```python
# Configuración básica para un proyecto Python
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]
html_theme = 'sphinx_rtd_theme'
```

### Generación de documentación desde docstrings

```python
# En docs/source/index.rst
.. automodule:: mi_paquete.modulo1
   :members:
   :undoc-members:
   :show-inheritance:
```

### Comandos para generar documentación

```bash
# Generar HTML
sphinx-build -b html source/ build/html

# Generar PDF (requiere LaTeX)
sphinx-build -b latex source/ build/latex
cd build/latex
make
```

## 📋 Actividades prácticas

- Añade un nuevo método a la clase SuperTabla que permita calcular estadísticas descriptivas (media, mediana, desviación estándar) para columnas numéricas.
- Crea un método para exportar la tabla a un archivo CSV.
- Implementa un método para unir dos tablas (similar al join de SQL o pandas).
- Documenta completamente tus métodos utilizando docstrings con formato `:param` y `:return:`.
- Genera documentación HTML con Sphinx para tu módulo de tablas.

## 📚 Referencias y recursos adicionales

- Documentación oficial de Python sobre clases
- Guía de estilo para docstrings
- Documentación de Sphinx
- Tutorial sobre creación de paquetes Python
