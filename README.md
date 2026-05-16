# BLT Health Service

Минимальный HTTP-сервис для ДЗ «Приложение в docker-образ».

## Структура проекта

```
blt-health-service/
├── main.py           # FastAPI приложение
├── requirements.txt  # Зависимости
├── Dockerfile        # Инструкции для сборки образа
└── .dockerignore     # Исключения при сборке
```

## Запуск локально (без Docker)

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

Проверка:
```bash
curl http://localhost:8000/health/
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
curl http://localhost:8000/health/
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

| Метод | Путь      | Ответ               |
|-------|-----------|---------------------|
| GET   | /health/  | `{"status": "OK"}`  |
