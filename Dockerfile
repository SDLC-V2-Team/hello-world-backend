FROM python:3.11-slim AS base

WORKDIR /app

# Copy only the necessary file
COPY main.py .

# Run the application
CMD ["python", "main.py"]
