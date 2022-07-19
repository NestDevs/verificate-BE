import os
from pathlib import Path

# Path to the folder where the certificates are stored
CERTIFICATE_FOLDER_PATH = os.path.join(os.path.dirname(__file__).replace("\\utils",""), 'certificates')

# windows machine path to the wkhtmltoimage(specific)
IMAGE_PATH = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe"

# Pinata api url
PINATA_URL_PIN_FILE = "https://api.pinata.cloud/pinning/pinFileToIPFS"

# Pinata api retrieval url
PINATA_URL_GET_FILE = "https://gateway.pinata.cloud/ipfs"

