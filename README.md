# Centro de Armonía Doméstica (HogarMonía)

[![Python](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-5.2-green.svg)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/postgresql-17.4-blueviolet.svg)](https://www.postgresql.org/)
<!--[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)-->

## Descripción del Proyecto

Esta aplicación, denominada 'Centro de Armonía Doméstica', se propone como una solución integral para la gestión y coordinación de las tareas y gastos compartidos en los hogares, ya sean de compañeros de piso o familias. Su objetivo es facilitar la convivencia y optimizar la organización doméstica.

Las principales tareas en las que se centrará esta aplicación serán:
* Gestión de tareas:  
    * La funcionalidad de la gestión de tareas servirá para la asignación de las tareas del hogar  a los distintos miembros del domicilio de forma aleatoria, al asignarse la tarea se elegirá qué miembro puede ser elegido para dicha tarea(para que en el caso de que se incluyan niños puedan ser excluidos, al no ser capaces de realizar todas las tareas) y también se incluirá la posibilidad de que a la misma persona no se le pueda asignar dos veces seguidas la misma tarea al registrarse la misma.

* Seguimiento de gastos conjuntos:
    * Ideado principalmente para compañeros de piso para la gestión de los gastos comunes, ya sean suscripciones a servicios o compras que se realicen para utilizar por todos los integrantes del piso. En el que se incluirá de cuanto es el importe y quien ha sido el encargado de pagarlo para que el resto de integrantes lo abonen a la mayor brevedad; y en el caso de familias para tener un control sobre los gastos imprescindibles que se realizan todos los meses, ya sean compras, contrataciones…
		
* Lista de la compra conjunta:  
    * La aplicación también incluirá una lista de la compra colaborativa, siendo este un apartado en el que cualquier miembro del grupo podrá ir introduciendo artículos o alimentos necesarios, en donde todos puedan tener acceso (idea: Se explorará la posibilidad de integrar un sistema que ordene la lista según la disposición de los productos en los supermercados, optimizando así el tiempo de compra).

> <!--[Escribe aquí una descripción concisa de tu aplicación web. ¿Cuál es su propósito principal? ¿Qué problema resuelve? ¿Cuáles son sus características clave? Por ejemplo: "Esta aplicación web permite a los usuarios gestionar sus tareas pendientes, realizar un seguimiento de sus gastos y crear listas de la compra de forma intuitiva."]-->

## Tecnologías Utilizadas

Para desarrollar esta aplicación web, se han utilizado las siguientes tecnologías principales:

* **Backend (Python):**
    * **Django:** Framework de alto nivel para Python que facilita la creación de aplicaciones web robustas y escalables.
    * **ORM de Django:** Permite la interacción con la base de datos PostgreSQL utilizando modelos de Python.
    * **Python estándar:** Para la lógica de la aplicación y el manejo de datos.
* **Frontend (JavaScript Vanilla):**
    * **HTML:** Para la estructuración del contenido de la interfaz de usuario.
    * **CSS:** Para el diseño y la aplicación de estilos a la interfaz de usuario.
    * **JavaScript:** Para la interactividad y el dinamismo del frontend, así como para las peticiones al backend.
* **Base de Datos:**
    * **PostgreSQL:** Sistema de gestión de bases de datos relacional utilizado para almacenar la información de la aplicación.
* **Otras Herramientas:**
    * **Git:** Para el control de versiones del código fuente.

## Configuración Local

1.  **Requisitos Previos:**
    * Asegúrate de tener instalado Python (versión 3.x). Puedes descargarlo desde [https://www.python.org/downloads/](https://www.python.org/downloads/).
    * Asegúrate de tener instalado PostgreSQL. Puedes descargarlo desde [https://www.postgresql.org/download/](https://www.postgresql.org/download/).

2.  **Clonar el Repositorio:**
    ```bash
    git clone https://github.com/asierCB/HogarMonia
    cd HogarMonia
    ```

3.  **Crear y Activar el Entorno Virtual (Recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/macOS
    venv\Scripts\activate  # En Windows
    ```

4.  **Instalar las Dependencias de Python:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Nota: Asegúrate de generar este archivo en la raíz de tu proyecto Django con `pip freeze > requirements.txt` después de instalar todas las dependencias de Django y otras librerías que utilices.)*

5.  **Configurar la Base de Datos PostgreSQL:**
    * Crea una base de datos en PostgreSQL para tu proyecto (puedes usar `psql` o una herramienta como pgAdmin).
    * Configura las credenciales de la base de datos en el archivo `settings.py` de tu proyecto Django. Busca la sección `DATABASES` y actualízala con tu configuración:

        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': '[nombre_de_tu_base_de_datos]',
                'USER': '[tu_usuario_de_postgresql]',
                'PASSWORD': '[tu_contraseña_de_postgresql]',
                'HOST': 'localhost',
                'PORT': '5432',
            }
        }
        ```

6.  **Realizar las Migraciones:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

<!--7.  **Crear un Superusuario (Opcional, para acceder al panel de administración de Django):**
    ```bash
    python manage.py createsuperuser
    ```
    Sigue las instrucciones para crear un usuario administrador.-->

7.  **Ejecutar el Servidor de Desarrollo:**
    ```bash
    python manage.py runserver
    ```
    La aplicación estará disponible en `http://127.0.0.1:8000/` (o la dirección que te indique la consola) y a continuación escribre `core/index/`, en el caso en el que la consola te indique la dirección que te he comentado el total quedaría: `http://127.0.0.1:8000/core/index/`.
    Esto te llevara a la página de inicio de la página web desde donde podrás acceder a todos los recursos.

## Uso

1.  Abre tu navegador web y navega a `http://127.0.0.1:8000/core/index/`.
2.  Una vez que accedas al link apareceras en una página de inicio (actualmente incompleta) en donde se describe un poco como en que se basa la aplicacion con las diferentes secciones.
3.  Actualmente puedes moverte por todas las páginas que estan disponible, tanto en el encabezado como en el footer, aunque de momento prácticamente todo a excepcion del apartado sobre el perfil (al cual se accede en el logo de user situado en la parte derecha del encabezado) es código estático de HTML, a falta de vincularlo con la BBDD para que se conecte y los datos de los diferentes formularios como de las tareas, gastos... vayan cambiando en función del grupo al que se pertenezca.
<!--3.  [Si creaste un superusuario, menciona cómo acceder al panel de administración: "Puedes acceder al panel de administración en `http://127.0.0.1:8000/admin/` utilizando las credenciales que creaste."]-->

<!--## Pruebas (Opcional)

```bash
python manage.py test-->
