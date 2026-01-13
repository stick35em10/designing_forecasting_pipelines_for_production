# Designing Forecasting Pipelines for Production

This repository contains the code and exercises for the book "Designing Forecasting Pipelines for Production".

## Project Structure

The repository is organized into chapters, each containing several exercises.

*   **Chapter 1: General Architecture** - Covers the basics of setting up a forecasting pipeline.
*   **Chapter 2: Experimentation** - Focuses on experimentation and backtesting.
*   **Chapter 3: Setting Automation** - (Content to be added)
*   **Chapter 4: From Deployment to Production** - Covers deploying and monitoring forecasting pipelines in a production environment. This chapter includes exercises on:
    *   Serving models with Flask.
    *   Monitoring for model drift.
    *   Best practices for development and scaling.

## Running the Code

The exercises can be run either directly using Python or within a Docker container.

### Using Python

To run the scripts directly, ensure you have the required packages installed:

```bash
pip install -r designing-forecasting-pipelines-for-production/chapter-4-From-Deployment-to-Production/requirements.txt
```

Then, you can run a specific script:

```bash
python designing-forecasting-pipelines-for-production/chapter-4-From-Deployment-to-Production/ex_7_model_drift/script.py
```

### Using Docker

To run the scripts in a containerized environment, you can use `docker-compose`. First, build the image:

```bash
cd designing-forecasting-pipelines-for-production/chapter-4-From-Deployment-to-Production
docker-compose build
```

Then, run a specific script:

```bash
docker-compose run --rm app python ex_7_model_drift/script.py
```