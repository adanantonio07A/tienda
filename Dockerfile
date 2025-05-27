# 1. Imagen base con Python
FROM python:3.11-slim

# 2. Establecer el directorio de trabajo
WORKDIR /app

# 3. Copiar los archivos de requisitos y luego instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar todo el proyecto
COPY . .

# 5. Exponer el puerto donde correrá la app (FastAPI usa 8000 por defecto)
EXPOSE 8000

# 6. Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
