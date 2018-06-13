#!/usr/bin/env python
import os
import paramiko
REMOTE_DIR = 'text_files'

with paramiko.Transport(('localhost', 22)) as transport:   # <1>
    transport.connect(username='python', password='l0lz')  # <2>
    sftp = paramiko.SFTPClient.from_transport(transport)   # <3>
    for item in sftp.listdir_iter():    # <4>
        print(item)
    print('-' * 60)

    remote_file = os.path.join(REMOTE_DIR, 'betsy.txt')  # <5>

    sftp.mkdir(REMOTE_DIR)      # <6>
    sftp.put('../DATA/alice.txt', remote_file)   # <7>
    sftp.get(remote_file, 'eileen.txt')   # <8>

with paramiko.SSHClient() as ssh:# <9>
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect('localhost', username='python', password='l0lz')
    except paramiko.SSHException as err:
        print(err)
        exit()

    stdin, stdout, stderr  = ssh.exec_command('ls -l {}'.format(REMOTE_DIR))
    print(stdout.read().decode())
    print('-' * 60)

    stdin, stdout, stderr = ssh.exec_command('rm -f {}/betsy.txt'.format(REMOTE_DIR))
    stdin, stdout, stderr = ssh.exec_command('rmdir {}'.format(REMOTE_DIR))
    stdin, stdout, stderr = ssh.exec_command('ls -l')
    with open('myoutput.txt', 'w') as my_out:
        my_out.write(stdout.read().decode())
    print('-' * 60)
