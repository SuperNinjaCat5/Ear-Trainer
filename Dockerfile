FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . /app

# Expose the port expected by Coolify / requested by user
EXPOSE 3000

# Run Gunicorn on port 3000, 4 workers
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:3000", "app:app"]
