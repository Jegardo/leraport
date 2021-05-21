from datetime import datetime, timedelta
from azure.storage.blob import generate_blob_sas, ContainerSasPermissions
from flask import current_app


def get_img_url(blob_name, container_name):
    account_name = current_app.config['AZURE_NAME']
    account_key = current_app.config['AZURE_STORAGE_KEY']
    blob_sas_token = generate_blob_sas(
        account_name=account_name,
        container_name=container_name,
        blob_name=blob_name,
        account_key=account_key,
        permission=ContainerSasPermissions(read=True),
        expiry=datetime.utcnow() + timedelta(hours=1))
    blob_url = f'https://{account_name}.blob.core.windows.net/{container_name}/{blob_name}?{blob_sas_token}'
    return blob_url
