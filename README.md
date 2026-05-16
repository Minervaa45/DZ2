# BLT Health Service

Минимальный HTTP-сервис с CRUD для пользователей и health-check.

## Структура проекта

```
blt-health-service/
├── main.py                 # FastAPI приложение
├── db.py                   # Подключение к БД
├── models.py               # SQLAlchemy модели
├── schemas.py              # Pydantic схемы
├── alembic.ini             # Alembic конфиг
├── migrations/             # Миграции
├── requirements.txt        # Зависимости
├── Dockerfile              # Инструкции для сборки образа
├── k8s/                    # Манифесты Kubernetes
└── postman/                # Postman коллекция
```

## Запуск локально (без Docker)

Нужен PostgreSQL. Переменные окружения:

- DB_HOST
- DB_PORT
- DB_NAME
- DB_USER
- DB_PASSWORD

Пример запуска:

```bash
pip install -r requirements.txt
alembic upgrade head
uvicorn main:app --host 0.0.0.0 --port 8000
```

Проверка:
```bash
curl http://localhost:8000/health
# {"status": "OK"}
```

## Сборка Docker-образа

```bash
# Сборка под AMD64 (обязательно для совместимости)
docker build --platform linux/amd64 -t minerva45/blt-health:v1 .
```

## Запуск контейнера локально

```bash
docker run -p 8000:8000 minerva45/blt-health:v1
```

Проверка:
```bash
curl http://localhost:8000/health
# {"status": "OK"}
```

## Публикация на DockerHub

```bash
# 1. Авторизация
docker login

# 2. Push образа
docker push minerva45/blt-health:v1
```

## API

| Метод | Путь            | Ответ                    |
|-------|-----------------|--------------------------|
| GET   | /health         | `{"status": "OK"}`     |
| POST  | /users          | пользователь             |
| GET   | /users          | список пользователей      |
| GET   | /users/{id}     | пользователь             |
| PUT   | /users/{id}     | пользователь             |
| DELETE| /users/{id}     | 204                       |

Пример тела пользователя:

```json
{
	"name": "Ada Lovelace",
	"email": "ada.lovelace@example.com"
}
```

## Kubernetes

Если нужен ingress-controller в minikube, установите nginx ingress через Helm (рекомендация из ДЗ).

1) Установить PostgreSQL через Helm (release name должен быть `blt-db`):

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm install blt-db bitnami/postgresql -f k8s/postgres-values.yaml
```

Важно: значения `username` и `password` в k8s/secret.yaml должны совпадать с k8s/postgres-values.yaml.

2) Применить манифесты приложения в правильном порядке:

```bash
kubectl apply -f k8s/configmap.yaml -f k8s/secret.yaml -f k8s/deployment.yaml -f k8s/service.yaml -f k8s/ingress.yaml
```

3) Применить миграции (Job):

```bash
kubectl apply -f k8s/migration-job.yaml
```

4) Добавить в hosts:

```
<minikube ip> arch.homework
```

Проверка:

```bash
curl http://arch.homework/health
```

## Postman / Newman

Коллекция: `postman/blt-health.postman_collection.json`

Запуск:

```bash
newman run postman/blt-health.postman_collection.json
```

Если newman не установлен:

```bash
npm install -g newman
```
