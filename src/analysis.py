import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from azureml.core import Workspace, Dataset, Model
from azureml.core.authentication import ServicePrincipalAuthentication
import joblib
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

def fun_model_azure_load(model_name, version="None"):
    """Loads a model from azure ml.

    Args:
        model_name (str): Model name
        version (str, optional): Version number.  If none takes the latest model. Defaults to "None".

    Returns:
        Model: Model that can be used to make predictions.
    """
    if version == "None":
        test_model = Model(workspace=workspace, name=model_name)
        test_model_path = test_model.get_model_path(
            model_name=model_name, _workspace=workspace
        )
    else:
        test_model = Model(workspace=workspace, version=version, name=model_name)
        test_model_path = test_model.get_model_path(
            model_name=model_name, version=version, _workspace=workspace
        )
    test_model_path_model = test_model_path + "/" + "model.pkl"
    model = joblib.load(test_model_path_model)
    return model

model_scheduler = fun_model_azure_load(model_name="compose_scheduler")

y_pred = model_scheduler.predict(data_scheduler)
y_pred = pd.DataFrame(y_pred).rename(columns={0: "retention_predictions"})
print(y_pred.head())

ds = Dataset.Tabular.register_pandas_dataframe(
    dataframe=y_pred,
    name="data_retention_predictions",
    description="Retention predictions",
    target=datastore,
)