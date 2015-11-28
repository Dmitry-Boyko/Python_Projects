"""
First of all you need install:
pip install pycrypto
pip install paramiko
pip install pysftp
"""

import pysftp as sftp

def push_file_to_server():
    s = sftp.Connection(host='111.111.111.111',
                        username='test',
                        password='passw')
    local_path = 'testme.txt'
    remote_path = '/Home/testme.txt'

    s.put(local_path, remote_path)
    s.close()

push_file_to_server()

def get_file_from_server():
    s = sftp.Connection(host='111.111.111.111',
                        username='test',
                        password='passw')
    local_path = 'testme.txt'
    remote_path = '/Home/testme.txt'

    s.get(remote_path, local_path)
    s.close()

get_file_from_server()

