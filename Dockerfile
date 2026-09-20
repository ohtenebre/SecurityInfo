FROM python:3.10-slim
WORKDIR /app
RUN pip install --no-cache-dir numpy
COPY . .
ENV PYTHONUNBUFFERED=1
CMD ["python", "main.py"]
