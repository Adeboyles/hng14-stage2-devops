FROM python:3.11-alpine AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

FROM python:3.11-alpine
WORKDIR /app
RUN adduser --disabled-password --no-create-home appuser
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY worker.py .
RUN chown -R appuser:appuser /app
USER appuser
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import redis, os; r = redis.Redis(host=os.environ.get('REDIS_HOST','redis')); r.ping()"
CMD ["python", "worker.py"]
