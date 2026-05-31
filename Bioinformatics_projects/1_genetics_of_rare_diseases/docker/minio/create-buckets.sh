#!/bin/sh

sleep 10

mc alias set local http://minio:9000 minioadmin minioadmin

mc mb local/raw || true
mc mb local/processed || true
mc mb local/iceberg || true

echo "Buckets created successfully"