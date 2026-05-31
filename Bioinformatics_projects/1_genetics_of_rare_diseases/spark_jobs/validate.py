from pyspark.sql import functions as F

from spark_jobs.config.spark_session import get_spark

spark = get_spark()

df = spark.read.parquet(
    "data/processed/raw_variants"
)

nulls = df.filter(
    F.col("variation_id").isNull()
).count()

print(f"Null variation IDs: {nulls}")

if nulls > 0:
    raise ValueError("Validation failed")

print("Validation passed")