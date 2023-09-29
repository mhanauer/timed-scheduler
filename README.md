# Azure ML Pipeline with Scheduled Execution

## Description

This Python script is used for creating, publishing, and scheduling a pipeline using Azure Machine Learning (Azure ML). The pipeline consists of two steps: one for data loading and another for data analysis. These are implemented as Python scripts (`data_loading.py` and `analysis.py` respectively).

## Prerequisites

- Azure subscription
- Azure ML workspace
- `.env` file containing required environment variables
- Python 3.x
- Dependencies listed in `requirements.txt`

## Setup

### Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required Python packages:


## Environment Variables

Create a `.env` file in the same directory as the script, and populate it with the following environment variables:

```bash
# Azure Subscription ID
subscription_id=YOUR_SUBSCRIPTION_ID

# Azure Resource Group
resource_group=YOUR_RESOURCE_GROUP

# Azure ML Workspace Name
workspace_name=YOUR_WORKSPACE_NAME

# Azure Tenant ID
tenant_id=YOUR_TENANT_ID

# Azure Client ID
client_id=YOUR_CLIENT_ID

# Azure Client Secret
client_secret=YOUR_CLIENT_SECRET
```

