from pydantic import BaseModel


class VariantRecord(BaseModel):
    variation_id: str
    gene_symbol: str
    chromosome: str
    clinical_significance: str