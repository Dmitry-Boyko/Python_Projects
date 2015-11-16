# create multiple folders
import os
root_path = '/Users/...'
folders = ['folder01', 'folder02', 'folder03']
for folder in folders:
  os.mkdir(os.path.join(root_path, folder))
