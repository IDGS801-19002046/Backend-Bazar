# Usar la imagen base de Python 3.12 slim
FROM python:3.12-slim

# Instalar dependencias del sistema necesarias para mysqlclient (usando MariaDB en lugar de MySQL)
RUN apt-get update && apt-get install -y \
    build-essential \
    libmariadb-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requerimientos (requirements.txt)
COPY requirements.txt .

# Crear el entorno virtual y activarlo
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install -r requirements.txt

# Agregar el entorno virtual al PATH para usar las dependencias de Python
ENV PATH="/opt/venv/bin:$PATH"

# Copiar el resto de los archivos de la aplicación
COPY . /app/

# Comando para ejecutar la aplicación Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
