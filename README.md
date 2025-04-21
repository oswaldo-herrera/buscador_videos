Descripción del Proyecto
Buscador de Videos es una aplicación web desarrollada con Python y el framework Django, cuyo propósito es
permitir a los usuarios registrarse, autenticarse y realizar búsquedas de videos en la plataforma YouTube, así
como marcar sus videos favoritos en una sección personalizada. Este proyecto fue creado como parte de un
ejercicio técnico con el fin de evaluar habilidades en desarrollo web, integración de APIs externas, y
aplicación de buenas prácticas de seguridad y diseño.

Tecnologías Utilizadas
- Backend: Python, Django
- Frontend: HTML, Bootstrap 5 (diseño responsivo)
- Autenticación: Sistema personalizado de registro/login
- Integración Externa: API de YouTube para búsqueda de videos
- Base de Datos: SQLite (puede adaptarse a PostgreSQL o MySQL)
- Despliegue: Render

Funcionalidades
-Registro de usuarios públicos
    Nombre, apellido, correo electrónico, nombre de usuario y contraseña 
    Confirmación de contraseña
-Inicio de sesión
    Autenticación por nombre de usuario o correo electrónico
-Sección principal de videos
    Buscador de videos con integración a la API de YouTube
    Listado dinámico de resultados con opción para marcar como favorito
-Sección de favoritos
    Listado de videos marcados por el usuario como favoritos
    Opción para eliminar videos de favoritos
-Otras características
    Navegación con nombre del usuario autenticado
    Sistema de cierre de sesión
    Diseño adaptado a dispositivos móviles (responsive)
    Seguridad adicional con almacenamiento cifrado de contraseñas

Despliegue
La aplicación ha sido desplegada en línea usando Render, lo cual permite acceder a la misma desde cualquier navegador sin necesidad de instalación local.
