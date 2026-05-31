from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("ClinVarIngestion")
    .getOrCreate()
)

df = spark.read.csv(
    "data/raw/clinvar_variants.tsv",
    sep="\t",
    header=True
)

print(df.count())

df.write.mode("overwrite").parquet(
    "data/processed/raw_variants"
)