#!/bin/bash
cd ../../

# Copy requirements.txt to a temporary location in the build context root
cp ex-1-Pipeline-architecture/ex_2_Defining_the_forecasting_pipeline/requirements.txt requirements.tmp.txt

# Append mlforecast to requirements.tmp.txt
echo "mlforecast" >> requirements.tmp.txt

# Modify Dockerfile to use the temporary requirements.txt
sed -i 's|ex-1-Pipeline-architecture/ex-2-Defining-the-forecasting-pipeline/requirements.txt|requirements.tmp.txt|g' Dockerfile

# Modify docker-compose.yml to set the full path to the script inside the container
sed -i 's|command: python ${SCRIPT_NAME}|command: python /app/ex-1-Pipeline-architecture/ex-3-Fitting-the-model/script.py|g' docker-compose.yml

# Run docker compose up --build
docker compose up --build

# Revert Dockerfile change
sed -i 's|requirements.tmp.txt|ex-1-Pipeline-architecture/ex-2-Defining-the-forecasting-pipeline/requirements.txt|g' Dockerfile

# Remove temporary requirements.txt
rm requirements.tmp.txt

# Revert docker-compose.yml change (optional, but good for idempotency)
sed -i 's|command: python /app/ex-1-Pipeline-architecture/ex-3-Fitting-the-model/script.py|command: python ${SCRIPT_NAME}|g' docker-compose.yml

cd -