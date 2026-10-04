FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY calc.py db_ops.py str_ops.py ./
COPY tests ./tests

CMD ["python", "-m", "pytest", "tests"]
