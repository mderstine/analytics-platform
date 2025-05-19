FROM python:3.12-slim

# Install uv for dependency management
RUN pip install uv

WORKDIR /app

# Copy dependency files
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen

# Copy the rest of the code
COPY . .

# Set DAGSTER_HOME (adjust if needed)
ENV DAGSTER_HOME=/app/dagster_home
RUN mkdir -p $DAGSTER_HOME

EXPOSE 4000

# Default command: start Dagster gRPC server for code location
CMD ["dagster", "api", "grpc", "-h", "0.0.0.0", "-p", "4000", "-f", "repository.py"]