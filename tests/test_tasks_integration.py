"""Tests de integración para endpoints de tareas"""
import pytest


@pytest.mark.integration
class TestTaskCRUD:
    """Tests para operaciones CRUD de tareas"""

    def test_create_task(self, client, sample_task_data):
        """Test crear una nueva tarea"""
        response = client.post("/tasks", json=sample_task_data)
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == sample_task_data["title"]
        assert data["description"] == sample_task_data["description"]
        assert data["status"] == sample_task_data["status"]
        assert data["category"] == sample_task_data["category"]
        assert "id" in data

    def test_create_task_invalid_status(self, client):
        """Test crear tarea con estado inválido"""
        invalid_task = {
            "title": "Invalid Task",
            "description": "Test",
            "status": "invalid_status",
            "category": "work"
        }
        response = client.post("/tasks", json=invalid_task)
        assert response.status_code == 422

    def test_get_tasks_empty(self, client):
        """Test listar tareas cuando no hay ninguna"""
        response = client.get("/tasks")
        assert response.status_code == 200
        assert response.json() == []

    def test_get_tasks(self, client, create_task):
        """Test listar todas las tareas"""
        response = client.get("/tasks")
        assert response.status_code == 200
        tasks = response.json()
        assert len(tasks) >= 1
        assert tasks[0]["id"] == create_task["id"]

    def test_get_task_by_id(self, client, create_task):
        """Test obtener tarea específica por ID"""
        task_id = create_task["id"]
        response = client.get(f"/tasks/{task_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == task_id
        assert data["title"] == create_task["title"]

    def test_get_task_not_found(self, client):
        """Test obtener tarea que no existe (404)"""
        response = client.get("/tasks/999")
        assert response.status_code == 404
        assert response.json()["detail"] == "Task not found"

    def test_update_task(self, client, create_task):
        """Test actualizar tarea completa"""
        task_id = create_task["id"]
        update_data = {
            "title": "Updated Task",
            "description": "Updated description",
            "status": "completed",
            "category": "personal"
        }
        response = client.put(f"/tasks/{task_id}", json=update_data)
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == update_data["title"]
        assert data["description"] == update_data["description"]
        assert data["status"] == update_data["status"]

    def test_update_task_not_found(self, client):
        """Test actualizar tarea que no existe"""
        update_data = {"title": "Updated", "status": "completed"}
        response = client.put("/tasks/999", json=update_data)
        assert response.status_code == 404

    def test_update_task_status(self, client, create_task):
        """Test actualizar solo el estado de la tarea"""
        task_id = create_task["id"]
        status_update = {"status": "completed"}
        response = client.patch(f"/tasks/{task_id}/status", json=status_update)
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "completed"
        assert data["title"] == create_task["title"]  # Title no cambió

    def test_delete_task(self, client, create_task):
        """Test eliminar tarea"""
        task_id = create_task["id"]
        response = client.delete(f"/tasks/{task_id}")
        assert response.status_code == 204
        
        # Verificar que ya no existe
        get_response = client.get(f"/tasks/{task_id}")
        assert get_response.status_code == 404

    def test_delete_task_not_found(self, client):
        """Test eliminar tarea que no existe"""
        response = client.delete("/tasks/999")
        assert response.status_code == 404


@pytest.mark.integration
class TestTaskSearch:
    """Tests para búsqueda y filtrado de tareas"""

    def test_search_tasks(self, client):
        """Test buscar tareas por texto"""
        # Crear algunas tareas
        client.post("/tasks", json={
            "title": "Python Development",
            "description": "Learn FastAPI",
            "status": "pending",
            "category": "work"
        })
        client.post("/tasks", json={
            "title": "Java Project",
            "description": "Build API",
            "status": "pending",
            "category": "work"
        })
        
        # Buscar tareas con "Python"
        response = client.get("/tasks/search?q=Python")
        assert response.status_code == 200
        tasks = response.json()
        assert len(tasks) >= 1
        assert "Python" in tasks[0]["title"]

    def test_search_tasks_no_results(self, client):
        """Test buscar tareas sin resultados"""
        response = client.get("/tasks/search?q=NonExistentTask")
        assert response.status_code == 200
        assert response.json() == []

    def test_filter_tasks_by_status(self, client):
        """Test filtrar tareas por estado"""
        # Crear tareas con diferentes estados
        client.post("/tasks", json={
            "title": "Task 1",
            "description": "Test",
            "status": "pending",
            "category": "work"
        })
        client.post("/tasks", json={
            "title": "Task 2",
            "description": "Test",
            "status": "completed",
            "category": "work"
        })
        
        # Filtrar por pending
        response = client.get("/tasks?status=pending")
        assert response.status_code == 200
        tasks = response.json()
        assert all(task["status"] == "pending" for task in tasks)
        
    def test_pagination(self, client):
        """Test paginación de tareas"""
        # Crear 5 tareas
        for i in range(5):
            client.post("/tasks", json={
                "title": f"Task {i}",
                "description": "Test",
                "status": "pending",
                "category": "work"
            })
        
        # Obtener primeras 2
        response = client.get("/tasks?skip=0&limit=2")
        assert response.status_code == 200
        assert len(response.json()) == 2
        
        # Obtener siguientes 2
        response = client.get("/tasks?skip=2&limit=2")
        assert response.status_code == 200
        assert len(response.json()) == 2