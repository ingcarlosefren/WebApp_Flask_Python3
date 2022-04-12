# WebApp_Flask_Python3
Un ejemplo de construcción de una webapp utilizando python3, flask, virtualenv y Docker.

## Configuracion del entorno


### Crear entorno virtual
1. Copie este repositorio `git clone https://github.com/ingcarlosefren/WebApp_Flask_Python3.git`
2. Acceder al directorio `cd WebApp_Flask_Python3`
3. Cree dentro de la anterior carpeta un entorno virual con `virtualenv -p python3 .env` o `python3 -m venv .env`
4. Instalar las librerias `pip install -r requirements.txt`
5. Contruye la imagen `docker build -t my-flask-web-app-docker:v0.01 .` 