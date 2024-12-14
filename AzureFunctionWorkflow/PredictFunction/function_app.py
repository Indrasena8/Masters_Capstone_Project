import azure.functions as func
import joblib
import logging
import os
from azure.storage.blob import BlobServiceClient

# Azure Blob Storage connection
BLOB_CONNECTION_STRING = "***********"
MODEL_CONTAINER = "models"
MODEL_BLOB = "model.pkl"

# Local paths for development (commented out for Azure usage)
# MODEL_FILE_PATH = "***/Project/SpamModelFunction/model.pkl"

MODEL_FILE_PATH = "/tmp/model.pkl"

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Ensure the model exists locally
        download_model()

        # Load the model
        model = joblib.load(MODEL_FILE_PATH)
        logging.info(f"Loaded model from {MODEL_FILE_PATH}.")

        # Get the input message
        data = req.get_json()
        message = data.get("message", "")

        if not message:
            return func.HttpResponse("No message provided.", status_code=400)

        # Predict if the message is spam or not
        prediction = model.predict([message])[0]

        return func.HttpResponse(f'{{"prediction": "{prediction}"}}', status_code=200)

    except Exception as e:
        logging.error(f"An error occurred in PredictFunction: {e}")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)

def download_model():
    """Download the model from Azure Blob Storage."""
    try:
        blob_service_client = BlobServiceClient.from_connection_string(BLOB_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=MODEL_CONTAINER, blob=MODEL_BLOB)
        with open(MODEL_FILE_PATH, "wb") as file:
            file.write(blob_client.download_blob().readall())
        logging.info(f"Downloaded {MODEL_BLOB} from {MODEL_CONTAINER} container.")
    except Exception as e:
        logging.error(f"Failed to download model: {str(e)}")
        raise
