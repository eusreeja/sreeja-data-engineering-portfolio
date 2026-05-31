import networkx as nx

from spark_jobs.config.spark_session import get_spark

spark = get_spark()

df = spark.read.parquet(
    "data/processed/curated_variants"
)

pairs = (
    df.select(
        "GeneSymbol",
        "DiseaseName"
    )
    .distinct()
    .collect()
)

G = nx.Graph()

for row in pairs:
    G.add_edge(
        row["GeneSymbol"],
        row["DiseaseName"]
    )

print(
    f"Nodes: {len(G.nodes())}"
)

print(
    f"Edges: {len(G.edges())}"
)