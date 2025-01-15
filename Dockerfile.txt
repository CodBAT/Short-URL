# Используем официальный базовый образ Python
FROM python:3.8-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Указываем том для базы данных
VOLUME /app/data

# Запуск приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
