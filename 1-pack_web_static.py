#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
from os.path import isdir
from fabric.api import local


def do_pack():
    """generates a .tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir -p versions")
        file_name = f"version/web_static_{date}.tgz"
        local(f"tar -cvzf {file_name} web_static")
        return file_name
    except:
        return None
