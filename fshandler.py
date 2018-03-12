import tempfile
import shutil
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class FsHandler:
    def __init__(self, drive=True):
        self.dirpath = tempfile.mkdtemp()
        if drive:
            gauth = GoogleAuth()
            self.drive = GoogleDrive(gauth)
    def get_path(self):
        return self.dirpath

    def remove(self):
        shutil.rmtree(self.dirpath)

    def upload(self, folder_name, drive_parent=''):
        lookup_table={}
        lookup_table[self.dirpath] = self._drive_create_folder(folder_name, drive_parent)
        print lookup_table
        for root, dirs, files in os.walk(self.dirpath):
            for dir in dirs:
                print 'create', dir, '@', root
                lookup_table[os.path.join(root, dir)] = self._drive_create_folder(dir, lookup_table[root])
            for file in files:
                print 'create', file, '@', root
                self._drive_create_file(os.path.join(root, file), lookup_table[root])

    def _drive_create_folder(self, name, parent=''):
        properties = {
            'title': name,
            'mimeType': 'application/vnd.google-apps.folder',
        }

        if parent:
            properties['parents'] = [{'kind': "drive#childList", "id": parent}]

        f = self.drive.CreateFile(properties)
        f.Upload()
        return f['id']

    def _drive_create_file(self, file_path, parent=''):
        file_name = os.path.basename(file_path)
        properties = {
            'title': file_name,
        }

        if parent:
            properties['parents'] = [{'kind': "drive#childList", "id": parent}]

        f = self.drive.CreateFile(properties)
        f.SetContentFile(file_path)
        f.Upload()
        return f['id']
