"""Клиент для работы с YouGile API"""

import requests
from config import BASE_URL, HEADERS


class YougileAPIClient:
    """Клиент для взаимодействия с YouGile API"""

    def __init__(self, base_url=BASE_URL, headers=HEADERS):
        self.base_url = base_url
        self.headers = headers
        self.created_projects = []  # для отслеживания созданных проектов

    def create_project(self, project_data):
        """
        Создание проекта
        POST /api-v2/projects
        """
        url = f"{self.base_url}/projects"
        response = requests.post(url, json=project_data, headers=self.headers)
        if response.status_code == 201:
            project_id = response.json().get("id")
            if project_id:
                self.created_projects.append(project_id)
        return response

    def get_project(self, project_id):
        """
        Получение проекта по ID
        GET /api-v2/projects/{id}
        """
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.get(url, headers=self.headers)
        return response

    def update_project(self, project_id, project_data):
        """
        Обновление проекта
        PUT /api-v2/projects/{id}
        """
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.put(url, json=project_data, headers=self.headers)
        return response

    def delete_project(self, project_id):
        """
        Удаление проекта (для очистки)
        DELETE /api-v2/projects/{id}
        """
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.delete(url, headers=self.headers)
        if project_id in self.created_projects:
            self.created_projects.remove(project_id)
        return response

    def cleanup(self):
        """Очистка всех созданных проектов"""
        for project_id in self.created_projects.copy():
            self.delete_project(project_id)