Every disease leaves clues in our DNA. This project uses Apache Spark to process public genomic datasets and uncover relationships between genes, mutations, and human diseases at scale.


# Mapping the Genetic Landscape of Human Disease with Apache Spark

## Overview

This project analyzes public genomic datasets from ClinVar to discover relationships between genes, variants, and diseases using Apache Spark.

## Technologies

- Apache Spark
- Docker
- MinIO (S3)
- Great Expectations
- PostgreSQL
- Pandas
- NetworkX

## Architecture

![Architecture](architecture/architecture.png)

## Insights Generated

- Top disease-associated genes
- Pathogenic variant distribution
- Disease similarity analysis
- Gene-disease network analysis

## Run

```bash
docker compose up -d
python spark_jobs/ingest.py
python spark_jobs/validate.py
python spark_jobs/transform.py





## Project Flow

ClinVar TSV
      |
      v
raw bucket
      |
      v
Spark Ingestion
      |
      v
Great Expectations Validation
      |
      v
Transformations
      |
      v
processed bucket
      |
      v
Disease Analytics
Gene Network Analytics
Pathogenic Variant Analytics





## Commands to Run

Start environment:

cd docker

docker compose up -d

Verify:

MinIO Console:

http://localhost:9001

Login:

username: minioadmin
password: minioadmin

Postgres:

psql -h localhost -U iceberg -d iceberg_catalog

Spark container:

docker exec -it spark-bioinformatics bash

