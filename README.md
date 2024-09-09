<h1>
    <img
        src="assets\logo.svg"
        alt="BI Validator logo"
        height=50
    />
    BI Validator
</h1>

## Table of contents
- [Summary](#summary)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#installation)
- [Configuration](#configuration)
- [Running test](#running-tests)
- [Contributing](#contributing)
- [License](#license)
- [How to use](#how-to-use)

## Summary

BI Validator is a Python tool designed to interact with Power BI service, enabling users to retrieve measure values, extract table lineage, and gather model metadata. It automates the process of validating and extracting key data from Power BI models for business intelligence tasks.

## Features

- **Measure Retrieval**: Fetch measure values from Power BI datasets.
- **Table Lineage Extraction**: Track the lineage of tables within Power BI datasets, ensuring clarity of data flow and relationships.
- **Model Metadata**: Retrieve metadata such as table definitions, relationships, and measures.
- **Power BI Service Integration**: Directly interacts with Power BI service to retrieve data via its API.

## Project Structure
```
BI_Validator/
│
├── bi_validator/
│   ├── __init__.py                # Initialize the package
│   ├── powerbi_service.py         # Handles interaction with Power BI service
│   ├── measure_retriever.py       # Retrieves measure values
│   ├── table_lineage.py           # Extracts table lineage
│   ├── model_metadata.py          # Retrieves metadata of the model
│   ├── config.py                  # Configuration settings (e.g., API keys, endpoints)
│   └── utils.py                   # Utility functions (e.g., logging, error handling)
│
├── tests/
│   ├── test_powerbi_service.py    # Unit tests for Power BI service interactions
│   ├── test_measure_retriever.py  # Unit tests for measure retrieval
│   ├── test_table_lineage.py      # Unit tests for table lineage extraction
│   ├── test_model_metadata.py     # Unit tests for model metadata retrieval
│
├── scripts/
│   └── run_validator.py           # Script to run the validation process end-to-end
│
├── docs/
│   └── README.md                  # Project documentation and how to use it
│
├── requirements.txt               # List of project dependencies
├── setup.py                       # For package installation
└── .gitignore                     # Files to be ignored by Git
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/QuangTrinh1612/BI_Validator.git
```

2. Navigate to the project directory:

```bash
cd BI_Validator
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Configure your Power BI API credentials in the `bi_validator/config.py` file.

## Usage
Run the validation script to retrieve measure values, table lineage, and model metadata:

```bash
python scripts/run_validator.py
```

The script will execute the entire validation process, fetching data from your Power BI service and outputting results.

## Example
To fetch measure values, you can run the following:

```bash
from bi_validator.measure_retriever import retrieve_measures

measures = retrieve_measures(dataset_id='<<your_dataset_id>>')
print(measures)
```

## Configuration
You need to configure the Power BI API settings in the `bi_validator/config.py` file. Example configuration:

```python
# config.py
POWER_BI_API_URL = 'https://api.powerbi.com/v1.0/myorg/'
CLIENT_ID = 'your-client-id'
CLIENT_SECRET = 'your-client-secret'
TENANT_ID = 'your-tenant-id'
```

## Running Tests
You can run the tests using `pytest`:

```bash
pytest tests/
```

## Contributing
Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License.

## How to Use
- Replace `your-client-id`, `your-client-secret`, `your-tenant-id` with actual values.
- Adjust URLs and configurations as needed based on your environment. 

This `README.md` provides all necessary steps for setup, configuration, and running the project.
