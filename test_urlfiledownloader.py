"""Test Module for UrlFileDownloader class"""
import os
import unittest

from urlfiledownloader import UrlFileDownloader

class UrlFileDownloaderTest(unittest.TestCase):
    """Test class for UrlFileDownloader class"""
    url = ''.join(["https://raw.githubusercontent.com/google/",
                   "dspl/master/datasets/us_census/",
                   "retail_sales/retail_sales_business.csv"])
    dest_path = "./g-sample-data"
    file_path = "./g-sample-data/retail_sales_business.csv.gz"
    sha_file_name = "./g-sample-data/.retail_sales_business.csv.sha256"

    def test_urlfiledownload(self):
        """Test case for UrlFileDownloader"""
        self.assertFalse(os.path.isdir(self.dest_path))
        ufd = UrlFileDownloader(self.url, self.dest_path)
        self.assertTrue(os.path.isdir(self.dest_path))
        self.assertTrue(ufd.file_path == self.file_path)
        self.assertTrue(ufd.sha_file_name == self.sha_file_name)
        ufd.downloadfile()
        ufd.printsha()
        os.remove(self.file_path)
        os.remove(self.sha_file_name)
        os.rmdir(self.dest_path)

if __name__ == '__main__':
    unittest.main()
