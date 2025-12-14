"""Tests unitarios para modelos y validaciones"""
import pytest
from pydantic import ValidationError
from models import TaskStatus, TaskCategory
from schemas import TaskCreate, TaskUpdate, TaskStatusUpdate


@pytest.mark.unit
class TestEnums:
    """Tests para enumeraciones"""

    def test_task_status_values(self):
        """Test valores válidos de TaskStatus"""
        assert TaskStatus.PENDING.value == "pending"
        assert TaskStatus.IN_PROGRESS.value == "in_progress"
        assert TaskStatus.COMPLETED.value == "completed"

    def test_task_category_values(self):
        """Test valores válidos de TaskCategory"""
        assert TaskCategory.WORK.value == "work"
        assert TaskCategory.PERSONAL.value == "personal"
        assert TaskCategory.SHOPPING.value == "shopping"
        assert TaskCategory.OTHER.value == "other"


@pytest.mark.unit
class TestSchemas:
    """Tests para validación de schemas Pydantic"""

    def test_task_create_valid(self):
        """Test crear TaskCreate con datos válidos"""
        task = TaskCreate(
            title="Test Task",
            description="Test description",
            status="pending",
            category="work"
        )
        assert task.title == "Test Task"
        assert task.status == "pending"

    def test_task_create_invalid_status(self):
        """Test TaskCreate con estado inválido"""
        with pytest.raises(ValidationError):
            TaskCreate(
                title="Test",
                description="Test",
                status="invalid_status",
                category="work"
            )

    def test_task_create_invalid_category(self):
        """Test TaskCreate con categoría inválida"""
        with pytest.raises(ValidationError):
            TaskCreate(
                title="Test",
                description="Test",
                status="pending",
                category="invalid_category"
            )

    def test_task_create_missing_title(self):
        """Test TaskCreate sin título (campo requerido)"""
        with pytest.raises(ValidationError):
            TaskCreate(
                description="Test",
                status="pending",
                category="work"
            )

    def test_task_update_partial(self):
        """Test TaskUpdate con actualización parcial"""
        update = TaskUpdate(title="New Title")
        assert update.title == "New Title"
        assert update.status is None
        assert update.description is None

    def test_task_status_update(self):
        """Test TaskStatusUpdate"""
        status_update = TaskStatusUpdate(status="completed")
        assert status_update.status == "completed"

    def test_task_status_update_invalid(self):
        """Test TaskStatusUpdate con estado inválido"""
        with pytest.raises(ValidationError):
            TaskStatusUpdate(status="invalid")