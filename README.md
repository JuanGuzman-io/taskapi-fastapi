# TaskAPI - Sistema de Gestión de Tareas

API REST desarrollada con FastAPI para gestionar tareas personales con operaciones CRUD completas, categorización y búsqueda.

## Características

- ✅ CRUD completo de tareas
- 🔍 Búsqueda por título y descripción
- 🏷️ Categorización (trabajo, personal, estudios, otros)
- ✔️ Filtrado por estado (pendiente/completada)
- 📊 Documentación automática con Swagger
- 💾 Persistencia con SQLite

## Tecnologías

- **FastAPI**: Framework web moderno y rápido
- **SQLAlchemy**: ORM para manejo de base de datos
- **Pydantic**: Validación de datos
- **SQLite**: Base de datos local
- **Uvicorn**: Servidor ASGI

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/JuanGuzman-io/taskapi-fastapi.git
cd taskapi-fastapi
```

2. Crear entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso

1. Iniciar el servidor:
```bash
uvicorn main:app --reload
```

2. Acceder a la documentación interactiva:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Endpoints

### Tareas

- `GET /tasks` - Listar todas las tareas (con filtro opcional por estado)
- `GET /tasks/{id}` - Obtener una tarea específica
- `GET /tasks/search?q=query` - Buscar tareas
- `POST /tasks` - Crear nueva tarea
- `PUT /tasks/{id}` - Actualizar tarea completa
- `PATCH /tasks/{id}/status` - Actualizar solo el estado
- `DELETE /tasks/{id}` - Eliminar tarea

## Modelo de Datos

```json
{
  "id": 1,
  "title": "Completar proyecto",
  "description": "Finalizar la API de tareas",
  "status": "pending",
  "category": "work",
  "created_at": "2025-12-08T20:00:00",
  "updated_at": "2025-12-08T20:00:00"
}
```

## Ejemplo de Uso

### Crear una tarea
```bash
curl -X POST "http://localhost:8000/tasks" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Estudiar FastAPI",
    "description": "Aprender sobre endpoints y validación",
    "status": "pending",
    "category": "study"
  }'
```

### Listar tareas pendientes
```bash
curl "http://localhost:8000/tasks?status=pending"
```

## Proyecto Académico

Este proyecto fue desarrollado como parte de la actividad "Desarrollo de aplicaciones con asistentes de programación basados en IA" utilizando ChatGPT como asistente principal para la generación de código.

## Autor

Juan D. Guzmán - [juan-dev.com](https://www.juan-dev.com/)

## Licencia

MIT