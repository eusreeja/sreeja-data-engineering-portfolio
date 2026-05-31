from pyspark.sql import functions as F

from spark_jobs.config.spark_session import get_spark

spark = get_spark()

df = spark.read.parquet(
    "data/processed/curated_variants"
)

pathogenic = (
    df.filter(
        F.col(
            "clinical_significance"
        ).contains("PATHOGENIC")
    )
)

result = (
    pathogenic
    .groupBy("Chromosome")
    .count()
    .orderBy(F.desc("count"))
)

result.show()