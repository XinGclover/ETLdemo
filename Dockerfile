
# Använd en officiell, lättviktig Python-image
FROM python:3.11-slim

# Sätt arbetskatalogen i containern
WORKDIR /app

# Kopiera in koden och datan till containern
COPY main.py .
COPY data/ ./data/

# Säkerställ att Python-loggar skrivs ut direkt i terminalen utan buffring
ENV PYTHONUNBUFFERED=1

# Kommandot som körs när containern startar
CMD ["python", "main.py"]