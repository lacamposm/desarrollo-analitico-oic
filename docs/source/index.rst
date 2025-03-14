.. _OIC: https://www.igac.gov.co/el-igac/areas-estrategicas/direccion-de-investigacion-prospectiva/observatorio-inmobiliario-catastral

.. image:: ./_static/logo_OIC_blue.png
   :alt: Logo del proyecto OIC
   :align: center
   :width: 500px
   :height: 100px

🏠 Documentación oficial de `my_pandas` 🏠
==================================================

**my_pandas** es una biblioteca ligera y elegante para el análisis de datos tabulares, 
diseñada con propósitos educativos y como introducción al análisis de datos en Python 🐍

🚀 **¿Por qué my_pandas?**

* 📊 Interfaz sencilla e intuitiva
* 🧩 Funcionalidades esenciales para manipulación de datos
* 📈 Perfecta para aprender conceptos de análisis de datos
* 🔍 Implementación transparente y bien documentada

💡 **Ejemplo rápido:**

.. code-block:: python

   from my_pandas import SuperTabla
   
   # Crear datos de ventas
   datos = [
       {"producto": "Laptop", "cantidad": 5, "precio": 1200},
       {"producto": "Monitor", "cantidad": 10, "precio": 300},
       {"producto": "Teclado", "cantidad": 15, "precio": 80}
   ]
   
   # Crear una tabla y calcular el valor total
   tabla = SuperTabla(datos)
   tabla_con_total = tabla.agregar_columna("total", lambda x: x["cantidad"] * x["precio"])
   print(tabla_con_total)

.. toctree::
   :maxdepth: 2
   :caption: 📑 Contenido:

   modules

📖 Índices y tablas
==================

* :ref:`genindex`
* :ref:`modindex`

🌟 Desarrollado con ♥️ como parte del curso de inducción para el desarrollo analítico del - `OIC`_