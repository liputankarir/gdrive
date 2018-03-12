#!/usr/bin/env python

from fshandler import FsHandler
from downloader import Downloader
import json
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('folder', help='Foldername in gDrive')
args = parser.parse_args()

# read config
with open('config.json') as config_file:
    config = json.load(config_file)

# create file system handler
fsh = FsHandler()

# get temporary file
base_path = fsh.get_path()

# get all files
Downloader.downloadList(config['files'], base_path)

# upload temp folder to gDrive
fsh.upload(args.folder, config['drive']['parent_id'])

# clean up the tmp
if config['options']['removeTemp']:
    fsh.remove()
