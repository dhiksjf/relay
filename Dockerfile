# ── Relay Drive — Koyeb-ready Dockerfile ─────────────────
#
# Deploy on Koyeb (free, no CC):
#   1. Push server.py + requirements.txt + Dockerfile to GitHub
#   2. Koyeb → New Service → GitHub → select repo
#   3. Builder: Dockerfile  |  Port: 8000
#   4. Environment variables:
#        SECRET_KEY     = any_random_string_at_least_32_chars
#        ENCRYPTION_KEY = any_random_string_at_least_32_chars
#   5. Click Deploy ✓
#
# The app auto-creates SQLite DB at /app/data/relay_drive.db
# Note: free tier filesystem resets on redeploy. Mount a volume
# at /app/data for persistence (Koyeb paid), or use Turso (free).

FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libffi-dev libssl-dev openssh-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install deps first (cached Docker layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .

RUN mkdir -p /app/data

ENV DB_PATH=/app/data/relay_drive.db \
    SECRET_KEY=change_me_use_a_long_random_string \
    ENCRYPTION_KEY=change_me_use_a_different_long_random_string

EXPOSE 8000

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
