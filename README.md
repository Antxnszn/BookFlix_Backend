# BookFlix Backend
## Instalación

Necesitaremos python y mysql previamente instalado:

Página oficial de MySQL: https://www.oracle.com/mysql/technologies/mysql-enterprise-edition-downloads.html#windows

Página oficial de Python: https://www.python.org/downloads/

Con sql instalado y corriendo en nuetsro equipo, hay que crear nuestras tablas de mysql, empezaremos creando una base de datos que llamaremos, bookflix:

```sql
create database bookflix;
```

Después, copiaremos y pegaremos las tablas que contiene el script de la ruta **app/sqlmodel.sql**

Y crearemos un usuario para acceder, ejecutar comando por comando preferentemente:

```sql
CREATE USER 'nombre_usuario'@'localhost' IDENTIFIED BY 'contraseña_segura';
GRANT ALL PRIVILEGES ON bookflix.* TO 'nombre_usuario'@'localhost';
FLUSH PRIVILEGES;
```

A su vez, haremos un archivo llamado .env en la ruta inicial del proyecto, de forma que esté en la misma altura que run.py, algo así:

—run.py

|—.env

|—app

…

Este archivo tiene que contener lo siguiente, copia y pega solamente, 

```
MYSQL_HOST=localhost
MYSQL_USER=nombre_usuario
MYSQL_PASSWORD=contraseña_segura
MYSQL_DB=bookflix
SECRET_KEY= contraseña_a_preferencia # cualquiera que decidas. 
```

Una vez cumplidos los requisitos, hay que clonar el repositorio:

```powershell
git clone https://github.com/Antxnszn/BookFlix_Backend
```

Clonado el repositorio, hay que crear un entorno virtual con el siguiente comando:

```bash
python -m venv venv
```

 Lo activamos:

```powershell
.\venv\Scripts\Activate.ps1
```

Desde la ruta donde clonamos el repositorio instalamos las dependencias necesarias con:

```powershell
pip install -r requirements.txt
```

Por último, corremos el archivo [run.py](http://run.py) con:

```powershell
python run.py
```

Ahora sigue instalar el frontend. Link del repositorio de front: https://github.com/Antxnszn/BookFlix
