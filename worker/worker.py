import redis
import time
import os
import signal
import sys

r = redis.Redis(host=os.environ.get("REDIS_HOST", "redis"), port=6379)

def handle_shutdown(signum, frame):
    print("Worker shutting down gracefully...")
    sys.exit(0)

signal.signal(signal.SIGTERM, handle_shutdown)
signal.signal(signal.SIGINT, handle_shutdown)

def process_job(job_id):
    print(f"Processing job {job_id}")
    time.sleep(2)  # simulate work
    r.hset(f"job:{job_id}", "status", "completed")
    print(f"Done: {job_id}")

while True:
    job = r.brpop("job", timeout=5)
    if job:
        _, job_id = job
        process_job(job_id.decode())
