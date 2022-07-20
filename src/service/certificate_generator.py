import imgkit
import os
import shutil
from src.utils.constants import CERTIFICATE_FOLDER_PATH,IMAGE_PATH

def generate_certificate(full_name, skill,level,certificate_template,certificate_folder_path=CERTIFICATE_FOLDER_PATH):
    """
        Generates a certificate for the user for a particular skill
        stores the certificate in the certificate folder
        :param full_name:
        :param skill:
        :param certficate_template:
        :return: returns boolean if the certificate was generated successfully or not

    """
    certificate_template = certificate_template(full_name=full_name, skill=skill, level=level) 
    #create a folder for the certificate
    if not os.path.exists(certificate_folder_path):
        os.makedirs(certificate_folder_path)

    #create a file name for the certificate
    file_name = "-".join(full_name.split(" "))+"_"+level+"_"+skill+".jpg"
    
    #create a config for the certificate
    config = imgkit.config(wkhtmltoimage=IMAGE_PATH)

    #create a certificate for the user
    ok = imgkit.from_string(certificate_template,f'{file_name}',config=config)
    
    #move the certificate to the certificate folder
    shutil.move(file_name,certificate_folder_path)

    #returns boolean if the certificate was generated successfully or not
    return ok,file_name
    

