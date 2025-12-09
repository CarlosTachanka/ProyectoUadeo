# Proyecto Escolar - Flask + PostgreSQL

Este proyecto es una aplicación web simple para un trabajo escolar, construida con:
- **Python Flask**: Backend.
- **PostgreSQL**: Base de datos.
- **Docker & Docker Compose**: Contenedorización y orquestación.

## Requisitos previos

- Tener instalado [Docker](https://www.docker.com/products/docker-desktop).
- Tener instalado Docker Compose (generalmente viene con Docker Desktop).

## Instrucciones para levantar el proyecto

1. **Configurar variables de entorno**
   El código ya incluye un archivo `.env` por defecto para facilitar pruebas. Si deseas cambiar las credenciales, edita el archivo `.env`.

2. **Iniciar la aplicación**
   Abre una terminal en la carpeta raíz del proyecto y ejecuta:

   ```bash
   docker-compose up --build
   ```

   Este comando descargará las imágenes necesarias, construirá el contenedor de la aplicación y levantará la base de datos.
   
   > **Nota:** La primera vez puede tardar unos minutos.

3. **Acceder a la aplicación**
   Una vez que veas en la terminal que los servicios están corriendo, abre tu navegador y ve a:

   [http://localhost:8000](http://localhost:8000)

## Estructura del Proyecto

- `app/`: Contiene el código fuente de la aplicación.
  - `routes.py`: Rutas de la web (Controladores).
  - `models.py`: Modelos de la base de datos (Usuario, Producto).
  - `templates/`: Archivos HTML.
- `Dockerfile`: Configuración para construir la imagen de Python.
- `docker-compose.yml`: Configuración para lenvantar Flask y PostgreSQL juntos.

## Uso

- **Inicio**: Página de bienvenida.
- **Usuarios**: Puedes agregar usuarios con nombre y email, y ver la lista.
- **Productos**: Puedes agregar productos con nombre, precio y stock, y ver la lista.

## Detener la aplicación

Presiona `Ctrl+C` en la terminal donde se está ejecutando, o ejecuta en otra terminal:

```bash
docker-compose down
```
