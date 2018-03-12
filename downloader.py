import requests
import os


class Downloader:
    def __init__(self):
        pass

    @staticmethod
    def download(url, file_path):
        r = requests.get(url, stream=True)
        with open(file_path, 'wb') as fd:
            for chunk in r.iter_content(10):
                fd.write(chunk)

    @staticmethod
    def downloadList(fileList, basePath):
        for entry in fileList:
            file_path = os.path.join(basePath, entry['path'])
            if not os.path.exists(os.path.dirname(file_path)):
                os.makedirs(os.path.dirname(file_path))
            Downloader.download(entry['url'], file_path)
