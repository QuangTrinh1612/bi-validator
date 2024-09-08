import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the variables from the environment
TENANT_ID = os.getenv('TENANT_ID')
WORKSPACE_ID = os.getenv('WORKSPACE_ID')
WORKSPACE_NAME = os.getenv('WORKSPACE_NAME')
DATASET_ID = os.getenv('DATASET_ID')
DATASET_NAME = os.getenv('DATASET_NAME')

if not all([TENANT_ID, WORKSPACE_ID, WORKSPACE_NAME, DATASET_ID, DATASET_NAME]):
    raise EnvironmentError("Some environment variables are missing in the .env file")