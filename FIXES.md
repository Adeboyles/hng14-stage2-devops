# Bug Fixes

## Fix 1 — frontend/app.js (Line 5)
**Problem:** API_URL hardcoded to localhost. Fails inside Docker containers.
**Fix:** Changed to `process.env.API_URL || "http://api:8000"`

## Fix 2 — api/main.py (Line 6)
**Problem:** Redis host hardcoded to localhost. Fails inside Docker containers.
**Fix:** Changed to `os.environ.get("REDIS_HOST", "redis")`

## Fix 3 — worker/worker.py (Line 5)
**Problem:** Redis host hardcoded to localhost. Fails inside Docker containers.
**Fix:** Changed to `os.environ.get("REDIS_HOST", "redis")`

## Fix 4 — worker/worker.py
**Problem:** signal module imported but never used. No graceful shutdown handling.
**Fix:** Added SIGTERM and SIGINT signal handlers.

## Fix 5 — api/requirements.txt
**Problem:** No pinned versions. Builds not reproducible.
**Fix:** Pinned fastapi==0.104.1, uvicorn==0.24.0, redis==5.0.1

## Fix 6 — worker/requirements.txt
**Problem:** No pinned versions.
**Fix:** Pinned redis==5.0.1
