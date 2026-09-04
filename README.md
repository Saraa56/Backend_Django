# Backend Django

Backend desarrollado con **Django y Django REST Framework** para la construcción de una API conectada a una base de datos **MySQL**.

El proyecto implementa la estructura base de una aplicación backend utilizando el patrón de organización propio de Django, incluyendo modelos, serializers, vistas, rutas y migraciones.

## Tecnologías

* Python
* Django 5.2
* Django REST Framework
* MySQL
* mysqlclient

## Características

* API desarrollada con Django REST Framework.
* Modelado de datos mediante Django ORM.
* Serialización de información mediante serializers.
* Definición de endpoints y rutas.
* Integración con base de datos MySQL.
* Sistema de migraciones de Django.
* Configuración separada entre proyecto y aplicación.

## Estructura

```text
Backend_Django/
├── backend/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── miapi/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── manage.py
├── requirements.txt
└── .gitignore
```

## Instalación

Clonar el repositorio e instalar las dependencias:

```bash
git clone https://github.com/Saraa56/Backend_Django.git
cd Backend_Django

python -m venv venv
```

Activar el entorno virtual:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Configurar la conexión a MySQL en `settings.py` y ejecutar las migraciones:

```bash
python manage.py migrate
```

Iniciar el servidor:

```bash
python manage.py runserver
```

La aplicación estará disponible en:

```text
http://127.0.0.1:8000/
```

## Contexto

Proyecto desarrollado como práctica de **desarrollo backend con Django**, orientado al diseño de APIs, manejo de modelos y conexión con bases de datos relacionales.

## Estado

**Proyecto académico / de aprendizaje.**

## Autora

**Sara Otero**

Ingeniería de Software.
