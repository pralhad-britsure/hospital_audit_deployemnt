import os
import paramiko
from dotenv import load_dotenv

load_dotenv()

SFTP_HOST = os.getenv("SFTP_HOST")
SFTP_USERNAME = os.getenv("SFTP_USERNAME")
SFTP_PASSWORD = os.getenv("SFTP_PASSWORD")
SFTP_BASE_PATH = os.getenv("SFTP_BASE_PATH")


def upload_file_to_sftp(file_data, remote_path: str):
    transport = paramiko.Transport((SFTP_HOST, 22))
    transport.connect(username=SFTP_USERNAME, password=SFTP_PASSWORD)
    sftp = paramiko.SFTPClient.from_transport(transport)

    try:
        # Ensure remote folders exist
        dirs = remote_path.strip("/").split("/")[:-1]
        current_path = ""
        for d in dirs:
            current_path += "/" + d
            try:
                sftp.listdir(current_path)
            except IOError:
                sftp.mkdir(current_path)

        # Upload file
        with sftp.open(remote_path, "wb") as f:
            f.write(file_data)
    finally:
        sftp.close()
        transport.close()
