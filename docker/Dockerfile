FROM python:3.12-slim as builder

# Install uv
RUN pip install uv

# Set working directory
WORKDIR /app

# Copy dependency files and sync (without installing the code yet)
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project

# Copy project code and install it
COPY . .
RUN uv sync --frozen

# Final image
FROM python:3.12-slim

# Set DAGSTER_HOME to match docker-compose.yaml
ENV DAGSTER_HOME=/app/dagster_home
WORKDIR /app

COPY --from=builder /app /app
RUN mkdir -p $DAGSTER_HOME

EXPOSE 3000

# Default command (can be overridden in docker-compose)
CMD ["dagster", "webserver", "-h", "0.0.0.0", "-p", "3000"]