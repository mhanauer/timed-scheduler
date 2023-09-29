import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from azureml.core import Workspace, Dataset
from azureml.core.authentication import ServicePrincipalAuthentication

from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Retrieve variables
subscription_id = os.getenv("subscription_id")
resource_group = os.getenv("resource_group")
workspace_name = os.getenv("workspace_name")
tenant_id = os.getenv("tenant_id")
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")

svc_pr = ServicePrincipalAuthentication(
    tenant_id=tenant_id,
    service_principal_id=client_id,
    service_principal_password=client_secret,
)

# Access the workspace
workspace = Workspace(
    subscription_id=subscription_id,
    resource_group=resource_group,
    workspace_name=workspace_name,
    auth=svc_pr,
)

datastore = workspace.get_default_datastore()

data_set = Dataset.get_by_name(workspace, name="data_scheduler")
data_scheduler = data_set.to_pandas_dataframe().drop(columns=["retention"])
print(data_scheduler.head())
