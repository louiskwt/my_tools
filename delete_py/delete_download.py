#!/usr/bin/env python
import os, shutil

def delete_folder(path):
    files = os.listdir(path)
    for filename in files:
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
            print(f'Delete {len(files)} from {path}')
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

folder_path = "test"

delete_folder(folder_path)
