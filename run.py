# server/run.py
from app import create_app

# Crea la instancia de la aplicación Flask
app = create_app()

if __name__ == "__main__":
    # Asegúrate de que el frontend React esté corriendo en un puerto diferente (ej. 3000)
    # El backend Flask por defecto corre en 5000
    app.run(debug=True, port=5000)
    