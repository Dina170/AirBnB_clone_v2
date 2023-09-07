#!/usr/bin/python3
"""
Fabric script that generates a tgz archive
from the contents of the web_static folder of the AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import local
from os import path


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
