import os
import sys
import time
from json import load as jsonLoad
from datetime import datetime, timedelta
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions


def load_parameters():
    """
    Loads the parameters JSON into a dictionary.
    It should be called 'parameters.json' in the same folder as this script.
    :return: dictionary containing the desired run parameters
    """
    this_dir = os.path.dirname(os.path.abspath(__file__))
    with open(this_dir + "/parameters.json") as confiFile:
        return jsonLoad(confiFile)


def extract_key(connection_string):
    """
    Extracts the account key from the given connect string.
    :param connection_string: the connect string to the storage account
    :return: the account key
    """
    keys = connection_string.split(';')
    key_name = "AccountKey="
    key_line = next((k for k in keys if k.startswith(key_name)), key_name)
    key = key_line.split(key_name)[1]
    return key


def create_blobs(number):
    """
    Creates a number of text blobs in a new sub folder.
    :param number: The number of blobs to create.
    :return: tuple: result of the run, and path to the created directory.
    """
    this_dir = os.path.dirname(os.path.abspath(__file__))
    dest = os.path.join(this_dir, f"blobs{int(time.time())}")  # time stamps assure a safe, unique destination
    res = os.system(f"powershell.exe -file blobber.ps1 {number} {dest}")
    return res, dest


def upload_dir_to_storage(blobs_dir, connection_string, container_name):
    """
    Uploads all blobs inside the given directory to the given storage account.
    Each blob will be deleted after its upload.
    :param blobs_dir: The path to the directory to upload.
    :param connection_string: the connection string to the storage account to upload to.
    :param container_name: the name of the destination container in the desired storage account
    """
    with BlobServiceClient.from_connection_string(connection_string) as service_client:
        # Using With to validate safe exit
        with service_client.get_container_client(container_name) as client:
            # Using With to validate safe exit
            print("Uploading starting...")
            for blob in os.listdir(blobs_dir):
                blob_full_path = os.path.join(blobs_dir, blob)
                with open(blob_full_path) as blob_file:
                    client.upload_blob(name=blob, data=blob_file.read(), overwrite=True)
                print(f"{blob} uploaded successfully.")
                os.remove(blob_full_path)
    print()


def copy_blobs(src_storage, dst_storage):
    """
    copies all blobs from the source storage into the destination storage
    :param src_storage: dictionary representing the source storage
    :param dst_storage: dictionary representing the destination storage. Each dictionary should
    contain two values: {'connectionString':'<connection string>', 'containerName':'<container name>'}
    :return:
    """
    src_storage_client = BlobServiceClient.from_connection_string(src_storage['connectionString'])
    src_container = src_storage_client.get_container_client(src_storage['containerName'])

    dst_storage_client = BlobServiceClient.from_connection_string(dst_storage['connectionString'])
    dst_container = dst_storage_client.get_container_client(dst_storage['containerName'])

    src_account_key = extract_key(src_storage['connectionString'])
    print(f"Attempting to copy BLOBs from {src_storage_client.account_name} to {dst_storage_client.account_name}...")
    try:
        for blob in src_container.list_blobs():
            src_blob = src_container.get_blob_client(blob.name)
            new_blob = dst_container.get_blob_client(blob.name)

            sasToken = generate_blob_sas(
                account_name=src_blob.account_name,
                container_name=src_blob.container_name,
                blob_name=blob.name,
                account_key=src_account_key,
                permission=BlobSasPermissions(*([True] * 7)),
                expiry=datetime.utcnow() + timedelta(hours=1)
            )

            new_blob.start_copy_from_url(src_blob.url + "?" + sasToken)
            print(f"{blob.name:>15} was copied successfully.")

        print("\nAll Blobs were copied successfully.")
    except Exception as e:
        print(e)
    finally:
        # clean exit
        dst_container.close()
        dst_storage_client.close()
        #
        src_container.close()
        src_storage_client.close()


params = load_parameters()  # load parameters
res, blobs_dir = create_blobs(params["blobsCount"])
if res != 0:
    print("Failed in creating blobs. Terminating...")
    sys.exit(1)

storage1 = params['storage1']
storage2 = params['storage2']

upload_dir_to_storage(blobs_dir, storage1['connectionString'], storage1['containerName'])
os.rmdir(blobs_dir)
copy_blobs(src_storage=storage1, dst_storage=storage2)
