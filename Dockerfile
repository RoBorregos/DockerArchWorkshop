# Usamos una imagen ligera de Python
FROM python:3.9-slim

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos los requerimientos e instalamos las librerías
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código de la app
COPY . .

# Comando para ejecutar la aplicación Flask
CMD ["flask", "run", "--host=0.0.0.0"]