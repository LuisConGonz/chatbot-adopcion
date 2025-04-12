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
