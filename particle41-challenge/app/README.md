# SimpleTimeService

A minimal microservice that returns current timestamp and client IP in JSON format.

## Features

- Returns UTC timestamp in ISO format
- Detects client IP address (works behind proxies)
- Runs as non-root user in container
- Small container footprint (~50MB)
- Production-ready with Gunicorn server

## Quick Start

### Prerequisites

- Docker installed

### Running the Service

1. Build the container:
```bash
docker build -t simple-time-service ./app
```
2.Run the container:
```
docker run -d -p 5000:5000 --name time-service simple-time-service
```
3. Verify it's working:
```
curl http://localhost:5000
```
