# ── Relay Drive — single-file Dockerfile ──────────────────
# Works out-of-the-box on Koyeb:
#   1. Push to GitHub
#   2. New Service → GitHub → select repo
#   3. Builder: Dockerfile
#   4. Port: 8000
#   5. Add env vars: SECRET_KEY, ENCRYPTION_KEY (optional: DB_PATH)
#   6. Deploy ✓

FROM python:3.11-slim

# System deps for paramiko / cryptography
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libffi-dev libssl-dev openssh-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python deps first (cached layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the single source file
COPY server.py .

# SQLite DB lives inside the container at /app/data/
# On Koyeb free tier the filesystem resets on redeploy.
# To persist data across redeploys, mount a volume at /app/data
# or set DB_PATH to a persistent volume path.
ENV DB_PATH=/app/data/relay_drive.db \
    SECRET_KEY=change_me_in_koyeb_env \
    ENCRYPTION_KEY=change_me_in_koyeb_env

RUN mkdir -p /app/data

EXPOSE 8000

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
