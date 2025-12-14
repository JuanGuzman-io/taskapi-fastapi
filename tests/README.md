# Tests Suite para TaskAPI 🧪

## Descripción

Suite completa de tests desarrollada para la **Actividad 2: Generación de entornos de pruebas**.
Todos los tests fueron generados utilizando asistentes de IA.

## Estructura

```
tests/
├── __init__.py              # Inicialización del paquete de tests
├── test_health.py           # Tests de salud de la API
├── test_tasks_integration.py # Tests de integración de endpoints
├── test_models_unit.py      # Tests unitarios de modelos
└── README.md                # Esta documentación
```

## Configuración

### Dependencias
Las dependencias de testing están en `requirements.txt`:
- pytest
- pytest-asyncio
- httpx
- pytest-cov

### Instalación
```bash
pip install -r requirements.txt
```

## Ejecución de Tests

### Ejecutar todos los tests
```bash
pytest
```

### Ejecutar con cobertura
```bash
pytest --cov=. --cov-report=html
```

### Ejecutar solo tests de integración
```bash
pytest -m integration
```

### Ejecutar solo tests unitarios
```bash
pytest -m unit
```

### Ejecutar test específico
```bash
pytest tests/test_health.py::test_read_root
```

### Modo verbose
```bash
pytest -v
```

## Cobertura de Tests

### Tests de Integración (test_tasks_integration.py)

#### CRUD Operations
- ✅ Crear tarea
- ✅ Crear tarea con datos inválidos (422)
- ✅ Listar todas las tareas
- ✅ Listar tareas vacías
- ✅ Obtener tarea por ID
- ✅ Obtener tarea no existente (404)
- ✅ Actualizar tarea completa
- ✅ Actualizar tarea no existente (404)
- ✅ Actualizar solo estado de tarea
- ✅ Eliminar tarea
- ✅ Eliminar tarea no existente (404)

#### Search & Filters
- ✅ Buscar tareas por texto
- ✅ Buscar sin resultados
- ✅ Filtrar por estado
- ✅ Paginación (skip/limit)

### Tests Unitarios (test_models_unit.py)
- ✅ Validación de enums (TaskStatus, TaskCategory)
- ✅ Validación de schemas Pydantic
- ✅ TaskCreate con datos válidos
- ✅ TaskCreate con datos inválidos
- ✅ TaskUpdate parcial
- ✅ TaskStatusUpdate
- ✅ Campos requeridos

### Tests de Health (test_health.py)
- ✅ Endpoint raíz
- ✅ Documentación (/docs)

## Fixtures (conftest.py)

### `test_db`
Crea una base de datos SQLite en memoria para cada test.

### `client`
Provee un TestClient de FastAPI con la base de datos de prueba.

### `sample_task_data`
Datos de ejemplo para crear tareas en tests.

### `create_task`
Crea una tarea de prueba y retorna sus datos.

## Resultados Esperados

### Cantidad de Tests
- **Total**: 27 tests
- **Integración**: 18 tests
- **Unitarios**: 9 tests

### Cobertura Esperada
- **Objetivo**: >80% de cobertura de código
- **Archivos cubiertos**: main.py, models.py, schemas.py, database.py

## Notas

- Todos los tests usan base de datos en memoria (SQLite :memory:)
- Cada test tiene su propia instancia de BD (aislamiento)
- Los tests de integración usan el TestClient de FastAPI
- Los tests unitarios validan modelos y schemas sin BD

## Próximos Pasos

- [ ] Agregar tests de performance
- [ ] Agregar tests de carga (stress testing)
- [ ] Mejorar cobertura a >90%
- [ ] Agregar tests de seguridad

---
**Desarrollado con**: Claude AI (Anthropic)  
**Fecha**: Diciembre 2025  
**Proyecto**: Actividad 2 - PSU
