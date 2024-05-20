#!/usr/bin/python3
""" Generate a .tgz achive from the contents of the web_static folder """
from fabric.api import local
from os import path
from datetime import datetime


def do_pack():
    """ Generate a .tgz achive from the contents of the web_static folder """
    print(path)
    local("[ ! -d versions ] && mkdir versions")

    curr_time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(curr_time)
    archive_path = path.join("versions", archive_name)

    try:
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_path
    except Exception:
        return None
