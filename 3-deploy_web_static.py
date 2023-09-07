#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your web servers
"""

from datetime import datetime
from fabric.api import local, put, run, env
from os import path

env.hosts = ['52.3.249.4', '54.160.86.137']


def do_pack():
    """Generates a tgz archive"""
    dt = datetime.now().strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(dt)
    try:
        if not path.isdir("versions"):
            local("mkdir versions")
        local("tar -cvzf {} web_static".format(file))
        return file
    except:
        return None


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


def deploy():
    """Creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
