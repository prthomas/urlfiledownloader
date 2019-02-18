"""This module implements UrlFileDownloader class"""
import gzip
import hashlib
import os
import requests

class UrlFileDownloader:
    """This class accepts two arguments url and dest_path"""
    def __init__(self, url, dest_path):
        """
        Initialize UrlFileDownloader object
          Download `url` into local path `dest_file` on downloadfile()
          Make `dest_path` directory if it does not exist
          if `dest_path`/.`file_name`.sha256 file exists read the message digest
        """
        self.url = url
        self.dest_path = dest_path
        self.file_name = self.url.split('/')[-1]
        self.file_path = f"{self.dest_path}/{self.file_name}.gz"
        self.sha_file_name = f"{self.dest_path}/.{self.file_name}.sha256"
        print(self.sha_file_name)
        self.sha256 = ""
        if not os.path.exists(self.dest_path):
            os.makedirs(self.dest_path)
        else:
            if os.path.exists(self.sha_file_name):
                with open(self.sha_file_name, 'rb') as shafile:
                    self.sha256 = shafile.read()

    def downloadfile(self):
        """
        Method downloadfile will download file and gzip it
        Open a stream to load file from url, use the stream to gz and store
        into local file and calculate the sha256 message digest.
        Compare with earlier message digest to identify if the file has been
        updated.
        """
        req = requests.get(self.url, stream=True)
        mdsha256 = hashlib.sha256()
        with gzip.open(self.file_path, "wb") as gfile:
            for line in req.iter_lines():
                if line:
                    gfile.write(line + b"\n")
                    mdsha256.update(line + b"\n")

        with open(self.sha_file_name, "wb") as sfile:
            sfile.write(mdsha256.digest())

        sha256 = mdsha256.digest()
        if self.sha256 != sha256:
            self.sha256 = sha256
            print("File updated!")
        else:
            print("File not updated!")

    def printsha(self):
        """Method to display file's message digest"""
        print(self.sha256.hex())

if __name__ == '__main__':
    MAIN_URL = ''.join(["https://raw.githubusercontent.com/google/",
                        "dspl/master/datasets/us_census/",
                        "retail_sales/retail_sales_business.csv"])
    MAIN_DEST_PATH = "./data"
    UFD = UrlFileDownloader(MAIN_URL, MAIN_DEST_PATH)
    UFD.downloadfile()
    UFD.printsha()
