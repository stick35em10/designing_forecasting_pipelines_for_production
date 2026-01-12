FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y libgomp1
# Copy and install requirements from ex-5
COPY ex-5-Making-an-API-request/requirements.txt /app/ex-5-reqs.txt
RUN pip install -r /app/ex-5-reqs.txt

# Copy and install requirements from ex-6
COPY ex-6-Preparing-and-visualizing-the-data/requirements.txt /app/ex-6-reqs.txt
RUN pip install -r /app/ex-6-reqs.txt

# Copy and install requirements from ex-9
COPY ex-8-Working-with-a-forecast-object/ex-9-Forecasting-with-ML-Models/requirements.txt /app/ex-9-reqs.txt
RUN pip install -r /app/ex-9-reqs.txt

# Copy the rest of the code
COPY . .
