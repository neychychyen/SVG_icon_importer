# Используем базовый образ Ubuntu
FROM ubuntu:noble

# Устанавливаем зависимости


RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    imagemagick \
    potrace && \
    rm -rf /var/lib/apt/lists/*

# Рабочая директория в контейнере
WORKDIR /app

# Устанавливаем точку входа в контейнер
CMD ["python3", "main.py"]