# Use the requested production-ready minimal base image
FROM python:3.12-slim

# Set environment variables to optimize Python performance inside containers
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Establish the working directory inside the container
WORKDIR /app

# Copy the local script into the container workspace
COPY app.py .

# Run the script automatically upon container startup
CMD ["python", "app.py"]
