import azure.functions as func
import pandas as pd
import joblib
import os
import logging
from azure.storage.blob import BlobServiceClient

# Azure Blob Storage connection
BLOB_CONNECTION_STRING = "**************"
DATASET_CONTAINER = "dataset"
MODEL_CONTAINER = "models"
DATASET_BLOB = "spam.csv"
MODEL_BLOB = "model.pkl"

# Local paths for development (commented out for Azure usage)
# DATASET_PATH = "***/Project/spam.csv"
# MODEL_FILE_PATH = "***/Project/SpamModelFunction/model.pkl"

MODEL_FILE_PATH = "/tmp/model.pkl"
DATASET_PATH = "/tmp/spam.csv"

def main(timer: func.TimerRequest):
    try:
        logging.info("RetrainFunction triggered by TimerTrigger.")
        
        # Download dataset from Azure Blob Storage
        download_dataset()

        # Preview the dataset
        if os.path.exists(DATASET_PATH):
            logging.info(f"Dataset exists at {DATASET_PATH}. File size: {os.path.getsize(DATASET_PATH)} bytes.")
            data_preview = pd.read_csv(DATASET_PATH).head()
            logging.info(f"Preview of spam.csv data: \n{data_preview}")
        else:
            logging.error(f"Dataset not found at {DATASET_PATH}.")
            return

        # Retrain the model
        retrain_model(DATASET_PATH)

        # Upload the trained model to Azure Blob Storage
        upload_model()

    except Exception as e:
        logging.error(f"An error occurred in RetrainFunction: {str(e)}")
        raise

def download_dataset():
    """Download the dataset from the Azure Blob Storage container."""
    try:
        blob_service_client = BlobServiceClient.from_connection_string(BLOB_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=DATASET_CONTAINER, blob=DATASET_BLOB)
        with open(DATASET_PATH, "wb") as file:
            file.write(blob_client.download_blob().readall())
        logging.info(f"Downloaded {DATASET_BLOB} from {DATASET_CONTAINER} container.")
    except Exception as e:
        logging.error(f"Failed to download dataset: {str(e)}")
        raise

def retrain_model(dataset_path):
    """Retrains the model using the updated spam.csv dataset."""
    try:
        data = pd.read_csv(dataset_path, usecols=["v1", "v2"])
        data.columns = ["label", "message"]  # Rename columns for consistency

        logging.info(f"Columns in spam.csv: {data.columns.tolist()}")

        X = data["message"]
        y = data["label"]

        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.naive_bayes import MultinomialNB
        from sklearn.pipeline import make_pipeline

        model = make_pipeline(CountVectorizer(), MultinomialNB())
        model.fit(X, y)

        # Save the trained model locally
        joblib.dump(model, MODEL_FILE_PATH)
        logging.info(f"Model retrained and saved locally at {MODEL_FILE_PATH}.")

    except Exception as e:
        logging.error(f"Failed to retrain the model: {str(e)}")
        raise

def upload_model():
    """Uploads the model to Azure Blob Storage."""
    try:
        blob_service_client = BlobServiceClient.from_connection_string(BLOB_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=MODEL_CONTAINER, blob=MODEL_BLOB)
        with open(MODEL_FILE_PATH, "rb") as model_file:
            blob_client.upload_blob(model_file, overwrite=True)
        logging.info(f"Uploaded {MODEL_BLOB} to {MODEL_CONTAINER} container.")
    except Exception as e:
        logging.error(f"Failed to upload model: {str(e)}")
        raise
