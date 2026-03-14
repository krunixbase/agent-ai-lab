# ---------- Stage 1: builder ----------
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .
COPY pyproject.toml .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ---------- Stage 2: runtime ----------
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

WORKDIR /app

# Create non-root user
RUN useradd -m appuser

# Copy installed dependencies
COPY --from=builder /install /usr/local

# Copy application code
COPY src ./src

# Give permissions to the user
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

EXPOSE 8000

CMD ["uvicorn", "src.api.api:app", "--host", "0.0.0.0", "--port", "8000"]

