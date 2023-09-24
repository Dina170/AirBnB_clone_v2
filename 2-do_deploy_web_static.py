#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os import path

env.hosts = ['52.3.249.4', '54.160.86.137']


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not path.exists(archive_path):
        return False
    try:
        full_file = archive_path.split("/")[-1]
        file_name = full_file.split(".")[0]
        dir_path = "/data/web_static/releases/"
        full_path = '{}{}'.format(dir_path, file_name)
        put(archive_path, '/tmp/')
        run('mkdir -p {}/'.format(full_path))
        run('tar -xzf /tmp/{} -C {}/'.format(full_file, full_path))
        run('rm /tmp/{}'.format(full_file))
        run('mv {}/web_static/* {}/'.format(full_path, full_path))
        run('rm -rf {}/web_static'.format(full_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {}/ /data/web_static/current'.format(full_path))
        return True
    except Exception as e:
        traceback.print_exc()
        return False
