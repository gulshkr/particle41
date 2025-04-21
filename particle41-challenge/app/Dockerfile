# Use official Python slim image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Create a non-root user
RUN useradd -m -u 1001 appuser

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies as root
RUN pip install --no-cache-dir -r requirements.txt

# Switch to non-root user
USER appuser

# Copy application code
COPY --chown=appuser:appuser . .

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "main.py"]