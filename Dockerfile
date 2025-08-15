# Lightweight Python + uv image
FROM ghcr.io/astral-sh/uv:python3.12-bookworm

# Prevent Python from writing .pyc files and ensure stdout/stderr are unbuffered
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    HOST=0.0.0.0 \
    PORT=8080

WORKDIR /app

# Copy dependency metadata first for better Docker layer caching
COPY pyproject.toml uv.lock ./

# Install dependencies into a virtual environment managed by uv
RUN uv sync --frozen --no-cache

# Copy the rest of the application code
COPY . .

# Expose the HTTP port
EXPOSE 8080

# Use uv to run the app
CMD ["uv", "run", "app.py"]
