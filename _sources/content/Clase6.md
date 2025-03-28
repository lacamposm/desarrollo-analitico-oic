# ***🚀 Clase 6: Despliegue con Docker Compose***
Docker Compose es una herramienta que permite definir y ejecutar aplicaciones multi-contenedor. Con Compose podemos gestionar fácilmente la creación, configuración y conexión de múltiples servicios dentro de un entorno aislado y reproducible.

## 🔧 ¿Por qué usar Docker Compose?

- **🌐 Reproducibilidad:** Define entornos consistentes mediante archivos YAML.
- **⚙️ Gestión sencilla:** Permite iniciar, detener y escalar servicios con comandos simples.
- **📦 Portabilidad:** Facilita la ejecución del entorno en cualquier máquina con Docker instalado.
- **🔗 Conectividad:** Gestiona redes y dependencias entre servicios automáticamente.
- **🗃️ Persistencia:** Maneja fácilmente el almacenamiento persistente a través de volúmenes.

## 📄 Estructura básica del archivo `docker-compose.yml`

Un archivo `docker-compose.yml` describe los servicios, redes y volúmenes necesarios para ejecutar tu aplicación:

```yaml
services:
  servicio-ejemplo:
    image: ejemplo-imagen:latest
    ports:
      - "8080:80"
    environment:
      - EJEMPLO_VAR=valor
    volumes:
      - ejemplo-volumen:/ruta/del/contenedor
    networks:
      - ejemplo-red

volumes:
  ejemplo-volumen:

networks:
  ejemplo-red:
    driver: bridge
```

## ▶️ Comandos frecuentes

```bash
# Construir e iniciar servicios
docker-compose up --build

# Detener servicios
docker-compose down

# Ver estado de servicios
docker-compose ps

# Visualizar logs
docker-compose logs -f
```

---

Algunos parámetros clave que encontraremos típicamente en nuestro archivo de configuración de Docker Compose:

## 🐳 `services`
Define los servicios o contenedores que serán desplegados.

## 📦 `image`
La imagen Docker que se utilizará para crear el contenedor. Puede ser local o descargada desde Docker Hub u otro repositorio.

## 🔨 `build`
Si no se tiene una imagen previamente creada, indica que Docker debe construirla desde un `Dockerfile`.

## 🚪 `ports`
Mapea puertos del contenedor al sistema local (`"puerto-local:puerto-contenedor"`), permitiendo acceso externo.

## 🌱 `environment`
Permite definir variables de entorno dentro del contenedor.

## 📄 `env_file`
Carga variables de entorno desde un archivo externo (`.env`).

## 💾 `volumes`
Gestiona la persistencia de datos montando directorios o archivos del sistema local dentro del contenedor.

## 🔗 `depends_on`
Especifica dependencias entre servicios. Un servicio espera que otro esté listo antes de iniciarse.

## ✅ `healthcheck`
Verifica regularmente que un servicio esté operativo. Es esencial para gestionar dependencias correctamente.

## 🌐 `networks`
Define redes internas para conectar y aislar los servicios del compose.

---

📌 Ahora que conocemos estos parámetros, profundicemos en cómo están aplicados específicamente en nuestro proyecto: 🔗 **[mini-proyecto-oic](https://github.com/lacamposm/mini-proyecto-oic)**
