__author__ = 'dmitryboyko'
# Create 3 folders and 3 files inside those folders
f_names = ['folder1','folder2','folder3']
files_names = ['1.txt','2.txt','3.txt']
for index in range(0, 3):
    file_path = os.path.join(root_path, f_names[index])
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    file_full_path = os.path.join(file_path, files_names[index])
    if not os.path.exists(file_full_path):
        open(file_full_path, 'w')
 
#print("Result:" + os.path.sep)
