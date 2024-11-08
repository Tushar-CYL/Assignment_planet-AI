from datasets import load_dataset

ds = load_dataset("charles828/vertex-ai-customer-support-training-dataset")

def collect_datasets():
    datasets = [
        {
            "name": "Customer Support on Twitter",
            "link": "datasets\twcs.csv",
            "description": "Dataset for customer interaction on Twitter"
        },
        {
            "name": "Customer Support Data",
            "link": ds,
            "description": "Dataset for general customer support interactions"
        },
    ]
    
    # Save datasets
    with open("results/datasets_links.md", "w") as f:
        for dataset in datasets:
            f.write(f"- **{dataset['name']}**: {dataset['link']} - {dataset['description']}\n")

if __name__ == "__main__":
    collect_datasets()
