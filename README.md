# Proyecto de Registro e Inicio de Sesión

Este proyecto es una aplicación web que permite a los usuarios registrarse e iniciar sesión. Utiliza un backend en Flask y una base de datos MySQL, junto con un frontend en React.

## Estructura del Proyecto

- **backend/**: Contiene el código del servidor Flask y la configuración de la base de datos.
- **frontend/**: Contiene el código de la aplicación React.
- **Dockerfiles**: Archivos de configuración para crear imágenes de Docker para el backend, la base de datos y el frontend.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalados los siguientes programas en tu máquina:

- Docker
- Node.js y npm
- Python 3.x

## Instrucciones para la Prueba

1. **Configurar el entorno**:
   - Clona el repositorio en tu máquina local.
   - Navega a la carpeta del proyecto.

2. **Construir las imágenes de Docker**:
   - Crea las imágenes de Docker para el backend, la base de datos y el frontend.

3. **Ejecutar los contenedores**:
   - Inicia los contenedores de la base de datos y el backend.
   - Asegúrate de que el backend esté vinculado a la base de datos.

4. **Iniciar el frontend**:
   - Ejecuta el contenedor del frontend y asegúrate de que esté conectado al backend.

5. **Acceder a la aplicación**:
   - Abre tu navegador y dirígete a la dirección donde se está ejecutando el frontend (por defecto, `http://localhost:3000`).

6. **Registrar un nuevo usuario**:
   - Completa el formulario de registro con un nombre de usuario y una contraseña.

7. **Iniciar sesión**:
   - Usa el nombre de usuario y la contraseña que registraste para iniciar sesión.

8. **Verificar la funcionalidad**:
   - Después de iniciar sesión, deberías ver un mensaje de bienvenida desde el backend.

## Notas

- Asegúrate de que los contenedores estén en ejecución antes de intentar acceder a la aplicación.
- Puedes modificar los archivos de configuración según sea necesario para adaptarlos a tu entorno.