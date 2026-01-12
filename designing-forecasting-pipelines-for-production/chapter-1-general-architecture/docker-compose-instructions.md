# How to run the script using Docker Compose

This document explains how to run the `script.py` file located in the `ex-5-Making-an-API-request` directory using Docker Compose.

## Prerequisites

- Docker
- Docker Compose

## Instructions

1.  **Navigate to the `1-general-architecture` directory:**

    ```bash
    cd 1-general-architecture
    ```

2.  **Run the `docker-compose up` command:**

    ```bash
    docker-compose up
    ```

    This command will:
    -   Build the Docker image based on the `ex-5-Making-an-API-request/Dockerfile`.
    -   Create and start a container based on that image.
    -   Run the `python script.py` command inside the container.
    -   The output of the script will be displayed in your terminal.

## Files

-   `docker-compose.yml`: This file defines the `api-requester` service, which runs the script. It is located in the `1-general-architecture` directory.
-   `ex-5-Making-an-API-request/Dockerfile`: This file defines the Docker image for the `api-requester` service. It uses a Python base image and copies the script into the container.
-   `ex-5-Making-an-API-request/.env`: This file should contain the environment variables required by the script, such as the `EIA_API_KEY`.
-   `ex-5-Making-an-API-request/script.py`: The Python script to be executed.

**Important Note on API Key:**
The `.env` file (located in the `1-general-architecture` directory) contains the `EIA_API_KEY`. Please ensure you replace `YOUR_API_KEY_HERE` with your actual EIA API key before running `docker-compose up`.
