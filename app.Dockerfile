FROM python:3.12.2-slim-bullseye

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_ROOT_USER_ACTION=ignore

COPY requirements.txt .

RUN python -m pip install -U pip \
    && python -m pip install --no-cache-dir -r requirements.txt

COPY src ./src

EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]