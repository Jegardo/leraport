from datetime import datetime, timedelta
from azure.storage.blob import BlobServiceClient, ContainerClient, generate_blob_sas, ContainerSasPermissions
from flask import current_app


def get_containers():
    conn_str = current_app.config['AZURE_STORAGE_CONNECTION_STRING']
    blob_service_client = BlobServiceClient.from_connection_string(conn_str)

    container_list = blob_service_client.list_containers()

    albums = []

    for album in container_list:
        albums.append(album.name)

    return albums


def get_img_names(container_name):
    conn_str = current_app.config['AZURE_STORAGE_CONNECTION_STRING']
    blob_service_client = BlobServiceClient.from_connection_string(conn_str)

    container_client = blob_service_client.get_container_client(container_name)

    blob_list = container_client.list_blobs()

    imgs = []

    for img in blob_list:
        imgs.append(img.name)

    return imgs


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

    blob_url = []

    blob_url[0] = f'https://{account_name}.blob.core.windows.net/{container_name}/{blob_name}'
    blob_url[1] = f'https://{account_name}.blob.core.windows.net/{container_name}/{blob_name}?{blob_sas_token}'

    return blob_url
