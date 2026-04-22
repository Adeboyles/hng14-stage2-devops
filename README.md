# HNG Stage 2 DevOps — Microservices Job Processor

A containerized job processing system with a full CI/CD pipeline.

## Services
- **Frontend** (Node.js) — Job submission UI on port 3000
- **API** (Python/FastAPI) — Job creation and status on port 8000
- **Worker** (Python) — Processes jobs from Redis queue
- **Redis** — Shared message queue

## Prerequisites
- Docker Desktop installed and running
- Docker Compose v2+
- Git

## How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/Adeboyles/hng14-stage2-devops.git
cd hng14-stage2-devops
```

### 2. Start the stack
```bash
docker compose up --build
```

### 3. Verify it's running
```bash
docker compose ps
```

### 4. Test the endpoints
```bash
# Submit a job
curl -X POST http://localhost:3000/submit

# Check job status
curl http://localhost:3000/status/<job_id>
```

### 5. Successful startup looks like
- redis: Healthy
- api: Healthy
- worker: running
- frontend: running on port 3000

## Tear Down
```bash
docker compose down
```
