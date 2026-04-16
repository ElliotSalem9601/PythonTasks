"""Автотесты для API проектов YouGile"""

import pytest
import uuid
from api_client import YougileAPIClient
from config import TEST_PROJECT, NON_EXISTENT_ID


class TestProjectsAPI:
    """Тесты для методов работы с проектами"""

    @pytest.fixture
    def api_client(self):
        """Фикстура для создания клиента API"""
        return YougileAPIClient()

    @pytest.fixture
    def created_project_id(self, api_client):
        """Фикстура для создания проекта перед тестом и удаления после"""
        project_data = {
            "title": f"Test Project {uuid.uuid4().hex[:8]}",
            "description": "Temporary project for testing"
        }
        response = api_client.create_project(project_data)
        assert response.status_code == 201
        project_id = response.json().get("id")
        yield project_id
        # Очистка после теста
        api_client.delete_project(project_id)

    # ========== POST /api-v2/projects ==========

    def test_create_project_positive(self, api_client):
        """Позитивный тест: создание проекта с валидными данными"""
        unique_title = f"Test Project {uuid.uuid4().hex[:8]}"
        project_data = {
            "title": unique_title,
            "description": "Project created by API test"
        }

        response = api_client.create_project(project_data)

        assert response.status_code == 201
        response_data = response.json()
        assert "id" in response_data
        assert response_data.get("title") == unique_title

        # Очистка
        api_client.delete_project(response_data["id"])

    def test_create_project_negative_missing_title(self, api_client):
        """Негативный тест: создание проекта без обязательного поля title"""
        project_data = {
            "description": "Project without title"
        }

        response = api_client.create_project(project_data)

        # Ожидается ошибка валидации
        assert response.status_code in [400, 422]
        response_data = response.json()
        assert "error" in response_data or "title" in str(response_data).lower()

    def test_create_project_negative_empty_title(self, api_client):
        """Негативный тест: создание проекта с пустым заголовком"""
        project_data = {
            "title": "",
            "description": "Project with empty title"
        }

        response = api_client.create_project(project_data)

        assert response.status_code in [400, 422]
        response_data = response.json()
        assert "error" in response_data

    # ========== GET /api-v2/projects/{id} ==========

    def test_get_project_positive(self, api_client, created_project_id):
        """Позитивный тест: получение существующего проекта по ID"""
        response = api_client.get_project(created_project_id)

        assert response.status_code == 200
        response_data = response.json()
        assert response_data.get("id") == created_project_id
        assert "title" in response_data

    def test_get_project_negative_not_found(self, api_client):
        """Негативный тест: получение проекта по несуществующему ID"""
        response = api_client.get_project(NON_EXISTENT_ID)

        assert response.status_code == 404
        response_data = response.json()
        assert "error" in response_data

    def test_get_project_negative_invalid_id(self, api_client):
        """Негативный тест: получение проекта по некорректному формату ID"""
        invalid_ids = ["invalid", "123", "abc", ""]

        for invalid_id in invalid_ids:
            response = api_client.get_project(invalid_id)
            assert response.status_code in [400, 404], \
                f"ID {invalid_id} should return 400 or 404"

    # ========== PUT /api-v2/projects/{id} ==========

    def test_update_project_positive(self, api_client, created_project_id):
        """Позитивный тест: обновление существующего проекта"""
        new_title = f"Updated Title {uuid.uuid4().hex[:8]}"
        update_data = {
            "title": new_title,
            "description": "Updated description"
        }

        response = api_client.update_project(created_project_id, update_data)

        assert response.status_code == 200
        response_data = response.json()
        assert response_data.get("title") == new_title

        # Проверка, что изменения сохранились
        get_response = api_client.get_project(created_project_id)
        assert get_response.json().get("title") == new_title

    def test_update_project_positive_partial(self, api_client, created_project_id):
        """Позитивный тест: частичное обновление проекта (только title)"""
        new_title = f"Partial Update {uuid.uuid4().hex[:8]}"
        update_data = {"title": new_title}

        response = api_client.update_project(created_project_id, update_data)

        assert response.status_code == 200
        response_data = response.json()
        assert response_data.get("title") == new_title

    def test_update_project_negative_not_found(self, api_client):
        """Негативный тест: обновление несуществующего проекта"""
        update_data = {"title": "This should fail"}

        response = api_client.update_project(NON_EXISTENT_ID, update_data)

        assert response.status_code == 404
        response_data = response.json()
        assert "error" in response_data

    def test_update_project_negative_invalid_id(self, api_client):
        """Негативный тест: обновление проекта с некорректным ID"""
        update_data = {"title": "Update with invalid ID"}

        response = api_client.update_project("invalid-id-format", update_data)

        assert response.status_code in [400, 404]