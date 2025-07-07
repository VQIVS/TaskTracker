FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-dev

COPY . .

EXPOSE 8000
CMD ["uvicorn", "cmd.main:app", "--host", "0.0.0.0", "--port", "8000"]
