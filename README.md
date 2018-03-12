# Download to GoogleDrive

This script lets you download files and will then upload them to GoogleDrive.

## Setup
1. Create a new app in your google [console](https://console.developers.google.com/project).
 1. Enable the drive API
 2. Create a new oAuth Client-ID
 3. Download the JSON and save it as `client_secrets.json` in this folder.
2. Rename the `config.sample` to `config.json`
 1. Specify all URLs for the files you want to backup and their relative path you want to have in your drive.
 2. Define `parent_id`, if you want all files created under a specific folder.
3. Install all dependencies: `pip install -r requirements.txt`

## Usage
```
./loader.py FOLDERNAME
```
Will download all files and save them in a folder called FOLDERNAME in your drive under the folder with the `parent_id`.
