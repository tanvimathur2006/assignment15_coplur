# Dockerized Python Version and Timestamp Printer

A minimal, Dockerized Python application based on `python:3.12-slim`. It prints out the container's execution timestamp along with its operational Python version.

## Prerequisites
* [Docker Desktop](
    https://docs.docker.com/
    ) installed and running.
* [Git](https://git-scm.com) installed.

## How to Build and Run

### 1. Clone the Repository
```bash
git clone <repository link>
```

### 2. Build the Docker Image
Compile the blueprint into a local container image:
```bash
docker build -t assignment15_coplur .
```

### 3. Run the Container
Instantiate and run the isolated app process:
```bash
docker run --rm assignment15_coplur
```

## Sample Output Screenshot
Below is the terminal output displayed upon running the built container architecture:

```text
==================================================
      DOCKERIZED PYTHON APPLICATION REPORT      
==================================================
Current Date and Time : 2026-06-20 16:01:22
Running Python Version : 3.12.12
Full Environment Info  : 3.12.12 (main, Oct 24 2025, 14:32:11) [GCC 12.2.0]
==================================================
```
