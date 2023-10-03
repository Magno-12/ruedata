# FastAPI Keylogger Analyzer

Este proyecto es una API desarrollada en FastAPI que permite subir archivos de registro de teclas (keylog) en formato de texto (.txt) y encontrar el código secreto más corto dentro de los registros. También proporciona documentación automática de la API y una forma de probarla utilizando Postman, elegí FastAPI porque permite crear APIs web en Python de forma eficiente y con alta velocidad de desarrollo. La simplicidad de su sintaxis y su documentación automática hacen que la implementación sea rápida y clara. Además, su rendimiento y soporte para características modernas son ideales para una solución rapida.

## Requisitos para correr el proyecto

### Clonar el repositorio

- Clona el repositorio en tu máquina:

```python
git clone https://github.com/Magno-12/ruedata
```

- Crear un entorno virtual utilizando los siguientes comandos de instalacion y activacion:

```python
pip install virtualenv
virtualenv env
```

**En Windows:**
```python
env\Scripts\activate
```

**En macOS and Linux:**
```python
source env/bin/activate
```

- Asegúrarse de tener Python 3.x instalado en su sistema. También necesitará instalar las dependencias del proyecto. Puedes hacerlo usando pip:

```python
pip install -r requirements.txt
```

- Ejecuta la aplicación FastAPI:

```python
uvicorn main:app --reload
```
La aplicación se ejecutará en http://localhost:8000.

## Uso de la API

- Utilizar Postman o cualquier otra herramienta para enviar solicitudes POST a la API para subir un archivo de registro de teclas. Asegúrate de que el archivo tenga extensión .txt. La API espera el archivo en un campo llamado "file".

### Usando Postman
1. Abre Postman y crea una nueva solicitud POST a la siguiente URL: http://localhost:8000/upload/.

2. Ve a la pestaña "Body" y selecciona "form-data". Agrega una clave llamada "file" y selecciona el archivo de registro de teclas en el valor.

3. Haz clic en "Send" para enviar la solicitud.

4. Obtener el código secreto más corto
La API procesará el archivo de registro de teclas y encontrará el código secreto más corto. El resultado se mostrará en la respuesta JSON.

## Diagrama de flujo

![image](https://github.com/Magno-12/ruedata/assets/66977118/16c50d7a-7e59-41e6-ae9c-3a6f0247a02a)

## Diagrama de procesos

![image](https://github.com/Magno-12/ruedata/assets/66977118/a277c6bd-d4a2-4df4-9baf-ca07666b6645)


