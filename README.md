# BookFlix Backend
## Instalación

Necesitaremos python y mysql previamente instalado:

Página oficial de MySQL: https://www.oracle.com/mysql/technologies/mysql-enterprise-edition-downloads.html#windows

Página oficial de Python: https://www.python.org/downloads/

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
