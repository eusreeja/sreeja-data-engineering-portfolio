from pyspark.sql import functions as F

from spark_jobs.config.spark_session import get_spark

spark = get_spark()

df = spark.read.parquet(
    "data/processed/curated_variants"
)

result = (
    df.groupBy("DiseaseName")
    .agg(
        F.countDistinct("VariationID")
        .alias("variant_count")
    )
    .orderBy(
        F.desc("variant_count")
    )
)

result.show(20, False)