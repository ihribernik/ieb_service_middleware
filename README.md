# ieb_service_middleware

esta app es un middleware para el servicio de ieb_challenge que se encarga de recibir las peticiones de los clientes mediante WebSocket y enviarlas a los servicios de ieb_challenge por http.

## Requerimientos

- python 3.6
- pip
- virtualenv

## Instalación

- clonar el repositorio
- crear un virtualenv
- instalar los requerimientos
- copiar el archivo .env.example a .env y configurar las variables de entorno

```bash
$ git clone
$ cd ieb_service_middleware
$ virtualenv -p python3.6 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Ejecución

```bash
$ python manage.py runserver
```

## Ejecución de pruebas

```bash
$ tox
```
