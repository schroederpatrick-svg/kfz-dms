# Base Image
FROM python:3.12-slim

# Arbeitsverzeichnis
WORKDIR /app

# Abhängigkeiten kopieren und installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# App-Code kopieren
COPY . .

# Environment-Variable für FastAPI
ENV PYTHONUNBUFFERED=1

# Port freigeben
EXPOSE 8000

# Startkommando
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
