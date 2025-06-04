# syntax=docker/dockerfile:1

FROM python:3.12-slim

# Install Poetry
RUN pip install --upgrade pip \
 && pip install poetry

# Set work directory
WORKDIR /app

# Copy only poetry files first to cache dependencies
COPY pyproject.toml poetry.lock* /app/

# Install dependencies
RUN poetry config virtualenvs.create false \
 && poetry install --no-root --only main

# Copy app code
COPY . /app
