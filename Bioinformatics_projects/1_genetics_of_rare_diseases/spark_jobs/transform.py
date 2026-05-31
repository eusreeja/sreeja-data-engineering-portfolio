from pyspark.sql import functions as F

from spark_jobs.config.spark_session import get_spark

spark = get_spark()

df = spark.read.parquet(
    "data/processed/raw_variants"
)

curated = (
    df
    .filter(
        F.col("ClinicalSignificance").isNotNull()
    )
    .withColumn(
        "clinical_significance",
        F.upper(
            F.col("ClinicalSignificance")
        )
    )
)

curated.write.mode("overwrite").parquet(
    "data/processed/curated_variants"
)