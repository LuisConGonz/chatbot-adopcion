# chatbot-adopcion
#  Chatbot de Adopción de Mascotas

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/Framework-FastAPI-green)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

## Descripción
Solución tecnológica para automatizar el proceso de consultas sobre mascotas disponibles para adopción. Integra:
- Backend en FastAPI (Python)
- Frontend web con HTML/JS
- Lógica de chatbot para responder preguntas frecuentes

##  Problema Identificado
Los refugios de animales reciben consultas repetitivas sobre requisitos de adopción y características de mascotas, saturando al personal. Este proyecto:
- **Automatiza** el 80% de preguntas frecuentes
- Reduce tiempos de respuesta de horas a segundos
- Centraliza información de mascotas disponibles

##  Solución
| Componente | Tecnología | Función |
|------------|------------|---------|
| Backend | FastAPI | Procesar preguntas y generar respuestas estructuradas |
| Frontend | HTML/JS | Interfaz web interactiva para usuarios |
| Datos | Diccionario Python | Almacenamiento temporal de perfiles de mascotas |

##  Arquitectura
```plaintext
chatbot/
├── chatbot.py          # Lógica principal del backend
├── templates/
│   └── index.html      # Interfaz web
├── requirements.txt    # Dependencias
└── README.md           # Documentación

Requerimientos Técnicos

Componente	Especificación
Servidor Web	FastAPI (Python 3.9+)
Base de Datos	SQLite (para desarrollo) / PostgreSQL (producción)
Paquetes	fastapi, uvicorn, jinja2
Memoria	Mínimo 512 MB RAM (1GB recomendado)
Plataformas	Linux, Windows, macOS, Docker, Heroku

Para su instalacion

1. Clonar repositorio
git clone https://github.com/LuisConGonz/chatbot-adopcion.git
cd chatbot-adopcion.

2. Crear entorno virtual (Python)
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

3. Instalar dependencias
pip install -r requirements.txt

4. Ejecutar (modo desarrollo)
uvicorn chatbot.chatbot:app --reload

Para hacer pruebas manuales seria probar endpoints con curl:
curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d '{"mensaje":"¿Qué perros tienen?"}'

¿Como implementar en heroku?
1. Crear archivo Procfile
echo "web: uvicorn chatbot.chatbot:app --host=0.0.0.0 --port=\$PORT" > Procfile

2. Crear runtime.txt
echo "python-3.9.13" > runtime.txt

3. Desplegar
heroku create
git push heroku main
heroku open

OPCIONES DE CONFIGURACIÓN

chatbot.py: Configuración de rutas y lógica
templates/index.html: Interfaz de usuario
.env (Ejemplo):
ini: DEBUG=False
DATABASE_URL=sqlite:///db.sqlite3

Manual de Usuario

Para Usuarios:

Accede a: (http://127.0.0.1:8000)
Escribe preguntas como:
"¿Qué mascotas están disponibles?"
"¿Cuáles son los requisitos para adoptar?"

Para Administradores:
Monitoreo de logs
heroku logs --tail  # (En Heroku)
uvicorn chatbot.chatbot:app --log-level debug  # Local

Guía de Contribución

Clonar y preparar:
git clone https://github.com/LuisConGonz/chatbot-adopcion.git
git checkout -b mi-feature

Hacer cambios y enviar PR:
git add .
git commit -m "feat: nueva funcionalidad"
git push origin mi-feature
Esperar revisión antes de merge.

Roadmap

Panel de administración web
Integración con redes sociales
Sistema de seguimiento post-adopción



