from bi_validator.measure_retriever import retrieve_measures
from bi_validator.table_lineage import retrieve_table_lineage
from bi_validator.model_metadata import retrieve_model_metadata

def run_validation(dataset_id):
    print("Fetching measure values...")
    measures = retrieve_measures(dataset_id)
    print("Measures:", measures)
    
    print("\nExtracting table lineage...")
    lineage = retrieve_table_lineage(dataset_id)
    print("Table Lineage:", lineage)
    
    print("\nFetching model metadata...")
    metadata = retrieve_model_metadata(dataset_id)
    print("Model Metadata:", metadata)

if __name__ == "__main__":
    dataset_id = 'your-dataset-id'  # Replace with actual dataset ID
    run_validation(dataset_id)
